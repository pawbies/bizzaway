from django.contrib import admin

# Register your models here.

from .models import Ingredient, Pizza, Order

admin.site.register(Ingredient)
admin.site.register(Pizza)
admin.site.register(Order)
