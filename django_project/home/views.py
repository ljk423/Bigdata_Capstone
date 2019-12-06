from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from chartit import DataPool, Chart
from . import models
import json
# Create your views here.

def loginpage(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('mainpage')
        else:
            return render(request, 'loginpage.html', {'error': 'username or password is incorrect'})
    else:
        return render(request, 'loginpage.html')

def mainpage(request):
    indexes = models.MainWeatherIndex.objects.order_by('name')
    return render(request, 'mainpage.html',{'indexes': indexes})

def mainpage1(request):
    indexes = models.MainWeatherIndex.objects.order_by('name')
    return render(request, 'mainpage1.html',{'indexes': indexes})

def disease_Asthma(request):
    #1. create datapool with the data
    indexes = models.AsthmaIndex.objects.order_by('date')

    return render(request, 'disease_asthma.html', {'indexes':indexes})

def disease_Cold(request):
    #1. create datapool with the data
    indexes = models.AsthmaIndex.objects.order_by('date')
    return render(request, 'disease_cold.html', {'indexes':indexes})

def disease_Stroke(request):
    #1. create datapool with the data
    indexes = [1, 2, 2, 2, 1]
    indexes_as_json = json.dumps(indexes)
    return render(request, 'disease_stroke.html', {'indexes':indexes_as_json})

def signup(request):
    return render(request, 'signup.html')

def memberInfo(request):
    return render(request, 'memberInfo.html')