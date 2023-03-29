import sqlite3, os

"""
    this module exports a database object that handles executing sql statements against the contacts table
"""
class ContactDatabase:
    _FILE_DATABASE = os.path.join(os.getcwd(), 'src', 'db', 'db.sql' )
    _FILE_CREATE_DATABASE  = os.path.join(os.getcwd(), 'src', 'db', 'create_database.sql' )

    def __init__(self):
        self.connection = sqlite3.connect(ContactDatabase._FILE_DATABASE)
        self.cursor = self.connection.cursor()
        self.init_db()

    def init_db(self):
        try:
            with open(ContactDatabase._FILE_CREATE_DATABASE, "r") as file:
                statements = file.read()
                self.cursor.execute(statements)
        except Exception as e:
            raise e

    def create(self, contact):
        try:
            statement = f"INSERT INTO contacts (_id, name, number) VALUES ('{contact._id}', '{contact.name}', '{contact.number}')"
            self.cursor.execute(statement)
            self.connection.commit()
            return True
        except Exception as e:
            raise e

    def read(self):
        try:
            statement = "SELECT * FROM contacts"
            result = self.cursor.execute(statement)
            return result.fetchall()
        except Exception as e:
            raise e

    def update(self, _id, contact):
        try:
            statement = f"UPDATE contacts SET name='{contact.name}', number='{contact.number}' WHERE _id='{_id}'"
            self.cursor.execute(statement)
            self.connection.commit()
            return True
        except Exception as e:
            raise e
        
    def delete(self, _id):
        try:
            statement = f"DELETE FROM contacts WHERE _id='{_id}'"
            self.cursor.execute(statement)
            self.connection.commit()
            return True
        except Exception as e:
            pass
        