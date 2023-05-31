from django.urls import path
from .views import *


urlpatterns = [
    path('', baners, name='baners'),
    path('addnews/', add_news, name='addnews'),
    path('listnews/', list_news, name='listnews'),
    path('news/<int:pk>/', news_edit, name='news_edit'),
]