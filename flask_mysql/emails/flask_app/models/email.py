from flask_app.config.mysqlconnection import MySQLConnection
import re

from flask import flash

from flask_app import app

class User():

    def __init__(self, data):
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def create_email(cls, data):
        query = 'INSERT INTO emails (email) VALUES (%(email)s);'

        result = MySQLConnection('email_schema').query_db(query, data)

        return result


    @classmethod
    def get_all_emails(cls):
        query = 'SELECT * FROM emails;'

        results = MySQLConnection('email_schema').query_db(query)
        emails=[]

        for item in results:
            email = User(item)
            emails.append(email)
        return emails



    @staticmethod
    def validate_email(data):
        is_valid = True

        email_regex = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

        if not email_regex.match(data['email']):
            is_valid = False
            flash('Email is not in the correct format')

        if len(data['email']) > 255:
            is_valid = False
            flash('Email must be under 255 characters')

        return is_valid

