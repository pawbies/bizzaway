from django.shortcuts import render
from django.http.response import HttpResponse
from django.contrib.auth.models import User

# Create your views here.

def index(request):
    return HttpResponse("Hello World")

def login(request):
    return HttpResponse("Hello World")


