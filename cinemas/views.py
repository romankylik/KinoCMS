from django.shortcuts import render, redirect
from .forms import *
from .models import *
from django.contrib.auth.decorators import login_required                #Перевірка чи користувач залогінився
from django.contrib.admin.views.decorators import staff_member_required #Перевірка на адміністратора
from django.forms.models import modelformset_factory, formset_factory
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



@login_required
def add_film(request):
    factory = modelformset_factory(Photo, fields=('photo',), extra=1)

    #for form in factory:
    #print(factory)
    #set_photo = modelformset_factory(Photo, , fields=('photo',))
    #set = set_photo(request.POST or None)

    if request.method == 'POST':
        film_form = AddFilm(request.POST, request.FILES)
        photoset = factory(request.POST, request.FILES)
        seo_form = AddSEO(request.POST, request.FILES)
        print(photoset)
        if film_form.is_valid() and seo_form.is_valid():
            gallery, created = Gallery.objects.get_or_create(name=f'film_{film_form.instance.name}')# назва галереї буде film+id фільма
            for form in photoset:
                form.instance.gallery = gallery
                form.save()
            film_form.instance.gallery = gallery
            seo_form.save()
            film_form.instance.seo = seo_form.instance
            film_form.save()
            return redirect('baners')

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
