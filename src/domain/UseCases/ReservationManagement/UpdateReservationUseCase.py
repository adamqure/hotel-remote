from domain.Entities.EmployeeRoles.ReservationManagement import ReservationManagement
from domain.Entities.People.Employee import Employee
from domain.Repositories.ReservationRepository import ReservationRepository
from domain.UseCases.UseCase import UseCase


class UpdateReservationUseCase(UseCase):
    def __init__(self, repository: ReservationRepository):
        self._repository = repository

    def execute(self, *args):
        # Validate user permissions
        if len(args) != 2 or not isinstance(args[0], Employee):
            raise f"Invalid input: {args}"
        
        user = args[0]
        reservation = args[1]
        guest = args[2]
        
        if any(isinstance(item, ReservationManagement) for item in user.getRoles()):
            return self._repository.updateReservation(reservation, guest)
        else:
            print(f'Employee does not have the correct roles to execute this use case: {input.getRoles()}')
            raise f"Insufficient permissions"