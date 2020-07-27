from django.contrib.auth.models import AbstractBaseUser
from django.db import models
import json


# Create your models here.
class Type (models.TextChoices):
    LIKE = 'LIKE'
    DISLIKE = 'DISLIKE'
    NEUTRAL = 'NEUTRAL'
    FAVORITE = 'FAVORITE'


class User(AbstractBaseUser):
    USERNAME_FIELD = 'id'
    REQUIRED_FIELDS = ['session_token']
    session_token = models.CharField(max_length=240)
    date_joined = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return json.dumps({'id': self.id, 'session_token': self.session_token})


class Preference(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    restaurant_id = models.CharField(max_length=120)
    type = models.CharField(
        max_length=60, choices=Type.choices)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return json.dumps({
            'user': self.user,
            'restaurant_id': self.restaurant_id,
            'preference_type': self.preference_type,
            'created_at': self.created_at,
        })
