# -*- encoding: utf-8 -*-
from django.core.exceptions import ValidationError

from photos.models import Photo
from django import forms

from photos.settings import BADWORDS


class PhotoForm(forms.ModelForm):
    """
    Formulario para el model Photo
    """
    class Meta:
        model=Photo
        exclude=['owner']

