from django.test import TestCase
import django

# Create your tests here.


def test_models():
    from backend.models import User, Preference
    u = User(session_token='abc')
    u.save()
    print(u)
    pref = Preference(user=u, restaurant_id='xyz', score=3)
    pref.save()
    print(pref)


if __name__ == '__main__':
    django.setup()
    test_models()
