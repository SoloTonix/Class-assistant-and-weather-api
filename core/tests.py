from django.test import TestCase

# Create your tests here.
import requests


def Api(url):
    response = requests.get(url).json()
    names = response['id']
    print(names)
    
url = 'http://127.0.0.1:8000/api/get-student-mark-1/'
Api(url)