from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("order/", views.order, name="order"),
    path("contact/", views.contact, name="contact"),
    path("imprint/", views.imprint, name="imprint"),
    path("privacy/", views.privacy, name="privacy"),

    path("order/add/", views.add_order, name="add_order"),
    path("order/remove/", views.remove_order, name="remove_order"),
]
