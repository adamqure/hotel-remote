import sqlite3
import jsonpickle
import pytest
from data.SQLiteDB.DAOs.SQLiteRoomDataAccessObject import SQLiteRoomDataAccessObject

from data.SQLiteDB.SQLiteDBConstants import DB_PATH
from domain.Entities.Room import Room
from domain.Entities.States.RoomState import RoomState


@pytest.fixture
def clearRoomsTable():
    connection = sqlite3.connect(DB_PATH)
    try:
        cursor = connection.cursor()
        cursor.execute("DROP TABLE Room")
        cursor.execute("CREATE TABLE \"Room\" (\"number\"	INTEGER NOT NULL UNIQUE, \"floor\"	INTEGER NOT NULL, \"state\"	INTEGER NOT NULL, \"reservedDates\"	TEXT, \"capacity\"	INTEGER NOT NULL, PRIMARY KEY(\"number\"))")
    except Exception as e:
        print("Failed to drop the Room table")
        print(e)
    finally:
        connection.close()

@pytest.fixture
def newAvailableRoom():
    connection = sqlite3.connect(DB_PATH)
    try:
        cursor = connection.cursor()
        newRoom = Room(
            number=1,
            floor=1,
            state=RoomState.AVAILABLE
        )
        command = f"INSERT INTO Room (number, floor, state, reservedDates, capacity) VALUES (?, ?, ?, ?, ?)"
        cursor.execute(command, (newRoom.number, newRoom.floor, newRoom._state.value, jsonpickle.encode(newRoom.reservedDates), newRoom.capacity))
        connection.commit()
    except Exception as e:
        print("Failed to create a new room")
        print(e)
    finally:
        connection.close()

def testGetRoomByNumberExists(clearRoomsTable, newAvailableRoom):
    roomNumber = 1
    dao = SQLiteRoomDataAccessObject()
    result = dao.getRoomByNumber(roomNumber)
    assert(result.number == 1)
    assert(result.floor == 1)
    assert(result._state == RoomState.AVAILABLE)
    assert(len(result.reservedDates) == 0)

def testGetRoomByNumberDoesNotExist(clearRoomsTable):
    roomNumber = 1
    dao = SQLiteRoomDataAccessObject()

    try:
        result = dao.getRoomByNumber(roomNumber)
        assert(False)
    except:
        assert(True)

def testGetAllRoomsContainsAllRooms(clearRoomsTable, newAvailableRoom):
    dao = SQLiteRoomDataAccessObject()
    result = dao.getAllRooms()
    assert(len(result) == 1)

def testGetAllRoomsWithNoRoomsReturnsEmptyList(clearRoomsTable):
    dao = SQLiteRoomDataAccessObject()
    result = dao.getAllRooms()
    assert(len(result) == 0)

def testCreateExistingRoomRaisesException(clearRoomsTable, newAvailableRoom):
    dao = SQLiteRoomDataAccessObject()

    room = Room(
        number=1,
        floor=1,
        state=RoomState.AVAILABLE
    )

    try:
        dao.createRoom(room)
        assert(False)
    except:
        assert(True)

def testCreateNewRoomSucceeds(clearRoomsTable):
    dao = SQLiteRoomDataAccessObject()

    room = Room(
        number=1,
        floor=1,
        state=RoomState.AVAILABLE
    )

    try:
        dao.createRoom(room)
        rooms = dao.getAllRooms()
        assert(room in rooms)
    except:
        assert(False)

def testDeleteExistingRoomSucceeds(clearRoomsTable, newAvailableRoom):
    dao = SQLiteRoomDataAccessObject()

    room = Room(
        number=1,
        floor=1,
        state=RoomState.AVAILABLE
    )

    try:
        dao.deleteRoom(room)
        rooms = dao.getAllRooms()
        assert(len(rooms) == 0)
    except:
        assert(False)

def testDeleteNonExistingRoomRaisesException(clearRoomsTable):
    dao = SQLiteRoomDataAccessObject()

    room = Room(
        number=1,
        floor=1,
        state=RoomState.AVAILABLE
    )

    try:
        dao.deleteRoom(room)
        assert(False)
    except:
        assert(True)