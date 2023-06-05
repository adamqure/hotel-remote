from data.DataSources.EmployeeDataSource import EmployeeDataSource
from domain.Entities.People.Employee import Employee
from domain.Repositories.EmployeeRepository import EmployeeRepository

class ConcreteEmployeeRepository(EmployeeRepository):
    def __init__(self, dataSource: EmployeeDataSource = EmployeeDataSource()):
        self._dataSource = dataSource
        
    def getEmployeeList(self) -> list[Employee]:
        return self._dataSource.getAllEmployees()