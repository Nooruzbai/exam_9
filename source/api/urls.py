from django.urls import path

from api.views import ApiImageDetailView, ApiGalleryDetailView

app_name = 'api'

urlpatterns = [
    path('image/<int:pk>/favourite/', ApiImageDetailView.as_view(), name='image'),
    path('gallery/<int:pk>/favourite/', ApiGalleryDetailView.as_view(), name='gallery'),
]
