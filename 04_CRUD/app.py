from flask import Flask, request, render_template, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///Movie.db'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)
db.init_app(app)

class Movie(db.Model):
    __tablename__ = "movies"
    movie_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String, nullable=False)
    title_en = db.Column(db.String, nullable=False)
    audience = db.Column(db.Integer, nullable=False)
    open_date = db.Column(db.String, nullable=False)
    genre = db.Column(db.String, nullable=False)
    watch_grade = db.Column(db.String, nullable=False)
    score = db.Column(db.String, nullable=False)
    poster_url = db.Column(db.TEXT, nullable=False)
    description = db.Column(db.TEXT, nullable=False)
    
db.create_all()

@app.route('/')
@app.route('/movies/')
def index():
    movies = Movie.query.all()
    return render_template('index.html', movies=movies)

@app.route('/movies/new/')
def new():
    return render_template('new.html')

@app.route('/movies/create/', methods=["POST"])
def create():
    title = request.form.get('title')
    title_en = request.form.get('title_en')
    audience = request.form.get('audience')
    open_date = request.form.get('open_date')
    genre = request.form.get('genre')
    watch_grade = request.form.get('watch_grade')
    score = request.form.get('score')
    poster_url = request.form.get('poster_url')
    description = request.form.get('description')
    movie = Movie(title=title, title_en=title_en, audience=audience, open_date=open_date, genre=genre, watch_grade=watch_grade, score=score, poster_url=poster_url, description=description)
    db.session.add(movie)
    db.session.commit()
    return redirect('/movies/')

@app.route('/movies/<int:movie_id>')
def show(movie_id):
    movie = Movie.query.get(movie_id)
    return render_template('show.html', movie=movie)

@app.route('/movies/<int:movie_id>/edit', methods=["POST"])
def edit(movie_id):
    movie = Movie.query.get(movie_id)
    return render_template('edit.html', movie=movie)

@app.route('/movies/<int:movie_id>/update', methods=["POST"])
def update(movie_id):
    movie = Movie.query.get(movie_id)
    movie.title = request.form.get('title')
    movie.title_en = request.form.get('title_en')
    movie.audience = request.form.get('audience')
    movie.open_date = request.form.get('open_date')
    movie.genre = request.form.get('genre')
    movie.watch_grade = request.form.get('watch_grade')
    movie.score = request.form.get('score')
    movie.poster_url = request.form.get('poster_url')
    movie.description = request.form.get('description')
    db.session.commit()
    return redirect('/movies/{}'.format(movie_id))

@app.route('/movies/<int:movie_id>/delete', methods=["POST"])
def delete(movie_id):
    movie = Movie.query.get(movie_id)
    db.session.delete(movie)
    db.session.commit()
    return redirect('/movies/')