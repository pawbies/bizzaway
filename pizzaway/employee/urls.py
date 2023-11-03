from django.urls import path, include

from . import views

urlpatterns = [
    path("", views.index, name="emp_index"),
    path("login/", views.login_page, name="login_page"),
    path("account/login", views.login, name="login"),
    path("account/logout", views.logout, name="logout"),

    path("latest_order/", views.latest_order, name="latest_order"),
]
