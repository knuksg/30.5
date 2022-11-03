from django.db import models
from reviews.models import Review

# Create your models here.
class Restaurant(models.Model):
    name = models.CharField(max_length=80)
    address = models.CharField(max_length=80)
    shop_number = models.CharField(max_length=80)
    between_pay = models.CharField(max_length=80)
    opening_time = models.CharField(max_length=80)
    break_day = models.CharField(max_length=80)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    hits = models.IntegerField(default=0)

    def __str__(self):
        return self.name

    @property
    def grade(self):
        reviews = Review.objects.filter(restaurant=self)
        if reviews:
            ratings = []
            for review in reviews:
                ratings.append(review.rating)
            return sum(ratings) / len(ratings)
        else:
            return 0





class Category(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    tag1 = models.CharField(blank=True, max_length=20)
    tag2 = models.CharField(blank=True, max_length=20)
    tag3 = models.CharField(blank=True, max_length=20)
    tag4 = models.CharField(blank=True, max_length=20)
    tag5 = models.CharField(blank=True, max_length=20)
