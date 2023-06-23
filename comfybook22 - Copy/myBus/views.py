from django.shortcuts import render,redirect
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from django.contrib.auth import login,authenticate
from .models import sleep
from .forms import UserRegisterForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django import forms


# Create your views here.
def login(request):
    if request.method=="POST":
        user = authenticate(request, username = request.POST.get('username'), password = request.POST.get('password'))
        if user is None:
            form = AuthenticationForm()
            error = "Invalid password or email"
            return render(request,'login.html', {'form':form, 'error':error})
        else:
            return redirect('home')
    else:
        form = AuthenticationForm()
        return render(request, 'login.html', {'form':form})
def signup(request):
    if request.method=="POST":
        form = UserCreationForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect('login')
            username = form.cleaned_data.get('username')
            messages.success(request, f'Hi {username}, your account was created successfully')
        else:
            form = UserCreationForm()
            return render(request, 'signup.html', {'form':form})
    else:
        form = UserCreationForm()
        return render(request, 'login.html', {'form':form}) 
@login_required()
def profile(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password= request.POST.get('password')

        userinfo = user(username=username, password=password)
        userinfo.save()
    return render(request, 'profile.html')      
def aboutus(request):
    return render(request,'aboutus.html')
def contactus(request):
    return render(request,'contactus.html')
def home(request):
    return render(request, 'home.html')    
def roomspage(request):    
    if request.method == "POST":
        roomnumber = request.POST.get('roomnumber')
        floor = request.POST.get('floor')
        duration = request.POST.get('duration')

        roominfo = sleep(roomnumber=roomnumber, floor=floor, duration=duration)
        roominfo.save()
    return render(request, 'rooms.html')  
def booking(request):
    roominfo = sleep.objects.all()
    return render(request, 'booking.html',{'roominfo':roominfo})
