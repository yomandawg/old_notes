from django.shortcuts import render, redirect, get_object_or_404
from .models import Genre, Movie, Score


# Create your views here.
def movie_list(request):
    movies = Movie.objects.all().order_by('-id')
    context = {
        'movies': movies,
    }
    return render(request, 'movies/list.html', context)


def movie_create(request):
    if request.method == 'POST':
        genre = get_object_or_404(Genre, id=request.POST.get('genre_id'))
        movie = Movie()
        movie.genre = genre
        movie.audience = request.POST.get('audience')
        movie.description = request.POST.get('description')
        movie.poster_url = request.POST.get('poster_url')
        movie.title = request.POST.get('title')
        movie.save()
        return redirect('movies:movie_read', movie.id)
    elif request.method == 'GET':
        return render(request, 'movies/new.html')


def movie_read(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    scores = movie.score_set.all()
    context = {
        'movie': movie,
        'scores': scores,
    }
    return render(request, 'movies/detail.html', context)


def movie_update(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    if request.method == 'GET':
        context = {
            'movie': movie
        }
        return render(request, 'movies/edit.html', context)
    elif request.method == 'POST':
        genre = get_object_or_404(Genre, id=request.POST.get('genre_id'))
        movie.genre = genre
        movie.audience = request.POST.get('audience')
        movie.description = request.POST.get('description')
        movie.poster_url = request.POST.get('poster_url')
        movie.title = request.POST.get('title')
        movie.save()
        return redirect('movies:movie_read', movie.id)


def movie_delete(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    if request.method == 'POST':
        movie.delete()
        return redirect('movies:movie_list')
    elif request.method == 'GET':
        return redirect('movies:movie_read', movie.id)


def score_create(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    if request.method == 'POST':
        score = Score()
        score.movie = movie
        score.score = request.POST.get('score')
        score.content = request.POST.get('content')
        score.save()
    return redirect('movies:movie_read', movie.id)


def score_delete(request, movie_id, score_id):
    movie = get_object_or_404(Movie, id=movie_id)
    score = get_object_or_404(Score, id=score_id)
    if request.method == 'POST':
        score.delete()
    return redirect('movies:movie_read', movie.id)
