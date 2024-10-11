from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
# Create your views here.
def Login(request):
    # Aunthentication and Authorisation
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, 'welcome')
            return redirect('Index')
        messages.success(request, 'This user does not exist...')

    return render(request, 'accounts/login.html')