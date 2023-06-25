from data.DAOs.ReservationRoomChargeJoiningDataAccessObject import ReservationRoomChargeJoiningDataAccessObject
from data.DAOs.RoomChargeDataAccessObject import RoomChargeDataAccessObject
from data.SQLiteDB.DAOs.SQLiteReservationRoomChargeJoiningDataAccessObject import SQLiteReservationRoomChargeJoiningDataAccessObject
from data.SQLiteDB.DAOs.SQLiteRoomChargeDataAccessObject import SQLiteRoomChargeDataAccessObject
from domain.Entities.Reservation import Reservation
from domain.Entities.RoomCharge import RoomCharge


class RoomChargeDataSource:
    def __init__(
            self, 
            joinDAO: ReservationRoomChargeJoiningDataAccessObject = SQLiteReservationRoomChargeJoiningDataAccessObject(),
            roomChargeDAO: RoomChargeDataAccessObject = SQLiteRoomChargeDataAccessObject()
    ):
        self._joinDAO = joinDAO
        self._roomChargeDAO = roomChargeDAO

    def getRoomChargesForReservation(self, reservation: Reservation):
        return self._joinDAO.getRoomChargesForReservation(reservation)

    def createRoomCharge(self, roomCharge: RoomCharge, reservation: Reservation):
        self._roomChargeDAO.createRoomCharge(roomCharge)
        self._joinDAO.createReservationRoomChargeJoin(reservation, roomCharge)

    def deleteRoomCharge(self, roomCharge: RoomCharge, reservation: Reservation):
        self._roomChargeDAO.deleteRoomCharge(roomCharge)
        self._joinDAO.deleteReservationRoomChargeJoin(reservation, roomCharge)