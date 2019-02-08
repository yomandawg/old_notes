from flask import Flask, request, redirect, render_template
import sqlite3
import datetime

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')
    
@app.route('/articles')
def articles():
    c = sqlite3.connect('blog.db')
    db = c.cursor()
    sql = "SELECT * FROM articles"
    db.execute(sql)
    data = db.fetchall()
    c.close()
    return render_template('articles.html', data=data)

@app.route('/articles/new')
def new():
    return render_template('new.html')

@app.route('/articles/create', methods=["POST"])
def create():
    title = request.form.get('title')
    content = request.form.get('content')
    author = request.form.get('author')
    created_at = (datetime.datetime.now() + datetime.timedelta(hours=9)).strftime('%Y-%m-%d %H:%M:%S')
    c = sqlite3.connect('blog.db')
    db = c.cursor()
    sql = "INSERT INTO articles (title, content, created_at, author) VALUES ('{}', '{}', '{}', '{}')".format(title, content, created_at, author)
    db.execute(sql)
    c.commit()
    c.close()
    return redirect('/articles')
    
@app.route('/articles/<int:article_id>')
def view(article_id):
    c = sqlite3.connect('blog.db')
    db = c.cursor()
    sql = "SELECT * FROM articles WHERE article_id={}".format(article_id)
    db.execute(sql)
    data = db.fetchall()
    c.close()
    return render_template('view.html', data=data)

@app.route('/articles/<int:article_id>/edit', methods=["POST"])
def edit(article_id):
    c = sqlite3.connect('blog.db')
    db = c.cursor()
    sql = "SELECT * FROM articles WHERE article_id={}".format(article_id)
    db.execute(sql)
    data = db.fetchall()
    c.close()
    return render_template('edit.html', data=data)
    
@app.route('/articles/<int:article_id>/update', methods=["POST"])
def update(article_id):
    title = request.form.get('title')
    author = request.form.get('author')
    content = request.form.get('content')
    created_at = (datetime.datetime.now() + datetime.timedelta(hours=9)).strftime('%Y-%m-%d %H:%M:%S')
    c = sqlite3.connect('blog.db')
    db = c.cursor()
    sql = "UPDATE articles SET title='{}', author='{}', created_at='{}', content='{}' WHERE article_id={}".format(title, author, created_at, content, article_id)
    db.execute(sql)
    c.commit()
    c.close()
    return redirect('/articles/{}'.format(article_id))

@app.route('/articles/<int:article_id>/delete', methods=["POST"])
def delete(article_id):
    c = sqlite3.connect('blog.db')
    db = c.cursor()
    sql = "DELETE FROM articles WHERE article_id={}".format(article_id)
    db.execute(sql)
    c.commit()
    c.close()
    return redirect('/articles')