import sqlite3
import pytest
from data.SQLiteDB.DAOs.SQLiteGuestDataAccessObject import SQLiteGuestDataAccessObject

from data.SQLiteDB.SQLiteDBConstants import DB_PATH
from domain.Entities.People.Guest import Guest


@pytest.fixture
def clearGuestTable():
    connection = sqlite3.connect(DB_PATH)
    try:
        cursor = connection.cursor()
        cursor.execute("DROP TABLE Guest")
        cursor.execute("CREATE TABLE \"Guest\" (\"id\"	TEXT NOT NULL UNIQUE, \"name\"	TEXT NOT NULL, \"emailAddress\"	TEXT NOT NULL, PRIMARY KEY(\"id\"))")
    except Exception as e:
        print("Failed to drop the Guest table")
        print(e)
    finally:
        connection.close()

@pytest.fixture
def createNewGuest():
    guest = Guest(
        name="Test",
        emailAddress="test@test.com",
        paymentMethod=None
    )

    connection = sqlite3.connect(DB_PATH)
    try:
        cursor = connection.cursor()
        command = f"INSERT INTO Guest (id, name, emailAddress) VALUES (?, ?, ?)"
        cursor.execute(command, (str(guest._id), guest._name, guest._emailAddress))
        connection.commit()
    except Exception as e:
        print("Failed to create the Guest")
        print(e)
    finally:
        connection.close()

def testGetAllGuestsReturnsEmptyListWhenNoGuests(clearGuestTable):
    dao = SQLiteGuestDataAccessObject()

    assert(len(dao.getAllGuests()) == 0)

def testGetAllGuestsReturnsAllExistingGuests(clearGuestTable, createNewGuest):
    dao = SQLiteGuestDataAccessObject()
    assert(len(dao.getAllGuests()) == 1)

def testDeletingNonExistingGuestRaisesException(clearGuestTable):
    dao = SQLiteGuestDataAccessObject()
    try:
        dao.deleteGuest("Test")
        assert(False)
    except:
        assert(True)

def testDeletingExistingGuestSuccessful(clearGuestTable):
    guest = Guest(
        name="Test",
        emailAddress="test@test.com",
        paymentMethod=None
    )

    dao = SQLiteGuestDataAccessObject()
    dao.deleteGuest(guest._id)

def testCreateExistingGuestRaisesException(clearGuestTable):
    guest = Guest(
        name="Test",
        emailAddress="test@test.com",
        paymentMethod=None
    )

    dao = SQLiteGuestDataAccessObject()
    dao.createGuest(guest)
    try:
        dao.createGuest(guest)
        assert(False)
    except:
        assert(True)

def testCreateGuestSuccessful(clearGuestTable):
    guest = Guest(
        name="Test",
        emailAddress="test@test.com",
        paymentMethod=None
    )

    dao = SQLiteGuestDataAccessObject()
    dao.createGuest(guest)

def testUpdateNonExistingGuestRaisesException(clearGuestTable):
    guest = Guest(
        name="Test",
        emailAddress="test@test.com",
        paymentMethod=None
    )

    dao = SQLiteGuestDataAccessObject()

    try:
        dao.updateGuest(guest)
        assert(False)
    except:
        assert(True)


def testUpdateExistingGuestSuccessful(clearGuestTable):
    guest = Guest(
        name="Test",
        emailAddress="test@test.com",
        paymentMethod=None
    )

    dao = SQLiteGuestDataAccessObject()
    dao.createGuest(guest)

    guest._name = "Testing"
    dao.updateGuest(guest)