from django.contrib import admin
from .models import Genre, Movie, Score


class MovieModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'genre_id', 'title',)
    list_display_links = ('id', 'title')


# class ScoreModelAdmin(admin.ModelAdmin):
#     readonly_fields = ('created_at', 'updated_at')
#     list_display = ('id', 'content', 'created_at', 'updated_at')
#     list_display_links = ('id', 'content')


# Register your models here.
admin.site.register(Genre)
admin.site.register(Movie, MovieModelAdmin)
admin.site.register(Score)
