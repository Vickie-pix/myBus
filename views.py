from django.shortcuts import render,redirect
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from django.contrib.auth import login,authenticate
from .models import travel


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
        else:
            form = UserCreationForm()
            return render(request, 'signup.html', {'form':form})
    else:
        form = UserCreationForm()
        return render(request, 'login.html', {'form':form})        
def aboutus(request):
    return render(request,'aboutus.html')
def services(request):
    return render(request,'services.html')
def contactus(request):
    return render(request,'contactus.html')
def home(request):
    return render(request, 'home.html')    
def trippage(request):    
    if request.method == "POST":
        routes = request.POST.get('route')
        durations = request.POST.get('duration')
        distances = request.POST.get('distance')
        prices = request.POST.get('price')

        tripinfo = travel(routes=routes, durations=durations, distances=distances, prices=prices)
        tripinfo.save()
    return render(request, 'trips.html')  
def buspage(request):
    return render(request, 'buses.html')
def booking(request):
    tripinfo = travel.objects.all()
    return render(request, 'booking.html',{'tripinfo':tripinfo})
def billingpage(request):
    return render(request,'billing.html')
