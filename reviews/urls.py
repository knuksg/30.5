from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

# from .django.conf.static import static
app_name = "reviews"

urlpatterns = [
    path("", views.index, name="index"),
    path(
        "detail/<int:restaurant_pk>/review_detail/<int:review_pk>/",
        views.review_detail,
        name="review_detail",
    ),
    path("<int:pk>/review/", views.review_create, name="review_create"),
    path(
        "detail/<int:restaurant_pk>/delete/<int:review_pk>/",
        views.review_delete,
        name="review_delete",
    ),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
