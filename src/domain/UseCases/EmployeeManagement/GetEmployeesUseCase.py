from domain.Entities.EmployeeRoles.EmployeeManagement import EmployeeManagement
from domain.Entities.People.Employee import Employee
from domain.Repositories.EmployeeRepository import EmployeeRepository
from domain.UseCases.UseCase import UseCase


class GetEmployeesUseCase(UseCase):
    def __init__(self, repository: EmployeeRepository):
        self._repository = repository

    def execute(self, user: Employee):
        if any(isinstance(item, EmployeeManagement) for item in user.getRoles()):
            return self._repository.getEmployeeList()
        else:
            print(f'User does not have the Employee Management role: {user.getRoles()}')
            raise f"Insufficient Permissions"
