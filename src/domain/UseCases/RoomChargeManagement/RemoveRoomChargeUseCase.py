from domain.Entities.EmployeeRoles.RoomChargeManagement import RoomChargeManagement
from domain.Entities.People.Employee import Employee
from domain.Repositories.RoomChargeRepository import RoomChargeRepository
from domain.UseCases.UseCase import UseCase


class RemoveRoomChargeUseCase(UseCase):
    def __init__(self, repository: RoomChargeRepository):
        self._repository = repository

    def execute(self, *args):
        # Validate user permissions
        if len(args) != 3 or not isinstance(args[0], Employee):
            raise f"Invalid input: {args}"
        
        user = args[0]
        reservation = args[1]
        roomCharge = args[2]
        
        if any(isinstance(item, RoomChargeManagement) for item in user.getRoles()):
            return self._repository.removeRoomCharge(reservation, roomCharge)
        else:
            print(f'Employee does not have the correct roles to execute this use case: {input.getRoles()}')
            raise f"Insufficient permissions"