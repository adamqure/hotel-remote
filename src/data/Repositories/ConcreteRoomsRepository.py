from datetime import datetime
from data.DataSources.RoomDataSource import RoomDataSource
from domain.Entities.Room import Room
from domain.Entities.States.RoomState import RoomState
from domain.Repositories.RoomsRepository import RoomsRepository


class ConcreteRoomsRepository(RoomsRepository):
    def __init__(self, dataSource: RoomDataSource = RoomDataSource()):
        self._dataSource = dataSource

    def getRoomList(self) -> list[Room]:
        return self._dataSource.getAllRooms()
    
    def getRoomsAvailableForDates(self, dates: list[datetime]) -> list[Room]:
        rooms = self._dataSource.getAllRooms()
        return list(filter(lambda room: self.roomAvailableOnDates(room, dates), rooms))

    def getRoomsWithCapacity(self, capacity: int) -> list[Room]:
        rooms = self._dataSource.getAllRooms()
        return list(filter(lambda room: (room.capacity >= capacity and room._state != RoomState.UNAVAILABLE), rooms))
        
    def roomAvailableOnDates(self, room: Room, dates: list[datetime]) -> bool:
        hasReservedRoom = any(x in room.reservedDates for x in dates) or room._state == RoomState.UNAVAILABLE
        return not hasReservedRoom
    
    def createRoom(self, room: Room):
        self._dataSource.createRoom(room)