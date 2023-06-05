from data.DAOs.EmployeeDataAccessObject import EmployeeDataAccessObject
from data.SQLiteDB.DAOs.SQLiteEmployeeDataAccessObject import SQLiteEmployeeDataAccessObject
from domain.Entities.People.Employee import Employee


class EmployeeDataSource:
    def __init__(self, dao: EmployeeDataAccessObject = SQLiteEmployeeDataAccessObject()):
        self._dao = dao

    def getEmployeeWithID(self, id: str) -> Employee:
        return self._dao.getEmployee(id)
    
    def getAllEmployees(self) -> list[Employee]:
        return self._dao.getAllEmployees()
    
    def addEmployee(self, employee: Employee):
        return self._dao.addEmployee(employee)

    def deleteEmployee(self, id: str):
        self._dao.deleteEmployee(id)