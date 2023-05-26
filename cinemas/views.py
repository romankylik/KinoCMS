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
    film = get_object_or_404(Films, pk=pk)
    film_form = AddFilm(instance=film)
    seo_form = AddSEO(instance=film.seo)

    factory = modelformset_factory(Photo, fields=('photo',), can_delete=True, extra=0)
    photoset = factory(queryset=Photo.objects.filter(gallery=film.gallery))

    if request.method == 'POST':
        photoset = factory(request.POST, request.FILES, queryset=Photo.objects.filter(gallery=film.gallery))

        if photoset.is_valid():
            print(photoset.errors)
            for form in photoset:
                if form.cleaned_data.get('DELETE'):
                    form.instance.delete()
                else:
                    form.instance.gallery = film.gallery
                    form.save()
        else:
            print(photoset.errors)
        return redirect('listfilms')


    context = {
        'film_form': film_form,
        'seo_form': seo_form,
        'photoset': photoset,
        'title': "F i l m",

        'edit': True,
        'pk': pk
    }
    return render(request, 'cinemas/add_film.html', context=context)

@login_required
def add_film(request, inst_f = None):
    factory = modelformset_factory(Photo, fields=('photo',), can_delete=True, extra=1)
    if request.method == 'POST':
        film_form = AddFilm(request.POST, request.FILES, instance=inst_f)
        photoset = factory(request.POST, request.FILES)
        seo_form = AddSEO(request.POST, request.FILES)
        print(film_form.is_valid())
        print(seo_form.is_valid())
        if film_form.is_valid() and seo_form.is_valid() and photoset.is_valid():
            gallery, created = Gallery.objects.get_or_create(name=f'film_{film_form.instance.name}')# назва галереї буде film_назва_дата створення
            for form in photoset:
                form.instance.gallery = gallery
                form.save()
            film_form.instance.gallery = gallery
            seo_form.save()
            film_form.instance.seo = seo_form.instance
            film_id = film_form.save()
            Gallery.objects.filter(id=gallery.pk).update(name= f'film_id_{film_id.id}')
            print(gallery.pk)
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
    if request.method == 'POST':
        cinema_form = AddCinema(request.POST, request.FILES)
        photo_form = AddPhoto(request.POST, request.FILES)
        seo_form = AddSEO(request.POST, request.FILES)
        if cinema_form.is_valid() and seo_form.is_valid():
            gallery, created = Gallery.objects.get_or_create(name=f'cinema{cinema_form.instance.pk}')# назва галереї буде film+id фільма
            photo_form.instance.gallery = gallery
            cinema_form.instance.gallery = gallery
            photo_form.save()
            seo_form.save()
            cinema_form.instance.seo = seo_form.instance
            cinema_form.save()
            return redirect('home')

    else:
        cinema_form = AddFilm()
        seo_form = AddSEO()
        photo_form = AddPhoto()
    context = {
        'cinema_form': cinema_form,
        'seo_form': seo_form,
        'photo_form': photo_form,
        'title': "C i n e m a",
    }
    return render(request, 'cinemas/add_cinema.html', context=context)
