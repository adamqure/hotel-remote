from domain.Entities.EmployeeRoles.EmployeeManagement import EmployeeManagement
from domain.Entities.People.Employee import Employee
from domain.Repositories.EmployeeRepository import EmployeeRepository
from domain.UseCases.UseCase import UseCase


class DeleteEmployeeUseCase(UseCase):
    def __init__(self, repository: EmployeeRepository):
        self._repository = repository

    def execute(self, input: list[Employee]):
        if len(input) != 2:
            raise f"Invalid Input. Missing either user or employee to delete"
        
        user = input[0]
        id = input[1]._id
        if any(isinstance(item, EmployeeManagement) for item in user.getRoles()):
            return self._repository.deleteEmployee(str(id))
        else:
            print(f'User does not have the Employee Management role: {user.getRoles()}')
            raise f"Insufficient Permissions"