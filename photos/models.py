from django.db import models
from django.conf import settings

class Photo(models.Model):
    title = models.CharField(max_length=100)
    discription = models.TextField(max_length=500, blank=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images')
    upload_date = models.DateTimeField()

    def __str__(self) -> str:
        return self.title
