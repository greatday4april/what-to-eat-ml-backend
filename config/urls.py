"""what_to_eat URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from django.views.generic.base import RedirectView
from api.views import SessionViewSet, PreferenceViewSet, UserViewSet


urlpatterns = [
    path('', RedirectView.as_view(url='api/session')),
    path(
        'api/session/',
        SessionViewSet.as_view({'get': 'retrieve'}),
        name='session'
    ),
    path(
        'api/preferences/',
        PreferenceViewSet.as_view({'get': 'list', 'post': 'create'}),
        name='preference'
    ),
    path(
        'api/user/',
        UserViewSet.as_view({'get': 'retrieve', 'post': 'create'}),
        name='user'
    )
]
