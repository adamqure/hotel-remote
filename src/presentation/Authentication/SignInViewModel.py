from domain.UseCases.Authentication.SignInUseCase import SignInUseCase

class SignInViewModel:
    def __init__(self, authRepository):
        self._repository = authRepository

    def signIn(self, id: str):
        useCase = SignInUseCase(
            repository=self._repository
        )

        useCase.execute(id)
        print(f"Sign In Successful. ID={id}")