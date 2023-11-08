from django.test import TestCase

from webinterface.models import Ingredient, Order, Pizza, PizzaOrder
from employee.models import Employee
from django.contrib.auth.models import User


class Tests(TestCase):
    user = None
    dough = None
    ham = None
    tomato_sauce = None
    pizza = None

    def setUp(self):
        self.user = User.objects.create_user(username="robin", password="robin")
        self.dough = Ingredient.objects.create(name="dough", protein=5, carbs=50, fat=10)
        self.ham = Ingredient.objects.create(name="ham", protein=20, carbs=0, fat=3)
        self.tomato_sauce = Ingredient.objects.create(name="tomato sauce", protein=0, carbs=5, fat=1)

        self.pizza = Pizza.objects.create(name="Ham pizza", image="none.png", price=10)
        self.pizza.ingredients.add(self.dough)
        self.pizza.ingredients.add(self.ham)
        self.pizza.ingredients.add(self.tomato_sauce)
        self.pizza.save()


    def test_employee_model(self):
        self.assertEqual(Employee.objects.all().count(), User.objects.all().count())

    def test_ingredient_model(self):
        self.assertEqual(self.ham.get_carbs(), 0)
        self.assertEqual(self.tomato_sauce.get_carbs(), 5)
        self.assertEqual(self.dough.get_carbs(), 50)

    def test_pizza_model(self):
        pizza = Pizza.objects.get(pk="Ham pizza")
        self.assertEqual(pizza.get_protein(), 25)
        self.assertEqual(pizza.get_carbs(), 55)
        self.assertEqual(pizza.get_fat(), 14)
        self.assertEqual(pizza.get_calories(), 432)

    def test_order_model(self):
        order = Order.objects.create(customer="Robin Vita", email="robin.vita@gmail.com", notes="please more spicy")
        pizzaOrder = PizzaOrder.objects.create(pizza=self.pizza, order=order, amount=10)
        self.assertEqual(pizzaOrder.pizza.name, "Ham pizza")
        self.assertEqual(PizzaOrder.objects.all().count(), 1)
        order.delete()
        self.assertEqual(PizzaOrder.objects.all().count(), 0)

    def test_index(self):
        response = self.client.get('/en/', follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "index.html")

    def test_order(self):
        response = self.client.get('/en/order/', follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "order.html")

    def test_contact(self):
        response = self.client.get('/en/contact/', follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "contact.html")

    def test_imprint(self):
        response = self.client.get('/en/imprint/', follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "imprint.html")

    def test_privacy(self):
        response = self.client.get('/en/privacy/', follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "privacy.html")

    def test_order_successful(self):
        response = self.client.get('/en/order_successful', follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "order_successful.html")

    def test_employee(self):
        self.client.login(username="robin", password="robin")
        response = self.client.get("/mitarbeiter/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'emp_index.html')

        self.client.logout()
        response = self.client.get("/mitarbeiter/")
        self.assertEqual(response.status_code, 302)

    def test_order_add(self):
        response = self.client.post("/en/order/add/", data={'csrfmiddlewaretoken': ['6cYfjFAbP7PDDPKR8LTjqgHiIzfdoFEr1MwtEvpYRIXQqmKc5vyAkssXESqY2w8T'], 'customer': ['Robin Vita'], 'email': ['robin.vita@gmail.com'], 'selected_pizzas[]': ['Ham pizza'], 'Ham pizza_amount': ['3'], 'notes': ['make it spicy']})
        self.assertEqual(response.status_code, 302)
    
    def test_order_remove(self):
        order = Order.objects.create(customer="Robin Vita", email="robin.vita@gmail.com", notes="hey ho")
        employee = Employee.objects.get(user=self.user)
        start_value = employee.orders_cooked
        
        
        self.assertEqual(Order.objects.all().count(), 1)
        
        response = self.client.post("/en/order/remove/", data={'order_id': [str(order.pk)], 'emp_id': [str(employee.pk)]})
        employee.refresh_from_db()

        self.assertEqual(Order.objects.all().count(), 0)
        self.assertEqual(employee.orders_cooked, start_value+1)
        self.assertEqual(response.status_code, 302)