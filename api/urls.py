from django.urls import path 
from.views import *
urlpatterns = [
    path('weather/', WeatherAPI, name='WeatherAPI'),
    path('news/', News, name='News'),

]