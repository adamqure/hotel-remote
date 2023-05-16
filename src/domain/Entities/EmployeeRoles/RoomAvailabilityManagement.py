from domain.Entities.EmployeeRoles.EmployeeRole import EmployeeRole
from domain.Entities.Room import Room

class RoomAvailabilityManagement(EmployeeRole):
    def __init__(self):
        super().__init__("Room Availability Management")

    def makeRoomAvailable(room: Room):
        pass

    def makeRoomUnavailable(room: Room):
        pass