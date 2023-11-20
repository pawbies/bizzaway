from django.db import models

#haha jokes on you
#who said i have to use sql if i want databases
#<insert evil laughter sounds here>

class Ingredient(models.Model):
    name = models.CharField(max_length=20, primary_key=True, blank=False)
    protein = models.IntegerField(blank=False, default=0)
    carbs = models.IntegerField(blank=False, default=0)
    fat = models.IntegerField(blank=False, default=0)

    def get_calories(self):
        return self.protein*4 + self.carbs*4 + self.fat*8
        #lil lesson in nutrition
        #a gram of protein has 4 calories
        #a gram of carbs also has 4
        #and a gram of fat 8
    
    def get_protein(self):
        return self.protein
    
    def get_fat(self):
        return self.fat
    
    def get_carbs(self):
        return self.carbs
    
    def __str__(self): #this is just for the admin panel
        return self.name


class Pizza(models.Model):
    name = models.CharField(max_length=20, primary_key=True, blank=False, null=False)
    #i'll just use the name of the pizza as the primary key
    ingredients = models.ManyToManyField(Ingredient, blank=False)
    #wow a many to many relationship
    #finally all the insy lessons are paying off
    image = models.ImageField(upload_to='pizzas/', null=False, blank=False, default="none.png")
    #you can add an picture that get's shown when you click the name on the menu
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    #and this is the price of the thing
    #it's probably too much because of inflation
    #but hey... everybody needs money and our employees just need a little more
    #and the azure servers this runs on don't pay for themselfs

    def get_calories(self): #add up all the calories of the ingredients
        total_calories = 0
        
        for ingredient in self.ingredients.all():
            total_calories += ingredient.get_calories()

        return total_calories
    
    def get_protein(self): #same jsut with protein and the other macros
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

    def __str__(self): #and also this thing... why can't it just do this by itself
        return self.name


class Order(models.Model):
    customer = models.CharField(max_length=50, blank=False, null=False)
    #name of the customer 
    email = models.CharField(max_length=50, blank=False, null=False)
    #email to scare of people that do fake orders
    #idk how but maybe it works
    notes = models.CharField(max_length=300, blank=False, null=False)
    #notes for the chef
    #mainly for weirdos with lactose intolerance
    #like
    #tf why do you want a pizza... there's so much cheese on most of them
    timestamp = models.DateTimeField(auto_now=True, blank=False, null=False)
    #and a timestamp to check if the order was already loaded on the employee dashboard

    def __str__(self):
        return self.customer


class PizzaOrder(models.Model):
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE, related_name='order')
    #foreign key to the pizza
    #the models.CASCADE just makes it so that when the referenced Pizza
    #or the order is deleted the PizzaOrder ceases to exist
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='pizza_order')
    #foreign key to the order
    amount = models.IntegerField(default=1)
    #and how many pizzas the customer wants of one kind

    def __str__(self):
        return f'{self.order.customer}`s {self.pizza.name}'


    
class Answer(models.Model):
    text = models.CharField(max_length=50, blank=False, null=False)


    def __str__(self):
        return self.text


class Question(models.Model):
    title = models.CharField(max_length=100, blank=False, null=False)
    subtitle = models.CharField(max_length=300, blank=False, null=False)

    
    class Types(models.Choices):
        Radio = 'Radio'
        Check = 'Check'
        Text = 'Text'
        Number = 'Number'

    type = models.CharField(
        max_length=15,
        choices=Types.choices,
        default=Types.Text,
    )

    answers = models.ManyToManyField(Answer, blank=True)

    def __str__(self):
        return self.title