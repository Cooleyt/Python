from flask_app.config.mysqlconnection import connectToMySQL

from .books import Book

class Author():
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.authors = []


    @classmethod
    def create_author(cls, data):
        query = "INSERT INTO author (name) VALUES (%(name)s);"

        new_author = connectToMySQL('books_schema').query_db(query, data)

        return new_author

    @classmethod
    def get_all(cls):
        query = " SELECT * FROM authors;"
        results = connectToMySQL('books_schema').query_db(query)
        authors = []
        for row in results:
            authors.append(cls(row))
        return authors

    @classmethod
    def author_favorites(cls, data):
        query = "SELECT * FROM books LEFT JOIN favorites ON books.id = favorites.book_id LEFT JOIN authors ON authors.id = favorites.author_id;"
        results = connectToMySQL('books_schema').query_db(query, data)
        print(results)
        books = cls(results[0])
        for row in results:
                n = {
                    'id': row['authors.id'],
                    'name': row['authors.name'],
                    'title': row['books.title'],
                    'num_of_pages': row['books.num_of_pages'],
                    'created_at': row['authors.created_at'],
                    'updated_at': row['authors.updated_at']
                }
                books.authors.append(Author(n) )
                return books

    @classmethod
    def get_single_author(cls, data):
        query = "SELECT * FROM authors WHERE id = author.id;"
        results = connectToMySQL('books_schema').query_db(query, data)
        print(results)