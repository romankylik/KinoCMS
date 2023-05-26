from django.conf.urls.static import static
from django.urls import path

from django.conf import settings
from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('films/', list_films, name='listfilms'),
    path('film/<int:pk>/', film_edit, name='film_edit'),
    path('addfilm/', add_film, name='addfilm'),
    path('addcinema/', add_cinema, name='addcinema'),


]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)