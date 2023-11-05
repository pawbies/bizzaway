from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

#those are all pretty self-explanatory
urlpatterns = [
    path("", views.index, name="index"),
    path("order/", views.order, name="order"),
    path("contact/", views.contact, name="contact"),
    path("imprint/", views.imprint, name="imprint"),
    path("privacy/", views.privacy, name="privacy"),
    path("order_successful", views.order_successful, name="order_successful"),

    path("order/add/", views.add_order, name="add_order"),
    path("order/remove/", views.remove_order, name="remove_order"),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
#the line above makes it so i can access the pizza images
#idk how bur after searching through stackoverflow i found this
#and like i like to say... never touch a running system
