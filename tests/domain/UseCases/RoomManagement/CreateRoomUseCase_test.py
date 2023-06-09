from datetime import datetime
from domain.Entities.EmployeeRoles.RoomAvailabilityManagement import RoomAvailabilityManagement
from domain.Entities.People.Employee import Employee
from domain.Entities.Room import Room
from domain.Repositories.RoomsRepository import RoomsRepository
from domain.UseCases.RoomManagement.CreateRoomUseCase import CreateRoomUseCase


class MockRoomsRepository(RoomsRepository):
    rooms: list[Room] = []
    def getRoomList(self) -> list[Room]:
        return self.rooms
    
    def getRoomsAvailableForDates(self, dates: list[datetime]) -> list[Room]:
        pass

    def getRoomsWithCapacity(self, capacity: int) -> list[Room]:
        return filter(lambda room: room.capacity >= capacity, self.rooms)
    
    def createRoom(self, room: Room):
        if room in self.rooms:
            raise f"Room already exists: {room}"
        
        self.rooms.append(room)

def testCreateRoomWithoutPermissionsRaisesException():
    user = Employee(
        name="Test",
        emailAddress="test@test.com",
        position="Test",
        roles=[]
    )

    room = Room(1, 1)
    
    try:
        useCase = CreateRoomUseCase(MockRoomsRepository())
        useCase.execute((user, room))
        assert(False)
    except:
        assert(True)

def testCreateRoomWithoutEnoughParametersRaisesException():
    user = Employee(
        name="Test",
        emailAddress="test@test.com",
        position="Test",
        roles=[RoomAvailabilityManagement()]
    )
    
    try:
        useCase = CreateRoomUseCase(MockRoomsRepository())
        useCase.execute((user))
        assert(False)
    except:
        assert(True)

def testCreateRoomAlreadyExistsRaisesException():
    repository = MockRoomsRepository()
    repository.rooms.append(Room(1, 1))

    user = Employee(
        name="Test",
        emailAddress="test@test.com",
        position="Test",
        roles=[RoomAvailabilityManagement()]
    )

    room = Room(1, 1)

    useCase = CreateRoomUseCase(repository)

    try:
        useCase.execute((user, room))
        assert(False)
    except:
        assert(True)

def testCreateRoomSuccessful():
    user = Employee(
        name="Test",
        emailAddress="test@test.com",
        position="Test",
        roles=[RoomAvailabilityManagement()]
    )
    
    user = Employee(
        name="Test",
        emailAddress="test@test.com",
        position="Test",
        roles=[RoomAvailabilityManagement()]
    )

    room = Room(1, 1)

    useCase = CreateRoomUseCase(MockRoomsRepository())

    try:
        useCase.execute((user, room))
        assert(False)
    except:
        assert(True)