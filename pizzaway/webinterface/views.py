from django.shortcuts import render, get_object_or_404
from django.http.response import HttpResponseRedirect, Http404, HttpResponse
from django.http.request import HttpRequest
from django.urls import reverse
from django.utils.translation import gettext as _
from django.utils.translation import activate

from .models import Order, Pizza, PizzaOrder
from employee.models import Employee

import math

#the most of our views are rather basic

def index(request: HttpRequest, language_code):
    activate(language_code)
    return render(request, "index.html", {"pizzas": Pizza.objects.all(), "language": language_code})

def order(request: HttpRequest, language_code):
    activate(language_code)
    return render(request, "order.html", {"pizzas": Pizza.objects.all(), "language": language_code})

def contact(request: HttpRequest, language_code):
    activate(language_code)
    return render(request, "contact.html", {"language": language_code})

def imprint(request: HttpRequest, language_code):
    activate(language_code)
    return render(request, "imprint.html", {"language": language_code})

def privacy(request: HttpRequest, language_code):
    activate(language_code)
    return render(request, "privacy.html", {"language": language_code})

def order_successful(request, language_code):
    activate(language_code)
    return render(request, "order_successful.html", {"time": request.GET.get("time"), "language": language_code})


def add_order(request: HttpRequest, language_code): #this is the only interesting thing
    #first we retrieve all the arguments from the post list

    name = request.POST.get("customer")
    email = request.POST.get("email")
    notes = request.POST.get("notes")
    pizzas = request.POST.getlist("selected_pizzas[]")
    
    #then we create a order object just to save it again
    #even though there is an easier way to do this which i've used in other parts
    # (i just noticed i even used it in the loop below this... so yeahhh)
    order = Order(customer=name, email=email, notes=notes)
    order.save()

    pizza_amount = 0

    for pizza in pizzas: # try to create an entry in PizzaOrder for every different pizza
        try:
            p = get_object_or_404(Pizza, name=pizza)
            amount = request.POST.get(f"{p.name}_amount")
            pizza_amount += int(amount)
            PizzaOrder.objects.create(pizza=p, order=order, amount=amount)
        except Http404: #and return a string if it didn't work because i won't code an entire page just for one edgecase
            return HttpResponse(f"{pizza} was not found in database")
    

        
    return HttpResponseRedirect(f"{reverse('order_successful', kwargs={'language_code': language_code})}?time={math.ceil(pizza_amount/4)*15}") #and we look up what the url for the successful page is and redirect the user there
    #oh yeah and we assume one pizza takes 10 minutes to make and we can make 4 at the same time

def remove_order(request: HttpRequest, language_code):
    #delete the order associated with the order_id in the post list
    order = get_object_or_404(Order, id=request.POST.get("order_id"))
    order.delete()
    #and raise the score of the employee that sent the request
    employee = get_object_or_404(Employee, id=request.POST.get("emp_id"))
    employee.orders_cooked += 1
    employee.save()
    return HttpResponseRedirect(reverse("emp_index")) #and back you go weeeee....

