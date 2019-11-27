from django.urls import path
from . import views

urlpatterns = [
    path('', views.loginpage, name='loginpage'),
    path("mainpage/", views.mainpage, name='mainpage'),
    path('mainpage/signup/', views.signup, name='signup'),
    path('mainpage/disease1', views.disease1, name='disease1'),
]