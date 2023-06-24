from datetime import datetime
import sqlite3
import pytest
from data.SQLiteDB.DAOs.SQLiteGuestDataAccessObject import SQLiteGuestDataAccessObject
from data.SQLiteDB.DAOs.SQLiteReservationDataAccessObject import SQLiteReservationDataAccessObject
from data.SQLiteDB.DAOs.SQLiteReservationGuestJoiningDataAccessObject import SQLiteReservationGuestJoiningDataAccessObject

from data.SQLiteDB.SQLiteDBConstants import DB_PATH
from domain.Entities.People.Guest import Guest
from domain.Entities.Reservation import Reservation
from domain.Entities.States.ReservationState import ReservationState

@pytest.fixture
def clearJoinTable():
    connection = sqlite3.connect(DB_PATH)
    try:
        cursor = connection.cursor()
        cursor.execute("DROP TABLE ReservationGuestJoining")
        cursor.execute("CREATE TABLE \"ReservationGuestJoining\" (\"id\"	INTEGER NOT NULL UNIQUE, \"guestID\"	TEXT NOT NULL, \"reservationID\"	TEXT NOT NULL UNIQUE, PRIMARY KEY(\"id\" AUTOINCREMENT))")
    except Exception as e:
        print("Failed to drop the Reservation table")
        print(e)
    finally:
        connection.close()

@pytest.fixture
def clearReservationTable():
    connection = sqlite3.connect(DB_PATH)
    try:
        cursor = connection.cursor()
        cursor.execute("DROP TABLE Reservation")
        cursor.execute("CREATE TABLE \"Reservation\" (\"id\"	TEXT NOT NULL UNIQUE, \"startDate\"	TEXT NOT NULL, \"endDate\"	TEXT NOT NULL, \"numberOfGuests\"	INTEGER NOT NULL, \"state\"	INTEGER NOT NULL DEFAULT 1, \"confirmationNumber\"	TEXT NOT NULL, PRIMARY KEY(\"id\"))")
    except Exception as e:
        print("Failed to drop the Reservation table")
        print(e)
    finally:
        connection.close()

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

def testGetGuestForReservationWithNoReservationRaisesException(clearJoinTable, clearReservationTable, clearGuestTable):
    dao = SQLiteReservationGuestJoiningDataAccessObject()

    reservation = Reservation(datetime.now(), datetime.now(), 1, None)
    guest = Guest("Test", "test@test.com", None)

    try:
        dao.getGuestForReservation(None)
        assert(False)
    except:
        assert(True)

def testGetGuestForReservationWithNoGuestRaisesException(clearJoinTable, clearReservationTable, clearGuestTable):
    dao = SQLiteReservationGuestJoiningDataAccessObject()

    reservation = Reservation(datetime.now(), datetime.now(), 1, None)
    guest = Guest("Test", "test@test.com", None)

    try:
        dao.getGuestForReservation(reservation)
        assert(False)
    except:
        assert(True)

def testGetGuestForReservationSuccessful(clearJoinTable, clearReservationTable, clearGuestTable):
    guestDao = SQLiteGuestDataAccessObject()
    dao = SQLiteReservationGuestJoiningDataAccessObject()

    reservation = Reservation(datetime.now(), datetime.now(), 1, None)
    guest = Guest("Test", "test@test.com", None)

    guestDao.createGuest(guest)
    dao.createGuestReservationJoin(guest, reservation)

    result = dao.getGuestForReservation(reservation)
    assert(result._id == guest._id)

def testGetGuestsActiveReservationsWithNoGuestRaisesException(clearJoinTable, clearReservationTable, clearGuestTable):
    dao = SQLiteReservationGuestJoiningDataAccessObject()

    guest = Guest("Test", "test@test.com", None)
    try:
        dao.getGuestsActiveReservation(None)
        assert(False)
    except:
        assert(True)


def testGetGuestsActiveReservationReturnsExistingReservations(clearJoinTable, clearReservationTable, clearGuestTable):
    dao = SQLiteReservationGuestJoiningDataAccessObject()
    reservationDao = SQLiteReservationDataAccessObject()

    guest = Guest("Test", "test@test.com", None)
    reservation = Reservation(datetime.now(), datetime.now(), 1, None, state=ReservationState.RESERVED)
    reservationDao.createReservation(reservation)

    dao.createGuestReservationJoin(guest, reservation)
    result = dao.getGuestsActiveReservation(guest)
    assert(len(result) == 1)
    assert(reservation in result)

def testCreateGuestReservationJoinWithNoReservationRaisesException(clearJoinTable, clearReservationTable, clearGuestTable):
    dao = SQLiteReservationGuestJoiningDataAccessObject()

    guest = Guest("Test", "test@test.com", None)
    reservation = Reservation(datetime.now(), datetime.now(), 1, None, state=ReservationState.RESERVED)

    try:
        dao.createGuestReservationJoin(guest, None)
        assert(False)
    except:
        assert(True)

def testCreateGuestReservationJoinWithNoGuestRaisesException(clearJoinTable, clearReservationTable, clearGuestTable):
    dao = SQLiteReservationGuestJoiningDataAccessObject()

    guest = Guest("Test", "test@test.com", None)
    reservation = Reservation(datetime.now(), datetime.now(), 1, None, state=ReservationState.RESERVED)

    try:
        dao.createGuestReservationJoin(None, reservation)
        assert(False)
    except:
        assert(True)

def testCreateSuccessful(clearJoinTable, clearReservationTable, clearGuestTable):
    dao = SQLiteReservationGuestJoiningDataAccessObject()

    guest = Guest("Test", "test@test.com", None)
    reservation = Reservation(datetime.now(), datetime.now(), 1, None, state=ReservationState.RESERVED)
    dao.createGuestReservationJoin(guest, reservation)

def testDeleteJoinWithNoReservationRaisesException(clearJoinTable, clearReservationTable, clearGuestTable):
    dao = SQLiteReservationGuestJoiningDataAccessObject()

    guest = Guest("Test", "test@test.com", None)
    reservation = Reservation(datetime.now(), datetime.now(), 1, None, state=ReservationState.RESERVED)

    try:
        dao.deleteGuestReservationJoin(guest, None)
        assert(False)
    except:
        assert(True)

def testDeleteJoinWithNoGuestRaisesException(clearJoinTable, clearReservationTable, clearGuestTable):
    dao = SQLiteReservationGuestJoiningDataAccessObject()

    guest = Guest("Test", "test@test.com", None)
    reservation = Reservation(datetime.now(), datetime.now(), 1, None, state=ReservationState.RESERVED)

    try:
        dao.deleteGuestReservationJoin(None, reservation)
        assert(False)
    except:
        assert(True)

def testDeleteSuccessful(clearJoinTable, clearReservationTable, clearGuestTable):
    dao = SQLiteReservationGuestJoiningDataAccessObject()

    guest = Guest("Test", "test@test.com", None)
    reservation = Reservation(datetime.now(), datetime.now(), 1, None, state=ReservationState.RESERVED)
    dao.createGuestReservationJoin(guest, reservation)
    dao.deleteGuestReservationJoin(guest, reservation)
