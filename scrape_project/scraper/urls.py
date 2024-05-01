from django.urls import path
from .views import SearchView, PlotView


urlpatterns = [
    path('search/', SearchView, name='search'),
    path('plot/', PlotView, name='plot'),
]
