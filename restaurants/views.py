from django.shortcuts import render
from .models import restaurants, categorys

def index(request):
    restaurant = restaurants.objects.get(pk=pk)
    return render(request, "restaurants/index.html")

def detail(request):
    restaurant = restaurants.objects.get(pk=pk)
    context = {
        'restaurant': restaurant
    }
    return render(request, "restaurants/detail.html", context)