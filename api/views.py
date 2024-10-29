from django.shortcuts import render, HttpResponse
from django.http import JsonResponse

from core.models import *

import requests
import datetime
import newsapi
# Create your views here.



def WeatherAPI(request):
    API_KEY = '80b8b675ee4c47c68665dc13e7a4f97e'
    if request.method == 'POST':
        if 'submit' in request.POST:
            city = request.POST['city']
    else:
        city = 'Lagos'
    
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}'
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
    API_KEY = '80b8b675ee4c47c68665dc13e7a4f97e'
    url = f'https://newsapi.org/v2/everything?q=Apple&from=2024-05-16&sortBy=popularity&apiKey={api_key}'
    url2 = f'https://api.mediastack.com/v1/news? access_key = {api_key}& keywords = tennis& countries = us, gb, de'
    response = requests.get(url2)
    
    data = response.json()
    information = data['articles']['bbc']['article']
    
   
    cards = [information[3],information[20],information[3]]
    mids = [information[20], information[18]]
    ads = Advertisement.objects.all()
    context = { 'cards':cards, 'ads':ads, 'mids':mids}
    return render(request, 'api/news.html', context)
        
        

