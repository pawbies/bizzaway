from django.shortcuts import render
from django.http.response import HttpResponse, HttpResponseRedirect, JsonResponse
from django.contrib.auth.decorators import login_required
from django.urls import reverse

from django.utils import timezone
from django.core.exceptions import ObjectDoesNotExist

from django.contrib.auth import login as django_login
from django.contrib.auth import logout as django_logout
from django.contrib.auth import authenticate as django_authenticate

from webinterface.models import Order
from .models import Employee

#this returns just returns the index page with the loged in user in it's context
#and i think you can figure out what the @login_required decorator does by yourself
@login_required(redirect_field_name="login")
def index(request):
    pizzas = Order.objects.all()
    employee = Employee.objects.get(user=request.user)
    return render(request, "emp_index.html", {"orders": pizzas, "emp": employee, "employees": Employee.objects.all()})

def login_page(request):
    return render(request, "login.html", {})


#this get's the request from the login page and tries to authenticate the user
def login(request):
    username = request.POST.get("username")
    password = request.POST.get("password")
    user = django_authenticate(request, username=username, password=password)
    if user is not None:
        django_login(request, user)
        return HttpResponseRedirect(reverse("emp_index"))
    
    #also maybe i'll code a page for that case but i'm also kind of fine
    #with this solution
    return HttpResponse("User doesn't exist")


#this logs an employee out again 
def logout(request):
    django_logout(request)
    return HttpResponseRedirect(reverse("login_page"))


#and this is the infamous latest_order function
#let's go over it
def latest_order(request):
    #this fails the first time because it tries it with "null" until it get's an order from it
    try:
        since = timezone.datetime.fromtimestamp(float(request.GET.get("timestamp")), tz=None)
    except ValueError:
        since = timezone.datetime(2020, 1, 1, 1, 1, 1, 0)

    #this also fails if no orders exist
    #but normally it would get all the orders since the "since" timestamp
    #orderd by the timestamp
    try:
        order_since = Order.objects.filter(timestamp__gt=since).order_by("timestamp")
        latest_timestamp = Order.objects.latest("timestamp").timestamp.timestamp()
    except ObjectDoesNotExist:
        order_since = []
        latest_timestamp = timezone.now().timestamp()


    #and this here builds the data that's returned to the browser
    data = []
    for order in order_since:

        pizza_orders = order.pizza_order.all()
        pizzas=[]

        for pizza_order in pizza_orders:
            pizzas.append(f"{pizza_order.pizza.name} x {pizza_order.amount}")
        
        data.append({
            "customer": order.customer,
            "email": order.email,
            "notes": order.notes,
            "timestamp": order.timestamp.timestamp(),
            "pizzas": list(pizzas),
            "id": order.id
        })

    #and then we package it into a dictionary with the timestamp of the latest order
    #and send it to the browser as json
    data = {"orders": data, "latest_timestamp": latest_timestamp}
    return JsonResponse(data)