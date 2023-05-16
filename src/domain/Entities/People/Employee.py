from domain.Entities.People.Person import Person
from domain.Constants import employeeIDLength
from domain.Entities.EmployeeRoles.StaffPosition import StaffPosition
from domain.Entities.EmployeeRoles.EmployeeRole import EmployeeRole
import random
import string

class Employee(Person):
    def __init__(self, name: str, emailAddress: str, position: StaffPosition, roles: EmployeeRole):
        self.position = position
        self._roles = roles
        self.employeeID = ''.join(random.choices(string.digits, k=employeeIDLength))
        super().__init__(name, emailAddress)

    def getRoles(self):
        return self._roles
