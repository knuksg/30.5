from django.db import models
from django.contrib.auth.models import AbstractUser
from PIL import Image
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill

# Create your models here.
class User(AbstractUser):
    phone = models.CharField(max_length=11, default='None')
    profile_image = ProcessedImageField(
        upload_to = 'media/',
        blank = True,
        processors=[ResizeToFill(100, 100)],
        format='JPEG',
        options={'quality': 80}
    )
    # like_restaurants = models.ManyToManyField()