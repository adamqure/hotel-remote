from domain.Entities.Room import Room


class RoomDataAccessObject:
    def getRoomByNumber(self, number: int) -> Room:
        pass

    def getAllRooms(self) -> list[Room]:
        pass

    def createRoom(self, room: Room):
        pass