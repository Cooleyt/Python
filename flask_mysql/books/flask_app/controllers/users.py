from flask import render_template, request, redirect

from flask_app import app

from flask_app.models.authors import Author
from flask_app.models.books import Book

@app.route("/authors")
def index():
    author = Author.get_all()
    print(author)
    return render_template("home.html", authors = author)

@app.route('/authors/<int:author_id>')    
def author_info(author_id):
    author = Author.get_single_author({'id': author_id})
    return render_template('author_show.html', author = author)


@app.route('/author/create', methods=['POST'])
def create_author():
    data = {
        'name': request.form['name'],
        'authors_id': request.form['authors_id']
    }
    books_id = int(request.form['books_id'])
    Author.create_author(data)

    return redirect(f'/show/{books_id}/books')


@app.route('/books/create', methods=['POST'])
def create_book():
    data = {
        'title': request.form['title'],
        'num_of_pages': request.form['num_of_pages']
    }
    Book.save(data)

@app.route('/book/new')
def new_book():
    return render_template('books.html', books = Book.get_all())


@app.route('/books/<int:author_id>')
def author_id(authors_id):

    data = {
        'id': authors_id
    }

    author = Author.get_single_author(data)

    books = Book.get_all()

    return render_template('author_show.html', author = author, books = books)