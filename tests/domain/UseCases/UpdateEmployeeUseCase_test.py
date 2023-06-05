from domain.Entities.EmployeeRoles.EmployeeManagement import EmployeeManagement
from domain.Entities.EmployeeRoles.Housekeeper import Housekeeper
from domain.Entities.People.Employee import Employee
from domain.Repositories.EmployeeRepository import EmployeeRepository
from domain.UseCases.UpdateEmployeeUseCase import UpdateEmployeeUseCase


class MockEmployeeRepository(EmployeeRepository):
    employees: list[Employee] = []
    def getEmployeeList(self) -> list[Employee]:
        return self.employees
    
    def addEmployee(self, newEmployee: Employee):
        self.employees.append(newEmployee)

    def deleteEmployee(self, id: str):
        employee = next(employee for employee in self.employees if str(employee._id) == id)
        if employee == None:
            raise f"Employee doesn't exist"
        else:
            self.employees.remove(employee)

    def updateEmployee(self, employee: Employee):
        existingEmployee = next(x for x in self.employees if x._id == employee._id)
        if employee == None:
            raise f"Employee doesn't exist"
        else:
            self.employees.remove(employee)
            self.employees.append(existingEmployee)

def testUpdateNonExistingEmployeeRaisesException():
    repository = MockEmployeeRepository()
    useCase = UpdateEmployeeUseCase(repository)

    manager = Employee(
        name="Test",
        emailAddress="test@test.com",
        position="Test",
        roles=[EmployeeManagement()]
    )

    employee = Employee(
        name="Test",
        emailAddress="test@test.com",
        position="Test",
        roles=[]
    )

    try:
        useCase.execute([manager, employee])
        assert(False)
    except:
        assert(True)

def testUpdateExistingEmployeeSucceeds():
    repository = MockEmployeeRepository()
    useCase = UpdateEmployeeUseCase(repository)

    manager = Employee(
        name="Test",
        emailAddress="test@test.com",
        position="Test",
        roles=[EmployeeManagement()]
    )

    employee = Employee(
        name="Test",
        emailAddress="test@test.com",
        position="Test",
        roles=[]
    )

    repository.addEmployee(employee)

    employee.addRole(Housekeeper())

    try:
        useCase.execute([manager, employee])
        updatedEmployee = next(x for x in repository.getEmployeeList() if str(x._id) == str(employee._id))
        assert(updatedEmployee.getRoles() == employee.getRoles())
    except:
        assert(False)

def testUpdateEmployeeWithoutPermissionsRaisesException():
    repository = MockEmployeeRepository()
    useCase = UpdateEmployeeUseCase(repository)

    manager = Employee(
        name="Test",
        emailAddress="test@test.com",
        position="Test",
        roles=[]
    )

    employee = Employee(
        name="Test",
        emailAddress="test@test.com",
        position="Test",
        roles=[]
    )

    try:
        useCase.execute([manager, employee])
        assert(False)
    except:
        assert(True)

def testUpdateInvalidInputRaisesException():
    useCase = UpdateEmployeeUseCase(MockEmployeeRepository())
    try:
        useCase.execute([])
        assert(False)
    except:
        assert(True)