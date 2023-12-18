from django.shortcuts import render

# Create your views here.

def game(request):
    return render(request, "game.html", {})

def dooklin_game(request):
    return render(request, "BizzawayGame/index.html", {})

def hub(request):
    return render(request, "hub.html", {})