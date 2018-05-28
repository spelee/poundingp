import sqlite3
from sqlite3 import Error

import poundingpave.person
from poundingpave.person import Person


class Person_DB_SQLite():

    def __init__(self, path="poundingpv.db"):
        self.path = path

    def header(self):
        return poundingpave.person.required_attributes

    def db_exists(self):
        # XXX doesn't work for sql version
        # i realize there can simply test if file exists.
        # written this way as more of an example of exception catching...
        try:
            with open(self.path, newline=''):
                pass
        except FileNotFoundError as fe:
            print(fe)
            return False
        return True

    def init_db(self, overwrite=False):
        """Initialize, possibly overwriting existing db"""
        # create a connection
        try:
            conn = sqlite3.connect(self.path)
        except Error as e:
            print(e)
        finally:
            conn.close()

        # XXX currently there is no sesne over overwritng here...

    def drop_db(self):
        """Simply deletes the db"""
        pass

    def get_people(self):
        """
        Returns all people in db as a list.  Init db if it doesn't exist
        XXX try making as a generator function in future?
        """
        people = []

        try:
            with open(self.path, newline='') as csvfile:
                person_reader = reader(csvfile, delimiter="|")
                for row in person_reader:
                    att = {k: v for k, v in zip(self.header(), row)}
                    person = Person(
                        att['first_name'], att['last_name'], att)

                    # notes and attributes are lists of strings!
                    nts = person.get_notes()
                    person.replace_notes(string_to_list(nts))

                    intract = person.get_interactions()
                    person.replace_interactions(string_to_list(intract))

                    # people.append(person)
                    yield person

        except FileNotFoundError:
            self.init_db()

        # return people

    def get_person(self, first_name, last_name):
        for p in self.get_people():
            if p.get_name() == (first_name, last_name):
                return p

    def add_person(self, p, overwrite=False):
        """
        Updates attributes if person already exists and overwrite is
        set to True.  Init db if it doesn't exist.
        """
        existing_as_dict = {q.get_name(): q for q in self.get_people()}
        if p.get_name() in existing_as_dict:
            if overwrite:
                orig = existing_as_dict[p.get_name()]
                orig.update(p.attributes)
            else:  # no overwriting
                pass

        else:
            existing_as_dict[p.get_name()] = p

        fd, temppath = mkstemp()
        with fdopen(fd, "w", newline='') as new_file:
            # pipe delimiter b/c commas used to separted list items
            person_writer = csv.writer(
                new_file, quoting=csv.QUOTE_NONE, delimiter="|")
            for e in existing_as_dict.values():
                person_writer.writerow(e.req_attributes_as_list())

        # replace with new file
        remove(self.path)
        move(temppath, self.path)

    def update_person(self, p):
        """
        This is currently an undefined action.  Updates occur via add.
        """
        pass

    def delete_person(self, first_name, last_name):
        existing = self.get_people()
        existing_as_dict = {q.get_name(): q for q in existing}
        try:
            del existing_as_dict[(first_name, last_name)]
        except KeyError:
            print("{} {} not found".format(first_name, last_name))
        else:
            df, temppath = mkstemp()
            with fdopen(df, "w", newline='') as new_file:
                # pipe delimiter b.c commas used to separate list items
                person_writer = csv.writer(
                    new_file, quoting=csv.QUOTE_NONE, delimiter="|")
                for e in existing_as_dict.values():
                    person_writer.writerow(e.req_attributes_as_list())

            # replace old with new file
            remove(self.path)
            move(temppath, self.path)


def touch(fname):
    with open(fname, 'a'):
        os.utime(fname)


def string_to_list(input):
    for i in reader([input.strip("[]")],
                    skipinitialspace=True,
                    quotechar="'"):
        return i
    """
    if(not input.strip("[]")):
        return []
    return [v.strip().strip("\'\"") for v in input.strip("[]").split(",")]
    """


if __name__ == '__main__':
    db = Person_DB_SQLite()
    print(db.db_exists())
    print(db.header())
    print(db.db_exists())
    db.init_db()
