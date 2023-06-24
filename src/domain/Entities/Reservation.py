import uuid
from domain.Entities.RoomCharge import RoomCharge
from domain.Entities.States.ReservationState import ReservationState

class Reservation:
    def __init__(self, startDate, endDate, numberOfGuests, room, roomCharges = [], id: uuid = None, confirmation: str = None, state: ReservationState = ReservationState.DRAFT):
        self.startDate = startDate
        self.endDate = endDate
        self.numberOfGuests = numberOfGuests
        self.roomCharges = roomCharges
        self.room = room
        if id == None:
            self._id = uuid.uuid4()
        else:
            self._id = id

        if confirmation == None:
            self.confirmationNumber = str(self._id)
        else:
            self.confirmationNumber = confirmation

        self.state = state

    def addRoomCharge(self, charge: RoomCharge):
        self.roomCharges.add(charge)

    def removeRoomCharge(self, charge: RoomCharge):
        self.roomCharges.remove(charge)

    def calculateTotalInvoice(self):
        pass

    def updateState(self, newState: ReservationState):
        self.state = newState

    def __eq__(self, other):
        return self._id == other._id