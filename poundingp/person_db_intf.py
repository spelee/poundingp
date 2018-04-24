import csv

import person

# TODO: Do I want to make this a class or a module of functions?
# Perhaps a class would know itself to connect based on some
# settings values...

# TODO: First pass is just a flat file... later relational db

# fix this later...
default_path = "people.csv"


def read_people(db_path):
    """Expect fields in the following order:
        first_name
        last_name
        company
        email
        mobile_phone
        work_phone
        role"""
    with open(db_path, newline='') as csvfile:
        person_reader = csv.reader(csvfile)
        for row in person_reader:
            print("|".join(row))


def add_person(p, db_path=default_path):
    with open(db_path, 'a', newline='') as csvfile:
        person_writer = csv.writer(csvfile)

        # TODO: there has got to be a better way...
        att = p.req_attributes_as_list()
        person_writer.writerow(att)


def update_person(db_path, p):
    pass


def delete_person(db_path, first_name, last_name):
    pass
