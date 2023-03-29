#!/usr/bin/env python
from src.utilities.args import args
from src.models.contact import Contact
from src.services.contact_service import ContactService

"""
    this module is the entry point of the command line application
"""
def main(args):
    contact_service = ContactService()

    if args.create:
        contact = Contact(args.create[0], args.create[1])
        contact_service.create(contact)

    if args.read:
        contact_service.read()

    if args.update:
        _id = args.update[0]
        contact = Contact(args.update[1], args.update[2])
        contact_service.update(_id, contact)

    if args.delete:
        _id = args.delete[0]
        contact_service.delete(_id)

if __name__ == "__main__":
    main(args())
    