from pathlib import Path
from tempfile import TemporaryDirectory

import cards
import pytest

@pytest.fixture(scope="module")
def cards_db():
    with TemporaryDirectory() as db_dir:
        db_path = Path(db_dir)
        db = cards.CardsDB(db_path)
        yield db
        db.close()


def test_empty(cards_db):
    assert cards_db.count() == 0


def test_two(cards_db):
    cards_db.add_card(cards.Card("first"))
    cards_db.add_card(cards.Card("second"))
    assert cards_db.count() == 2

# scope='function'
# Run once per test function. The setup portion is run before each test using
# the fixture. The teardown portion is run after each test using the fixture.
# This is the default scope used when no scope parameter is specified.
# scope='class'
# Run once per test class, regardless of how many test methods are in the class.
# scope='module'
# Run once per module, regardless of how many test functions or methods
# or other fixtures in the module use it.
# scope='package'
# Run once per package, or test directory, regardless of how many test
# functions or methods or other fixtures in the package use it.
# scope='session'
# Run once per session. All test methods and functions using a fixture of
# session scope share one setup and teardown call.