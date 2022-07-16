from django.urls import path, include
from .views import CoffeeListView, CoffeeDetailView

app_name = "coffeebeans"

urlpatterns = [
    # path("", index, name="list"),
    path("", CoffeeListView.as_view(), name="list"),
    path("<int:pk>/", CoffeeDetailView.as_view(), name="details"),

    # path("<str:kind_name>/", CoffeeKindListView.as_view(), name="kind-list")
]

