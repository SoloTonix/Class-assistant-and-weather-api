from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from .forms import *
from .models import Profile
from core.models import *
from django.views.generic import DetailView
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.contrib.auth.decorators import login_required, user_passes_test
# Create your views here.


@login_required
def UserProfile(request):
    profile = Profile.objects.get(user=request.user)
    courses = Course.objects.filter(author=profile.user)
    
    context = {'profile' : profile,
               'courses':courses}
    return render(request, 'accounts/profile.html', context)


def Register(request):
    form = RegisterUserForm()
    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been succesfully created...')
            return redirect('Login')
        else:
            messages.warning(request,'Sorry something went wrong')
    else:
        form = RegisterUserForm()
    context = {'form':form}
    return render(request, 'accounts/register.html', context)

def Login(request):
    # Aunthentication and Authorisation
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None and user.is_active:
            login(request, user)
            messages.success(request, f'Welcome {username}')
            return redirect('Index')
        else:
            messages.error(request, 'This user does not exist...')

    return render(request, 'accounts/login.html')

def Logout(request):
    logout(request)
    return redirect('Login')