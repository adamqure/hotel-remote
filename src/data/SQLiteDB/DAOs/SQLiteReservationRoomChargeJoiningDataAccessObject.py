import sqlite3
from data.DAOs.ReservationRoomChargeJoiningDataAccessObject import ReservationRoomChargeJoiningDataAccessObject
from data.SQLiteDB.SQLiteDBConstants import DB_PATH
from domain.Entities.Reservation import Reservation
from domain.Entities.RoomCharge import RoomCharge
import jsonpickle


class SQLiteReservationRoomChargeJoiningDataAccessObject(ReservationRoomChargeJoiningDataAccessObject):
    def createReservationRoomChargeJoin(self, reservation: Reservation, roomCharge: RoomCharge):
        connection = sqlite3.connect(DB_PATH)
        try:
            cursor = connection.cursor()
            command = f"INSERT INTO ReservationRoomChargeJoining (reservationID, roomChargeID) VALUES (?, ?)"
            cursor.execute(command, (reservation._id, roomCharge.id))
            connection.commit()
        except Exception as e:
            print(f"Failed to create join")
            raise e
        finally:
            connection.close()

    def deleteReservationRoomChargeJoin(self, reservation: Reservation, roomCharge: RoomCharge):
        connection = sqlite3.connect(DB_PATH)
        try:
            cursor = connection.cursor()
            command = f"DELETE FROM ReservationRoomChargeJoining WHERE reservationID = ? AND roomChargeID = ?"
            cursor.execute(command, (reservation.id, roomCharge.id))
            connection.commit()
        except Exception as e:
            print(f"Failed to delete join")
            raise e
        finally:
            connection.close()

    def getRoomChargesForReservation(self, reservation: Reservation) -> list[RoomCharge]:
        connection = sqlite3.connect(DB_PATH)
        try:
            cursor = connection.cursor()
            command = f"SELECT RoomCharge.id as id, itemName, unitCost, creator, date, count FROM ReservationRoomChargeJoining JOIN RoomCharge ON roomChargeID = RoomCharge.id WHERE reservationID = ?"
            cursor.execute(command, (reservation._id))
            dataObjects = cursor.fetchall()
            result: list[RoomCharge] = []

            for roomChargeData in dataObjects:
                result.append(
                    RoomCharge(
                        itemName=roomChargeData[1],
                        unitCost=roomChargeData[2],
                        count=roomChargeData[5],
                        creator=roomChargeData[3],
                        id=roomChargeData[0],
                        date=jsonpickle.decode(roomChargeData[4])
                    )
                )

            return result
        except Exception as e:
            print(f"Failed to featch RoomCharges for reservation {reservation}")
            raise e
        finally:
            connection.close()