from domain.Entities.EmployeeRoles.RoomAvailabilityManagement import RoomAvailabilityManagement
from domain.Entities.People.Employee import Employee
from domain.Repositories.RoomsRepository import RoomsRepository
from domain.UseCases.UseCase import UseCase


class MakeRoomAvailableUseCase(UseCase):
    def __init__(self, repository: RoomsRepository):
        self._repository = repository

    def execute(self, *args):
        # Validate user permissions
        if len(args) != 2 or not isinstance(args[0], Employee):
            raise f"Invalid input: {args}"
        
        user = args[0]
        room = args[1]
        
        if any(isinstance(item, RoomAvailabilityManagement) for item in user.getRoles()):
            return self._repository.makeRoomAvailable(room)
        else:
            print(f'Employee does not have the correct roles to execute this use case: {input.getRoles()}')
            raise f"Insufficient permissions"