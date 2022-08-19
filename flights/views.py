from django.shortcuts import render
from .models import Flight, Airport, Passenger
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
# Create your views here.

def index(request):
    if request.user.is_authenticated:
        flights = Flight.objects.all()
        return render(request,'flights/index.html',{
            'flights':flights
        })
    else:
        return HttpResponseRedirect(reverse('login'))

def flight(request, flight_id):
    f = Flight.objects.get(id=flight_id)
    passnegers = f.passengers.all()
    # non_passengers = passnegers

    non_passengers = Passenger.objects.exclude(flights=f)
    return render(request,'flights/flight.html',{
        'flight':f,
        'passengers':passnegers,
        'non_passengers':non_passengers
    })

def book(request, flight_id):
    if request.method == 'POST':
        f = Flight.objects.get(id=flight_id)
        pass_id = int(request.POST['passenger'])
        passenger = Passenger.objects.get(id=pass_id)
        passenger.flights.add(f)

        return HttpResponseRedirect(reverse('flight', args=[f.id]))
    if request.method == 'GET':
        return HttpResponseRedirect(reverse('index'))

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "flights/login.html", {
                "message": "Invalid Credentials"
            })
    if request.method == 'GET':  
        return render(request,'flights/login.html')

def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('login'))
        