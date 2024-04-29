from django.urls import path
from .views import SearchView


urlpatterns = [
    path('search/', SearchView, name='search'),
]
