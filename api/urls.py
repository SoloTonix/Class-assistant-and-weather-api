from django.urls import path 
from.views import *
urlpatterns = [
    path('notes/', List, name='List'),
    path('weather/', WeatherAPI, name='WeatherAPI'),
    path('news/', NewsAPI, name='NewsAPI'),
    path('test/', Test, name='Test'),
]