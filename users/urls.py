from django.urls import path
from .views import *


urlpatterns = [
    path('edit/', edit_users, name='edit_users'),
    path('list/', list_users, name='list_users'),
]