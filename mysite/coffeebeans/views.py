from django.shortcuts import render, get_object_or_404
from django.http import HttpRequest

from .models import Coffeebean


def index(request: HttpRequest):
    coffees = Coffeebean.objects.select_related("kind", "roast_level", "origin").order_by("id").all()
    context = {
        "coffeebeans": coffees
    }

    return render(request, 'coffeebeans/index.html', context=context)

def details(request: HttpRequest, pk: int):
    coffee = get_object_or_404(
        Coffeebean.objects.select_related("kind", "roast_level", "origin").prefetch_related("methods"),
        pk=pk
    )
    context = {
        "coffeebean": coffee,
    }
    return render(request, 'coffeebeans/details.html', context=context)
