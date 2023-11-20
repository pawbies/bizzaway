from django.contrib import admin

#i put all the models here that i want to manage via the
#admin panel 
#i don't wanna code a dashboard for that stuff myself
#so i'll just take the easy route

from .models import Ingredient, Pizza, Order, PizzaOrder, Answer, Question

admin.site.register(Ingredient)
admin.site.register(Pizza)
admin.site.register(Order)
admin.site.register(PizzaOrder)

admin.site.register(Answer)
admin.site.register(Question)