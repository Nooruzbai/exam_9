from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

from webapp.models import Image, Gallery


class ApiImageDetailView(APIView):
    def get(self, request, *args, **kwargs):
        image = Image.objects.get(pk=kwargs.get('pk'))
        if self.request.user in image.favourite.all():
            image.favourite.remove(request.user)
            return Response({}, status=200)
        else:
            image.favourite.add(request.user)
            image.favourite.save()
            return Response({}, status=200)


class ApiGalleryDetailView(APIView):

    def get(self, request, *args, **kwargs):
        gallery = Gallery.objects.get(pk=kwargs.get('pk'))
        if self.request.user in gallery.favourite.all():
            gallery.favourite.remove(request.user)
            return Response({}, status=200)
        else:
            gallery.favourite.add(request.user)
            gallery.favourite.save()
            return Response({}, status=200)
