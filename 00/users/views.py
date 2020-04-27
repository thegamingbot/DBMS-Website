from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponse
from django.template import Context, loader

# Create your views here.

def index(request):
    return render(request, "users/index.html")

def accomodation(request):
    return render(request, "users/accomodation.html")

def contact_us(request):
    return render(request, "users/contact_us.html")

def events(request):
    return render(request, "users/events.html")

def register(request):
    return render(request, "users/register.html")

def schedule(request):
    return render(request, "users/schedule.html")

def sponsors(request):
    return render(request, "users/sponsors.html")
