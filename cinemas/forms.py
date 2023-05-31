from django import forms
from django.core.exceptions import ValidationError
from django.forms import widgets

from .models import *

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Field

class AddPhoto(forms.ModelForm):
    existing_images = forms.ModelChoiceField(queryset=Photo.objects.all(), empty_label=None)
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    class Meta:
        model = Photo
        fields = ['photo']


class AddFilm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    class Meta:
        model = Films
        fields = ['name', 'content', 'big_photo', 'trailerURL', 'type1', 'type2', 'type3']
        widgets = {
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),

                   }


class AddSEO(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    class Meta:
        model = SEO
        fields = ['url', 'title', 'keywords', 'description']
        widgets = {
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }


class AddCinema(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        model = Cinemas
        fields = ['name', 'content', 'logo', 'conditions', 'photo_banner']
        widgets = {
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'conditions': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }

class AddHall(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        model = Halls
        fields = ['number', 'content', 'schema_hall', 'photo_banner']
        widgets = {
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }