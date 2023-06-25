from data.DAOs.ReservationDataAccessObject import ReservationDataAccessObject
from data.DAOs.ReservationGuestJoiningDataAccessObject import ReservationGuestJoiningDataAccessObject
from data.SQLiteDB.DAOs.SQLiteReservationDataAccessObject import SQLiteReservationDataAccessObject
from data.SQLiteDB.DAOs.SQLiteReservationGuestJoiningDataAccessObject import SQLiteReservationGuestJoiningDataAccessObject
from domain.Entities.People.Guest import Guest
from domain.Entities.Reservation import Reservation


class ReservationDataSource:
    def __init__(
            self, 
            reservationDAO: ReservationDataAccessObject = SQLiteReservationDataAccessObject(),
            reservationGuestDAO: ReservationGuestJoiningDataAccessObject = SQLiteReservationGuestJoiningDataAccessObject()
    ):
        self._reservationDAO = reservationDAO
        self._reservationGuestJoinDAO = reservationGuestDAO

    def updateReservation(self, reservation: Reservation):
        self._reservationDAO.updateReservation(reservation)

    def createReservation(self, reservation: Reservation, guest: Guest):
        self._reservationDAO.createReservation(reservation)
        self._reservationGuestJoinDAO.createGuestReservationJoin(guest, reservation)

