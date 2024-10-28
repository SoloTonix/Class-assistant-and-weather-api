from django.urls import path
from .views import *
urlpatterns = [
    path('profile/', UserProfile, name='UserProfile'),
    path('login/',Login, name='Login'),
    path('logout/', Logout, name='Logout'),
    path('register/', Register, name='Register'),
]