from django.urls import path, include
from .views import index, details

app_name = "coffeebeans"

urlpatterns = [
    path("", index, name="list"),
    path("<int:pk>/", details, name="details")
]

