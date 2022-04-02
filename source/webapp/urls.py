from django.urls import path

from webapp.views.gallery import GalleryDetailView
from webapp.views.images import ImagesListView, ImageCreateView, ImageDeleteView, ImageDetailView, ImageUpdateView

app_name = 'webapp'

urlpatterns = [
    path("", ImagesListView.as_view(), name="images_list_view"),
    path('image/create/', ImageCreateView.as_view(), name="image_create_view"),
    path('image/delete/<int:pk>/', ImageDeleteView.as_view(), name='image_delete_view'),
    path('image/details/<int:pk>/', ImageDetailView.as_view(), name='image_detail_view'),
    path('image/update/<int:pk>/', ImageUpdateView.as_view(), name='image_update_view'),
    path('gallery/details/<int:pk>', GalleryDetailView.as_view(), name="gallery_detail_view"),
    path('gallery/image/create/<int:pk>', GalleryImageCreateView.as_view(), name='gallery_image_create_view')
]
