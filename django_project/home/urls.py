from django.urls import path
from . import views

urlpatterns = [
    path('', views.loginpage, name='loginpage'),
    path("mainpage_서울/", views.mainpage_서울, name='mainpage_서울'),
    path("mainpage_인천/", views.mainpage_인천, name='mainpage_인천'),
    path("mainpage_춘천/", views.mainpage_춘천, name='mainpage_춘천'),
    path("mainpage_대전/", views.mainpage_대전, name='mainpage_대전'),
    path("mainpage_광주/", views.mainpage_광주, name='mainpage_광주'),
    path("mainpage_부산/", views.mainpage_부산, name='mainpage_부산'),
    path('mainpage/signup/', views.signup, name='signup'),
    path('mainpage/disease_asthma', views.disease_Asthma, name='disease_asthma'),
    path('mainpage/mainpage_서울/disease_asthma_서울', views.disease_Asthma_서울, name='disease_asthma_서울'),
    path('mainpage/mainpage_서울/cold/disease_cold_서울/', views.disease_Cold_서울, name='disease_cold_서울'),
    path('mainpage_부산/disease_cold_부산/', views.disease_Cold_부산, name='disease_cold_부산'),
    path('mainpage_대전/disease_cold_대전/', views.disease_Cold_대전, name='disease_cold_대전'),
    path('mainpage_광주/disease_cold_광주/', views.disease_Cold_광주, name='disease_cold_광주'),
    path('mainpage_인천/disease_cold_인천/', views.disease_Cold_인천, name='disease_cold_인천'),
    path('mainpage_춘천/disease_cold_춘천/', views.disease_Cold_춘천, name='disease_cold_춘천'),
    path('mainpage/disease_stroke_inchoen', views.disease_Stroke, name='disease_stroke_incheon'),
    path('signup', views.signup, name='signup'),
    path('mainpage/memberInfo', views.memberInfo, name='memberInfo'),
    path('mainpage_new/', views.mainpage_new, name='mainpage_new'),
    path('localcode/', views.localcode, name='localcode'),
]