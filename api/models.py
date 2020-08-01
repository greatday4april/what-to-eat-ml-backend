from django.contrib.auth.models import AbstractBaseUser
from django.db import models
from typing import List, Dict, Optional
from config.settings import CACHE_TTL
import utils.yelp_api_utils as yelp_api_utils

import json
import random

from django.contrib.sessions.backends.cache import SessionStore


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

    def __str__(self):
        return json.dumps({'id': self.id})


class Preference(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    restaurant_id = models.CharField(max_length=120)
    type = models.CharField(
        max_length=60, choices=PreferenceType.choices)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return json.dumps({
            'user': str(self.user),
            'restaurant_id': self.restaurant_id,
            'preference_type': self.type,
            'created_at': str(self.created_at),
        })


class Session():
    def __init__(self, user_id: int):
        self.user = User.objects.get(id=user_id)
        yelp_response = yelp_api_utils.search().get('businesses')
        self.preferences: Dict[str, Preference] = {}
        self.restaurants: List[Dict] = list(yelp_response)

    @staticmethod
    def find_by_user(user_id: int) -> Optional['Session']:
        user = User.objects.get(id=user_id)
        store = SessionStore(user.session_key)
        return store['session'] if 'session' in store else None

    def add_preference(self, restaurant_id: str, type: PreferenceType) -> 'Session':
        pref = Preference(
            user=self.user,
            restaurant_id=restaurant_id,
            type=type,
        )
        pref.save()
        assert(restaurant_id not in self.preferences)
        self.preferences[restaurant_id] = pref
        return self

    @property
    def next_restaurant(self) -> Optional[Dict]:
        pool = [item for item in self.restaurants if item['id'] not in self.preferences]
        if len(pool) == 0:
            return None
        restaurant = random.choice(pool)
        return yelp_api_utils.get_business(restaurant['id'])

    def save(self) -> 'Session':
        store = SessionStore(session_key=self.user.session_key)
        store['session'] = self
        store.set_expiry(CACHE_TTL)
        store.save()
        self.user.session_key = store.session_key
        self.user.save()
        return self
