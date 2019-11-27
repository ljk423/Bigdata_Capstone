from django.shortcuts import render, render_to_response
from chartit import DataPool, Chart
from .models import WeatherIndex
# Create your views here.

def loginpage(request):
    return render(request, 'loginpage.html')

def mainpage(request):
    return render(request, 'mainpage.html')

def disease1(request):
    #1. create datapool with the data\

    return render(request, 'disease1.html')

def signup(request):
    return render(request, 'signup.html')