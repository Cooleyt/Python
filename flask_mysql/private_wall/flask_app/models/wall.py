from flask_app.config.mysqlconnection import MySQLConnection
import re

from flask import flash

from flask_app import app

from flask_app.models.user import User

class Wall():

    def __init__(self, data):
        self.message = data['message']
        self.date = data['date']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.users_id = data['users_id']

    @classmethod
    def wall_index(cls, data):
        query = 'INSERT INTO users (first_name, message) VALUES (%(first_name)s, %(message)s);'

        result = MySQLConnection('wall_schema').query_db(query, data)

        return result


    @classmethod
    def create_message(cls, data):
        query = "INSERT INTO messages (message, users_id) VALUES (%(message)s, %(users_id)s);"

        new_message = MySQLConnection('wall_schema').query_db(query, data)

        return new_message

    @classmethod
    def get_all_messages(cls):
        query = "SELECT * FROM messages JOIN users ON messages.users_id = users.id;"
        
        results = MySQLConnection('wall_schema').query_db(query)
        
        messages = []

        for item in results:
            message = Wall(item)
            user_data = {
                'id': item['users.id'],
                'first_name': item['first_name'],
                'last_name': item['last_name'],
                'email': item['email'],
                'password': item['password'],
                'created_at': item['users.created_at'],
                'updated_at': item['users.updated_at']
            }
            user = User(user_data)
            message.user = user
            messages.append(message)

        return messages

    

    @classmethod
    def get_messages(cls, data):
        query = "SELECT * FROM messages JOIN users ON messages.users_id = users.id WHERE messages.id = %(id)s;"

        results = MySQLConnection('wall_schema').query_db(query, data)

        message = Wall(results[0])
        user_data = {
                'id': results[0]['users.id'],
                'first_name': results[0]['first_name'],
                'last_name': results[0]['last_name'],
                'email': results[0]['email'],
                'password': results[0]['password'],
                'created_at': results[0]['users.created_at'],
                'updated_at': results[0]['users.updated_at']
        }
        message.user = User(user_data)
        return message

    @classmethod
    def edit_message(cls, data):
        query = "UPDATE messages SET message = %(message)s WHERE messages.id = %(id)s;"

        edit_message = MySQLConnection('wall_schema').query_db(query, data)

        return edit_message

    @classmethod
    def delete(cls, data):
        query = "DELETE FROM messages WHERE messages.id = %(id)s;"

        return MySQLConnection('wall_schema').query_db(query, data)

    @staticmethod
    def validate_message(data):
        is_valid = True

        if len(data['message']) < 5:
            is_valid = False
            flash('Message must be at least 5 characters long')

        return is_valid