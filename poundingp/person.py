import argparse


class Person():
    """A person"""

    def __init__(self, first_name, last_name, person_att={}):
        self.first_name = first_name
        self.last_name = last_name
        self.company = None
        self.email = None
        self.mobile_phone = None
        self.work_phone = None
        self.role = None
        self.interaction = []
        self.notes = []

    def set_company(self, company):
        self.company = company

    def set_email(self, email):
        self.email = email

    def set_mobile_phone(self, mobile_phone):
        self.mobile_phone = mobile_phone

    def set_work_phone(self, work_phone):
        self.work_phone = work_phone

    def set_role(self, role):
        self.role = role

    def add_interaction(self, interaction):
        self.interaction.append(interaction)

    def add_note(self, note):
        self.notes.append(note)


def store_name():
    parser = argparse.ArgumentParser()
    parser.add_argument("first_name",
                        help="contact's first name")  # pos arg req
    parser.add_argument("last_name",
                        help="contact's last name")  # pos arg req
    parser.add_argument("-v", "--verbose",
                        help="increase output verbosity",
                        action="store_true")
    args = parser.parse_args()

#    print(args.first_name)
#    print(args.last_name)


if __name__ == "__main__":
    # TODO: Should the argparse import be here?
    #    import argparse

    store_name()
