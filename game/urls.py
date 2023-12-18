from django.urls import path
from django.views.static import serve
from django.urls import re_path
from django.conf import settings

from . import views

urlpatterns = [
    path("", views.game, name="game"),
    path("dooklin_game/", views.dooklin_game, name="dooklin_game"),
    path("hub/", views.hub, name="hub"),
    re_path(r'^game.data$', serve, {'document_root': settings.BASE_DIR, 'path': '/static/games/connect/game.data'}),

    path("dooklin_game/TemplateData/style.css", serve, {'document_root': settings.BASE_DIR, 'path': '/static/games/BizzawayGame/TemplateData/style.css'}),
    path("dooklin_game/Build/ActualGame.js", serve, {'document_root': settings.BASE_DIR, 'path': '/static/games/BizzawayGame/Build/ActualGame.js'}),
    path("dooklin_game/TemplateData/favicon.ico", serve, {'document_root': settings.BASE_DIR, 'path': '/static/games/BizzawayGame/TemplateData/favicon.ico'}),
    path("dooklin_game/Build/ActualGame.loader.js", serve, {'document_root': settings.BASE_DIR, 'path': '/static/games/BizzawayGame/Build/ActualGame.loader.js'}),
    path("dooklin_game/Build/ActualGame.framework.js", serve, {'document_root': settings.BASE_DIR, 'path': '/static/games/BizzawayGame/Build/ActualGame.framework.js'}),
    path("dooklin_game/Build/ActualGame.wasm", serve, {'document_root': settings.BASE_DIR, 'path': '/static/games/BizzawayGame/Build/ActualGame.wasm'}),
    path("dooklin_game/Build/ActualGame.data", serve, {'document_root': settings.BASE_DIR, 'path': '/static/games/BizzawayGame/Build/ActualGame.data'}),

    path("dooklin_game/TemplateData/fullscreen-button.png", serve, {'document_root': settings.BASE_DIR, 'path': '/static/games/BizzawayGame/TemplateData/fullscreen-button.png'}),
    path("dooklin_game/TemplateData/MemoryProfiler.png", serve, {'document_root': settings.BASE_DIR, 'path': '/static/games/BizzawayGame/TemplateData/MemoryProfiler.png'}),
    path("dooklin_game/TemplateData/progress-bar-empty.png", serve, {'document_root': settings.BASE_DIR, 'path': '/static/games/BizzawayGame/TemplateData/progress-bar-empty.png'}),
    path("dooklin_game/TemplateData/progress-bar-empty-dark.png", serve, {'document_root': settings.BASE_DIR, 'path': '/static/games/BizzawayGame/TemplateData/progress-bar-empty-dark.png'}),
    path("dooklin_game/TemplateData/progress-bar-empty-light.png", serve, {'document_root': settings.BASE_DIR, 'path': '/static/games/BizzawayGame/TemplateData/progress-bar-empty-light.png'}),
    path("dooklin_game/TemplateData/progress-bar-full-dark.png", serve, {'document_root': settings.BASE_DIR, 'path': '/static/games/BizzawayGame/TemplateData/progress-bar-full-dark.png'}),
    path("dooklin_game/TemplateData/progress-bar-full-light.png", serve, {'document_root': settings.BASE_DIR, 'path': '/static/games/BizzawayGame/TemplateData/progress-bar-full-light.png'}),
    path("dooklin_game/TemplateData/unity-logo-dark.png", serve, {'document_root': settings.BASE_DIR, 'path': '/static/games/BizzawayGame/TemplateData/unity-logo-dark.png'}),
    path("dooklin_game/TemplateData/unity-logo-light.png", serve, {'document_root': settings.BASE_DIR, 'path': '/static/games/BizzawayGame/TemplateData/unity-logo-light.png'}),
    path("dooklin_game/TemplateData/webgl-logo.png", serve, {'document_root': settings.BASE_DIR, 'path': '/static/games/BizzawayGame/TemplateData/webgl-logo.png'}),
    path("dooklin_game/TemplateData/webmemd-icon.png", serve, {'document_root': settings.BASE_DIR, 'path': '/static/games/BizzawayGame/TemplateData/webmemd-icon.png'}),
]