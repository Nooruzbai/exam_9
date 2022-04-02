from django.urls import path

from webapp.views.images import ImagesListView, ImageCreateView, ImageDeleteView

app_name = 'webapp'


urlpatterns = [
    path("", ImagesListView.as_view(), name="images_list_view"),
    path('image/create/', ImageCreateView.as_view(), name="image_create_view"),
    path('image/delete/<int:pk>/', ImageDeleteView.as_view(), name='image_delete_view'),
]
