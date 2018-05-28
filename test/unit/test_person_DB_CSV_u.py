import copy
import os
import pytest
#from poundingpave.person import Person
from poundingpave.person_db_csv import Person_DB_CSV as DB


"""
Unit tests for the CSV version of the DB
"""

# XXX db setup and teardown should be as a fixture

# XXX If test fails... there should be some sense of cleanup...
# would this occur as part of setup and teardown?


def test_header():
    db = DB()
    assert db.header() == ['first_name', 'last_name', 'company', 'email',
                           'mobile_phone', 'work_phone', 'role',
                           'interaction', 'notes']


def test_creation():
    db = DB()

    # should not exist
    assert not os.path.isfile(db.path)
    assert not db.db_exists()

    # should exist
    db.init_db()
    assert os.path.isfile(db.path)
    assert db.db_exists()

    ts_orig = os.path.getmtime(db.path)
    # should not overwrite
    db.init_db()
    ts_new = os.path.getmtime(db.path)
    assert ts_orig == ts_new

    # should  overwrite
    db.init_db(overwrite=True)
    ts_new = os.path.getmtime(db.path)
    assert ts_orig != ts_new

    # remove the db manually... cleanup
    os.remove(db.path)


def test_existence():

    db = DB()

    # should not exist
    assert not db.db_exists()

    # should exist
    db.init_db()
    assert db.db_exists()

    os.remove(db.path)
    assert not db.db_exists()


def test_drop():
    db = DB()

    # should not exist
    assert not db.db_exists()

    # should exist
    db.init_db()
    assert db.db_exists()

    db.drop_db()
    assert not db.db_exists()
