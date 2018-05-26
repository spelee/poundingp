import pytest
from poundingpave.person import Person


""" XXX Apply use of fixtures later
@pytest.fixture(autouse=True)
def initialized_tasks_db(tmpdir):
    # Connect to db before testing, disconnect after.
    tasks.start_tasks_db(str(tmpdir), 'tiny')
    yield
    tasks.stop_tasks_db()
"""

""" XXX Person attributes.  Need to pull these as constants from person module...
'first_name', 'last_name', 'company', 'email', 'mobile_phone', 'work_phone',
'role', 'interaction', 'notes'
"""

# valid people test input set.  incudes full atributes
test_person_argnames = "first,last,attributes"

test_people_inputs = [
    ("james", "dean", {}),  # no attributes
    ("billy", "joel", {  # full attributes, mult inter & notes
        'company': 'piano man co',
        'email': 'billyj@pianoman.org',
        'mobile_phone': '925-414-8282',
        'work_phone': '415-777-6942',
        'role': 'musician',
        'interaction': ["coffee, 5/12", "phone call, 5/14",
                        "phone call, 6/30"],
        'notes':['good person to know for music composition',
                 'starting music production company']
    }),
    ('katie', 'holmes', {  # select attributesl single note
        'company': 'girl next door inc',
        'role': 'ceo',
        'notes': ['wants to beat honest co.']
    }),
    ('shohei', 'ohtani', {  # single interaction
        'interaction': ['caught foul his foul ball and got sig, 5/28']
    })
]


@pytest.mark.parametrize(test_person_argnames, test_people_inputs)
class TestPerson():
    """Unit tests for poundingpave.person.Person classs"""

    def test_name(self, first, last, attributes):
        # name test cases
        p = Person(first, last, attributes)
        n = p.get_name()
        assert isinstance(n, tuple)
        assert n == (first, last)

    def test_set_company(self, first, last, attributes):
        p = Person(first, last, attributes)
        v = "different company"
        p.set_company(v)
        assert p.attributes['company'] == v

    def test_set_email(self, first, last, attributes):
        p = Person(first, last, attributes)
        v = "different email"
        p.set_email(v)
        assert p.attributes['email'] == v

    def test_set_mobile_phone(self, first, last, attributes):
        p = Person(first, last, attributes)
        v = "555-555-5555"
        p.set_mobile_phone(v)
        assert p.attributes['mobile_phone'] == v

    def test_set_work_phone(self, first, last, attributes):
        p = Person(first, last, attributes)
        v = '777-777-7777'
        p.set_work_phone(v)
        assert p.attributes['work_phone'] == v

    def set_role(self, first, last, attributes):
        p = Person(first, last, attributes)
        v = "lazy bum"
        p.set_role(v)
        assert p.attributes['role'] == v


'''
    def add_interactions(self, interactions):
        self.attributes.setdefault("interaction", []).extend(interactions)

    def replace_interactions(self, interactions):
        self.attributes["interaction"] = interactions

    def get_interactions(self):
        return self.attributes.get("interaction", [])

    def add_notes(self, notes):
        self.attributes.setdefault("notes", []).extend(notes)

    def replace_notes(self, notes):
        self.attributes["notes"] = notes

    def get_notes(self):
        return self.attributes.get("notes", [])

    def update(self, attributes):

    def req_attributes(self):

    def req_attributes_as_list(self):

    def __str__(self):

    def __eq__(self, other):

    def __ne__(self, other):
'''
