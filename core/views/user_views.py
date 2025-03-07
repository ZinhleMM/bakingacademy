from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib import messages
from core.forms import UserRegistrationForm, UserLoginForm

def home(request):
    return render(request, 'core/home.html')

def register_user(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful!")
            return redirect('home')
    else:
        form = UserRegistrationForm()
    return render(request, 'core/register.html', {'form': form})

def login_user(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, f"Welcome back, {user.username}!")
            return redirect('home')
    else:
        form = UserLoginForm()
    return render(request, 'core/login.html', {'form': form})

def logout_user(request):
    logout(request)
    messages.success(request, "You have been logged out.")
    return redirect('login')
