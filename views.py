from django.shortcuts import render, HttpResponse, redirect
from .models import Dojos, Movie, Ninjas


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

    Movie.objects.create(title=request.session['nombre'], description=request.session['descripcion'], release_date=request.session['fecha'], duration=request.session['duracion'])

    return redirect('/peliculas')


def dojos(request):
    dojos = Dojos.objects.all()

    ninjas = Ninjas.objects.all()

    context = {
        'dojos': dojos,
        'ninjas': ninjas,
    }
    return render(request, 'samurai.html', context)


def sensei(request):

    name_dojo = request.POST['name_dojo']
    print(name_dojo)
    city = request.POST['city']
    print(city)
    state = (request.POST['state'])
    print(state)
    desc = (request.POST['desc'])
    print(desc)

    request.session['name_dojo'] = name_dojo
    request.session['city'] = city
    request.session['state'] = state
    request.session['desc'] = desc

    Dojos.objects.create(name=request.session['name_dojo'], city = request.session['city'], state = request.session['state'], desc = request.session['desc'])

    return redirect('/dojos')


def samurai(request):

    first_name = request.POST['first']
    print(first_name)
    last_name = request.POST['last']
    print(last_name)
    dojo = int(request.POST['dojo'])
    print(dojo)
    
    dojo_id = Dojos.objects.get(id=dojo)

    request.session['first_name'] = first_name
    request.session['last_name'] = last_name
    request.session['dojo'] = dojo

    Ninjas.objects.create(first_name=request.session['first_name'], last_name=request.session['last_name'], dojo=dojo_id)

    return redirect('/dojos')
