from datetime import datetime
from domain.Entities.States.RoomState import RoomState
import uuid

class Room:
    def __init__(self, number: int, floor: int, state: RoomState = RoomState.UNAVAILABLE, reservedDates: list[datetime] = [], capacity: int = 0, id: uuid = None):
        self.number = number
        self.floor = floor
        self._state = state
        self.reservedDates: list[datetime] = reservedDates
        self.capacity = capacity
        if id == None:
            self._id = uuid.uuid4()
        else:
            self._id = id

    def updateState(self, newState: RoomState):
        self._state = newState

    def addReservation(self, newDate: datetime):
        if newDate in self.reservedDates:
            raise f"Date already reserved"
        
        self.reservedDates.append(newDate)

    def __eq__(self, other):
        return self._id == other._id