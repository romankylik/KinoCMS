from datetime import datetime
from django.forms import modelformset_factory
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from cinemas.views import pre_delete
from cinemas.forms import AddSEO
from cinemas.models import Photo, Gallery
from frontend.forms import AddNews
from frontend.models import News_and_Evens


@login_required
def baners(request):
    context = {
        'title': "Baners",
    }
    return render(request, 'frontend/index.html', context=context)



def add_news (request):
    factory = modelformset_factory(Photo, fields=('photo',), can_delete=True, extra=1)
    if request.method == 'POST':
        news_form = AddNews(request.POST, request.FILES)
        photoset = factory(request.POST, request.FILES)
        seo_form = AddSEO(request.POST, request.FILES)
        if all([news_form.is_valid(), seo_form.is_valid(), photoset.is_valid()]):
            gallery, created = Gallery.objects.get_or_create(name=f'News_{news_form.instance.name}')  # назва галереї буде film_назва_дата створення
            for form in photoset:
                if form.instance.photo:
                    form.instance.gallery = gallery
                    form.save()
            news_form.instance.gallery = gallery
            seo_form.save()
            news_form.instance.seo = seo_form.instance
            news_form.instance.type_object = 'news'
            news = news_form.save()
            Gallery.objects.filter(id=gallery.pk).update(name=f'News_id_{news.id}')
            return redirect('listnews')

    else:
        news_form = AddNews()
        seo_form = AddSEO()
        photoset = factory(queryset=Photo.objects.none())
    context = {
        'news_form': news_form,
        'seo_form': seo_form,
        'photoset': photoset,
        'title': "N e w s",
    }
    return render(request, 'frontend/add_news.html', context=context)
def news_edit (request, pk):
    # інстанс  який редагуємо
    get_news = get_object_or_404(News_and_Evens, pk=pk)
    factory = modelformset_factory(Photo, fields=('photo',), can_delete=True, extra=0)
    if request.method == 'POST':
        news_form = AddNews(request.POST, request.FILES,instance=get_news)
        photoset = factory(request.POST, request.FILES,queryset=Photo.objects.filter(gallery=get_news.gallery))
        seo_form = AddSEO(request.POST, request.FILES,instance=get_news.seo)
        print(news_form.errors)
        if all([news_form.is_valid(), seo_form.is_valid(), photoset.is_valid()]):
            for form in photoset:
                if form.cleaned_data.get('DELETE'):
                    pre_delete.send(sender=Photo,
                                    instance=form.instance)  # Відправити сигнал pre_delete для видалення медіа файлу
                    form.instance.delete()
                else:
                    if form.instance.photo:
                        form.instance.gallery = get_news.gallery
                        form.save()
            seo_form.save()
            news_form.save()
            return redirect('listnews')

    else:
        news_form = AddNews(instance=get_news)
        seo_form = AddSEO(instance=get_news.seo)
        photoset = factory(queryset=Photo.objects.filter(gallery=get_news.gallery))

    context = {
        'news_form': news_form,
        'seo_form': seo_form,
        'photoset': photoset,
        'title': f'{get_news.name}',
        'edit': True,
        'pk': pk
    }
    return render(request, 'frontend/add_news.html', context=context)

def list_news (request):
    news = News_and_Evens.objects.filter(type_object='news').values('id','name','date_create','date_publications')
    for i in news:
        if datetime.now() >= i['date_publications'].replace(tzinfo=None):
            i['status']= 'Активна'
        else:
            i['status'] = 'Неактивна'
    context = {'news': news,
               }
    return render(request, "frontend/list_news.html", context=context)



