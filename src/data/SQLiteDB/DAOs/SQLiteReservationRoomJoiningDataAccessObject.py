import sqlite3
from data.DAOs.ReservationRoomJoiningDataAccessObject import ReservationRoomJoiningDataAccessObject
from data.SQLiteDB.SQLiteDBConstants import DB_PATH
from domain.Entities.Reservation import Reservation
from domain.Entities.Room import Room
from domain.Entities.States.ReservationState import ReservationState
import jsonpickle

class SQLiteReservationRoomJoiningDataAccessObject(ReservationRoomJoiningDataAccessObject):
    def getRoomForReservation(self, reservation: Reservation) -> Room:
        connection = sqlite3.connect(DB_PATH)
        try:
            cursor = connection.cursor()
            command = f"SELECT Room.id as id, number, floor, state, capacity FROM ReservationRoomJoining JOIN Room ON ReservationRoomJoining.roomID = Room.id WHERE ReservationRoomJoining.reservationID = ?"
            cursor.execute(command, (reservation._id))
            
            dataObjects = cursor.fetchall()
            if len(dataObjects) == 0:
                raise f"Failed to find Room that matches reservation {reservation}"
            
            reservationData = dataObjects[0]
            return Reservation(
                startDate=jsonpickle.decode(reservationData[1]),
                endDate=jsonpickle.decode(reservationData[2]),
                numberOfGuests=reservationData[3],
                room=None,
                roomCharges=[],
                id=reservationData[0],
                confirmation=reservationData[5],
                reservationData=ReservationState(reservationData[4])
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
            cursor.execute(command, (reservation.id, room.id))
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
            cursor.execute(command, (reservation.id, room.id))
            connection.commit()
        except Exception as e:
            print(f"Failed to create join")
            raise e
        finally:
            connection.close()