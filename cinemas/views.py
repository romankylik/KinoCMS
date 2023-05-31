from django.db.models.signals import pre_delete
from django.dispatch import receiver
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse

from .forms import *
from .models import *
from django.contrib.auth.decorators import login_required                #Перевірка чи користувач залогінився
from django.contrib.admin.views.decorators import staff_member_required #Перевірка на адміністратора
from django.forms.models import modelformset_factory, formset_factory, inlineformset_factory


def index(request):
    if request.method == 'POST':
        form = AddPhoto(request.POST, request.FILES)
        if form.is_valid():
            gallery, created = Gallery.objects.get_or_create(name='baners')
            form.instance.gallery = gallery
            form.save()
            return redirect('baners')

    else:
        form = AddPhoto()
    context = {
        'form': form,
        'title': "ADMIN Панель",
    }
    return render(request, 'cinemas/index.html', context=context)

def list_films(request):
    films = Films.objects.all()[:6]
    context = {
        'films': films
    }
    return render(request, 'cinemas/list_films.html', context=context)
def film_edit(request, pk):
    # інстанс фільму який редагуємо
    film = get_object_or_404(Films, pk=pk)
    film_form = AddFilm(instance=film)
    seo_form = AddSEO(instance=film.seo)
    factory = modelformset_factory(Photo, fields=('photo',), can_delete=True, extra=0)
    photoset = factory(queryset=Photo.objects.filter(gallery=film.gallery))

    if request.method == 'POST':
        film_form = AddFilm(request.POST, request.FILES, instance=film)
        seo_form = AddSEO(request.POST, request.FILES, instance=film.seo)
        photoset = factory(request.POST, request.FILES, queryset=Photo.objects.filter(gallery=film.gallery))
        if all([film_form.is_valid(), seo_form.is_valid(), photoset.is_valid()]):
            #обновляємо фото
            for form in photoset:
                if form.cleaned_data.get('DELETE'):
                    pre_delete.send(sender=Photo,
                                    instance=form.instance)  # Відправити сигнал pre_delete для видалення медіа файлу
                    form.instance.delete()
                else:
                    if form.instance.photo:
                        form.instance.gallery = film.gallery
                        form.save()
            #Зберігаємо сео та фільм
            seo_form.save()
            film_form.save()

        return redirect('listfilms')

    #Видалення медіа файлу з папки при видаленні обєтку Photo
    @receiver(pre_delete, sender=Photo)
    def delete_photo(sender, instance, **kwargs):
        # Виконати дії для видалення медіа файлу, пов'язаного з фото
        if instance.photo:
            instance.photo.delete()
    context = {
        'film_form': film_form,
        'seo_form': seo_form,
        'photoset': photoset,
        'title': f'{film.name}',
        'edit': True,
        'pk': pk
    }
    return render(request, 'cinemas/add_film.html', context=context)
def prototyp():
    ...

@login_required
def add_film(request):
    factory = modelformset_factory(Photo, fields=('photo',), can_delete=True, extra=1)
    if request.method == 'POST':
        film_form = AddFilm(request.POST, request.FILES)
        photoset = factory(request.POST, request.FILES)
        seo_form = AddSEO(request.POST, request.FILES)
        if all([film_form.is_valid(), seo_form.is_valid(), photoset.is_valid()]):
            gallery, created = Gallery.objects.get_or_create(name=f'film_{film_form.instance.name}')# назва галереї буде film_назва_дата створення
            for form in photoset:
                if form.instance.photo:
                    form.instance.gallery = gallery
                    form.save()
            film_form.instance.gallery = gallery
            seo_form.save()
            film_form.instance.seo = seo_form.instance
            film = film_form.save()
            Gallery.objects.filter(id=gallery.pk).update(name= f'film_id_{film.id}')
            return redirect('listfilms')

    else:
        film_form = AddFilm()
        seo_form = AddSEO()
        photoset = factory(queryset=Photo.objects.none())
    context = {
        'film_form': film_form,
        'seo_form': seo_form,
        'photoset': photoset,
        'title': "F i l m",
    }
    return render(request, 'cinemas/add_film.html', context=context)
@staff_member_required
def add_cinema(request):
    factory = modelformset_factory(Photo, fields=('photo',), can_delete=True, extra=1)
    factory2 = modelformset_factory(Halls, fields=('number', 'content', 'schema_hall', 'photo_banner', 'cinema'), can_delete=True, extra=1)
    if request.method == 'POST':
        cinema_form = AddCinema(request.POST, request.FILES)
        photoset = factory(request.POST, request.FILES)
        seo_form = AddSEO(request.POST, request.FILES)
        if all([cinema_form.is_valid(), seo_form.is_valid(), photoset.is_valid()]):
            gallery, created = Gallery.objects.get_or_create(name=f'film_{cinema_form.instance.name}')# назва галереї буде film_назва_дата створення
            for form in photoset:
                if form.instance.photo:
                    form.instance.gallery = gallery
                    form.save()
            cinema_form.instance.gallery = gallery
            seo_form.save()
            cinema_form.instance.seo = seo_form.instance
            cinema = cinema_form.save()
            Gallery.objects.filter(id=gallery.pk).update(name=f'cinema_id_{cinema.id}')
            return redirect('home')
    else:
        cinema_form = AddCinema()
        seo_form = AddSEO()
        photoset = factory(queryset=Photo.objects.none())
        hallset = factory2(queryset=Halls.objects.all())
    context = {
        'cinema_form': cinema_form,
        'seo_form': seo_form,
        'photoset': photoset,
        'hallset' : hallset,
        'title': "C i n e m a",
    }
    return render(request, 'cinemas/add_cinema.html', context=context)

def add_hall(request):
    factory = modelformset_factory(Photo, fields=('photo',), can_delete=True, extra=1)
    if request.method == 'POST':
        hall_form = AddHall(request.POST, request.FILES)
        photoset = factory(request.POST, request.FILES)
        seo_form = AddSEO(request.POST, request.FILES)
        if all([hall_form.is_valid(), seo_form.is_valid(), photoset.is_valid()]):
            gallery, created = Gallery.objects.get_or_create(name=f'Hall_{hall_form.instance.number}')# назва галереї буде film_назва_дата створення
            for form in photoset:
                if form.instance.photo:
                    form.instance.gallery = gallery
                    form.save()
            hall_form.instance.gallery = gallery
            seo_form.save()
            hall_form.instance.seo = seo_form.instance
            # обєкт кінотеатр треба виправити
            cinema, cin_created = Cinemas.objects.get_or_create(name=f'Hall_{hall_form.instance.number}')
            hall_form.instance.cinema= cinema
            hall_id = hall_form.save()
            #Gallery.objects.filter(id=gallery.pk).update(name= f'Hall_id_{hall_id.id}')
            return redirect('listfilms')

    else:
        hall_form = AddHall()
        seo_form = AddSEO()
        photoset = factory(queryset=Photo.objects.none())
    context = {
        'hall_form': hall_form,
        'seo_form': seo_form,
        'photoset': photoset,
        'title': "H a l l",
    }
    return render(request, 'cinemas/add_hall.html', context=context)
def hall_edit(request, pk):
    # інстанс фільму який редагуємо
    hall = get_object_or_404(Halls, pk=pk)
    hall_form = AddHall(instance=hall)
    seo_form = AddSEO(instance=hall.seo)
    factory = modelformset_factory(Photo, fields=('photo',), can_delete=True, extra=0)
    photoset = factory(queryset=Photo.objects.filter(gallery=hall.gallery))

    if request.method == 'POST':
        hall_form = AddHall(request.POST, request.FILES, instance=hall)
        seo_form = AddSEO(request.POST, request.FILES, instance=hall.seo)
        photoset = factory(request.POST, request.FILES, queryset=Photo.objects.filter(gallery=hall.gallery))
        if all([hall_form.is_valid(), seo_form.is_valid(), photoset.is_valid()]):
            #обновляємо фото
            for form in photoset:
                if form.cleaned_data.get('DELETE'):
                    pre_delete.send(sender=Photo,
                                    instance=form.instance)  # Відправити сигнал pre_delete для видалення медіа файлу
                    form.instance.delete()
                else:
                    if form.instance.photo:
                        form.instance.gallery = hall.gallery
                        form.save()
            #Зберігаємо сео та фільм
            seo_form.save()
            hall_form.save()

        return redirect('listfilms')

    #Видалення медіа файлу з папки при видаленні обєтку Photo
    @receiver(pre_delete, sender=Photo)
    def delete_photo(sender, instance, **kwargs):
        # Виконати дії для видалення медіа файлу, пов'язаного з фото
        if instance.photo:
            instance.photo.delete()
    context = {
        'film_form': hall_form,
        'seo_form': seo_form,
        'photoset': photoset,
        'title': f'{hall.number}',
        'edit': True,
        'pk': pk
    }
    return render(request, 'cinemas/add_hall.html', context=context)

