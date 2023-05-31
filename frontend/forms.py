from django.contrib.auth import password_validation
from django.core.exceptions import ValidationError
from django import forms
from .models import *
class AddNews(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    class Meta:
        model = News_and_Evens
        fields = ['name', 'content', 'main_photo', 'date_publications', 'videoURL']
        widgets = {
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }