from django.shortcuts import render, redirect
from .models import Movie

def index(request):
    movies = Movie.objects.all().order_by('id')
    context = {'movies': movies}
    return render(request, 'movies/index.html', context)

def new(request):
    return render(request, 'movies/new.html')

def create(request):
    title = request.POST.get('title')
    audience = request.POST.get('audience')
    genre = request.POST.get('genre')
    score = request.POST.get('score')
    poster_url = request.POST.get('poster_url')
    description = request.POST.get('description')
    movie = Movie(title=title, audience=audience, genre=genre, score=score, poster_url=poster_url, description=description)
    movie.save()
    return redirect('detail', movie.id)

def detail(request, movie_id):
    movie = Movie.objects.get(id=movie_id)
    context = {'movie': movie}
    return render(request, 'movies/detail.html', context)

def edit(request, movie_id):
    movie = Movie.objects.get(id=movie_id)
    context = {'movie': movie}
    return render(request, 'movies/edit.html', context)

def update(request, movie_id):
    movie = Movie.objects.get(id=movie_id)
    movie.title = request.POST.get('title')
    movie.audience = request.POST.get('audience')
    movie.genre = request.POST.get('genre')
    movie.score = request.POST.get('score')
    movie.poster_url = request.POST.get('poster_url')
    movie.description = request.POST.get('description')
    movie.save()
    return redirect('detail', movie_id)

def delete(request, movie_id):
    movie = Movie.objects.get(id=movie_id)
    movie.delete()
    return redirect('index')