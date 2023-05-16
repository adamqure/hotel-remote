from domain.Entities.EmployeeRoles.EmployeeRole import EmployeeRole
from domain.Entities.People.Guest import Guest
from domain.Entities.Reservation import Reservation

class ReservationManagement(EmployeeRole):
    def __init__(self):
        super().__init__("Reservation Management")

    def makeReservation(guest: Guest, reservation: Reservation):
        pass

    def updateReservation(guest: Guest, reservation: Reservation):
        pass

    def cancelReservation(guest: Guest, reservation: Reservation):
        pass