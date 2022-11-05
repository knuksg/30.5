from django.urls import path
from . import views

app_name = "restaurants"

urlpatterns = [
    path("", views.top_lists, name="top_lists"),
    path("list/", views.list, name="list"),
    path("korea/", views.korea, name="korea"),
    path("china/", views.china, name="china"),
    path("japan/", views.japan, name="japan"),
    path("western/", views.western, name="western"),
    path("school/", views.school, name="school"),
    path("<int:pk>/", views.detail, name="detail"),
    path("create/", views.create, name="create"),
    path("<int:pk>/update/", views.update, name="update"),
    path("<int:pk>/delete/", views.delete, name="delete"),
    path("<int:pk>/like/", views.like, name="like"),
]
