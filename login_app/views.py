from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import authenticate,  login, logout
from django.contrib import messages

def home_page(request):
    if request.user.is_authenticated:
        username = request.user.username
        return render(request, 'home_page.html', {"username":username})
    else:
        return render(request, "home_page.html")

def login_user(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user= authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user=user)
            return redirect('home_page')
        else:
           return redirect('login_page')
        
    else:
        return render(request, 'login_page.html')
    

def logout_user(request):
    logout(request)
    return redirect('home_page')
