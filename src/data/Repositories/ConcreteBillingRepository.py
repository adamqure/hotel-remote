from data.DataSources.RoomChargeDataSource import RoomChargeDataSource
from domain.Entities.Reservation import Reservation
from domain.Entities.RoomCharge import RoomCharge
from domain.Repositories.BillingRepository import BillingRepository


class ConcreteBillingRepository(BillingRepository):
    def __init__(self, dataSource: RoomChargeDataSource = RoomChargeDataSource()):
        self._dataSource = dataSource

    def generateInvoice(self, reservation: Reservation) -> list[RoomCharge]:
        return self._dataSource.getRoomChargesForReservation(reservation) 

    def processPayment(self, reservation: Reservation):
        print("NOT IMPLEMENTING PAYMENT PROCESSING FOR THIS PROJECT")

    def processRefund(self, reservation: Reservation):
        print("NOT IMPLEMENTING PAYMENT PROCESSING FOR THIS PROJECT")