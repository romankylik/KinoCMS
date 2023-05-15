from django.shortcuts import render, redirect
from .forms import *
from .models import *
from django.forms.models import modelformset_factory
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




def add_film(request):
    formset = modelformset_factory(Films, form=AddFilm)
    if request.method == 'POST':
        film_form = AddFilm(request.POST, request.FILES)
        photo_form = AddPhoto(request.POST, request.FILES)
        seo_form = AddSEO(request.POST, request.FILES)
        if film_form.is_valid() and seo_form.is_valid():
            gallery, created = Gallery.objects.get_or_create(name='films')
            photo_form.instance.gallery = gallery
            film_form.instance.gallery = gallery
            photo_form.save()
            seo_form.save()
            film_form.instance.seo = seo_form.instance
            film_form.save()
            return redirect('baners')

    else:
        film_form = AddFilm()
        seo_form = AddSEO()
        photo_form = AddPhoto()
    context = {
        'film_form': film_form,
        'seo_form': seo_form,
        'photo_form': photo_form,
        'title': "ADMIN Панель",
    }
    return render(request, 'cinemas/add_film.html', context=context)

