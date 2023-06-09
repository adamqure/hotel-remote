from domain.Entities.EmployeeRoles.ReservationManagement import ReservationManagement
from domain.Entities.EmployeeRoles.RoomAvailabilityManagement import RoomAvailabilityManagement
from domain.Entities.People.Employee import Employee
from domain.Entities.Room import Room
from domain.Repositories.RoomsRepository import RoomsRepository
from domain.UseCases.UseCase import UseCase


class GetRoomsUseCase(UseCase):
    def __init__(self, repository: RoomsRepository):
        self._repository = repository

    def execute(self, input: Employee) -> list[Room]:
        # Validate user permissions
        if any(isinstance(item, RoomAvailabilityManagement) for item in input.getRoles()):
            return self._repository.getRoomList()
        else:
            print(f'Employee does not have the correct roles to access this information: {input.getRoles()}')
            raise f"Insufficient permissions"