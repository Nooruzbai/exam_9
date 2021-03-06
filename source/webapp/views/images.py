import uuid

from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from django.views.generic import ListView, CreateView, DetailView, DeleteView, UpdateView
from django.contrib.auth import get_user_model
from webapp.forms import ImageUpdateForm, ImageCreateForm
from webapp.models import Image


User = get_user_model()


class ImagesListView(LoginRequiredMixin, ListView):
    template_name = 'images/images_list_view.html'
    model = Image
    context_object_name = "images"
    paginate_by = 10
    paginate_orphans = 0
    ordering = ['date_created']


class ImageCreateView(LoginRequiredMixin, CreateView):
    model = Image
    template_name = 'images/image_create.html'
    form_class = ImageCreateForm

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['request'] = self.request
        return kwargs

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('webapp:images_list_view')


class ImageDetailView(DetailView):
    template_name = 'images/details_image.html'
    model = Image
    context_object_name = 'image'

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     users = User.obje
    #     if self.request.user.groups.filter(name="moderators"):
    #         context['users'] = users
    #     if reviews.filter(author=self.request.user):
    #         reviews = reviews.filter(author_id=self.request.user.id).filter(moderated=True)
    #         context['reviews'] = reviews
    #     return context


class ImageDeleteView(PermissionRequiredMixin, DeleteView):
    model = Image
    template_name = "images/delete_image.html"
    context_object_name = 'image'
    permission_required = "webapp.delete_image"

    def has_permission(self):
        return super().has_permission() or self.request.user == self.get_object().author

    def get_success_url(self):
        return reverse('webapp:images_list_view')


class ImageUpdateView(PermissionRequiredMixin, UpdateView):
    form_class = ImageUpdateForm
    template_name = "images/update_image.html"
    model = Image
    permission_required = "webapp.change_image"

    def has_permission(self):
        return super().has_permission() or self.request.user == self.get_object().author

    def get_success_url(self):
        return reverse('webapp:image_detail_view', kwargs={'pk': self.object.pk})


class TokenGeneratorView(LoginRequiredMixin, View):

    def get(self, *args, **kwargs):
        image = Image.objects.get(pk=kwargs.get('pk'))
        token = uuid.uuid4()
        if not image.token:
            image.token = token
            image.save()
            return redirect('webapp:image_detail_view', pk=kwargs.get('pk'))
        return redirect('webapp:image_detail_view', pk=kwargs.get('pk'))


class DetailViewUIIDView(View):
    def get(self, request, *args, **kwargs):
        image = Image.objects.get(token=kwargs['uiid_pk'])
        return render(request, 'images/details_image.html', {'image': image})







