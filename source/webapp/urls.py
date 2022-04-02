from django.urls import path

from webapp.views.images import ImagesListView

app_name = 'webapp'

urlpatterns = [
    path("", ImagesListView.as_view(), name="images_list_view"),
]
