from domain.Entities.EmployeeRoles.Billing import Billing
from domain.Entities.People.Employee import Employee
from domain.Repositories.BillingRepository import BillingRepository
from domain.UseCases.UseCase import UseCase


class ProcessPaymentUseCase(UseCase):
    def __init__(self, repository: BillingRepository):
        self._repository = repository

    def execute(self, *args):
        # Validate user permissions
        if len(args) != 2 or not isinstance(args[0], Employee):
            raise f"Invalid input: {args}"
        
        user = args[0]
        reservation = args[1]
        
        if any(isinstance(item, Billing) for item in user.getRoles()):
            return self._repository.processPayment(reservation)
        else:
            print(f'Employee does not have the correct roles to execute this use case: {input.getRoles()}')
            raise f"Insufficient permissions"