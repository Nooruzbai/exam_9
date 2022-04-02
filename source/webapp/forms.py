from django import forms
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError

from .models import Image, Gallery

User = get_user_model()


class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = "__all__"
        error_messages = {
            "name": {
                "required": "The field is required to be filled"
            }
        }
