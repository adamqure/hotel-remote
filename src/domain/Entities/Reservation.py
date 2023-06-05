import uuid
from domain.Entities.RoomCharge import RoomCharge
from domain.Entities.States.ReservationState import ReservationState
from domain.Entities.States.RoomState import RoomState

class Reservation:
    def __init__(self, startDate, endDate, numberOfGuests, room, roomCharges = []):
        self.startDate = startDate
        self.endDate = endDate
        self.numberOfGuests = numberOfGuests
        self.roomCharges = roomCharges
        self.room = room
        self.id = uuid.uuid4()
        self.confirmationNumber = str(id)
        self.state = ReservationState.DRAFT

    def addRoomCharge(self, charge: RoomCharge):
        self.roomCharges.add(charge)

    def removeRoomCharge(self, charge: RoomCharge):
        self.roomCharges.remove(charge)

    def calculateTotalInvoice(self):
        pass

    def updateState(self, newState: RoomState):
        self.state = newState