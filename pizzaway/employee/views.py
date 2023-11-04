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

# Create your views here.

@login_required(redirect_field_name="login")
def index(request):
    pizzas = Order.objects.all()
    employee = Employee.objects.get(user=request.user)
    return render(request, "emp_index.html", {"orders": pizzas, "emp": employee, "employees": Employee.objects.all()})

def login_page(request):
    return render(request, "login.html", {})


def login(request):
    username = request.POST.get("username")
    password = request.POST.get("password")
    user = django_authenticate(request, username=username, password=password)
    if user is not None:
        django_login(request, user)
        return HttpResponseRedirect(reverse("emp_index"))
    
    return HttpResponse("User doesn't exist")


def logout(request):
    django_logout(request)
    return HttpResponseRedirect(reverse("login_page"))


def latest_order(request):
    try:
        since = timezone.datetime.fromtimestamp(float(request.GET.get("timestamp")), tz=None)
    except ValueError:
        since = timezone.datetime(2020, 1, 1, 1, 1, 1, 0)

    try:
        order_since = Order.objects.filter(timestamp__gt=since).order_by("timestamp")
        latest_timestamp = Order.objects.latest("timestamp").timestamp.timestamp()
    except ObjectDoesNotExist:
        order_since = []
        latest_timestamp = timezone.now().timestamp()


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

    data = {"orders": data, "latest_timestamp": latest_timestamp}

    return JsonResponse(data)