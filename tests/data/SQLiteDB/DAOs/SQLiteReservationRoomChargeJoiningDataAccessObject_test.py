import sqlite3
import pytest

from data.SQLiteDB.SQLiteDBConstants import DB_PATH


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

