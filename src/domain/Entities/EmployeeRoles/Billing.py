from domain.Entities.EmployeeRoles.EmployeeRole import EmployeeRole
from domain.Entities.Reservation import Reservation

class Billing(EmployeeRole):
    def __init__(self, name = "Billing"):
        super().__init__(name)

    def generateInvoice(reservation: Reservation):
        pass

    def processPayment(reservation: Reservation):
        pass