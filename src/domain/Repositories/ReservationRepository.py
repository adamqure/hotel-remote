from domain.Entities.People.Guest import Guest
from domain.Entities.Reservation import Reservation


class ReservationRepository:
    def cancelReservation(self, reservation: Reservation):
        pass

    def checkIn(self, reservation: Reservation):
        pass

    def checkOut(self, reservation: Reservation):
        pass

    def createReservation(self, reservation: Reservation, guest: Guest):
        pass

    def updateReservation(self, reservation: Reservation, guest: Guest):
        pass