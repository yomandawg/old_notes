from django.urls import path
from . import views

app_name = 'movies'

urlpatterns = [
    path('genres/', views.genre_list, name="genre_list"),
    path('genres/<int:genre_pk>/', views.genre, name="genre"),
    path('movies/', views.movie_list, name="movie_list"),
    path('movies/<int:movie_pk>/', views.movie, name="movie"),
    path('movies/<int:movie_pk>/scores/', views.score, name="scores"),
    path('scores/<int:score_pk>', views.score_list, name="score_list"),
]