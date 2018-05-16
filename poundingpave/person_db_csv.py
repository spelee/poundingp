import csv

from tempfile import mkstemp
from shutil import move
from os import fdopen, remove

import person
from person import Person


class Person_DB_CSV():
    """
    Can add, update, query, and delete people in a csv file, but very inefficient.  Every action requires at least one read/write of the file.
    """

    def __init__(self, path="people.csv"):
        self.path = path

    def header(self):
        return person.required_attributes

    def get_people(self):
        """
        Returns all people in db as a list
        """
        people = []
        with open(self.path, newline='') as csvfile:
            person_reader = csv.reader(csvfile)
            for row in person_reader:
                att = {k: v for k, v in zip(self.header(), row)}
                people.append(Person(att['first_name'],
                                     att['last_name'], att))
        return people

    def get_person(self, first_name, last_name):
        for p in self.get_people():
            if p.get_name() == (first_name, last_name):
                return p

    def add_person(self, p, overwrite=False):
        """
        Updates attributes if person already exists and overwrite is set to True
        """

        existing = self.get_people()
        existing_as_dict = {q.get_name(): q for q in existing}
        updating_p = existing_as_dict.setdefault(p.get_name(), p)
        if overwrite:
            updating_p.update(p.attributes)
        fd, temppath = mkstemp()
        with fdopen(fd, "w", newline='') as new_file:
            person_writer = csv.writer(new_file)
            for e in existing_as_dict.values():
                person_writer.writerow(e.req_attributes_as_list())

        # replace with new file
        remove(self.path)
        move(temppath, self.path)

    def update_person(self, p):
        pass

    def delete_person(self, first_name, last_name):
        existing = self.get_people()
        existing_as_dict = {q.get_name(): q for q in existing}
        del existing_as_dict[(first_name, last_name)]
        df, temppath = mkstemp()
        with fdopen(df, "w", newline='') as new_file:
            person_writer = csv.writer(new_file)
            for e in existing_as_dict.values:
                person_writer.writerow(e.req_attributes_as_list())

        # replace old with new file
        remove(self.path)
        move(temppath, self.path)
