from datetime import datetime
import sqlite3
import pytest
from data.SQLiteDB.DAOs.SQLiteReservationRoomChargeJoiningDataAccessObject import SQLiteReservationRoomChargeJoiningDataAccessObject
from data.SQLiteDB.DAOs.SQLiteRoomChargeDataAccessObject import SQLiteRoomChargeDataAccessObject

from data.SQLiteDB.SQLiteDBConstants import DB_PATH
from domain.Entities.Reservation import Reservation
from domain.Entities.RoomCharge import RoomCharge


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
def clearRoomChargeTable():
    connection = sqlite3.connect(DB_PATH)
    try:
        cursor = connection.cursor()
        cursor.execute("DROP TABLE RoomCharge")
        cursor.execute("CREATE TABLE \"RoomCharge\" (\"id\"	TEXT NOT NULL UNIQUE, \"itemName\"	TEXT NOT NULL, \"unitCost\"	REAL NOT NULL, \"creator\"	TEXT NOT NULL, \"date\"	TEXT NOT NULL, \"count\"	INTEGER NOT NULL DEFAULT 1, PRIMARY KEY(\"id\"))")
    except Exception as e:
        print("Failed to drop the RoomCharge table")
        print(e)
    finally:
        connection.close()

def testCreateJoinWithNoReservationRaisesException(clearJoinTable, clearReservationTable, clearRoomChargeTable):
    reservation = Reservation(datetime.now(), datetime.now(), 1, None)
    roomCharge = RoomCharge("Test", 1.5, 1, "Test")
    dao = SQLiteReservationRoomChargeJoiningDataAccessObject()

    try:
        dao.createReservationRoomChargeJoin(None, roomCharge)
        assert(False)
    except:
        assert(True)

def testCreateJoinWithNoRoomChargeRaisesException(clearJoinTable, clearReservationTable, clearRoomChargeTable):
    reservation = Reservation(datetime.now(), datetime.now(), 1, None)
    roomCharge = RoomCharge("Test", 1.5, 1, "Test")
    dao = SQLiteReservationRoomChargeJoiningDataAccessObject()

    try:
        dao.createReservationRoomChargeJoin(reservation, None)
        assert(False)
    except:
        assert(True)

def testCreateJoinSuccessful(clearJoinTable, clearReservationTable, clearRoomChargeTable):
    reservation = Reservation(datetime.now(), datetime.now(), 1, None)
    roomCharge = RoomCharge("Test", 1.5, 1, "Test")
    dao = SQLiteReservationRoomChargeJoiningDataAccessObject()
    dao.createReservationRoomChargeJoin(reservation, roomCharge)

def testDeleteJoinWithNoReservationRaisesException(clearJoinTable, clearReservationTable, clearRoomChargeTable):
    reservation = Reservation(datetime.now(), datetime.now(), 1, None)
    roomCharge = RoomCharge("Test", 1.5, 1, "Test")
    dao = SQLiteReservationRoomChargeJoiningDataAccessObject()

    try:
        dao.deleteReservationRoomChargeJoin(None, roomCharge)
        assert(False)
    except:
        assert(True)

def testDeleteJoinWithNoRoomChargeRaisesException(clearJoinTable, clearReservationTable, clearRoomChargeTable):
    reservation = Reservation(datetime.now(), datetime.now(), 1, None)
    roomCharge = RoomCharge("Test", 1.5, 1, "Test")
    dao = SQLiteReservationRoomChargeJoiningDataAccessObject()

    try:
        dao.deleteReservationRoomChargeJoin(reservation, None)
        assert(False)
    except:
        assert(True)

def testDeleteJoinSuccessful(clearJoinTable, clearReservationTable, clearRoomChargeTable):
    reservation = Reservation(datetime.now(), datetime.now(), 1, None)
    roomCharge = RoomCharge("Test", 1.5, 1, "Test")
    dao = SQLiteReservationRoomChargeJoiningDataAccessObject()
    dao.createReservationRoomChargeJoin(reservation, roomCharge)
    dao.deleteReservationRoomChargeJoin(reservation, roomCharge)

def testGetRoomChargesForReservationWithNoReservationRaisesException(clearJoinTable, clearReservationTable, clearRoomChargeTable):
    reservation = Reservation(datetime.now(), datetime.now(), 1, None)
    roomCharge = RoomCharge("Test", 1.5, 1, "Test")
    dao = SQLiteReservationRoomChargeJoiningDataAccessObject()
    
    try:
        dao.getRoomChargesForReservation(reservation)
        assert(False)
    except:
        assert(True)

def testGetRoomChargesForReservationReturnsCharges(clearJoinTable, clearReservationTable, clearRoomChargeTable):
    reservation = Reservation(datetime.now(), datetime.now(), 1, None)
    roomCharge = RoomCharge("Test", 1.5, 1, "Test")
    roomCharge2 = RoomCharge("Test2", 2.0, 2, "Test")
    dao = SQLiteReservationRoomChargeJoiningDataAccessObject()
    roomChargeDao = SQLiteRoomChargeDataAccessObject()
    roomChargeDao.createRoomCharge(roomCharge)
    roomChargeDao.createRoomCharge(roomCharge2)

    dao.createReservationRoomChargeJoin(reservation, roomCharge)
    dao.createReservationRoomChargeJoin(reservation, roomCharge2)

    result = dao.getRoomChargesForReservation(reservation)
    assert(len(result) == 2)
    assert(roomCharge in result)
    assert(roomCharge2 in result)