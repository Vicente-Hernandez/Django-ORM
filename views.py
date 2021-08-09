from django.shortcuts import render, HttpResponse, redirect
from .models import Movie

def index(request):
    context = {
        'saludo': 'Hola'
    }
    return render(request, 'index.html', context)


def second(request, name):
    return HttpResponse('Hola ' + name)


def peliculas(request):
    movies = Movie.objects.all()
    context = {
        'movies': movies,
    }
    return render(request, 'peliculas.html', context)


def pelis(request):
    nombre = request.POST['nombre']
    print(nombre)
    descripcion = request.POST['descripcion']
    print(descripcion)
    estreno = (request.POST['estreno'])
    print(estreno)
    duracion = (request.POST['duracion'])
    print(duracion)
    
    request.session['nombre'] = nombre
    request.session['descripcion'] = descripcion
    request.session['fecha'] = estreno
    request.session['duracion'] = duracion
    
    Movie.objects.create(title = request.session['nombre'], description = request.session['descripcion'], release_date = request.session['fecha'], duration = request.session['duracion'])
    
    #Movie.objects.save()
    
    return redirect('/peliculas')
