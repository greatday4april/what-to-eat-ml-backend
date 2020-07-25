from django.contrib.auth.models import AbstractBaseUser
from django.db import models
import json

# Create your models here.


class Preference(models.Model):
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    restaurant_id = models.CharField(max_length=120)
    score = models.IntegerField(default=0)

    def _str_(self):
        return json.dumps({'user_id': self.user_id, 'restaurant_id': self.restaurant_id, 'score': self.score})


class User(AbstractBaseUser):
    USERNAME_FIELD = 'id'
    REQUIRED_FIELDS = ['session_token']
    session_token = models.CharField(max_length=240)
    date_joined = models.DateTimeField(auto_now_add=True)

    def _str_(self):
        return json.dumps({'session_token': self.session_token})


if __name__ == "__main__":
    u = User(session_token='abc')
    u.save()
    print(u.id)
