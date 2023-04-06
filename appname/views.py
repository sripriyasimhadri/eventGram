from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def account(request):
    return render(request, 'account.html')

def signup(request):
    return render(request, 'signup.html')

def dashboard(request):
    return render(request, 'dashboard.html')

def events1(request):
    return render(request, 'events1.html')

def events2(request):
    return render(request, 'events2.html')

def events3(request):
    return render(request, 'events3.html')

def register(request):
    return render(request, 'register.html')
def contactus(request):
    return render(request, 'contactus.html')