from domain.UseCases.UseCase import UseCase
from domain.Repositories.AuthenticationRepository import AuthenticationRepository
from domain.Constants import employeeIDLength

class SignInUseCase(UseCase):
    def __init__(self, repository: AuthenticationRepository):
        self._repository = repository

    def execute(self, input: str):
        if str.count != employeeIDLength:
            raise "Must enter a valid id"
        
        self._repository.signIn(input)
