from datetime import datetime
import sqlite3

import pytest
from data.SQLiteDB.DAOs.SQLiteGuestDataAccessObject import SQLiteGuestDataAccessObject
from data.SQLiteDB.DAOs.SQLiteReservationRoomJoiningDataAccessObject import SQLiteReservationRoomJoiningDataAccessObject
from data.SQLiteDB.DAOs.SQLiteRoomDataAccessObject import SQLiteRoomDataAccessObject

from data.SQLiteDB.SQLiteDBConstants import DB_PATH
from domain.Entities.Reservation import Reservation
from domain.Entities.Room import Room
from domain.Entities.States.RoomState import RoomState


@pytest.fixture
def clearJoinTable():
    connection = sqlite3.connect(DB_PATH)
    try:
        cursor = connection.cursor()
        cursor.execute("DROP TABLE ReservationGuestJoining")
        cursor.execute("CREATE TABLE \"ReservationRoomJoining\" (\"id\"	INTEGER NOT NULL, \"reservationID\"	TEXT NOT NULL, \"roomID\"	TEXT NOT NULL, PRIMARY KEY(\"id\" AUTOINCREMENT))")
    except Exception as e:
        print("Failed to drop the Joining table")
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
def clearRoomTable():
    connection = sqlite3.connect(DB_PATH)
    try:
        cursor = connection.cursor()
        cursor.execute("DROP TABLE Room")
        cursor.execute("CREATE TABLE \"Room\" (\"id\" TEXT NOT NULL UNIQUE, \"number\"	INTEGER NOT NULL, \"floor\"	INTEGER NOT NULL, \"state\"	INTEGER NOT NULL, \"reservedDates\"	TEXT, \"capacity\"	INTEGER NOT NULL, PRIMARY KEY(\"id\"))")
    except Exception as e:
        print("Failed to drop the Room table")
        print(e)
    finally:
        connection.close()

def testCreateJoinWithNoRoomRaisesException():
    dao = SQLiteReservationRoomJoiningDataAccessObject()

    room = Room(
        number=1,
        floor=1,
        state=RoomState.AVAILABLE
    )

    reservation = Reservation(datetime.now(), datetime.now(), 1, None)

    try:
        dao.createReservationRoomJoin(reservation, None)
        assert(False)
    except:
        assert(True)

def testCreateJoinWithNoReservationRaisesException():
    dao = SQLiteReservationRoomJoiningDataAccessObject()

    room = Room(
        number=1,
        floor=1,
        state=RoomState.AVAILABLE
    )

    reservation = Reservation(datetime.now(), datetime.now(), 1, None)

    try:
        dao.createReservationRoomJoin(None, room)
        assert(False)
    except:
        assert(True)

def testCreateJoinSuccessful():
    dao = SQLiteReservationRoomJoiningDataAccessObject()

    room = Room(
        number=1,
        floor=1,
        state=RoomState.AVAILABLE
    )

    reservation = Reservation(datetime.now(), datetime.now(), 1, None)
    dao.createReservationRoomJoin(reservation, room)


def testDeleteJoinWithNoRoomRaisesException():
    dao = SQLiteReservationRoomJoiningDataAccessObject()

    room = Room(
        number=1,
        floor=1,
        state=RoomState.AVAILABLE
    )

    reservation = Reservation(datetime.now(), datetime.now(), 1, None)

    try:
        dao.deleteReservationRoomJoin(reservation, None)
        assert(False)
    except:
        assert(True)

def testDeleteJoinWithNoReservationRaisesException():
    dao = SQLiteReservationRoomJoiningDataAccessObject()

    room = Room(
        number=1,
        floor=1,
        state=RoomState.AVAILABLE
    )

    reservation = Reservation(datetime.now(), datetime.now(), 1, None)

    try:
        dao.deleteReservationRoomJoin(None, room)
        assert(False)
    except:
        assert(True)

def testDeleteJoinSuccessful():
    dao = SQLiteReservationRoomJoiningDataAccessObject()

    room = Room(
        number=1,
        floor=1,
        state=RoomState.AVAILABLE
    )

    reservation = Reservation(datetime.now(), datetime.now(), 1, None)
    dao.createReservationRoomJoin(reservation, room)
    dao.deleteReservationRoomJoin(reservation, room)


def testGetRoomWithNoReservationRaisesException():
    dao = SQLiteReservationRoomJoiningDataAccessObject()

    room = Room(
        number=1,
        floor=1,
        state=RoomState.AVAILABLE
    )

    reservation = Reservation(datetime.now(), datetime.now(), 1, None)

    try:
        dao.getRoomForReservation(reservation)
        assert(False)
    except:
        assert(True)

def testGetRoomWithNoRoomsRaisesException():
    dao = SQLiteReservationRoomJoiningDataAccessObject()

    room = Room(
        number=1,
        floor=1,
        state=RoomState.AVAILABLE
    )

    reservation = Reservation(datetime.now(), datetime.now(), 1, None)
    dao.createReservationRoomJoin(reservation, room)

    try:
        dao.getRoomForReservation(reservation)
        assert(False)
    except:
        assert(True)

def testGetRoomSuccessful():
    dao = SQLiteReservationRoomJoiningDataAccessObject()
    roomDao = SQLiteRoomDataAccessObject()

    room = Room(
        number=1,
        floor=1,
        state=RoomState.AVAILABLE
    )

    roomDao.createRoom(room)
    reservation = Reservation(datetime.now(), datetime.now(), 1, None)
    dao.createReservationRoomJoin(reservation, room)

    result = dao.getRoomForReservation(reservation)
    assert(result._id == room._id)