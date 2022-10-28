from flask_app.config.mysqlconnection import connectToMySQL

class Ninja:
    def __init__(self, data):
        self.id = data['id']
        self.dojo_id = data['dojo_id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.age = data['age']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    
    @classmethod
    def save(cls, data):
        query = "INSERT INTO ninjas (dojo_id, first_name, last_name, age) VALUES (%(dojo_id)s, %(first_name)s, %(last_name)s, %(age)s);"
        return connectToMySQL('dojos_and_ninjas_schema').query_db(query, data)
    
    @classmethod
    def get_all_ninjas(cls):
        query = "SELECT ninjas.id, ninjas.first_name, ninjas.last_name, ninjas.age, dojos.name AS dojo_name FROM ninjas LEFT JOIN dojos ON ninjas.dojo_id = dojos.id"
        return connectToMySQL('dojos_and_ninjas_schema').query_db(query)
    
    @classmethod
    def delete(cls, data):
        query = "DELETE FROM ninjas WHERE ninjas.id = %(id)s"
        return connectToMySQL('dojos_and_ninjas_schema').query_db(query, data)
    
    @classmethod
    def get_one_ninja(cls, data):
        query = "SELECT * FROM ninjas WHERE ninjas.id = %(id)s"
        return connectToMySQL('dojos_and_ninjas_schema').query_db(query, data)

    @classmethod
    def update_ninja(cls, data):
        query = "UPDATE ninjas SET first_name = %(first_name)s, last_name = %(last_name)s, age = %(age)s WHERE id = %(id)s;"
        return connectToMySQL('dojos_and_ninjas_schema').query_db(query, data)
