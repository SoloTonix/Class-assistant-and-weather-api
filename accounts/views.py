from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from .forms import *
# Create your views here.
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
        messages.success(request, 'This user does not exist...')

    return render(request, 'accounts/login.html')

def Logout(request):
    logout(request)
    return redirect('Login')