from django.db import models


class Genre(models.Model):
    name = models.CharField(max_length=20, default='')

    def __str__(self):
        return f'{self.name[:10]}'


class Movie(models.Model):
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    title = models.CharField(max_length=30, default='')
    audience = models.IntegerField()
    poster_url = models.CharField(max_length=140, default='')
    description = models.TextField()

    def __str__(self):
        return f'{self.genre.name[:10]}: {self.title[:20]}'


class Score(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    content = models.CharField(max_length=140, default='')
    score = models.IntegerField()

    def __str__(self):
        return f'{self.movie.title[:20]}: {self.score}'
