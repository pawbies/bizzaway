from django.shortcuts import render
from django.http.response import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse

from django.contrib.auth import login as django_login
from django.contrib.auth import logout as django_logout
from django.contrib.auth import authenticate as django_authenticate

# Create your views here.

@login_required(redirect_field_name="login")
def index(request):
    return render(request, "emp_index.html", {})

def login_page(request):
    return render(request, "login.html", {})



def login(request):
    username = request.POST["username"]
    password = request.POST["password"]
    user = django_authenticate(request, username=username, password=password)
    if user is not None:
        django_login(request, user)
        return HttpResponseRedirect(reverse("emp_index"))
    
    else:
        return HttpResponse("User doesn't exist")
    
def logout(request):
    django_logout(request)
    return HttpResponse("Loged out")