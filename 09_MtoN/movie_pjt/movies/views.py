from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from .models import Genre, Movie, Score
from .forms import ScoreForm

# Create your views here.
def list(request):
    movies = Movie.objects.all()
    return render(request, 'movies/list.html', {'movies': movies})

def detail(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    score_form = ScoreForm()
    return render(request, 'movies/detail.html', {'movie': movie, 'score_form': score_form})

@login_required
@require_POST
def new_score(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    form = ScoreForm(request.POST)
    if form.is_valid():
        score = form.save(commit=False)
        score.user = request.user
        score.movie = movie
        score.save()
    return redirect('movies:detail', movie_pk)

@login_required
def delete_score(request, movie_pk, score_pk):
    score = get_object_or_404(Score, pk=score_pk)
    if score.user == request.user:
        score.delete()
    return redirect('movies:detail', movie_pk)
