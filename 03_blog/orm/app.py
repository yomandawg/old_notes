from flask import Flask, request, render_template, redirect
from flask_sqlalchemy import SQLAlchemy
import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog2.db'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)
db.init_app(app)

class Article(db.Model):
    __tablename__ = "articles"
    article_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String, nullable=False)
    author = db.Column(db.String, nullable=False)
    created_at = db.Column(db.String, nullable=False)
    content = db.Column(db.String, nullable=False)
    
db.create_all()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/articles')
def articles():
    articles = Article.query.all()
    return render_template('articles.html', articles=articles)

@app.route('/articles/new')
def new():
    return render_template('new.html')

@app.route('/articles/create', methods=["POST"])
def create():
    title = request.form.get('title')
    content = request.form.get('content')
    author = request.form.get('author')
    created_at = (datetime.datetime.now() + datetime.timedelta(hours=9)).strftime('%Y-%m-%d %H:%M:%S')
    article = Article(title=title, author=author, created_at=created_at, content=content)
    db.session.add(article)
    db.session.commit()
    return redirect('/articles')

@app.route('/articles/<int:article_id>')
def view(article_id):
    article = Article.query.filter_by(article_id=article_id).first()
    return render_template('view.html', article=article)

@app.route('/articles/<int:article_id>/edit', methods=["POST"])
def edit(article_id):
    article = Article.query.get(article_id)
    return render_template('edit.html', article=article)

@app.route('/articles/<int:article_id>/update', methods=["POST"])
def update(article_id):
    title = request.form.get('title')
    author = request.form.get('author')
    content = request.form.get('content')
    created_at = (datetime.datetime.now() + datetime.timedelta(hours=9)).strftime('%Y-%m-%d %H:%M:%S')
    article = Article.query.get(article_id)
    article.title = title
    article.author = author
    article.created_at = created_at
    article.content = content
    db.session.commit()
    return redirect('/articles/{}'.format(article_id))

@app.route('/articles/<int:article_id>/delete', methods=["POST"])
def delete(article_id):
    article = Article.query.get(article_id)
    db.session.delete(article)
    db.session.commit()
    return redirect('/articles')