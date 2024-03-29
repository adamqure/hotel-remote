from datetime import datetime
import sqlite3
import jsonpickle
import pytest
from data.Repositories.ConcreteRoomsRepository import ConcreteRoomsRepository

from data.SQLiteDB.SQLiteDBConstants import DB_PATH
from domain.Entities.Room import Room
from domain.Entities.States.RoomState import RoomState


@pytest.fixture
def clearRoomsTable():
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
        command = f"INSERT INTO Room (id, number, floor, state, reservedDates, capacity) VALUES (?, ?, ?, ?, ?, ?)"
        cursor.execute(command, (str(newRoom._id), newRoom.number, newRoom.floor, newRoom._state.value, jsonpickle.encode(newRoom.reservedDates), newRoom.capacity))
        connection.commit()
    except Exception as e:
        print("Failed to create a new room")
        print(e)
    finally:
        connection.close()

@pytest.fixture
def roomWith4Capacity():
    connection = sqlite3.connect(DB_PATH)
    try:
        cursor = connection.cursor()
        newRoom = Room(
            number=2,
            floor=1,
            state=RoomState.AVAILABLE,
            capacity=4
        )
        command = f"INSERT INTO Room (id, number, floor, state, reservedDates, capacity) VALUES (?, ?, ?, ?, ?, ?)"
        cursor.execute(command, (str(newRoom._id), newRoom.number, newRoom.floor, newRoom._state.value, jsonpickle.encode(newRoom.reservedDates), newRoom.capacity))
        connection.commit()
    except Exception as e:
        print("Failed to create a new room")
        print(e)
    finally:
        connection.close()

@pytest.fixture
def roomReservedOn02022023():
    connection = sqlite3.connect(DB_PATH)
    try:
        cursor = connection.cursor()
        newRoom = Room(
            number=2,
            floor=1,
            state=RoomState.AVAILABLE,
            reservedDates=[datetime(year=2023, month=2, day=2)],
            capacity=2
        )
        command = f"INSERT INTO Room (id, number, floor, state, reservedDates, capacity) VALUES (?, ?, ?, ?, ?, ?)"
        cursor.execute(command, (str(newRoom._id), newRoom.number, newRoom.floor, newRoom._state.value, jsonpickle.encode(newRoom.reservedDates), newRoom.capacity))
        connection.commit()
    except Exception as e:
        print("Failed to create a new room")
        print(e)
    finally:
        connection.close()

def testGetRoomList(clearRoomsTable, newAvailableRoom):
    repository = ConcreteRoomsRepository()
    assert(len(repository.getRoomList()) == 1)
    
def testGetRoomsAvailableForDatesReturnsAvailable(clearRoomsTable, roomReservedOn02022023):
    repository = ConcreteRoomsRepository()
    assert(len(repository.getRoomsAvailableForDates([datetime(year=2023, month=5, day=1)])) == 1)

def testGetRoomsUnavailableForDatesreturnsEmpty(clearRoomsTable, roomReservedOn02022023):
    repository = ConcreteRoomsRepository()
    assert(len(repository.getRoomsAvailableForDates([datetime(year=2023, month=2, day=2)])) == 0)

def testGetRoomsWithCapacityReturnsAvailable(clearRoomsTable, roomWith4Capacity):
    repository = ConcreteRoomsRepository()
    assert(len(repository.getRoomsWithCapacity(3)) == 1)

def testGetRoomsWithoutCapacityReturnsUnavailable(clearRoomsTable, roomWith4Capacity):
    repository = ConcreteRoomsRepository()
    assert(len(repository.getRoomsWithCapacity(5)) == 0)

def testAlreadyExistingRoomRaisesException(clearRoomsTable, newAvailableRoom):
    repository = ConcreteRoomsRepository()
    
    try:
        repository.createRoom(Room(
            number=1,
            floor=1,
            state=RoomState.AVAILABLE
        ))
        assert(False)
    except:
        assert(True)

def testNonExistingRoomIsAdded(clearRoomsTable):
    newRoom = Room(
        number=1,
        floor=1,
        state=RoomState.AVAILABLE
    )
    repository = ConcreteRoomsRepository()
    repository.createRoom(newRoom)
    assert(newRoom in repository.getRoomList())

def testDeleteNonexistingRoomRaisesException(clearRoomsTable):
    repository = ConcreteRoomsRepository()

    newRoom = Room(
        number=1,
        floor=1,
        state=RoomState.AVAILABLE
    )

    try:
        repository.deleteRoom(newRoom)
        assert(False)
    except:
        assert(True)

def testDeleteExistingRoomSucceeds(clearRoomsTable):
    repository = ConcreteRoomsRepository()

    newRoom = Room(
        number=1,
        floor=1,
        state=RoomState.AVAILABLE
    )

    repository.createRoom(newRoom)

    try:
        repository.deleteRoom(newRoom)
        assert(len(repository.getRoomList()) == 0)
    except:
        assert(False)

def testUpdateNonexistingRoomRaisesException(clearRoomsTable):
    repository = ConcreteRoomsRepository()

    newRoom = Room(
        number=1,
        floor=1,
        state=RoomState.AVAILABLE
    )

    try:
        repository.updateRoom(newRoom)
        assert(False)
    except:
        assert(True)

def testUpdateExistingRoomSucceeds(clearRoomsTable):
    repository = ConcreteRoomsRepository()

    newRoom = Room(
        number=1,
        floor=1,
        state=RoomState.UNAVAILABLE
    )

    repository.createRoom(newRoom)

    newRoom.number = 2

    try:
        repository.updateRoom(newRoom)
        room = repository.getRoomList()[0]
        assert(room._id == newRoom._id)
        assert(room.number == newRoom.number)
        assert(room._state == RoomState.UNAVAILABLE)
    except:
        assert(False)