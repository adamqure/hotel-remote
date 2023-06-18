from domain.Entities.Reservation import Reservation


class ReservationDataAccessObject:
    def updateReservation(self, reservation: Reservation):
        pass

    def createReservation(self, reservation: Reservation):
        pass

    def getAllReservations(self) -> list[Reservation]:
        pass