from domain.UseCases.SignInUseCase import SignInUseCase
from domain.Repositories.AuthenticationRepository import AuthenticationRepository

class MockAuthenticationRepository(AuthenticationRepository):
    def signIn(self, code: str):
        return

def testSignInUseCaseWithEmptyStringThrowsError():
    useCase = SignInUseCase(MockAuthenticationRepository())
    
    try:
        useCase.execute("")
        assert(False)
    except:
        assert(True)

def testSignInUseCaseWith5CharactersThrowsError():
    useCase = SignInUseCase(MockAuthenticationRepository())

    try:
        useCase.execute("12345")
        assert(False)
    except:
        assert(True)

def testSignInUseCaseWith7CharactersThrowsError():
    useCase = SignInUseCase(MockAuthenticationRepository())

    try:
        useCase.execute("1234567")
        assert(False)
    except:
        assert(True)

def testSignInUseCaseWith6CharactersPasses():
    useCase = SignInUseCase(MockAuthenticationRepository())

    try:
        useCase.execute("123456")
        assert(True)
    except:
        assert(False)
