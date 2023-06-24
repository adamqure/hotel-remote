from domain.Entities.Reservation import Reservation
from domain.Entities.RoomCharge import RoomCharge


class BillingRepository:
    def generateInvoice(self, reservation: Reservation) -> list[RoomCharge]:
        pass

    def processPayment(self, reservation: Reservation):
        pass

    def processRefund(self, reservation: Reservation):
        pass
        