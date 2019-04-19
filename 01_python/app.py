from flask import Flask, render_template, request
import csv
from movie.movieOOP.movieOOP import Movie

app = Flask(__name__, static_url_path='/static')

@app.route('/')
def index():
    # MovieSearch = Movie(1, './movie/movieOOP')
    # MovieSearch.boxoffice()
    # MovieSearch.movie()
    # MovieSearch.movie_naver()
    # MovieSearch.image()

    movie_info = csv.reader(open("{}/csv/movie_naver.csv".format('./movie/movieOOP'), "r", encoding="utf-8"))
    return render_template('index.html', movie_info=movie_info)