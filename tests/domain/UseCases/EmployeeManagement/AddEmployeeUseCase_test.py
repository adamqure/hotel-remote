from domain.Entities.EmployeeRoles.EmployeeManagement import EmployeeManagement
from domain.Entities.People.Employee import Employee
from domain.Repositories.EmployeeRepository import EmployeeRepository
from domain.UseCases.EmployeeManagement.AddEmployeeUseCase import AddEmployeeUseCase
    
class MockEmployeeRepository(EmployeeRepository):
    employees: list[Employee] = []
    def getEmployeeList(self) -> list[Employee]:
        return self.employees
    
    def addEmployee(self, newEmployee: Employee):
        if newEmployee._id == "Existing":
            raise f"Employee already exists"
        
        self.employees.append(newEmployee)

def testAddEmployeeWithInsufficientInputs():
    useCase = AddEmployeeUseCase(MockEmployeeRepository())

    try:
        useCase.execute([])
        assert(False)
    except:
        assert(True)

def testAddEmployeeWithoutPermissionsRaisesException():
    useCase = AddEmployeeUseCase(MockEmployeeRepository())

    employee = Employee(
        name="Test",
        emailAddress="test@test.com",
        position="Test",
        roles=[]
    )

    try:
        useCase.execute([employee, employee])
        assert(False)
    except:
        assert(True)

def testAddEmployeeWithDuplicateIDRaisesException():
    useCase = AddEmployeeUseCase(MockEmployeeRepository())
    employee = Employee(
        name="Test",
        emailAddress="test@test.com",
        position="Test",
        roles=[EmployeeManagement()]
    )

    newEmployee = Employee(
        name="Test",
        emailAddress="test@test.com",
        position="Test",
        roles=[EmployeeManagement()],
        id="Existing"
    )
    
    try:
        useCase.execute([employee, newEmployee])
        assert(False)
    except:
        assert(True)

def testAddNewEmployeeSuccessful():
    repository = MockEmployeeRepository()
    useCase = AddEmployeeUseCase(repository=repository)
    employee = Employee(
        name="Test",
        emailAddress="test@test.com",
        position="Test",
        roles=[EmployeeManagement()]
    )

    newEmployee = Employee(
        name="Test",
        emailAddress="test@test.com",
        position="Test",
        roles=[EmployeeManagement()],
    )
    
    try:
        useCase.execute([employee, newEmployee])
        assert(len(repository.getEmployeeList()) == 1)
        assert(repository.getEmployeeList()[0]._id == newEmployee._id)
    except:
        assert(False)