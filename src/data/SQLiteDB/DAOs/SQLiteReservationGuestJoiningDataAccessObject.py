import sqlite3
from uuid import UUID
from data.DAOs.ReservationGuestJoiningDataAccessObject import ReservationGuestJoiningDataAccessObject
from data.SQLiteDB.SQLiteDBConstants import DB_PATH
from domain.Entities.People.Guest import Guest
from domain.Entities.Reservation import Reservation
from domain.Entities.States.ReservationState import ReservationState
import jsonpickle

class SQLiteReservationGuestJoiningDataAccessObject(ReservationGuestJoiningDataAccessObject):
    def getGuestForReservation(self, reservation: Reservation) -> Guest:
        connection = sqlite3.connect(DB_PATH)
        try:
            cursor = connection.cursor()
            command = f"SELECT Guest.id as id, name, emailAddress FROM ReservationGuestJoining JOIN Guest ON ReservationGuestJoining.guestID = Guest.id WHERE reservationID = \"{reservation._id}\""
            cursor.execute(command)
            dataObjects = cursor.fetchall()
            if len(dataObjects) == 0:
                raise f"Failed to find Guest that matches reservation {reservation}"
            
            guestData = dataObjects[0]
            return Guest(
                name=guestData[1],
                emailAddress=guestData[2],
                paymentMethod=None,
                reservations=[],
                id=UUID(guestData[0])
            )
        except Exception as e:
            print(f"Failed to get Guest for reservation {reservation}")
            raise e
        finally:
            connection.close()

    def getGuestsActiveReservation(self, guest: Guest) -> list[Reservation]:
        connection = sqlite3.connect(DB_PATH)
        try:
            cursor = connection.cursor()
            command = f"SELECT Reservation.id as id, startDate, endDate, numberOfGuests, state, confirmationNumber FROM ReservationGuestJoining JOIN Reservation ON ReservationGuestJoining.reservationID = Reservation.id WHERE guestID = \"{guest._id}\" AND (Reservation.state = 2 OR Reservation.state = 4 OR Reservation.state = 5)"
            cursor.execute(command)
            dataObjects = cursor.fetchall()
            result: list[Reservation] = []
            for reservationData in dataObjects:
                result.append(
                    Reservation(
                    startDate=jsonpickle.decode(reservationData[1]),
                    endDate=jsonpickle.decode(reservationData[2]),
                    numberOfGuests=reservationData[3],
                    room=None,
                    roomCharges=[],
                    id=UUID(reservationData[0]),
                    confirmation=reservationData[5],
                    state=ReservationState(reservationData[4])
                    )
                )
            return result
        except Exception as e:
            print(f"Failed to get Reservations for guest {guest}")
            raise e
        finally:
            connection.close()

    def createGuestReservationJoin(self, guest: Guest, reservation: Reservation):
        connection = sqlite3.connect(DB_PATH)
        try:
            cursor = connection.cursor()
            command = f"INSERT INTO ReservationGuestJoining (guestID, reservationID) VALUES (?, ?)"
            cursor.execute(command, (str(guest._id), str(reservation._id)))
            connection.commit()
        except Exception as e:
            print(f"Failed to delete join")
            raise e
        finally:
            connection.close()

    def deleteGuestReservationJoin(self, guest: Guest, reservation: Reservation):
        connection = sqlite3.connect(DB_PATH)
        try:
            cursor = connection.cursor()
            command = f"DELETE FROM ReservationGuestJoining WHERE guestID = ? AND reservationID = ?"
            cursor.execute(command, (str(guest._id), str(reservation._id)))
            connection.commit()
        except Exception as e:
            print(f"Failed to delete join")
            raise e
        finally:
            connection.close()