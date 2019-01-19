from flask import Flask, render_template, request
import csv
from movie.movieOOP.movieOOP import Movie

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/movie')
def movie():
    # MovieSearch = Movie(1, './movie/movieOOP')
    # MovieSearch.boxoffice()
    # MovieSearch.movie()
    # MovieSearch.movie_naver()
    # MovieSearch.image()

    # movie_naver.writerow(['movie_name', 'movie_code', 'thumb_url', 'link_url', 'user_rating'])
    movie_info = csv.reader(open("{}/csv/movie_naver.csv".format('./movie/movieOOP'), "r", encoding="utf-8"))
    
    return render_template('movie.html', movie_info=movie_info)