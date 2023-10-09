from django.db import models

# Create your models here.

class Ingredient(models.Model):
    name = models.CharField(max_length=20, primary_key=True, blank=False)

    def __str__(self):
        return self.name


class Pizza(models.Model):
    name = models.CharField(max_length=20, primary_key=True, blank=False, null=False)
    Ingredients = models.ManyToManyField(Ingredient, blank=False)

    def __str__(self):
        return self.name


class Order(models.Model):
    customer = models.CharField(max_length=50, blank=False, null=False)
    email = models.CharField(max_length=50, blank=False, null=False)
    notes = models.CharField(max_length=300, blank=False, null=False)
    timestamp = models.DateTimeField(auto_now=True, blank=False, null=False)
    pizzas = models.ManyToManyField(Pizza, blank=False)

    def __str__(self):
        return self.customer
