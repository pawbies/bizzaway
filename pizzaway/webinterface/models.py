from django.db import models

# Create your models here.

class Ingredient(models.Model):
    name = models.CharField(max_length=20, primary_key=True, blank=False)
    protein = models.IntegerField(blank=False, default=0)
    carbs = models.IntegerField(blank=False, default=0)
    fat = models.IntegerField(blank=False, default=0)

    def get_calories(self):
        return self.protein*4 + self.carbs*4 + self.fat*8
    
    def get_protein(self):
        return self.protein
    
    def get_fat(self):
        return self.fat
    
    def get_carbs(self):
        return self.carbs
    
    def __str__(self):
        return self.name


class Pizza(models.Model):
    name = models.CharField(max_length=20, primary_key=True, blank=False, null=False)
    ingredients = models.ManyToManyField(Ingredient, blank=False)
    image = models.ImageField(upload_to='pizzas/', null=False, blank=False, default="none.png")
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    def get_calories(self):
        total_calories = 0
        
        for ingredient in self.ingredients.all():
            total_calories += ingredient.get_calories()

        return total_calories
    
    def get_protein(self):
        total_protein = 0
        
        for ingredient in self.ingredients.all():
            total_protein += ingredient.get_protein()

        return total_protein

    def get_fat(self):
        total_fat = 0
        
        for ingredient in self.ingredients.all():
            total_fat += ingredient.get_fat()

        return total_fat

    def get_carbs(self):
        total_carbs = 0
        
        for ingredient in self.ingredients.all():
            total_carbs += ingredient.get_carbs()

        return total_carbs

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
