from datetime import datetime

from django.db import models
from cinemas.models import SEO, Gallery
# Create your models here.
class Baners(models.Model):
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/")
    type_obj = models.CharField(max_length=255, verbose_name="Тип")
    speed = models.SmallIntegerField(verbose_name="Швидкість обертання")
    active = models.BooleanField(verbose_name="Статус")
    trailerURL = models.URLField(blank=True, verbose_name="URL")
    text = models.CharField(max_length=255,blank=True)

    class Meta:
        verbose_name = 'Банер'
        verbose_name_plural = 'Банери'

class Background_Baner(models.Model):
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/")
    active = models.BooleanField(verbose_name="Статус")

    class Meta:
        verbose_name = 'Банер заднього фону'

class Pages(models.Model):
    name = models.CharField(max_length=255, verbose_name="Назва Сторінки")
    content = models.TextField(blank=True, verbose_name="Опис")
    main_photo = models.ImageField(upload_to="photos/%Y/%m/%d/", verbose_name="Головна картинка")
    gallery = models.OneToOneField(Gallery, on_delete=models.CASCADE)
    seo = models.OneToOneField(SEO, on_delete=models.CASCADE)
    date_create = models.DateTimeField(auto_now_add=True, verbose_name="Дата створення")


class News_and_Evens (Pages):
    videoURL = models.URLField(verbose_name="Відео")
    date_publications = models.DateTimeField(verbose_name="Дата публікації")
    type_object = models.CharField(max_length=255, verbose_name="Тип")