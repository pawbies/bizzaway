from django.db import models
from django.contrib.auth.models import User

from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.

class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    orders_cooked = models.IntegerField(default=0)

    def __str__(self) -> str:
        return f"{self.user.username} user account"



@receiver(post_save, sender=User)
def create_employee(sender, instance, created, **kwargs):
    print("create employee")
    if created:
        Employee.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_employee(sender, instance, **kwargs):
    print("save employee")
    instance.employee.save()
