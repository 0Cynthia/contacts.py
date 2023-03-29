from src.databases.contact_database import ContactDatabase


"""
    this module exports a service object that handles CRUD operations against the contacts table
"""
class ContactService:
    def __init__(self):
        self.contactDB = ContactDatabase()

    def create(self, contact):
        try:
            contact = self.contactDB.create(contact)

            if contact:
                print(f"successfully created a new contact!")
            else:
                print(f"failed to create a new contact!")
                
        except Exception as e:
            print("something went wrong on our side...")

    def read(self):
        try:
            contacts = self.contactDB.read()

            if len(contacts) == 0:
                print("no contacts exist yet; go make some!")
            else:
                for contact in contacts:
                    print("\t\t".join(contact))

        except Exception as e:
            print("something went wrong on our side...")

    def update(self, _id, contact):
        try:
            contact = self.contactDB.update(_id, contact)

            if contact:
                print(f"successfully updated the contact!")
            else:
                print(f"failed to update the contact")

        except Exception as e:
            print("something went wrong on our side...")

    def delete(self, _id):
        try:
            contact = self.contactDB.delete(_id)

            if contact:
                print(f"successfully deleted the contact!")
            else:
                print(f"failed to delete the contact")
        except Exception as e:
            print("something went wrong on our side...")
            