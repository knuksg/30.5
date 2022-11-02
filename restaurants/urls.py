from django.urls import path
from . import views

app_name = "restaurants"

urlpatterns = [
    path("", views.main, name="main"),
    path("restaurants/", views.index, name="index"),
    path("restaurants/detail/<int:pk>/", views.detail, name="detail"),
    path("restaurants/create/", views.create, name="create"),
    path("restaurants/update/<int:pk>/", views.update, name="update"),
    path("restaurants/delete/<int:pk>/", views.delete, name="delete"),
]
