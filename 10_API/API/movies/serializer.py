from rest_framework import serializers
from .models import Genre, Movie, Score

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ['id', 'name']

class MovieSerializer(serializers.ModelSerializer):
    genres = GenreSerializer(source='genre', many=False, read_only=True)
    class Meta:
        model = Movie
        fields = ['id', 'title', 'audience', 'poster_url', 'description', 'genres']
        
class GenreMovieSerializer(serializers.ModelSerializer):
    movies = MovieSerializer(source='movie_set', many=True, read_only=True)
    class Meta:
        model = Genre
        fields = ['id', 'movies']
        
class ScoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Score
        fields = ['content', 'score', 'movie']