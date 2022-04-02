from django.shortcuts import render
from django.views.generic import ListView

from webapp.models import Image


class ImagesListView(ListView):
    template_name = 'images/images_list_view.html'
    model = Image
    context_object_name = "images"
    paginate_by = 10
    paginate_orphans = 0
    # ordering = ['category', 'name']


