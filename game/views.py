from django.shortcuts import render
from django.contrib.staticfiles.views import serve

# Create your views here.

def game(request):
    return render(request, "game.html", {})

def dooklin_game(request):
    return render(request, "dook.html", {})

def hub(request):
    return render(request, "hub.html", {})



def ds(request):
    print("ds")
    return serve(request, "/static/games/BizzawayGame/TemplateData/style.css")
def da(request):
    print("da")
    return serve(request, "/static/games/BizzawayGame/Build/ActualGame.js")
def df(request):
    print("df")
    return serve(request, "/static/games/BizzawayGame/TemplateData/favicon.ico")