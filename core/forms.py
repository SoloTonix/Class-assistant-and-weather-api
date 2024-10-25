from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User 
from django import forms 
from.models import *

class CreateNoteForm(forms.ModelForm):   
    class Meta:
        model = Note
        fields = ['title', 'content']
        


class CreateCourseForm(forms.ModelForm):
    description = forms.CharField(required=False, widget=forms.TextInput(attrs={'rows':3}))
    class Meta:
        model = Course
        fields = ['title', 'description']

class WeatherForm(forms.Form):
    city = forms.CharField(widget=forms.widgets.TextInput(attrs={'placeholder':'Enter city', 'class':'form-control'}))

    class Meta:
        model = City
        fields = '__all__'