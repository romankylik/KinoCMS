from django.urls import path
from .views import *


urlpatterns = [
    path('admin/', edit_users, name='edit_users'),
]