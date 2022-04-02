from django.urls import path

from webapp.views.gallery import GalleryDetailView, GalleryCreateView, GalleryDeleteView, GalleryUpdateView
from webapp.views.images import ImagesListView, ImageCreateView, ImageDeleteView, ImageDetailView, ImageUpdateView

app_name = 'webapp'

urlpatterns = [
    path("", ImagesListView.as_view(), name="images_list_view"),
    path('image/create/', ImageCreateView.as_view(), name="image_create_view"),
    path('image/delete/<int:pk>/', ImageDeleteView.as_view(), name='image_delete_view'),
    path('image/details/<int:pk>/', ImageDetailView.as_view(), name='image_detail_view'),
    path('image/update/<int:pk>/', ImageUpdateView.as_view(), name='image_update_view'),
    path('gallery/details/<int:pk>', GalleryDetailView.as_view(), name="gallery_detail_view"),
    path('gallery/create/', GalleryCreateView.as_view(), name='gallery_create_view'),
    path('gallery/delete/<int:pk>/', GalleryDeleteView.as_view(), name='gallery_delete_view'),
    path('gallery/update/<int:pk>', GalleryUpdateView.as_view(), name='gallery_update_view')
]
