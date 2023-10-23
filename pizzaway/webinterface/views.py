from django.shortcuts import render, get_object_or_404
from django.http.response import HttpResponseRedirect
from django.http.request import HttpRequest
from django.urls import reverse

from .models import Order, Pizza
from employee.models import Employee

# Create your views here.

def index(request: HttpRequest):
    return render(request, "index.html", {})

def order(request: HttpRequest):
    return render(request, "order.html", {})

def contact(request: HttpRequest):
    return render(request, "contact.html", {})

def imprint(request: HttpRequest):
    return render(request, "imprint.html", {})

def privacy(request: HttpRequest):
    return render(request, "privacy.html", {})




def add_order(request: HttpRequest):
    name = request.POST.get("customer")
    email = request.POST.get("email")
    notes = request.POST.get("notes")
    order = Order(customer=name, email=email, notes=notes)
    order.save()
    order.pizzas.add(get_object_or_404(Pizza, name=request.POST.get("pizza")))
    return HttpResponseRedirect(reverse("index", current_app="webinterface"))


def remove_order(request: HttpRequest):
    order = get_object_or_404(Order, id=request.POST.get("order_id"))
    order.delete()
    employee = get_object_or_404(Employee, id=request.POST.get("emp_id"))
    employee.orders_cooked += 1
    employee.save()
    return HttpResponseRedirect(reverse("emp_index"))
