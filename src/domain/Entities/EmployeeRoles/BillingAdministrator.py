from domain.Entities.EmployeeRoles.Billing import Billing
from domain.Entities.Reservation import Reservation

class BillingAdministrator(Billing):
    def __init__(self):
        super().__init__("Billing Administrator")

    def processRefund(reservation: Reservation, credit: float):
        pass