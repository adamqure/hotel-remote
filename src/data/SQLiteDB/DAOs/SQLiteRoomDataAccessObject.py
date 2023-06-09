import sqlite3

import jsonpickle
from data.DAOs.RoomDataAccessObject import RoomDataAccessObject
from data.SQLiteDB.SQLiteDBConstants import DB_PATH
from domain.Entities.Room import Room
from domain.Entities.States.RoomState import RoomState

class SQLiteRoomDataAccessObject(RoomDataAccessObject):
    def getRoomByNumber(self, number: int) -> Room:
        connection = sqlite3.connect(DB_PATH)
        try:
            cursor = connection.cursor()
            selectCommand = f"SELECT * FROM Room WHERE number = ?;"
            cursor.execute(selectCommand, (str(number)))
            result = cursor.fetchall()
            if len(result) == 0:
                raise f"Failed to find room that matches number {number}"
            
            roomData = result[0]
            room = Room(
                number=roomData[0],
                floor=roomData[1],
                state=RoomState(roomData[2]),
                reservedDates=jsonpickle.decode(roomData[3]),
                capacity=roomData[4]
            )

            return room
        except Exception as e:
            raise f"Failed to find room that matches number {number}: {e}"
        finally:        
            connection.close()

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
                        number=roomData[0],
                        floor=roomData[1],
                        state=RoomState(roomData[2]),
                        reservedDates=jsonpickle.decode(roomData[3]),
                        capacity=roomData[4]
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
            command = f"INSERT INTO Room (number, floor, state, reservedDates, capacity) VALUES (?, ?, ?, ?, ?)"
            cursor.execute(command, (newRoom.number, newRoom.floor, newRoom._state.value, jsonpickle.encode(newRoom.reservedDates), newRoom.capacity))
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
            command = f"DELETE FROM Room WHERE number = \"{room.number}\";"
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
            updateCommand = f"UPDATE Room SET number = ?, floor = ?, state = ?, reservedDates = ?, capacity = ? WHERE number = ?"
            cursor.execute(updateCommand, (newRoom.number, newRoom.floor, newRoom._state.value, jsonpickle.encode(newRoom.reservedDates), newRoom.capacity, newRoom.number))
            connection.commit()
        except Exception as e:
            print(f"Failed to update room: {newRoom}")
            raise e
        finally:
            connection.close()