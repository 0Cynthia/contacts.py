from argparse import ArgumentParser

"""
    this module exports a function that declares this command line application"s arguments
"""
def args():
    parser = ArgumentParser(
        prog="contacts.py",
        description="a command line application for managing contacts and their phone numbers",
        epilog="youtube told me to build this"
    )

    parser.add_argument(
        "-c",
        "--create",
        nargs=2,
        metavar=("str: name", "str: number"),
        help="this command creates a new contact"
    )

    parser.add_argument(
        "-r",
        "--read",
        action="store_true",
        help="this command prints all contacts"
    )

    parser.add_argument(
        "-u",
        "--update",
        nargs=3,
        metavar=("str: _id", "str: new name", "str: new number"),
        help="this command updates an existing contact by its _id"
    )

    parser.add_argument(
        "-d",
        "--delete",
        nargs=1,
        metavar=("str: _id"),
        help="this commnad deletes an existing contact by its _id"
    )

    return parser.parse_args()