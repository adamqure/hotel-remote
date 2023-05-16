from domain.UseCases.UseCase import UseCase
from domain.Repositories.AuthenticationRepository import AuthenticationRepository
from domain.Constants import employeeIDLength

class SignInUseCase(UseCase):
    def __init__(self, repository: AuthenticationRepository):
        self._repository = repository

    def execute(self, input: str):
        if len(input) != employeeIDLength:
            print(f'Received {len(input)} characters, expected {employeeIDLength}')
            raise f"Must enter a valid id"
        
        self._repository.signIn(input)
