from datetime import datetime
from uuid import UUID
import uuid
from domain.Entities.EmployeeRoles.Billing import Billing
from domain.Entities.People.Employee import Employee
from domain.Entities.Reservation import Reservation
from domain.Entities.RoomCharge import RoomCharge
from domain.Repositories.BillingRepository import BillingRepository
from domain.UseCases.BillingManagement.GenerateInvoiceUseCase import GenerateInvoiceUseCase


class MockBillingRepository(BillingRepository):
    def __init__(self, emptyID: UUID, fullid: UUID) -> None:
        super().__init__()
        self._emptyID = emptyID
        self._fullID = fullid

    def generateInvoice(self, reservation: Reservation) -> list[RoomCharge]:
        if reservation._id == self._emptyID:
            return []
        elif reservation._id == self._fullID:
            charge1 = RoomCharge("Test1", 1.5, 1, "Test")
            charge2 = RoomCharge("Test2", 3.5, 1, "Test")
            return [charge1, charge2]
        else:
            raise f"Reservation {reservation} does not exist"
        
def testGenerateInvoiceForNoReservation():
    useCase = GenerateInvoiceUseCase(MockBillingRepository(emptyID=None, fullid=None))
    employee = Employee(
        name="Test",
        emailAddress="test@test.com",
        position="Test",
        roles=[Billing()]
    )

    reservation = Reservation(datetime.now(), datetime.now(), 1, None)

    try:
        useCase.execute(employee, reservation)
    except:
        assert(True)

def testGenerateInvoiceForReservationWithNoRoomCharges():
    emptyID = uuid.uuid4()
    useCase = GenerateInvoiceUseCase(MockBillingRepository(emptyID=emptyID, fullid=None))
    employee = Employee(
        name="Test",
        emailAddress="test@test.com",
        position="Test",
        roles=[Billing()]
    )

    reservation = Reservation(datetime.now(), datetime.now(), 1, None, id = emptyID)
    assert(len(useCase.execute(employee, reservation)) == 0)

def testGenerateInvoiceForReservationWithCharges():
    fullID = uuid.uuid4()
    useCase = GenerateInvoiceUseCase(MockBillingRepository(emptyID=None, fullid=fullID))
    employee = Employee(
        name="Test",
        emailAddress="test@test.com",
        position="Test",
        roles=[Billing()]
    )

    reservation = Reservation(datetime.now(), datetime.now(), 1, None, id = fullID)
    assert(len(useCase.execute(employee, reservation)) == 2)
    
def testGenerateInvoiceWithNoPermissions():
    useCase = GenerateInvoiceUseCase(MockBillingRepository(emptyID=None, fullid=None))
    employee = Employee(
        name="Test",
        emailAddress="test@test.com",
        position="Test",
        roles=[]
    )

    reservation = Reservation(datetime.now(), datetime.now(), 1, None)

    try:
        useCase.execute(employee, reservation)
        assert(False)
    except:
        assert(True)