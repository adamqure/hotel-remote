from domain.Entities.States.RoomState import RoomState

class Room:
    def __init__(self, number, floor):
        self.number = number
        self.floor = floor
        self._state = RoomState.AVAILABLE

    def updateState(self, newState: RoomState):
        self._state = newState