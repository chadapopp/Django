from django.urls import path 
from . import views
from django.shortcuts import render, HttpResponse

urlpatterns = [
    path('', views.index),
]

def index(request):
    return HttpResponse("this is the equivalent of @app.route('/')!")
