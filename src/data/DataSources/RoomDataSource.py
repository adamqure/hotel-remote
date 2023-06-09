from data.DAOs.RoomDataAccessObject import RoomDataAccessObject
from data.SQLiteDB.DAOs.SQLiteRoomDataAccessObject import SQLiteRoomDataAccessObject
from domain.Entities.Room import Room


class RoomDataSource:
    def __init__(self, dao: RoomDataAccessObject = SQLiteRoomDataAccessObject()):
        self._dao = dao

    def getAllRooms(self) -> list[Room]:
        return self._dao.getAllRooms()