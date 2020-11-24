from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import *

urlpatterns = [
    path('success', success, name='success'),
    path('add_new', add_new_view, name='add_new'),
    path('available_books', available_books_view, name='avb'),
]
