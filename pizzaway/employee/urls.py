from django.urls import path, include

from . import views

#django also provides me with views for login and logout and stuff like that
#but figuring out how i can set that up would take longer than to do it myself

#and the latest_order is an api for the employee dashboard to check if there are
#new orders it didn't know yet

urlpatterns = [
    path("", views.index, name="emp_index"),
    path("login/", views.login_page, name="login_page"),
    path("account/login", views.login, name="login"),
    path("account/logout", views.logout, name="logout"),

    path("latest_order/", views.latest_order, name="latest_order"),
]
