from django.db import models

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=30)
    audience = models.IntegerField()
    genre = models.CharField(max_length=10)
    score = models.FloatField()
    poster_url = models.URLField()
    description = models.TextField()