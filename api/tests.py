from django.test import TestCase
import django

# Create your tests here.


def test_models():
    from api.models import User, Preference, PreferenceType
    u = User()
    u.save()
    print(u)
    pref = Preference(user=u, restaurant_id='xyz', type=PreferenceType.LIKE)
    pref.save()
    print(pref)


if __name__ == '__main__':
    django.setup()
    test_models()
