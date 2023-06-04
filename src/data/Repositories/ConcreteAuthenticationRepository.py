from data.DataSources.EmployeeDataSource import EmployeeDataSource
from domain.Repositories.AuthenticationRepository import AuthenticationRepository

class ConcreteAuthenticationRepository(AuthenticationRepository):
    def __init__(self, dataSource: EmployeeDataSource = EmployeeDataSource()):
        self._dataSource = dataSource


    def signIn(self, code: str):
        return self._dataSource.getEmployeeWithID(code)