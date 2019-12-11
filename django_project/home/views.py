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

def localcode(request):
    indexes = models.LocalCode.objects.order_by('name')
    return render(request, 'localcode.html', {'indexes':indexes})


def mainpage_춘천(request):
    indexes = models.MainWeatherIndex.objects.order_by('name')
    return render(request, 'mainpage/mainpage_춘천.html', {'indexes': indexes})

def mainpage_대전(request):
    indexes = models.MainWeatherIndex.objects.order_by('name')
    return render(request, 'mainpage/mainpage_대전.html', {'indexes': indexes})

def mainpage_서울(request):
    indexes = models.MainWeatherIndex.objects.order_by('name')
    return render(request, 'mainpage/mainpage_서울.html', {'indexes': indexes})

def mainpage_부산(request):
    indexes = models.MainWeatherIndex.objects.order_by('name')
    return render(request, 'mainpage/mainpage_부산.html', {'indexes': indexes})

def mainpage_광주(request):
    indexes = models.MainWeatherIndex.objects.order_by('name')
    return render(request, 'mainpage/mainpage_광주.html', {'indexes': indexes})
def mainpage_인천(request):
    indexes = models.MainWeatherIndex.objects.order_by('name')
    return render(request, 'mainpage/mainpage_인천.html', {'indexes': indexes})

def disease_Asthma(request):
    #1. create datapool with the data
    indexes = models.AsthmaIndex.objects.order_by('date')

    return render(request, 'asthma/disease_asthma_서울.html', {'indexes':indexes})

def disease_Cold_서울(request):
    #1. create datapool with the data

    indexes = models.ColdIndex.objects.order_by('date')
    return render(request, 'cold/disease_cold_서울.html', {'indexes':indexes})
def disease_Cold_부산(request):
    #1. create datapool with the data

    indexes = models.ColdIndex.objects.order_by('date')
    return render(request, 'cold/disease_cold_부산.html', {'indexes':indexes})
def disease_Cold_대전(request):
    #1. create datapool with the data

    indexes = models.ColdIndex.objects.order_by('date')
    return render(request, 'cold/disease_cold_대전.html', {'indexes':indexes})
def disease_Cold_광주(request):
    #1. create datapool with the data

    indexes = models.ColdIndex.objects.order_by('date')
    return render(request, 'cold/disease_cold_광주.html', {'indexes':indexes})
def disease_Cold_춘천(request):
    #1. create datapool with the data

    indexes = models.ColdIndex.objects.order_by('date')
    return render(request, 'cold/disease_cold_춘천.html', {'indexes':indexes})
def disease_Cold_인천(request):
    #1. create datapool with the data

    indexes = models.ColdIndex.objects.order_by('date')
    return render(request, 'cold/disease_cold_인천.html', {'indexes':indexes})
def disease_Stroke(request):
    #1. create datapool with the data
    indexes = models.StrokeIndex.objects.order_by('date')
    ## dictionary, list식으로 전달 후 template에서 정해진 자리에 맞춰 사용

    return render(request, 'stroke/disease_stroke.html', {'indexes':indexes})

def mainpage_new(request):
    indexes = models.MainWeatherIndex.objects.order_by('name')
    return render(request, 'mainpage/mainpage_new.html', {'indexes': indexes}, {'region' : 'Seoul'})



def signup(request):
    return render(request, 'signup.html')

def memberInfo(request):
    return render(request, 'memberInfo.html')