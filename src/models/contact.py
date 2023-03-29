from uuid import uuid4

"""
    this module exports a model of a Contact
"""
class Contact:
    def __init__(self, name, number):
        self._id = uuid4()
        self.name = name
        self.number = number

    def get_name(self):
        return self.name
    
    def set_name(self, name):
        self.name = name

    def get_number(self):
        return self.number
    
    def set_number(self, number):
        self.number = number
