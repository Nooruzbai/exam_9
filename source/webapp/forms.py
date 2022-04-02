from django import forms
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError

from .models import Image, Gallery

User = get_user_model()


class ImageCreateForm(forms.ModelForm):
    def __init__(self, request, *args, **kwargs):
        super(ImageCreateForm, self).__init__(*args, **kwargs)
        self.fields['gallery'].queryset = Gallery.objects.filter(author=request.user)

    class Meta:
        model = Image
        exclude = ('author', 'favourite','token', 'users')
        error_messages = {}
        widgets = {
            'date_started': forms.DateInput(format='%d-%m-%Y',
                                            attrs={'class': 'form-control', 'placeholder': 'Select a date',
                                                   'type': 'date'}),
            'date_closed': forms.DateInput(format='%d-%m-%Y',
                                           attrs={'class': 'form-control', 'placeholder': 'Select a date',
                                                  'type': 'date'})
        }


class ImageUpdateForm(forms.ModelForm):
    class Meta:
        model = Image
        exclude = ('author',)
        # error_messages = {
        #     "name": {
        #         "required": "The field is required to be filled"
        #     }
        # }


class GalleryCreateForm(forms.ModelForm):

    class Meta:
        model = Gallery
        exclude = ('author', 'favourite',)


class GalleryUpdateForm(forms.ModelForm):
    class Meta:
        model = Gallery
        exclude = ('author',)
