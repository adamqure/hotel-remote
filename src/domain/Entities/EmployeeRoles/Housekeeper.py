from domain.Entities.EmployeeRoles.EmployeeRole import EmployeeRole
from domain.Entities.Room import Room

class Housekeeper(EmployeeRole):
    def __init__(self):
        super().__init__("Housekeeper")

    def cleanRoom(self, room: Room):
        pass