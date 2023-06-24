from data.DataSources.RoomChargeDataSource import RoomChargeDataSource
from domain.Entities.Reservation import Reservation
from domain.Entities.RoomCharge import RoomCharge
from domain.Repositories.RoomChargeRepository import RoomChargeRepository


class ConcreteRoomChargeRepository(RoomChargeRepository):
    def __init__(
            self, 
            dataSource: RoomChargeDataSource = RoomChargeDataSource()
    ):
        self._dataSource = dataSource

    def addRoomCharge(self, reservation: Reservation, roomCharge: RoomCharge):
        self._dataSource.createRoomCharge(roomCharge, reservation)

    def removeRoomCharge(self, reservation: Reservation, roomCharge: RoomCharge):
        self._dataSource.deleteRoomCharge(roomCharge, reservation)