from domain.UseCases.SignInUseCase import SignInUseCase

def testSignInUseCaseWithEmptyStringThrowsError():
    useCase = SignInUseCase()
    
    try:
        useCase.execute("")
        assert(False)
    except:
        assert(True)

def testSignInUseCaseWith5CharactersThrowsError():
    useCase = SignInUseCase()

    try:
        useCase.execute("12345")
        assert(False)
    except:
        assert(True)

def testSignInUseCaseWith7CharactersThrowsError():
    useCase = SignInUseCase()

    try:
        useCase.execute("1234567")
        assert(False)
    except:
        assert(True)

def testSignInUseCaseWith6CharactersPasses():
    useCase = SignInUseCase()

    try:
        useCase.execute("123456")
        assert(True)
    except:
        assert(False)
