from django.shortcuts import render, get_object_or_404
from django.http import HttpRequest
from django.views.generic import ListView, DetailView, DeleteView, CreateView

from .models import Coffeebean, CoffeeKind


# def index(request: HttpRequest):
#     coffees = Coffeebean.objects.select_related("kind", "roast_level", "origin").order_by("id").all()
#     context = {
#         "coffeebeans": coffees
#     }
#
#     return render(request, 'coffeebeans/index.html', context=context)

#
# def details(request: HttpRequest, pk: int):
#     coffee = get_object_or_404(
#         Coffeebean.objects.select_related("kind", "roast_level", "origin").prefetch_related("methods"),
#         pk=pk
#     )
#     context = {
#         "coffeebean": coffee,
#     }
#     return render(request, 'coffeebeans/details.html', context=context)


class CoffeeListView(ListView):
    queryset = Coffeebean.objects.order_by("id").all()
    context_object_name = "coffeebeans"
    template_name = "coffeebeans/index.html"

class CoffeeDetailView(DetailView):
    queryset = Coffeebean.objects.select_related("kind", "origin", "roast_level").prefetch_related("methods")
    context_object_name = "coffee_details"
    template_name = "coffeebeans/details.html"
