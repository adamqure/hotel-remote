from domain.Entities.EmployeeRoles.EmployeeManagement import EmployeeManagement
from domain.Entities.People.Employee import Employee
from domain.Repositories.EmployeeRepository import EmployeeRepository
from domain.UseCases.EmployeeManagement.GetEmployeesUseCase import GetEmployeesUseCase

class MockEmptyEmployeeRepository(EmployeeRepository):
    def getEmployeeList(self) -> list[Employee]:
        return []
    
class MockEmployeeRepository(EmployeeRepository):
    def getEmployeeList(self) -> list[Employee]:
        employee = Employee(
            name="Test",
            emailAddress="test@test.com",
            position="Test",
            roles=[]
        )
        return [employee]

def testGetEmployeesWithInsufficeintPermissionsRaisesException():
    useCase = GetEmployeesUseCase(MockEmployeeRepository())
    employee = Employee(
        name="Test",
        emailAddress="test@test.com",
        position="Test",
        roles=[]
    )

    try:
        response = useCase.execute(employee)
        assert(False)
    except:
        assert(True)

def testGetEmployeesWithNoEmployeesReturnsEmptyList():
    useCase = GetEmployeesUseCase(MockEmptyEmployeeRepository())
    employee = Employee(
        name="Test",
        emailAddress="test@test.com",
        position="Test",
        roles=[EmployeeManagement()]
    )
    try:
        response = useCase.execute(employee)
        assert(len(response) == 0)
    except:
        assert(False)

def testGetEmployeesReturnsAllEmployees():
    useCase = GetEmployeesUseCase(MockEmployeeRepository())
    employee = Employee(
        name="Test",
        emailAddress="test@test.com",
        position="Test",
        roles=[EmployeeManagement()]
    )
    try:
        response = useCase.execute(employee)
        assert(len(response) == 1)
    except:
        assert(False)