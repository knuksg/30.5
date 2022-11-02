from django.db import models
from django.conf import settings
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill
# Create your models here.

class Story(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=20)
    subtitle = models.CharField(max_length=30)
    main_image = ProcessedImageField(
        upload_to="media/",
        processors=[ResizeToFill(300, 200)],
        format="JPEG",
        options={"quality": 90},
    )
    content = models.TextField(max_length=10000, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)