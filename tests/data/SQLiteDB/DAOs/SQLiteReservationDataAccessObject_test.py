from datetime import datetime
import sqlite3
import pytest
from data.SQLiteDB.DAOs.SQLiteReservationDataAccessObject import SQLiteReservationDataAccessObject

from data.SQLiteDB.SQLiteDBConstants import DB_PATH
from domain.Entities.Reservation import Reservation
from domain.Entities.States.ReservationState import ReservationState
from domain.Entities.States.RoomState import RoomState


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

def testUpdateNonExistingReservationRaisesException(clearReservationTable):
    reservation = Reservation(datetime.now(), datetime.now(), 1, None)
    dao = SQLiteReservationDataAccessObject()

    try:
        dao.updateReservation(reservation)
        assert(False)
    except:
        assert(True)

def testUpdateReservationSuccessful(clearReservationTable):
    reservation = Reservation(datetime.now(), datetime.now(), 1, None)
    dao = SQLiteReservationDataAccessObject()
    dao.createReservation(reservation)
    reservation.updateState(ReservationState.RESERVED)
    dao.updateReservation(reservation)


def testCreateExistingReservationRaisesException(clearReservationTable):
    dao = SQLiteReservationDataAccessObject()
    reservation = Reservation(datetime.now(), datetime.now(), 1, None)
    dao.createReservation(reservation)

    try:
        dao.createReservation(reservation)
        assert(False)
    except:
        assert(True)

def testCreateReservationSuccessful(clearReservationTable):
    dao = SQLiteReservationDataAccessObject()
    reservation = Reservation(datetime.now(), datetime.now(), 1, None)
    dao.createReservation(reservation)

def testGetAllReservationsReturnsAllExistingReservations(clearReservationTable):
    dao = SQLiteReservationDataAccessObject()
    reservation = Reservation(datetime.now(), datetime.now(), 1, None)
    dao.createReservation(reservation)

    result = dao.getAllReservations()
    assert(len(result) == 1)
    assert(reservation in result)
