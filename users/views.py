from django.shortcuts import render, redirect
from.forms import *
from django.contrib import messages
from django.contrib.auth import logout, login, authenticate
# Create your views here.
def SignUp(request):
    form = SignUpForm()
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Index')
            
    else:
        form = SignUpForm()
    context = {'form':form}
    return render(request, 'users/signup.html', context)

def UserLogin(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, username=cd['username'], password=cd['password'])
            if user is not None:
                login(request, user)
                messages.success(request, 'Welcome ')
                return redirect('Index')
            else:
                messages.success(request, 'Sorry this user does not exist..')
        else:
            messages.success(request, 'Invalid details...')
    else:
        form = LoginForm()
        

    context = {'form':form}
    return render(request, 'users/login.html', context)

def UserLogout(request):
    logout(request)
    return redirect('Index')

def UserProfile(request):
    curr_user = User.objects.filter(id=request.user.id)
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST , instance=curr_user)
        prof_form = ProfileUpdateForm(request.POST , request.FILES, instance=curr_user)

        if user_form.is_valid() and prof_form.is_valid():
            user_form.save() 
            prof_form.save()
            messages.success(request, 'Your profile has been successfully updated.')
            return redirect('UserProfile')
        
    else:
        user_form = UserUpdateForm(instance=request.user)
        prof_form = ProfileUpdateForm(instance=request.user)       
        
    context = {'user_form':user_form, 'prof_form':prof_form, 'curr_user':curr_user}
    return render(request, 'users/profile.html', context)