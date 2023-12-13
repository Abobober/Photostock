from django.db import models
from django.conf import settings
from taggit.managers import TaggableManager
from django.contrib.auth import get_user_model
from imagekit.models import ImageSpecField
from pilkit.processors import Thumbnail


class Photo(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images')
    upload_date = models.DateTimeField(auto_now_add = True)
    tags = TaggableManager()
    image_thumbnail = ImageSpecField(source='image',
                                     processors=[Thumbnail(600, 360)],
                                     format='JPEG',
                                     options={'quality': 80})
    watermarked_image = models.ImageField(upload_to='watermarked_images', blank=True, null=True)

    def __str__(self) -> str:
        return self.title
    
