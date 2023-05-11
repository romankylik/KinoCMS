from django.db import models

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
