from django.shortcuts import render
from .models import Photo

def photo_list(request):
    images = Photo.objects.all()
    return render(request, 'photos/photo_list.html', {'images': images})
