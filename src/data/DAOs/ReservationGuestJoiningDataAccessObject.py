from domain.Entities.People.Guest import Guest
from domain.Entities.Reservation import Reservation


class ReservationGuestJoiningDataAccessObject:
    def getGuestForReservation(self, reservation: Reservation) -> Guest:
        pass

    def getGuestsActiveReservation(self, guest: Guest) -> list[Reservation]:
        pass

    def createGuestReservationJoin(self, guest: Guest, reservation: Reservation):
        pass

    def deleteGuestReservationJoin(self, guest: Guest, reservation: Reservation):
        pass