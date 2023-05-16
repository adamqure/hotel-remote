import uuid
from domain.Entities.States.ReservationState import ReservationState

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

    def addRoomCharge(self, charge):
        pass

    def removeRoomCharge(self, charge):
        pass

    def calculateTotalInvoice(self):
        pass

    def updateState(self, newState):
        pass