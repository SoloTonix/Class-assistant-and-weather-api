from django.urls import path
from .views import *
urlpatterns = [
    path('profile/', UserProfile, name='UserProfile'),
    path('profile/edit/', ProfileEdit.as_view(), name='ProfileEdit'),
    path('login/',Login, name='Login'),
    path('logout/', Logout, name='Logout'),
    path('register/', Register, name='Register'),
]