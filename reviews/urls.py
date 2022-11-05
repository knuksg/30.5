from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

# from .django.conf.static import static
app_name = "reviews"

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:restaurant_pk>/create/", views.review_create, name="review_create"),
    path("<int:restaurant_pk>/<int:review_pk>/detail/", views.review_detail, name="review_detail"),
    path("<int:restaurant_pk>/<int:review_pk>/delete/", views.review_delete, name="review_delete"),
    path("<int:restaurant_pk>/<int:review_pk>/update/", views.review_update, name="review_update"),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
