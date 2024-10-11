from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from. serializer import NoteSeralizer
from core.models import *
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status 

# Create your views here.

@api_view(['GET','POST'])
def List(request):
    if request.method == 'GET':
        query = Note.objects.all()
        serializer = NoteSeralizer(Note, many=True)
        return JsonResponse({'notes':serializer.data})
    if request.method == 'POST':
        serializer = NoteSeralizer(data=request.POST) 
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
# THIRD PARTY API'S.
import requests
import datetime


def WeatherAPI(request):
    API_KEY = '86562ae457c21890ef25f6fdcaf212a9'
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



def NewsAPI(request):
    API_KEY = '80b8b675ee4c47c68665dc13e7a4f97e'
    url = f'https://newsapi.org/v2/everything?q=Apple&from=2024-05-16&sortBy=popularity&apiKey={API_KEY}'
    url2 = 'https://api.mediastack.com/v1/news? access_key = YOUR_ACCESS_KEY& keywords = tennis& countries = us, gb, de'
    response = requests.get(url)
    
    data = response.json().text
    information = data['articles']
    
    info = data['articles'][:6]
    cards = [information[3],information[20],information[3]]
    mids = [information[20], information[18]]
    ads = Advertisement.objects.all()
    context = {'info':info, 'cards':cards, 'ads':ads, 'mids':mids}
    return render(request, 'api/news.html', context)
        
        

from django.contrib import messages
def Test(request):
    if 'one' in request.GET:
        return HttpResponse('One')
    elif 'two' in request.GET:
        return HttpResponse('two')
    return render(request, 'api/test.html')