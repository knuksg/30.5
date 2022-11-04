from django.urls import path
from . import views

app_name = "restaurants"

urlpatterns = [
    path("", views.main, name="main"),
    path("category/", views.category, name="category"),
    path("restaurants/", views.index, name="index"),
    path("restaurants/tag/", views.tag, name="tag"),
    path("restaurants/korea/", views.korea, name="korea"),
    path("restaurants/china/", views.china, name="china"),
    path("restaurants/japan/", views.japan, name="japan"),
    path("restaurants/western/", views.western, name="western"),
    path("restaurants/school/", views.school, name="school"),
    path("restaurants/detail/<int:pk>/", views.detail, name="detail"),
    path("restaurants/create/", views.create, name="create"),
    path("restaurants/update/<int:pk>/", views.update, name="update"),
    path("restaurants/delete/<int:pk>/", views.delete, name="delete"),
    path("restaurants/<int:pk>/like/", views.like, name="like"),
]
