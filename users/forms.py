from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from.models import *
class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'password2']

class LoginForm(forms.ModelForm):
    password = forms.CharField(widget=forms.widgets.PasswordInput(attrs={'class':'form-control'}))
    class Meta:
        model = User 
        fields = ('username', 'password',)

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User 
        fields = ('username', 'email',)

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']