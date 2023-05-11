from django.db import models

class SEO(models.Model):
    url = models.URLField(verbose_name="URL")
    title = models.CharField(max_length=255, verbose_name="Title")
    keywords = models.CharField(max_length=255, verbose_name="Keywords")
    description = models.TextField(blank=True, verbose_name="Description")
    #film = models.OneToOneField('Films', on_delete=models.CASCADE, primary_key=True, related_name='seo')

class Films(models.Model):
    name = models.CharField(max_length=255, verbose_name="Фільм")
    big_photo = models.ImageField(upload_to="photos/%Y/%m/%d/", verbose_name="Головна картинка")
    trailerURL = models.URLField(verbose_name="Трейлер")
    type1 = models.BooleanField(verbose_name="Тип 2D")
    type2 = models.BooleanField(verbose_name="Тип 3D")
    type3 = models.BooleanField(verbose_name="Тип imax")
    seo = models.OneToOneField('SEO', on_delete=models.CASCADE, related_name="film_key", db_column='seo_key')

    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'Фільм'
        verbose_name_plural = 'Фільми'
        ordering = ['name']
