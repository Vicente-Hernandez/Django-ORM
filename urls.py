from django.urls import path
from . import views
urlpatterns = [
    path('', views.index),
    path('second/<name>', views.second),
    path('peliculas', views.peliculas),
    path('pelis', views.pelis),
]
