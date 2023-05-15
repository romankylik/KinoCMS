from django import forms


from django.core.exceptions import ValidationError

from .models import *

class AddPhoto(forms.ModelForm):
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
        label_classes = {
            'type1': 'checkbox-inline',
            'type2': 'checkbox-inline',
            'type3': 'checkbox-inline',
        }

class AddSEO(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    class Meta:
        model = SEO
        fields = ['url', 'title', 'keywords', 'description']