import copy
# XXX make 'static'
required_attributes = ['first_name',
                       'last_name',
                       'company',
                       'email',
                       'mobile_phone',
                       'work_phone',
                       'role',
                       'interaction',
                       'notes']


class Person():
    """A person"""

    def __init__(self, first_name, last_name, attributes=None):
        # XXX do we want to store a copy?
        self.attributes = \
            {} if not attributes else copy.deepcopy(attributes)
        self.attributes.setdefault('notes', [])
        self.attributes.setdefault('interaction', [])
        self.attributes['first_name'] = first_name
        self.attributes['last_name'] = last_name

    def get_name(self):
        """Gets full name as tuple (first, last)"""
        return (self.attributes['first_name'], self.attributes['last_name'])

    def set_company(self, company):
        self.attributes['company'] = company

    def set_email(self, email):
        self.attributes['email'] = email

    def set_mobile_phone(self, mobile_phone):
        self.attributes['mobile_phone'] = mobile_phone

    def set_work_phone(self, work_phone):
        self.attributes['work_phone'] = work_phone

    def set_role(self, role):
        self.attributes['role'] = role

    def add_interactions(self, interactions):
        """
        Accepts iterable
        """
        if isinstance(interactions, str):
            interactions = [interactions]
        self.attributes.setdefault("interaction", []).extend(interactions)

    def reset_interactions(self):
        """zeros out interactions"""
        self.attributes['interaction'] = []

    def replace_interactions(self, interactions):
        self.attributes["interaction"] = interactions

    def get_interactions(self):
        return self.attributes.get("interaction", [])

    def add_notes(self, notes):
        """
        Accepts iterable of notes
        """
        if isinstance(notes, str):
            notes = [notes]
        self.attributes.setdefault("notes", []).extend(notes)

    def reset_notes(self):
        """zeros out notes"""
        self.attributes['notes'] = []

    def replace_notes(self, notes):
        self.attributes["notes"] = notes

    def get_notes(self):
        return self.attributes.get("notes", [])

    def update(self, attributes):
        """
        Update attributes means copy attributes to the person.
        Updating 'interaction' and 'notes' means appending
        """
        for k in attributes:
            if k == "interaction":
                self.add_interactions(attributes[k])

            elif k == "notes":
                self.add_notes(attributes[k])

            else:
                self.attributes[k] = attributes[k]

    def req_attributes(self):
        """Return dict (copy) w/only those attributes defined as required"""
        return {k: self.attributes.get(k, None) for k in required_attributes}

    def req_attributes_as_list(self):
        return [self.attributes.get(k, None) for k in required_attributes]

    def __str__(self):
        return "|".join(
            [self.attributes.get(k, "").__str__() for k in required_attributes])

    def __eq__(self, other):
        """Equality only tests for name!"""
        if isinstance(self, other.__class__):

            return (self.attributes['first_name'] == other.attributes['first_name'] and
                    self.attributes['last_name'] == other.attributes['last_name'])
        return NotImplemented

    def __ne__(self, other):
        x = self.__eq__(other)
        if x is NotImplemented:
            return NotImplemented
        return not x

    def deep_equals(self, other):
        if isinstance(self, other.__class__):
            for att in required_attributes:
                if (self.attributes.get(att, '') !=
                        other.attributes.get(att, '')):
                    return False
            return True
        return False  # NotImplemented not nec because deep_equals is custom

    def deep_membership(self, others):
        for o in others:
            if self.deep_equals(o):
                return True
        return False


def print_dict(d, prefix=""):
    # recursive print
    for k in d:
        print("{}{} -> ".format(prefix, k))
        if isinstance(d[k], dict):
            print_dict(d[k], prefix=prefix + "\t")
        elif isinstance(d[k], list):
            print_list(d[k], prefix=prefix + "\t")
        else:
            print("{}{}".format(prefix + "\t", d[k]))


def print_list(l, prefix=""):
    # recursive print
    for i in l:
        if isinstance(i, dict):
            print_dict(i, prefix=prefix + "\t")
        elif isinstance(i, list):
            print_list(i, prefix=prefix + "\t")
        else:
            print("{}{}".format(prefix, i))
    pass
