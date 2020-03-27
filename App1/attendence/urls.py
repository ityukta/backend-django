from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from . import views
urlpatterns = [
    path('', views.indexView, name='Home Page'),
    path('user/register/', views.registrationUserView, name='Register User'),

]
