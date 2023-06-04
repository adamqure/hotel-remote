from domain.Repositories.AuthenticationRepository import AuthenticationRepository
from presentation.Authentication.SignInViewModel import SignInViewModel

class MockAuthenticationRepository(AuthenticationRepository):
    def signIn(self, code: str):
        return

def testSignInFailsWithSmallInput():
    viewModel = SignInViewModel(
        authRepository=MockAuthenticationRepository()
    )

    try:
        viewModel.signIn("Test")
        assert(False)
    except:
        assert(True)

def testSignInFailsWithNoInput():
    viewModel = SignInViewModel(
        authRepository=MockAuthenticationRepository()
    )

    try:
        viewModel.signIn("")
        assert(False)
    except:
        assert(True)

def testSignInSuccessfulWithValidInput():
    viewModel = SignInViewModel(
        authRepository=MockAuthenticationRepository()
    )

    try:
        viewModel.signIn("GoodID")
        assert(True)
    except:
        assert(False)