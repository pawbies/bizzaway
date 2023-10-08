from django.shortcuts import render
from django.http.response import HttpResponse

# Create your views here.

def index(request):
    return render(request, "index.html", {})

def order(request):
    return render(request, "order.html", {})

def contact(request):
    return render(request, "contact.html", {})

def imprint(request):
    return render(request, "imprint.html", {})

def privacy(request):
    return render(request, "privacy.html", {})

