from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def account(request):
    return render(request, 'account.html')

def signup(request):
    return render(request, 'signup.html')

def dashboard(request):
    return render(request, 'dashboard.html')