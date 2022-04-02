from django.contrib import admin

from django.contrib import admin

# Register your models here.
from webapp.models import Image, Gallery


class ImageAdmin(admin.ModelAdmin):
    list_display = ['id', 'author', 'private', 'date_created']


class GalleryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'author', 'private', 'date_created']


admin.site.register(Image, ImageAdmin)
admin.site.register(Gallery, GalleryAdmin)

