from domain.Entities.EmployeeRoles.EmployeeRole import EmployeeRole
from domain.Entities.Room import Room
from domain.Entities.RoomCharge import RoomCharge

class RoomChargeManagement(EmployeeRole):
    def __init__(self):
        super().__init__("Room Charge Management")

    def addRoomCharge(room: Room, charge: RoomCharge):
        pass

    def removeRoomCharge(room: Room, charge: RoomCharge):
        pass