from django.db import models
from django.conf import settings

# Create your models here.


class Review(models.Model):
    restaurant = models.ForeignKey(
        "restaurants.Restaurant", related_name="reviews", on_delete=models.CASCADE
    )
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.TextField(max_length=500, null=True)
    RATING = (
        (1, "🍚"),
        (2, "🍚☕️"),
        (3, "🍚☕️🍷"),
        (4, "🍚☕️🍷🍰"),
        (5, "🍚☕️🍷🍰🍔"),
    )
    rating = models.IntegerField(choices=RATING, default=None)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class ReviewImage(models.Model):
    restaurant = models.ForeignKey(
        "restaurants.Restaurant", related_name="review_images", on_delete=models.CASCADE
    )
    reviews = models.ForeignKey(Review, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    photo1 = models.ImageField(upload_to="reviewBoard/images", blank=True)
    photo2 = models.ImageField(upload_to="reviewBoard/images", blank=True)
    photo3 = models.ImageField(upload_to="reviewBoard/images", blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
