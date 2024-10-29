from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from.models import *
class RegisterUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']

class ProfileForm:
    class Meta:
        model = Profile
        fields = '__all__'