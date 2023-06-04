from domain.Entities.People.Employee import Employee


class EmployeeDataAccessObject:
    def getEmployee(self, id: str) -> Employee:
        pass

    def getAllEmployees(self) -> list[Employee]:
        pass

    def deleteEmployee(self, id: str):
        pass

    def updateEmployee(self, employee: Employee):
        pass

    def addEmployee(self, employee: Employee):
        pass