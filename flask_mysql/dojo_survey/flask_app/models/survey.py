from flask_app.config.mysqlconnection import connectToMySQL

from flask import flash

class Survey():
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.location = data['location']
        self.language = data['language']
        self.comment = data['comments']
        self.created_on = data['created_on']
        self.updated_on = data['updated_on']


    @classmethod
    def save(cls, data):
        query = "INSERT INTO surveys (name, location, language, comments) VALUES (%(name)s, %(location)s, %(language)s, %(comments)s);"
        new_survey = connectToMySQL('dojo_survey_schema').query_db(query, data)
        # return connectToMySQL('dojo_survey_schema').query_db(query, data)
        return new_survey


    @classmethod
    def get_single_survey(cls, data):
        query = "SELECT * FROM surveys WHERE surveys.id = %(id)s;"

        new_survey = connectToMySQL('dojo_survey_schema').query_db(query, data)

        return cls(new_survey[0])

    @staticmethod
    def validate_name(data):
        is_valid = True

        if len(data['name']) < 3 or len(data['name']) > 100:
            is_valid = False
            flash('Name should be between 1 and 100 characters.')
        return is_valid


