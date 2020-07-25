from django.contrib.auth.models import AbstractBaseUser
from django.db import models
import json


# Create your models here.
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
    score = models.IntegerField(default=0)

    def __str__(self):
        return json.dumps({'user_id': self.user_id, 'restaurant_id': self.restaurant_id, 'score': self.score})
