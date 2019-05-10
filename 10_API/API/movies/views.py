from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializer import GenreSerializer, MovieSerializer, ScoreSerializer, GenreMovieSerializer
from .models import Genre, Movie, Score

@api_view(['GET'])
def genre_list(request):
    genres = Genre.objects.all()
    serializer = GenreSerializer(genres, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def genre(request, genre_pk):
    genre = Genre.objects.get(id=genre_pk)
    serializer = GenreMovieSerializer(genre)
    return Response(serializer.data)

@api_view(['GET'])
def movie_list(request):
    movies = Movie.objects.all()
    serializer = MovieSerializer(movies, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def movie(request, movie_pk):
    movie = Movie.objects.get(id=movie_pk)
    serializer = MovieSerializer(movie)
    return Response(serializer.data)

@api_view(['GET', 'POST'])
def score(request, movie_pk):
    if request.method == "GET":
        movie = Movie.objects.get(id=movie_pk)
        scores = Score.objects.filter(movie=movie)
        serializer = ScoreSerializer(scores, many=True)
        return Response(serializer.data)
    if request.method == "POST":
        request.data.update({"movie": movie_pk})
        serializer = ScoreSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "작성되었습니다."})

@api_view(['GET', 'PUT', 'DELETE'])
def score_list(request, score_pk):
    if request.method == "GET":
        score = Score.objects.get(id=score_pk)
        serializer = ScoreSerializer(score, many=False)
        return Response(serializer.data)
    elif request.method == "PUT":
        score = Score.objects.get(id=score_pk)
        serializer = ScoreSerializer(score, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "수정되었습니다."})
    elif request.method == "DELETE":
        score = Score.objects.get(id=score_pk)
        score.delete()
        return Response({"message": "삭제되었습니다."})