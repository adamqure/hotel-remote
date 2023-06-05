from domain.Entities.People.Employee import Employee


class EmployeeRepository:
    def getEmployeeList(self) -> list[Employee]:
        pass

    def addEmployee(self, newEmployee: Employee):
        pass

    def deleteEmployee(self, id: str):
        pass

    def updateEmployee(self, employee: Employee):
        pass