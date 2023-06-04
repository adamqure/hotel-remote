from data.DAOs.EmployeeDataAccessObject import EmployeeDataAccessObject
from data.SQLiteDB.DAOs.SQLiteEmployeeDataAccessObject import SQLiteEmployeeDataAccessObject
from domain.Entities.People.Employee import Employee


class EmployeeDataSource:
    def __init__(self, dao: EmployeeDataAccessObject = SQLiteEmployeeDataAccessObject()):
        self._dao = dao

    def getEmployeeWithID(self, id: str) -> Employee:
        return self._dao.getEmployee(id)