from domain.Entities.EmployeeRoles.EmployeeManagement import EmployeeManagement
from domain.Entities.People.Employee import Employee
from domain.Repositories.EmployeeRepository import EmployeeRepository
from domain.UseCases.DeleteEmployeeUseCase import DeleteEmployeeUseCase


class MockEmployeeRepository(EmployeeRepository):
    employees: list[Employee] = []
    def getEmployeeList(self) -> list[Employee]:
        return self.employees
    
    def addEmployee(self, newEmployee: Employee):
        if newEmployee._id == "Existing":
            raise f"Employee already exists"
        
        self.employees.append(newEmployee)

    def deleteEmployee(self, id: str):
        employee = next(employee for employee in self.employees if employee._id == id)
        if employee == None:
            raise f"Employee doesn't exist"
        else:
            self.employees.remove(employee)

def testDeleteNonExistingEmployeeRaisesException():
    useCase = DeleteEmployeeUseCase(MockEmployeeRepository())

    employee = Employee(
        name="Test",
        emailAddress="test@test.com",
        position="Test",
        roles=[EmployeeManagement()]
    )

    try:
        useCase.execute(
            [employee, employee]
        )
        assert(False)
    except:
        assert(True)

def testDeleteWithoutPermissionsRaisesException():
    useCase = DeleteEmployeeUseCase(MockEmployeeRepository())

    employee = Employee(
        name="Test",
        emailAddress="test@test.com",
        position="Test",
        roles=[]
    )

    try:
        useCase.execute(
            [employee, employee]
        )
        assert(False)
    except:
        assert(True)

def testDeleteWithInvalidInputRaisesException():
    useCase = DeleteEmployeeUseCase(MockEmployeeRepository())

    try:
        useCase.execute([])
        assert(False)
    except:
        assert(True)

def testDeleteExistingEmployeeSuccessful():
    repository = MockEmployeeRepository()
    useCase = DeleteEmployeeUseCase(repository)

    employee = Employee(
        name="Test",
        emailAddress="test@test.com",
        position="Test",
        roles=[]
    )

    manager = Employee(
        name="Test",
        emailAddress="test@test.com",
        position="Test",
        roles=[EmployeeManagement()]
    )

    repository.addEmployee(employee)
    assert(len(repository.getEmployeeList()) == 1)

    try:
        useCase.execute([manager, employee])
        assert(len(repository.getEmployeeList()) == 0)
    except:
        assert(False)