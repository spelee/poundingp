"""Command line interface to interact with the persons db.
"""

import argparse

from poundingpave.person import Person
from poundingpave.person_db_csv import Person_DB_CSV
from poundingpave.settings import Settings


def person_cli():
    settings = Settings()

    parser = argparse.ArgumentParser(
        description="Interface with the person db")
    subparsers = parser.add_subparsers(help="person db CLI subcommands",
                                       dest="{add,get,del}")
    subparsers.required = True

    # subparser to add/update person
    parser_add = subparsers.add_parser("add", help="add/update person")
    parser_add.add_argument("first_name", help="contact's first name")
    parser_add.add_argument("last_name", help="contact's last name")
    parser_add.add_argument("-t", "--attributes", nargs="+",
                            help="<attribute>=<value>")
    parser_add.set_defaults(func=add_person_cli)

    # subparser to query people
    parser_get = subparsers.add_parser("get", help="query person")
    group_get = parser_get.add_mutually_exclusive_group(required=True)
    group_get.add_argument("-a", "--all",
                           action='store_true', help="retrieve all")
    group_get.add_argument("-p", "--person",
                           nargs=2,
                           metavar=("first_name", "last_name"),
                           help="retrieve person with first and last name")
    parser_get.set_defaults(func=print_person_cli)

    # subparser to delete person
    parser_del = subparsers.add_parser("del", help="delete person")
    parser_del.add_argument("first_name", help="contact's first name")
    parser_del.add_argument("last_name", help="contact's last name")
    parser_del.set_defaults(func=del_person_cli)

    # subparser for testing...
    parser_test = subparsers.add_parser("test")
    parser_test.add_argument("attrs", nargs="*", metavar="key=value")
    parser_test.set_defaults(func=run_test_cli)

    db = Person_DB_CSV(settings.db_people_path)
    args = parser.parse_args()

    args.func(args, db)


def add_person_cli(args, db):
    """Creating/updating person and adding to db via CLI"""
    print("Adding/updating person...")
    first_name = args.first_name
    last_name = args.last_name

    p = Person(first_name, last_name, cli_att_to_dict(args.attributes))
    db.add_person(p, overwrite=True)


def print_person_cli(args, db):
    print("Getting person...")
    if args.all:
        for p in db.get_people():
            print(p)
    elif args.person:
        found_person = db.get_person(*args.person)
        if found_person:
            print(found_person)
    else:
        print("hmmm")  # XXX throw an exception here?


def del_person_cli(args, db):
    print("Deleting person...")
    first_name = args.first_name
    last_name = args.last_name

    db.delete_person(first_name, last_name)


def run_test_cli(args, db):
    """
    For testing the CLI and db interface
    """
    print("Running test...")
    # print(args)
    print(db.header())
    print(type(db.header()))


def print_people_cli(args):
    """List people from db via CLI"""
    pass


def cli_att_to_dict(atts):
    if not atts:
        return {}
    attributes = dict([att.split("=") for att in atts])
    # XXX shouldn't "interaction" and "notes" be tied to a
    # constant in person?
    # make these a list. otherwise string defaults to a char list
    # XXX list for now... but may be a container obj later
    if "interaction" in attributes:
        attributes["interaction"] = [attributes["interaction"]]
    if "notes" in attributes:
        attributes["notes"] = [attributes["notes"]]

    return attributes


if __name__ == "__main__":
    person_cli()
