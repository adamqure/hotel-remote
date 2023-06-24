import sqlite3
from data.DAOs.RoomChargeDataAccessObject import RoomChargeDataAccessObject
from data.SQLiteDB.SQLiteDBConstants import DB_PATH
from domain.Entities.RoomCharge import RoomCharge
import jsonpickle

class SQLiteRoomChargeDataAccessObject(RoomChargeDataAccessObject):
    def updateRoomCharge(self, roomCharge: RoomCharge):
        connection = sqlite3.connect(DB_PATH)
        try:
            cursor = connection.cursor()
            command = f"UPDATE RoomCharge SET id=?, itemName=?, unitCost=?, creator=?, date=?, count=? WHERE id = ?"
            cursor.execute(command, (roomCharge._id, roomCharge.itemName, roomCharge.unitCost, roomCharge.creator, jsonpickle.encode(roomCharge.date), roomCharge.count, roomCharge._id))
            connection.commit()
        except Exception as e:
            print("Failed to create a new Room Charge")
            print(e)
        finally:
            connection.close()

    def deleteRoomCharge(self, roomCharge: RoomCharge):
        connection = sqlite3.connect(DB_PATH)
        try:
            cursor = connection.cursor()
            command = f"DELETE FROM RoomCharge WHERE id = ?"
            cursor.execute(command, (roomCharge._id))
            connection.commit()
        except Exception as e:
            print("Failed to delete Room Charge")
            print(e)
        finally:
            connection.close()

    def createRoomCharge(self, roomCharge: RoomCharge):
        connection = sqlite3.connect(DB_PATH)
        try:
            cursor = connection.cursor()
            command = f"INSERT INTO RoomCharge (id, itemName, unitCost, creator, date, count) VALUES (?, ?, ?, ?, ?, ?)"
            cursor.execute(command, (str(roomCharge._id), roomCharge.itemName, roomCharge.unitCost, roomCharge.creator, jsonpickle.encode(roomCharge.date), roomCharge.count))
            connection.commit()
        except Exception as e:
            print("Failed to create a new Room Charge")
            print(e)
        finally:
            connection.close()