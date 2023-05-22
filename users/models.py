from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import AbstractUser
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.db.models.functions import datetime
from django.urls import reverse



class AdvUsers(AbstractUser):
    town = models.CharField(max_length=255, verbose_name="Місто")
    address = models.CharField(max_length=255, verbose_name="Адреса")
    bank_card = models.IntegerField(default=0 )
    language = models.CharField(max_length=255, verbose_name="Мова")
    gender = models.CharField(max_length=255, choices=[], verbose_name="Стать")
    phone_number = PhoneNumberField(blank=True)
    date_birth = models.DateTimeField(default='2000-01-01 10:00', verbose_name="Дата народження")


'''
class Tickets(models.Model):
    user = models.ForeignKey('Users', on_delete=models.PROTECT, verbose_name="Клієнт")
    session = models.ForeignKey('Sessions', on_delete=models.PROTECT, verbose_name="Сеанс фільму")
    date_buy = models.DateTimeField(auto_now_add=True, verbose_name="Дата покупки")
    state_buy = models.BooleanField(default=True, verbose_name="Стан оплати")
    range = models.SmallIntegerField()
    place = models.SmallIntegerField()

    def __str__(self):
        return self.pk

    class Meta:
        verbose_name = 'Квиток'
        verbose_name_plural = 'Квитки'


class Sessions(models.Model):
    #film = models.OneToOneField()
    #cinema = models.OneToOneField()
    #hall = models.OneToOneField()
    show_date = models.DateTimeField( verbose_name="Дата сеансу")
    date_add = models.DateTimeField(auto_now_add=True, verbose_name="Дата створення")
    reservation = models.BooleanField(default=False, verbose_name="Бронювання")

'''






