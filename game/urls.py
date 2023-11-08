from django.urls import path
from django.views.static import serve
from django.urls import re_path
from django.conf import settings

from . import views

urlpatterns = [
    path("", views.game, name="game"),
    re_path(r'^game.data$', serve, {'document_root': settings.BASE_DIR, 'path': 'game/static/game.data'}),
]
