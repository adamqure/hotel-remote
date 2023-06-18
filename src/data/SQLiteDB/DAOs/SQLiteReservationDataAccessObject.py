import sqlite3
from data.DAOs.ReservationDataAccessObject import ReservationDataAccessObject
from data.SQLiteDB.SQLiteDBConstants import DB_PATH
from domain.Entities.Reservation import Reservation
from domain.Entities.States.ReservationState import ReservationState
import jsonpickle


class SQLiteReservationDataAccessObject(ReservationDataAccessObject):
    def updateReservation(self, reservation: Reservation):
        connection = sqlite3.connect(DB_PATH)
        try:
            cursor = connection.cursor()
            command = f"UPDATE Reservation SET id=?, startDate=?, endDate=?, numberOfGuests=?, state=?, confirmationNumber=? WHERE id=?"
            cursor.execute(command, (str(reservation.id), jsonpickle.encode(reservation.startDate), jsonpickle.encode(reservation.endDate), reservation.numberOfGuests, reservation.state.value, reservation.confirmationNumber, reservation.id))
            connection.commit()
        except Exception as e:
            print(f"Failed to update the reservation")
            raise e
        finally:
            connection.close()

    def createReservation(self, reservation: Reservation):
        connection = sqlite3.connect(DB_PATH)
        try:
            cursor = connection.cursor()
            command = f"INSERT INTO Reservation (id, startDate, endDate, numberOfGuests, state, confirmationNumber) VALUES (?, ?, ?, ?, ?, ?)"
            cursor.execute(command, (str(reservation.id), jsonpickle.encode(reservation.startDate), jsonpickle.encode(reservation.endDate), reservation.numberOfGuests, reservation.state.value, reservation.confirmationNumber))
            connection.commit()
        except Exception as e:
            print(f"Failed to create the new reservation")
            raise e
        finally:
            connection.close()

    def getAllReservations(self) -> list[Reservation]:
        connection = sqlite3.connect(DB_PATH)
        try:
            cursor = connection.cursor()
            command = f"SELECT * FROM Reservation"
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
                    id=reservationData[0],
                    confirmation=reservationData[5],
                    reservationData=ReservationState(reservationData[4])
                    )
                )
            return result
        except Exception as e:
            print(f"Failed to fetch reservations")
            raise e
        finally:
            connection.close()