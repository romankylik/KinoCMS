# Generated by Django 4.2 on 2023-05-11 17:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='SEO',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField(verbose_name='URL')),
                ('title', models.CharField(max_length=255, verbose_name='Title')),
                ('keywords', models.CharField(max_length=255, verbose_name='Keywords')),
                ('description', models.TextField(blank=True, verbose_name='Description')),
            ],
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to='photos/%Y/%m/%d/')),
                ('gallery', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cinemas.gallery')),
            ],
        ),
        migrations.CreateModel(
            name='Films',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Фільм')),
                ('big_photo', models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Головна картинка')),
                ('trailerURL', models.URLField(verbose_name='Трейлер')),
                ('type1', models.BooleanField(verbose_name='Тип 2D')),
                ('type2', models.BooleanField(verbose_name='Тип 3D')),
                ('type3', models.BooleanField(verbose_name='Тип imax')),
                ('seo', models.OneToOneField(db_column='seo_key', on_delete=django.db.models.deletion.CASCADE, related_name='film_key', to='cinemas.seo')),
            ],
            options={
                'verbose_name': 'Фільм',
                'verbose_name_plural': 'Фільми',
                'ordering': ['name'],
            },
        ),
    ]
