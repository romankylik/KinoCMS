# Generated by Django 4.2 on 2023-05-30 12:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cinemas', '0003_halls_cinema_alter_halls_number_alter_photo_photo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cinemas',
            name='address',
        ),
        migrations.RemoveField(
            model_name='cinemas',
            name='coordinates',
        ),
    ]
