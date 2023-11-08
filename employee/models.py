from django.db import models
from django.contrib.auth.models import User

from django.db.models.signals import post_save
from django.dispatch import receiver


#employee to extend the user model
class Employee(models.Model): 
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    orders_cooked = models.IntegerField(default=0)

    def __str__(self) -> str:
        return f"{self.user.username} user account"



#and those things make it so that for each user an employee account is created
@receiver(post_save, sender=User)
def create_employee(sender, instance, created, **kwargs):
    if created:
        Employee.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_employee(sender, instance, **kwargs):
    instance.employee.save()
