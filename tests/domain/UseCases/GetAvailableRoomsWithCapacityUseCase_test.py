from datetime import datetime
from domain.Entities.EmployeeRoles.ReservationManagement import ReservationManagement
from domain.Entities.People.Employee import Employee
from domain.Entities.Room import Room
from domain.Entities.States.RoomState import RoomState
from domain.Repositories.RoomsRepository import RoomsRepository
from domain.UseCases.GetAvailableRoomsWithCapacityUseCase import GetAvailableRoomsWithCapacityUseCase


class MockRoomsRepository(RoomsRepository):
    rooms: list[Room] = []
    
    def getRoomsWithCapacity(self, capacity: int) -> list[Room]:
        return list(filter(lambda room: (room.capacity >= capacity and room._state != RoomState.UNAVAILABLE), self.rooms))
    
def testReservationManagementRoleCanFetchRooms():
    repository = MockRoomsRepository()
    repository.rooms.append(
        Room(
            number=1, floor=1, state=RoomState.AVAILABLE, reservedDates=[datetime(year=2023, month=2, day=1)]
        )
    )
    
    user = Employee(
        name="Test",
        emailAddress="test@test.com",
        position="Test",
        roles=[ReservationManagement()]
    )

    useCase = GetAvailableRoomsWithCapacityUseCase(repository=repository)
    response = useCase.execute(user, 0)
    assert(len(response) == 1)

def testNoRoleRaisesError():
    repository = MockRoomsRepository()
    
    user = Employee(
        name="Test",
        emailAddress="test@test.com",
        position="Test",
        roles=[]
    )

    useCase = GetAvailableRoomsWithCapacityUseCase(repository=repository)

    try:    
        response = useCase.execute(user, 0)
        assert(False)
    except:
        assert(True)

def testRoomWithoutSpaceIsFilteredOut():
    repository = MockRoomsRepository()
    repository.rooms.clear()
    repository.rooms.append(
        Room(
            number=1, floor=1, state=RoomState.AVAILABLE, reservedDates=[datetime(year=2023, month=2, day=1)], capacity=3
        )
    )
    
    user = Employee(
        name="Test",
        emailAddress="test@test.com",
        position="Test",
        roles=[ReservationManagement()]
    )

    useCase = GetAvailableRoomsWithCapacityUseCase(repository=repository)
    response = useCase.execute(user, 4)
    assert(len(response) == 0)

def testRoomWithSpaceIsAvailable():
    repository = MockRoomsRepository()
    repository.rooms.clear()
    repository.rooms.append(
        Room(
            number=1, floor=1, state=RoomState.AVAILABLE, reservedDates=[datetime(year=2023, month=2, day=1)], capacity=3
        )
    )
    
    user = Employee(
        name="Test",
        emailAddress="test@test.com",
        position="Test",
        roles=[ReservationManagement()]
    )

    useCase = GetAvailableRoomsWithCapacityUseCase(repository=repository)
    response = useCase.execute(user, 2)
    assert(len(response) == 1)

def testRoomMarkedUnavailableIsFilteredOut():
    repository = MockRoomsRepository()
    repository.rooms.clear()
    repository.rooms.append(
        Room(
            number=1, floor=1, state=RoomState.UNAVAILABLE, reservedDates=[datetime(year=2023, month=2, day=1)], capacity=1
        )
    )
    
    user = Employee(
        name="Test",
        emailAddress="test@test.com",
        position="Test",
        roles=[ReservationManagement()]
    )

    useCase = GetAvailableRoomsWithCapacityUseCase(repository=repository)
    response = useCase.execute(user, 2)
    assert(len(response) == 0)
