from data.DataSources.GuestDataSource import GuestDataSource
from data.DataSources.ReservationDataSource import ReservationDataSource
from domain.Entities.People.Guest import Guest
from domain.Entities.Reservation import Reservation
from domain.Entities.States.ReservationState import ReservationState
from domain.Repositories.ReservationRepository import ReservationRepository


class ConcreteReservationRepository(ReservationRepository):
    def __init__(
            self, 
            reservationDataSource: ReservationDataSource = ReservationDataSource(),
            guestDatasource: GuestDataSource = GuestDataSource()
    ):
        self._reservationDataSource = reservationDataSource
        self._guestDataSource = guestDatasource

    def cancelReservation(self, reservation: Reservation):
        if (reservation.state == ReservationState.DRAFT 
        or reservation.state == ReservationState.RESERVED):
            reservation.updateState(ReservationState.CANCELLED)
            self._reservationDataSource.updateReservation(reservation)
        else:
            raise f'Reservation cannot be cancelled in state {reservation.state}'

    def checkIn(self, reservation: Reservation):
        if (reservation.state == ReservationState.RESERVED):
            reservation.updateState(ReservationState.CHECKED_IN)
            self._reservationDataSource.updateReservation(reservation)
        else:
            raise f'Guest cannot check in in state {reservation.state}'  

    def checkOut(self, reservation: Reservation):
        if (reservation.state == ReservationState.CHECKED_IN):
            reservation.updateState(ReservationState.CHECKED_IN)
            self._reservationDataSource.updateReservation(reservation)
        else:
            raise f'Guest not checked-in: {reservation.state}'

    def createReservation(self, reservation: Reservation, guest: Guest):
        self._reservationDataSource.createReservation(reservation, guest)
        self._guestDataSource.createGuest(guest)

    def updateReservation(self, reservation: Reservation, guest: Guest):
        self._reservationDataSource.updateReservation(reservation)
        self._guestDataSource.updateGuest(guest)