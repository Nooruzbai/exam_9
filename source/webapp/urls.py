from django.urls import path

from webapp.views.gallery import GalleryDetailView, GalleryCreateView, GalleryDeleteView, GalleryUpdateView
from webapp.views.images import ImagesListView, ImageCreateView, ImageDeleteView, ImageDetailView, ImageUpdateView, \
    TokenGeneratorView, DetailViewUIIDView

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
    path('gallery/update/<int:pk>', GalleryUpdateView.as_view(), name='gallery_update_view'),
    path('image/token/<int:pk>/', TokenGeneratorView.as_view(), name='token_generator_view'),
    path('image/token/<uuid:uiid_pk>/detail/view/', DetailViewUIIDView.as_view(), name='image_detail_uuid_view'),
]
# http://localhost:8000/webapp/image/ee629fcc-0a91-4b33-8f9f-7154e26fa6e3