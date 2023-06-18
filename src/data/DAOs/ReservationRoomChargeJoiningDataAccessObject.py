from domain.Entities.Reservation import Reservation
from domain.Entities.RoomCharge import RoomCharge


class ReservationRoomChargeJoiningDataAccessObject:
    def createReservationRoomChargeJoin(self, reservation: Reservation, roomCharge: RoomCharge):
        pass

    def deleteReservationRoomChargeJoin(self, reservation: Reservation, roomCharge: RoomCharge):
        pass

    def getRoomChargesForReservation(self, reservation: Reservation) -> list[RoomCharge]:
        pass