from django.urls import path
from . import views

urlpatterns = [
    path('', views.loginpage, name='loginpage'),
    path("mainpage/", views.mainpage, name='mainpage'),
    path('mainpage/signup/', views.signup, name='signup'),
    path('mainpage/disease_asthma', views.disease_Asthma, name='disease_asthma'),
    path('mainpage/disease_cold', views.disease_Cold, name='disease_cold'),
    path('mainpage/disease_stroke', views.disease_Stroke, name='disease_stroke'),
    path('signup', views.signup, name='signup'),
    path('mainpage/memberInfo', views.memberInfo, name='memberInfo'),
]