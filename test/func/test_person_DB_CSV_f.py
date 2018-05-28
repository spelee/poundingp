import copy
import pytest
from poundingpave.person import Person
from poundingpave.person_db_csv import Person_DB_CSV as DB

# XXX this is (semi-)faulty test input  because we are not resetting
# the test data
# all changes are being made inplace..
test_people_inputs = [
    Person("james", "dean", {}),  # no attributes
    Person("billy", "joel", {  # full attributes, mult inter & notes
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
    Person('katie', 'holmes', {  # select attributesl single note
        'company': 'girl next door inc',
        'role': 'ceo',
        'notes': ['wants to beat honest co.']
    }),
    Person('shohei', 'ohtani', {  # single interaction
        'interaction': ['caught foul his foul ball and got sig, 5/28']
    })
]


def test_add_get_people():
    """Functional task of adding people and retrieving the same people."""
    db = DB()
    db.init_db(overwrite=True)

    for p in test_people_inputs:
        db.add_person(p)
        # test get as we add each
        p_from_db = db.get_person(*p.get_name())
        assert p_from_db == p

    # testing getting all people
    db_people = db.get_people()
    for p in test_people_inputs:
        assert p in db_people
    for p in db_people:
        assert p in test_people_inputs

    db.drop_db()


def test_update_people():
    """Functional task of adding people and updating some people."""
    db = DB()
    db.init_db(overwrite=True)

    for p in test_people_inputs:
        db.add_person(p)    # add people to db

    updated_test_people = []

    test_people_inputs[0].set_company("new comp")
    test_people_inputs[0].set_work_phone("spam")
    updated_test_people.append(test_people_inputs[0])

    test_people_inputs[1].set_email("fake email")
    tst_cp_1 = copy.deepcopy(test_people_inputs[1])
    test_people_inputs[1].reset_notes()
    test_people_inputs[1].add_notes("first note")
    tst_cp_1.add_notes("first note")
    test_people_inputs[1].add_notes(["2nd note", '3rd note'])
    tst_cp_1.add_notes(["2nd note", '3rd note'])

    test_people_inputs[1].reset_interactions()
    test_people_inputs[1].add_interactions(["2nd note", '3rd note'])
    tst_cp_1.add_interactions(["2nd note", '3rd note'])
    updated_test_people.append(tst_cp_1)

    test_people_inputs[2].set_role("fake job")
    test_people_inputs[2].set_mobile_phone("not real")
    tst_cp_2 = copy.deepcopy(test_people_inputs[2])
    test_people_inputs[2].reset_notes()
    test_people_inputs[2].reset_interactions()
    updated_test_people.append(tst_cp_2)

    tst_cp_3 = copy.deepcopy(test_people_inputs[3])
    test_people_inputs[3].reset_notes()
    test_people_inputs[3].reset_interactions()
    test_people_inputs[3].update({
        'company': 'comp a',
        'email': 'email b',
        'mobile_phone': 'phone c',
        'work_phone': 'phone d',
        'interaction': ["itc e", "itc f", "itc g"],
        'notes': ['notes h', 'notes i']
    })

    tst_cp_3.set_company('comp a')
    tst_cp_3.set_email('email b')
    tst_cp_3.set_mobile_phone('phone c')
    tst_cp_3.set_work_phone('phone d')

    tst_cp_3.add_notes(['notes h', 'notes i'])
    tst_cp_3.add_interactions(["itc e", "itc f", "itc g"])
    updated_test_people.append(tst_cp_3)

    # make changes in db
    for p in test_people_inputs:
        db.add_person(p, overwrite=True)

    db_people = db.get_people()
    for p in updated_test_people:
        assert p.deep_membership(db_people)
    for p in db_people:
        assert p.deep_membership(updated_test_people)

    db.drop_db()


def test_delete_person():
    """Functional task of adding people and updating some people."""
    db = DB()
    db.init_db(overwrite=True)

    for p in test_people_inputs:
        db.add_person(p)    # add people to db

    deleted_person = test_people_inputs.pop(1)
    db.delete_person(*deleted_person.get_name())

    db_people = db.get_people()
    for p in test_people_inputs:
        assert p.deep_membership(db_people)
    for p in db_people:
        assert p.deep_membership(test_people_inputs)

    db.drop_db()
