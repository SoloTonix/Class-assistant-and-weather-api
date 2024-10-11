from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User 
from django import forms 
from.models import *

class CreateNoteForm(forms.ModelForm):
    title = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={'placeholder':'Title', 'class' : 'form-control'}))
    content = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={'placeholder':'Content', 'class' : 'form-control'}))
   
    class Meta:
        model = Note
        fields = ['title', 'content']
        


class CreateCourseForm(forms.ModelForm):
    description = forms.CharField(required=False)
    class Meta:
        model = Course
        fields = ['title', 'description']

class WeatherForm(forms.Form):
    city = forms.CharField(widget=forms.widgets.TextInput(attrs={'placeholder':'Enter city', 'class':'form-control'}))

    class Meta:
        model = City
        fields = '__all__'