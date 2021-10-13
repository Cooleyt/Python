from flask_app.config.mysqlconnection import connectToMySQL


class Book():
    def __init__(self, data):
        self.id = data['id']
        self.title = data['title']
        self.num_of_pages = data['num_of_pages']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM books;"

        results = connectToMySQL('books_schema').query_db(query)
        books = []

        for d in results:
            books.append( cls(d) )
        return books

    @classmethod
    def save(cls, data):
        query= "INSERT INTO books (title, num_of_pages) VALUES (%(title)s, %(num_of_pages)s);"
        result = connectToMySQL('books_schema').query_db(query,data)
        return result

    @classmethod
    def get_one_with_author(cls, data ):
        query = "SELECT * FROM books LEFT JOIN authors on books.id = authors.books_id WHERE books.id = %(id)s;"
        results = connectToMySQL('books_schema').query_db(query,data)
        print(results)
        book = cls(results[0])
        for row in results:
            n = {
                'id': row['authors.id'],
                'name': row['name'],
                'created_at': row['authors.created_at'],
                'updated_at': row['authors.updated_at']
            }
            book.authors.append(Book(n))
        return book