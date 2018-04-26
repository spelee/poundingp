import argparse

import person_db_intf


class Person():
    """A person"""

    def __init__(self, first_name, last_name, attributes={}):

        self.req_attributes = ['first_name',
                               'last_name',
                               'company',
                               'email',
                               'mobile_phone',
                               'work_phone',
                               'role',
                               'interaction',
                               'notes']

        self.attributes = {}
        self.attributes['first_name'] = first_name
        self.attributes['last_name'] = last_name

        # Storing attributes in a dict (as copies)
        for k in attributes:
            self.attributes[k] = attributes[k]

        # Defaults for req'd attributes
        for k in self.req_attributes:
            self.attributes.setdefault(k, "")

        # Set defaults for lists
        self.attributes['interaction'] = []
        self.attributes['notes'] = []

    def set_company(self, company):
        self.attirbutes['company'] = company

    def set_email(self, email):
        self.attributes['email'] = email

    def set_mobile_phone(self, mobile_phone):
        self.attributes['mobile_phone'] = mobile_phone

    def set_work_phone(self, work_phone):
        self.attributes['work_phone'] = work_phone

    def set_role(self, role):
        self.attributes['role'] = role

    def add_interaction(self, interaction):
        self.attributes["interaction"].append(interaction)

    def add_note(self, note):
        self.attributes["notes"].append(note)

    def __str__(self):
        return "{first_name},{last_name},{company},{email},{mobile_phone},{work_phone},{role},{interaction},{notes}".format(
            **self.attributes)

    def req_attributes(self):
        """Return dict (copy) w/only those attributes defined as required"""
        req_dict = {}
        for att in self.req_attributes:
            req_dict[att] = self.attributes[att]
        return req_dict

    def req_attributes_as_list(self):
        req_list = []
        for att in self.req_attributes:
            req_list.append(self.attributes[att])
        return req_list


def person_cli():
    parser = argparse.ArgumentParser(
        description="Interface with the person db")
    subparsers = parser.add_subparsers(help="person db CLI subcommands")

    # subparser to add person
    parser_add = subparsers.add_parser("add", help="add person")
    parser_add.add_argument("first_name", help="contact's first name")
    parser_add.add_argument("last_name", help="contact's last name")
    parser_add.add_argument("-e", "--email",
                            help="person's email address")
    parser_add.set_defaults(func=add_person_cli)

    args = parser.parse_args()

    print(args.func(args))


def add_person_cli(args):
    """Creating person and adding to db via CLI"""
    print("Adding person...")
    att = dict(vars(args))  # XXX is it nec to make copy of args.__dict__?
    first_name = att.pop('first_name')
    last_name = att.pop('last_name')
    att.pop('func')
    p = Person(first_name, last_name, att)
    person_db_intf.add_person(p)


def print_people_cli(args):
    """List people from db via CLI"""
    pass


if __name__ == "__main__":
    # TODO: Should the argparse import be here?
    #    import argparse

    person_cli()
