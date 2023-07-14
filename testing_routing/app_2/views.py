from django.shortcuts import render, HttpResponse

def first_view(request):
    return HttpResponse("Hello World"
                        "<br>This is my first view from app2")

def second_view(request):
    return HttpResponse("This is my second view from app2")
