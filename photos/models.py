from django.db import models
from django.conf import settings
from taggit.managers import TaggableManager
from django.contrib.auth import get_user_model

class Photo(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images')
    upload_date = models.DateTimeField(auto_now_add = True)
    tags = TaggableManager()

    def __str__(self) -> str:
        return self.title
