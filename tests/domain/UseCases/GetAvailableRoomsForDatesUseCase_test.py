from datetime import datetime
from domain.Entities.EmployeeRoles.ReservationManagement import ReservationManagement
from domain.Entities.People.Employee import Employee
from domain.Entities.Room import Room
from domain.Entities.States.RoomState import RoomState
from domain.Repositories.RoomsRepository import RoomsRepository
from domain.UseCases.GetAvailableRoomsForDatesUseCase import GetAvailableRoomsForDatesUseCase


class MockRoomsRepository(RoomsRepository):
    rooms: list[Room] = []
    def getRoomList(self) -> list[Room]:
        return self.rooms
    
    def getRoomsAvailableForDates(self, dates: list[datetime]) -> list[Room]:
        return list(filter(lambda room: self.roomAvailableOnDates(room, dates), self.rooms))

    def getRoomsWithCapacity(self, capacity: int) -> list[Room]:
        return list(filter(lambda room: (room.capacity >= capacity and room._state != RoomState.UNAVAILABLE), self.rooms))
    
    def roomAvailableOnDates(self, room: Room, dates: list[datetime]) -> bool:
        hasReservedRoom = any(x in room.reservedDates for x in dates) or room._state == RoomState.UNAVAILABLE
        return not hasReservedRoom
    
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

    useCase = GetAvailableRoomsForDatesUseCase(repository=repository)
    response = useCase.execute(user, [])
    assert(len(response) == 1)

def testNoRoleRaisesError():
    repository = MockRoomsRepository()
    
    user = Employee(
        name="Test",
        emailAddress="test@test.com",
        position="Test",
        roles=[]
    )

    useCase = GetAvailableRoomsForDatesUseCase(repository=repository)

    try:    
        response = useCase.execute(user, [datetime.now()])
        assert(False)
    except:
        assert(True)

def testRoomWithStartDateIsFiltered():
    repository = MockRoomsRepository()
    repository.rooms.append(
        Room(
            number=1, floor=1, reservedDates=[datetime(year=2023, month=2, day=1)]
        )
    )
    
    user = Employee(
        name="Test",
        emailAddress="test@test.com",
        position="Test",
        roles=[ReservationManagement()]
    )

    useCase = GetAvailableRoomsForDatesUseCase(repository=repository)
    response = useCase.execute(user, [datetime(year=2023, month=2, day=1), datetime(year=2023, month=2, day=2)])
    assert(len(response) == 0)

def testRoomWithEndDateIsFiltered():
    repository = MockRoomsRepository()
    repository.rooms.append(
        Room(
            number=1, floor=1, reservedDates=[datetime(year=2023, month=2, day=2)]
        )
    )
    
    user = Employee(
        name="Test",
        emailAddress="test@test.com",
        position="Test",
        roles=[ReservationManagement()]
    )

    useCase = GetAvailableRoomsForDatesUseCase(repository=repository)
    response = useCase.execute(user, [datetime(year=2023, month=2, day=1), datetime(year=2023, month=2, day=2)])
    assert(len(response) == 0)

def testRoomWithAllDatesIsFiltered():
    repository = MockRoomsRepository()
    repository.rooms.append(
        Room(
            number=1, floor=1, reservedDates=[datetime(year=2023, month=2, day=1), datetime(year=2023, month=2, day=2)]
        )
    )
    
    user = Employee(
        name="Test",
        emailAddress="test@test.com",
        position="Test",
        roles=[ReservationManagement()]
    )

    useCase = GetAvailableRoomsForDatesUseCase(repository=repository)
    response = useCase.execute(user, [datetime(year=2023, month=2, day=1), datetime(year=2023, month=2, day=2)])
    assert(len(response) == 0)

def testRoomStateUnavailableIsFiltered():
    repository = MockRoomsRepository()
    repository.rooms.append(
        Room(
            number=1, floor=1, state= RoomState.UNAVAILABLE, reservedDates=[datetime(year=2023, month=2, day=1), datetime(year=2023, month=2, day=2)]
        )
    )
    
    user = Employee(
        name="Test",
        emailAddress="test@test.com",
        position="Test",
        roles=[ReservationManagement()]
    )

    useCase = GetAvailableRoomsForDatesUseCase(repository=repository)
    response = useCase.execute(user, [datetime(year=2023, month=2, day=1), datetime(year=2023, month=2, day=2)])
    assert(len(response) == 0)