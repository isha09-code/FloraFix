from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .models import Profile


def signup_view(request):
    if request.method == 'POST':
        full_name = request.POST.get('full_name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if password != confirm_password:
            return render(request, 'signup.html', {"error": "Passwords do not match"})

        if User.objects.filter(username=email).exists():
            return render(request, 'signup.html', {"error": "An account with this email already exists"})

        if full_name and email and password:
            user = User.objects.create_user(username=email, email=email, password=password)
            Profile.objects.create(user=user, full_name=full_name)
            messages.success(request, "Successfully registered! Please sign in.")
            return redirect('accounts:signin')

    return render(request, 'signup.html')


def signin_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, username=email, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, f"Welcome, {user.profile.full_name}!")
            return redirect('accounts:signin')

        return render(request, 'signin.html', {"error": "Invalid credentials"})

    return render(request, 'signin.html')
