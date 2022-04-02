from django.contrib.auth.mixins import PermissionRequiredMixin
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views.generic import ListView, CreateView, DetailView, DeleteView, UpdateView
from django.contrib.auth import get_user_model
from webapp.forms import ImageUpdateForm, ImageCreateForm, GalleryCreateForm, GalleryUpdateForm
from webapp.models import Image, Gallery

User = get_user_model()


# PermissionRequiredMixin
# class ImageCreateView(CreateView):
#     model = Image
#     template_name = 'images/image_create.html'
#     form_class = ImageCreateForm
#     # permission_required = 'otzovik.add_product'
#
#     def form_valid(self, form):
#         image = form.save(commit=False)
#         image.author.add(self.request.user)
#         image.save()
#         return super().form_valid(form)
#
#     # def get_photo_form(self):
#     #     form_kwargs = {'instance': self.object.profile}
#     #     if self.request.method == 'POST':
#     #         form_kwargs['data'] = self.request.POST
#     #         form_kwargs['files'] = self.request.FILES
#     #     return Image(**form_kwargs)
#
#     def get_success_url(self):
#         return reverse('webapp:images_list_view', kwargs={'pk': self.object.pk})
#
#
class GalleryDetailView(DetailView):
    template_name = 'gallery/details_gallery.html'
    model = Gallery
    context_object_name = 'gallery'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        images = self.object.images.all()
        context['images'] = images

        # if self.request.user.groups.filter(name="moderators"):
        #     context['users'] = users
        # if reviews.filter(author=self.request.user):
        #     reviews = reviews.filter(author_id=self.request.user.id).filter(moderated=True)
        #     context['reviews'] = reviews
        return context


class GalleryCreateView(CreateView):
    model = Gallery
    template_name = 'gallery/gallery_create_view.html'
    form_class = GalleryCreateForm

    def form_valid(self, form):
        # product = get_object_or_404(Gallery, pk=self.kwargs.get('pk'))
        # form.instance.product = product
        form.instance.author = self.request.user
        form.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('webapp:gallery_detail_view', kwargs={"pk": self.object.pk})


class GalleryDeleteView(PermissionRequiredMixin, DeleteView):
    model = Gallery
    template_name = "gallery/delete_gallery.html"
    context_object_name = 'gallery'
    permission_required = "webapp.delete_gallery"

    def has_permission(self):
        return super().has_permission() or self.request.user == self.get_object().author

    def get_success_url(self):
        return reverse('webapp:gallery_delete_view', kwargs={"pk": self.object.pk})


class GalleryUpdateView(PermissionRequiredMixin, UpdateView):
    form_class = GalleryUpdateForm
    template_name = "gallery/gallery_update.html"
    model = Gallery
    permission_required = "webapp.change_gallery"

    def has_permission(self):
        return super().has_permission() or self.request.user == self.get_object().author

    def get_success_url(self):
        return reverse('webapp:gallery_detail_view', kwargs={'pk': self.object.pk})

