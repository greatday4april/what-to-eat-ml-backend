from django.contrib.auth.models import AbstractBaseUser
from django.db import models
from typing import List, Dict, Optional
from config.settings import SESSION_TTL
from django.contrib.postgres.fields import ArrayField
from collections import defaultdict
from ordered_set import OrderedSet

import utils.yelp_api_utils as yelp_api_utils
import utils.rakuten_menu_api_utils as rakuten_menu_api_utils
from recommender import get_similar_restaurant_ids

import json
import random
import datetime

from django.contrib.sessions.backends.cached_db import SessionStore


# Create your models here.
class PreferenceType(models.TextChoices):
    LIKE = 'LIKE'
    DISLIKE = 'DISLIKE'
    NEUTRAL = 'NEUTRAL'
    FAVORITE = 'FAVORITE'


class User(AbstractBaseUser):
    USERNAME_FIELD = 'id'
    REQUIRED_FIELDS = []
    session_key = models.CharField(max_length=240, null=True, default=None)
    date_joined = models.DateTimeField(auto_now_add=True)
    cuisine_tags = ArrayField(
        models.CharField(max_length=100), null=True, default=None
    )

    def __str__(self):
        return json.dumps({
            'id': self.id,
            'last_login': self.last_login,
            'date_joined': self.date_joined,
            'session_key': self.session_key,
            'cusine_tags': self.cuisine_tags})


class Preference(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=False, default=None)
    restaurant_id = models.CharField(max_length=120, null=False, default=None)
    type = models.CharField(
        max_length=60, choices=PreferenceType.choices, null=False, default=None)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return json.dumps({
            'user': str(self.user),
            'restaurant_id': self.restaurant_id,
            'preference_type': self.type,
            'created_at': str(self.created_at),
        })


class Session():
    def __init__(self, user_id: int, page_size: Optional[int], location: Optional[List]):
        self.user = User.objects.get(id=user_id)
        self.page_size = page_size if page_size else 2
        self.preferences: Dict[str, Preference] = {}
        self.restaurants: List[Dict] = list(
            rakuten_menu_api_utils.search(location)
        )
        self.random = random
        self.random.seed(datetime.datetime.weekday())
        self.favorites = defaultdict(int)
        self.dislikes = defaultdict(int)
        self.__update_restaurant_pool()

    def __update_restaurant_pool(self):
        user_preferences = Preference.objects.filter(user=self.user).all()
        for user_preference in user_preferences:
            if user_preference.type == PreferenceType.LIKE:
                self.favorites[user_preference.restaurant_id] += 1
            elif user_preference.type == PreferenceType.DISLIKE:
                self.favorites[user_preference.restaurant_id] -= 1
        for key, value in self.favorites.items():
            if value <= 0:
                if value < 0:
                    self.dislikes[key] = value
                del self.favorites[key]

    @staticmethod
    def find_by_user(user_id: int) -> Optional['Session']:
        user = User.objects.get(id=user_id)
        store = SessionStore(session_key=user.session_key)
        return store['session'] if 'session' in store else None

    @property
    def next_restaurants(self) -> Optional[List[Dict]]:
        favorites_count = len(self.favorites)
        if favorites_count == 0:
            return None
        reference_restaurant_ids = self.random.choices(
            self.favorites.keys,
            weights=self.favorites.values,
            k=(7 if favorites_count >= 7 else favorites_count)
        )
        candidate_ids = [candidate['restaurant_id']
                         for candidate in self.restaurants]
        candidate_ids = [
            candidate_id for candidate_id in candidate_ids if candidate_id not in self.preferences
        ]
        recommended_restaurant_ids = [get_similar_restaurant_ids(reference_id, candidate_ids) for reference_id in reference_restaurant_ids]
        recommended_restaurant_ids = list(OrderedSet(
            [id for sublist in recommended_restaurant_ids for id in sublist]))

        return [{
            **yelp_api_utils.get_business(id),
            'reviews': yelp_api_utils.get_reviews(id)['reviews']
        } for id in recommended_restaurant_ids]

    def save(self) -> 'Session':
        store = SessionStore(session_key=self.user.session_key)
        store['session'] = self
        store.set_expiry(SESSION_TTL)
        store.save()
        self.user.session_key = store.session_key
        self.user.save()
        self.__update_restaurant_pool()
        return self
