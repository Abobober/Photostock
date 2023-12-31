from django.urls import path
from .views import (
    PhotoListView,
    PhotoTagListView,
    PhotoDetailView,
    PhotoCreateView,
    PhotoUpdateView,
    PhotoDeleteView,
    DownloadThumbnailView,
    DownloadOriginalImageView,
)
from django.conf import settings
from django.conf.urls.static import static

app_name = 'photo'

urlpatterns = [
    path('', PhotoListView.as_view(), name='list'),
    path('tag/<slug:tag>/', PhotoTagListView.as_view(), name='tag'),
    path('photo/<int:pk>/', PhotoDetailView.as_view(), name='detail'),
    path('photo/create/', PhotoCreateView.as_view(), name='create'),
    path('photo/<int:pk>/update/', PhotoUpdateView.as_view(), name='update'),
    path('photo/<int:pk>/delete/', PhotoDeleteView.as_view(), name='delete'),
    path('download_original/<int:pk>/', DownloadOriginalImageView.as_view(), name='download_original'),
    path('download_thumbnail/<int:pk>/', DownloadThumbnailView.as_view(), name='download_thumbnail'),
    
]


urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)