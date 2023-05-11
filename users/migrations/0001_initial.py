# Generated by Django 4.2 on 2023-05-05 07:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name="Ім'я")),
                ('surname', models.CharField(max_length=255, verbose_name='Прізвище')),
                ('login', models.CharField(max_length=255, verbose_name='Псевдонім')),
                ('mail', models.EmailField(max_length=255)),
            ],
            options={
                'verbose_name': 'Користувач',
                'verbose_name_plural': 'Користувачі',
                'ordering': ['name'],
            },
        ),
    ]