from django.contrib import admin

# I don't really have to make it accessable via the admin panel
#Employee is handled automatically when i create a new user

from .models import Employee

admin.site.register(Employee)
