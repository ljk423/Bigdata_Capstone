from django.shortcuts import render

# Create your views here.

def loginpage(request):
    return render(request, 'loginpage.html')

def mainpage(request):
    return render(request, 'mainpage.html')

def disease1(request):
    return render(request, 'disease1.html')

def signup(request):
    return render(request, 'signup.html')