from flask_app.config.mysqlconnection import connectToMySQL

from .ninja import Ninja

class Dojo():
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.ninjas = []

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM dojos;"

        results = connectToMySQL('dojos_and_ninjas_schema').query_db(query)
        dojos = []

        for d in results:
            dojos.append( cls(d) )
        return dojos

    @classmethod
    def save(cls, data):
        query= "INSERT INTO dojos (name) VALUES (%(name)s);"
        result = connectToMySQL('dojos_and_ninjas_schema').query_db(query,data)
        return result

    @classmethod
    def get_one_with_ninjas(cls, data ):
        query = "SELECT * FROM dojos LEFT JOIN ninjas on dojos.id = ninjas.dojos_id WHERE dojos.id = %(id)s;"
        results = connectToMySQL('dojos_and_ninjas_schema').query_db(query,data)
        print(results)
        dojo = cls(results[0])
        for row in results:
            n = {
                'id': row['ninjas.id'],
                'first_name': row['first_name'],
                'last_name': row['last_name'],
                'age': row['age'],
                'created_at': row['ninjas.created_at'],
                'updated_at': row['ninjas.updated_at']
            }
            dojo.ninjas.append( Ninja(n) )
        return dojo

    # @classmethod
    # def create_dojo(cls, data):
    #     query = "INSERT INTO dojos (name) VALUES (%(name)s);"

    #     new_dojo_id = connectToMySQL('dojos_and_ninjas_schema').query_db(query, data)

    #     return new_dojo_id

    # @classmethod
    # def get_all_dojos(cls):

    #     query = "SELECT * FROM dojos JOIN ninjas ON dojo.id = ninjas.dojos_id;"

    #     results = connectToMySQL('dojos_and_ninjas_schema').query_db(query)
    #     dojos = cls(results[0])
    #     for row in results: 
    #         ninja = {
    #             "id": row["ninjas.id"],
    #             "first_name": row["first_name"],
    #             "last_name": row["last_name"],
    #             "age": row["age"],
    #             "created_at": row["ninjas.created_at"],
    #             "updated_at": row["ninjas.updated_at"]
    #         }
    #         dojos.ninjas.append(Ninja(ninja))
    #     return dojos

    # @classmethod
    # def delete_dojo(cls, data):

    #     query = "DELETE FROM dojos WHERE id = %(id)s;"

    #     connectToMySQL('dojos_and_ninjas_schema').query_db(query, data)

    # @classmethod
    # def get_dojo_by_id(cls, data):

    #     query = "SELECT * FROM dojos LEFT JOIN ninjas ON dojos.id = ninjas.dojos_id WHERE dojos_id = %(id)s;"

    #     results = connectToMySQL('dojos_and_ninjas_schema').query_db(query, data)

    #     print(results)

    #     dojo = Dojo(results[0])

    #     for item in results:
    #         if item['ninjas.id'] != None:
    #             ninjas_data = {
    #                 'id': item['ninjas.id'],
    #                 'first_name': item['first_name'],
    #                 'last_name': item['last_name'],
    #                 'age': item['age'],
    #                 'dojos_id': item['dojos_id'],
    #                 'created_at': item['ninjas.created_at'],
    #                 'updated_at': item['ninjas.updated_at']
    #             }

    #             new_ninjas = Ninja(ninjas_data)
    #             new_ninjas.dojo = dojo
    #             dojo.ninjas.append(new_ninjas)

    #     return dojo

    # @classmethod
    # def update_dojo(cls, data):

    #     query = "UPDATE dojos SET name = %(name)s WHERE id = %(id)s;"

    #     connectToMySQL('dojos_and_ninjas_schema').query_db(query, data)