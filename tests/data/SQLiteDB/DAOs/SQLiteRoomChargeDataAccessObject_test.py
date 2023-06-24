import sqlite3
import pytest
from data.SQLiteDB.DAOs.SQLiteRoomChargeDataAccessObject import SQLiteRoomChargeDataAccessObject
from data.SQLiteDB.DAOs.SQLiteRoomDataAccessObject import SQLiteRoomDataAccessObject

from data.SQLiteDB.SQLiteDBConstants import DB_PATH
from domain.Entities.Room import Room
from domain.Entities.RoomCharge import RoomCharge
from domain.Entities.States.RoomState import RoomState


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

def testCreateExistingRoomChargeRaisesException(clearRoomChargeTable):
    dao = SQLiteRoomChargeDataAccessObject()

    roomCharge = RoomCharge("Test", 1.5, 1, "Test")

    dao.createRoomCharge(roomCharge)
    try:
        dao.createRoomCharge(roomCharge)
        assert(False)
    except:
        assert(True)

def testCreateRoomChargeSuccessful(clearRoomChargeTable):
    dao = SQLiteRoomChargeDataAccessObject()

    roomCharge = RoomCharge("Test", 1.5, 1, "Test")

    dao.createRoomCharge(roomCharge)

def testDeleteNonExistingRoomChargeRaisesException(clearRoomChargeTable):
    dao = SQLiteRoomChargeDataAccessObject()
    roomCharge = RoomCharge("Test", 1.5, 1, "Test")

    try:
        dao.deleteRoomCharge(roomCharge)
        assert(False)
    except:
        assert(True)

def testDeleteRoomChargeSuccessful(clearRoomChargeTable):
    dao = SQLiteRoomChargeDataAccessObject()

    roomCharge = RoomCharge("Test", 1.5, 1, "Test")

    dao.createRoomCharge(roomCharge)
    dao.deleteRoomCharge(roomCharge)

def testUpdateNonExistingRoomChargeRaisesException(clearRoomChargeTable):
    dao = SQLiteRoomChargeDataAccessObject()
    roomCharge = RoomCharge("Test", 1.5, 1, "Test")

    try:
        dao.updateRoomCharge(roomCharge)
        assert(False)
    except:
        assert(True)

def testUpdateRoomChargeSuccessful(clearRoomChargeTable):
    dao = SQLiteRoomChargeDataAccessObject()

    roomCharge = RoomCharge("Test", 1.5, 1, "Test")

    dao.createRoomCharge(roomCharge)

    roomCharge.count = 2
    dao.updateRoomCharge(roomCharge)