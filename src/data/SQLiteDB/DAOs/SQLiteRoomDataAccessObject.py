import sqlite3

import jsonpickle
from data.DAOs.RoomDataAccessObject import RoomDataAccessObject
from data.SQLiteDB.SQLiteDBConstants import DB_PATH
from domain.Entities.Room import Room
from domain.Entities.States.RoomState import RoomState
import uuid

class SQLiteRoomDataAccessObject(RoomDataAccessObject):
    def getAllRooms(self) -> list[Room]:
        connection = sqlite3.connect(DB_PATH)
        try:
            cursor = connection.cursor()
            selectCommand = f"SELECT * FROM Room"
            cursor.execute(selectCommand)
            dataObjects = cursor.fetchall()
            result: list[Room] = []
            for roomData in dataObjects:
                result.append(
                    Room(
                        number=roomData[1],
                        floor=roomData[2],
                        state=RoomState(roomData[3]),
                        reservedDates=jsonpickle.decode(roomData[4]),
                        capacity=roomData[5],
                        id=uuid.UUID(roomData[0])
                    )
                )
            return result
        except:
            raise f"Failed to fetch room list"
        finally:        
            connection.close() 

    def createRoom(self, newRoom: Room):
        connection = sqlite3.connect(DB_PATH)
        try:
            cursor = connection.cursor()
            command = f"INSERT INTO Room (id, number, floor, state, reservedDates, capacity) VALUES (?, ?, ?, ?, ?, ?)"
            cursor.execute(command, (str(newRoom._id), newRoom.number, newRoom.floor, newRoom._state.value, jsonpickle.encode(newRoom.reservedDates), newRoom.capacity))
            connection.commit()
        except Exception as e:
            print("Failed to create a new room")
            print(e)
        finally:
            connection.close()

    def deleteRoom(self, room: Room):
        connection = sqlite3.connect(DB_PATH)
        try:
            cursor = connection.cursor()
            command = f"DELETE FROM Room WHERE id = \"{str(room._id)}\";"
            cursor.execute(command)
            connection.commit()
        except Exception as e:
            print(f"Failed to delete room: {room}")
            print(e)
        finally:
            connection.close()

    def updateRoom(self, newRoom: Room):
        connection = sqlite3.connect(DB_PATH)
        try:
            cursor = connection.cursor()
            updateCommand = f"UPDATE Room SET id = ?, number = ?, floor = ?, state = ?, reservedDates = ?, capacity = ? WHERE id = ?"
            cursor.execute(updateCommand, (str(newRoom._id), newRoom.number, newRoom.floor, newRoom._state.value, jsonpickle.encode(newRoom.reservedDates), newRoom.capacity, str(newRoom._id)))
            connection.commit()
        except Exception as e:
            print(f"Failed to update room: {newRoom}")
            raise e
        finally:
            connection.close()