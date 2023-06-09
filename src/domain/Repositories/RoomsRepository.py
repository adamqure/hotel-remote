from datetime import datetime
from domain.Entities.Room import Room


class RoomsRepository:
    def getRoomList(self) -> list[Room]:
        pass
    
    def getRoomsAvailableForDates(self, dates: list[datetime]) -> list[Room]:
        pass

    def getRoomsWithCapacity(self, capacity: int) -> list[Room]:
        pass