import sqlite3
from uuid import UUID
from data.DAOs.ReservationRoomJoiningDataAccessObject import ReservationRoomJoiningDataAccessObject
from data.SQLiteDB.SQLiteDBConstants import DB_PATH
from domain.Entities.Reservation import Reservation
from domain.Entities.Room import Room
from domain.Entities.States.ReservationState import ReservationState
import jsonpickle

from domain.Entities.States.RoomState import RoomState

class SQLiteReservationRoomJoiningDataAccessObject(ReservationRoomJoiningDataAccessObject):
    def getRoomForReservation(self, reservation: Reservation) -> Room:
        connection = sqlite3.connect(DB_PATH)
        try:
            cursor = connection.cursor()
            command = f"SELECT Room.id as id, number, floor, state, reservedDates, capacity FROM ReservationRoomJoining JOIN Room ON ReservationRoomJoining.roomID = Room.id WHERE ReservationRoomJoining.reservationID = \"{reservation._id}\""
            cursor.execute(command)
            
            dataObjects = cursor.fetchall()
            if len(dataObjects) == 0:
                raise f"Failed to find Room that matches reservation {reservation}"
            
            roomData = dataObjects[0]
            return Room(
                number=roomData[1],
                floor=roomData[2],
                state=RoomState(roomData[3]),
                reservedDates=jsonpickle.decode(roomData[4]),
                capacity=roomData[5],
                id=UUID(roomData[0])
            )
        except Exception as e:
            print(f"Failed to get Room for reservation {reservation}")
            raise e
        finally:
            connection.close()

    def deleteReservationRoomJoin(self, reservation: Reservation, room: Room):
        connection = sqlite3.connect(DB_PATH)
        try:
            cursor = connection.cursor()
            command = f"DELETE FROM ReservationRoomJoining WHERE reservationID = ? AND roomID = ?"
            cursor.execute(command, (str(reservation._id), str(room._id)))
            connection.commit()
        except Exception as e:
            print(f"Failed to delete join")
            raise e
        finally:
            connection.close()

    def createReservationRoomJoin(self, reservation: Room, room: Room):
        connection = sqlite3.connect(DB_PATH)
        try:
            cursor = connection.cursor()
            command = f"INSERT INTO ReservationRoomJoining (reservationID, roomID) VALUES (?, ?)"
            cursor.execute(command, (str(reservation._id), str(room._id)))
            connection.commit()
        except Exception as e:
            print(f"Failed to create join")
            raise e
        finally:
            connection.close()