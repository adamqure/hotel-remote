from domain.Entities.Reservation import Reservation
from domain.Entities.Room import Room


class ReservationRoomJoiningDataAccessObject:
    def getRoomForReservation(self, reservation: Reservation) -> Room:
        pass

    def deleteReservationRoomJoin(self, reservation: Reservation, room: Room):
        pass

    def createReservationRoomJoin(self, reservation: Room, room: Room):
        pass