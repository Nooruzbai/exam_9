from django.contrib.auth.models import User
from django.shortcuts import render
from django.urls import reverse
from django.views.generic import ListView, CreateView, DetailView, DeleteView

from webapp.forms import ImageForm
from webapp.models import Image


class ImagesListView(ListView):
    template_name = 'images/images_list_view.html'
    model = Image
    context_object_name = "images"
    paginate_by = 10
    paginate_orphans = 0
    ordering = ['date_created']


# PermissionRequiredMixin
class ImageCreateView(CreateView):
    model = Image
    template_name = 'images/image_create.html'
    form_class = ImageForm
    # permission_required = 'otzovik.add_product'

    def get_success_url(self):
        return reverse('webapp:images_list_view', kwargs={'pk': self.object.pk})


class ImageDetailView(DetailView):
    template_name = 'images/details_image.html'
    model = Image
    context_object_name = 'image'

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     users = User.objects.all()
    #
    #     if self.request.user.groups.filter(name="moderators"):
    #         context['users'] = users
    #     if reviews.filter(author=self.request.user):
    #         reviews = reviews.filter(author_id=self.request.user.id).filter(moderated=True)
    #         context['reviews'] = reviews
    #     return context


class ImageDeleteView(DeleteView):
    model = Image
    template_name = "images/delete_image.html"
    context_object_name = 'image'
    # permission_required = "otzovik.delete_product"

    def get_success_url(self):
        return reverse('webapp:images_list_view')
