from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="emp_index"),
    path("login/", views.login, name="login"),
]
