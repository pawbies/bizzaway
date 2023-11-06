#this mapps different urls to their views

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("mitarbeiter/", include("employee.urls")),
    path("<str:language_code>/", include("webinterface.urls")),
    path("game/", include("game.urls")),
    path('admin/', admin.site.urls),
]
