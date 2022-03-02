from django.urls import path

from .views import index, search_city

urlpatterns = [
    path('', index, name='index'),
    path('search/', search_city, name='search-city'),
]
