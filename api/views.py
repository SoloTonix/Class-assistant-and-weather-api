from django.shortcuts import render, HttpResponse
from django.http import JsonResponse

from core.models import *

import requests
import datetime
import os


# Create your views here.



def WeatherAPI(request):
    api_key = '86562ae457c21890ef25f6fdcaf212a9'
    if request.method == 'POST':
        if 'submit' in request.POST:
            city = request.POST['city']
    else:
        city = 'Lagos'
    
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'
    PARAMS = {'unit':'metric'}
    response = requests.get(url, params=PARAMS).json()
    temperature = response['main']['temp']
    description = response['weather'][0]['description']
    icon = response['weather'][0]['icon']
    date = datetime.date.today()
    
    context = {'temperature':temperature, 'description':description, 'icon':icon, 'date':date, 'city':city}

    return render(request, 'api/weather.html', context)



# UNCOMPLETED #
def News(request):
    
    api_key = '80b8b675ee4c47c68665dc13e7a4f97e'
    url = f'https://newsapi.org/v2/everything?q=tesla&from=2024-10-04&sortBy=publishedAt&apiKey={api_key}'
    
    response = requests.get(url)
    
    data = response.json()
    information = data['articles']
    cards = [information[3],information[4],information[3]]
    mids = [information[5], information[18]]
    ads = Advertisement.objects.all()
    context = {'info':information, 'cards':cards, 'ads':ads, 'mids':mids}
    return render(request, 'api/news.html', context)
        
        

