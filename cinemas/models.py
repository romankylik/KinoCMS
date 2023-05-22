from django.db import models

class SEO(models.Model):
    url = models.URLField(verbose_name="URL")
    title = models.CharField(max_length=255, verbose_name="Title")
    keywords = models.CharField(max_length=255, verbose_name="Keywords")
    description = models.TextField(blank=True, verbose_name="Description")
    #film = models.OneToOneField('Films', on_delete=models.CASCADE, primary_key=True, related_name='seo')

class Films(models.Model):
    name = models.CharField(max_length=255, verbose_name="Фільм")
    content = models.TextField(blank=True, verbose_name="Опис")
    big_photo = models.ImageField(upload_to="photos/%Y/%m/%d/", verbose_name="Головна картинка")
    trailerURL = models.URLField(verbose_name="Трейлер")
    type1 = models.BooleanField(verbose_name="2D")
    type2 = models.BooleanField(verbose_name="3D")
    type3 = models.BooleanField(verbose_name="imax")
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Дата створення")
    seo = models.OneToOneField('SEO', on_delete=models.CASCADE)
    gallery = models.OneToOneField('Gallery', on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'Фільм'
        verbose_name_plural = 'Фільми'
        ordering = ['name']

class Cinemas(models.Model):
    name = models.CharField(max_length=255, verbose_name="Кінотеатр")
    content = models.TextField(blank=True, verbose_name="Опис")
    conditions = models.TextField(blank=True, verbose_name="Умови")
    logo = models.ImageField(upload_to="photos/%Y/%m/%d/", verbose_name="Логотип")
    photo_banner = models.ImageField(upload_to="photos/%Y/%m/%d/", verbose_name="Фото банера")
    address = models.TextField(blank=True, verbose_name="Адреса")
    coordinates = models.CharField(max_length=255, verbose_name="Координати")
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Дата створення")
    seo = models.OneToOneField('SEO', on_delete=models.CASCADE)
    gallery = models.OneToOneField('Gallery', on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'Кінотеатр'
        verbose_name_plural = 'Кінотеатри'
        ordering = ['name']

class Halls(models.Model):
    number = models.IntegerField(default=0, verbose_name="Номер залу")
    content = models.TextField(blank=True, verbose_name="Опис")
    schema_hall = models.ImageField(upload_to="photos/%Y/%m/%d/", verbose_name="Схема залу")
    photo_banner = models.ImageField(upload_to="photos/%Y/%m/%d/", verbose_name="Фото банера")
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Дата створення")
    cinema = models.ForeignKey('Cinemas', on_delete=models.CASCADE, verbose_name="Кінотеатр")
    seo = models.OneToOneField('SEO', on_delete=models.CASCADE)
    gallery = models.OneToOneField('Gallery', on_delete=models.CASCADE)

    def __str__(self):
        return f'Зал {self.number}'
    class Meta:
        verbose_name = 'Зал'
        verbose_name_plural = 'Зали'
        ordering = ['number']

class Gallery(models.Model):
    name = models.CharField(max_length=255, blank=True, unique=True)

class Photo(models.Model):
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/")
    gallery = models.ForeignKey('Gallery', on_delete=models.CASCADE)
