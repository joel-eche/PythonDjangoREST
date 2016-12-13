# -*- encoding: utf-8 -*-
from photos.models import Photo
from django import forms


class PhotoForm(forms.ModelForm):
    """
    Formulario para el model Photo
    """
    class Meta:
        model=Photo
        exclude=['owner']