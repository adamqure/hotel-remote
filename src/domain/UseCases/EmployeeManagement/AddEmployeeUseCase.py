from domain.Entities.EmployeeRoles.EmployeeManagement import EmployeeManagement
from domain.Entities.People.Employee import Employee
from domain.Repositories.EmployeeRepository import EmployeeRepository
from domain.UseCases.UseCase import UseCase


class AddEmployeeUseCase(UseCase):
    def __init__(self, repository: EmployeeRepository):
        self._repository = repository

    def execute(self, input: list[Employee]):
        if len(input) != 2:
            raise f"Invalid Input. Missing either user or new employee"
        
        user = input[0]
        newEmployee = input[1]
        if any(isinstance(item, EmployeeManagement) for item in user.getRoles()):
            return self._repository.addEmployee(newEmployee)
        else:
            print(f'User does not have the Employee Management role: {user.getRoles()}')
            raise f"Insufficient Permissions"