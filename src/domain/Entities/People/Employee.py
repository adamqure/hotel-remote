from domain.Entities.People.Person import Person
from domain.Constants import employeeIDLength
from domain.Entities.EmployeeRoles.StaffPosition import StaffPosition
from domain.Entities.EmployeeRoles.EmployeeRole import EmployeeRole
import uuid
import random
import string

class Employee(Person):
    def __init__(self, name: str, emailAddress: str, position: StaffPosition, roles: list[EmployeeRole], employeeID: str = '', id: uuid = None):
        self.position = position
        self._roles = roles

        if id == None:
            self._id = uuid.uuid4()
        else:
            self._id = id

        if employeeID == '':
            self.employeeID = ''.join(random.choices(string.digits, k=employeeIDLength))
        else:
            self.employeeID = employeeID

        super().__init__(name, emailAddress, self._id)

    def getRoles(self):
        return self._roles
