from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("order/", None, name="order"),
    path("contact/", None, name="contact"),
    path("imprint/", None, name="imprint"),
    path("privacy/", None, name="privacy")
]
