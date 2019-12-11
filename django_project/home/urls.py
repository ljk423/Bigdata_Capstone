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
    path('mainpage/disease_cold', views.disease_Cold, name='disease_cold'),
    path('mainpage/disease_stroke', views.disease_Stroke, name='disease_stroke'),
    path('signup', views.signup, name='signup'),
    path('mainpage/memberInfo', views.memberInfo, name='memberInfo'),
    path('mainpage_new/', views.mainpage_new, name='mainpage_new'),
    path('localcode/', views.localcode, name='localcode'),
]