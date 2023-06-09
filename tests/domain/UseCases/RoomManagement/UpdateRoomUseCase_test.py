from datetime import datetime
from domain.Entities.EmployeeRoles.RoomAvailabilityManagement import RoomAvailabilityManagement
from domain.Entities.People.Employee import Employee
from domain.Entities.Room import Room
from domain.Repositories.RoomsRepository import RoomsRepository
from domain.UseCases.RoomManagement.UpdateRoomUseCase import UpdateRoomUseCase


class MockRoomsRepository(RoomsRepository):
    rooms: list[Room] = []
    def getRoomList(self) -> list[Room]:
        return self.rooms

    def updateRoom(self, room: Room):
        if room in self.rooms:
            self.rooms.remove(room)
            self.rooms.append(room)
        else:
            raise f"Room does not exist" 



def testUpdateRoomWithoutPermissionsRaisesException():
    user = Employee(
        name="Test",
        emailAddress="test@test.com",
        position="Test",
        roles=[]
    )

    room = Room(1, 1)
    
    try:
        useCase = UpdateRoomUseCase(MockRoomsRepository())
        useCase.execute(user, room)
        assert(False)
    except:
        assert(True)

def testUpdateRoomWithoutEnoughParametersRaisesException():
    user = Employee(
        name="Test",
        emailAddress="test@test.com",
        position="Test",
        roles=[RoomAvailabilityManagement()]
    )
    
    try:
        useCase = UpdateRoomUseCase(MockRoomsRepository())
        useCase.execute(user)
        assert(False)
    except:
        assert(True)

def testUpdateRoomAlreadyExistsSucceeds():
    repository = MockRoomsRepository()
    repository.rooms.append(Room(1, 1))

    user = Employee(
        name="Test",
        emailAddress="test@test.com",
        position="Test",
        roles=[RoomAvailabilityManagement()]
    )

    room = Room(1, 1)

    useCase = UpdateRoomUseCase(repository)

    try:
        useCase.execute(user, room)
        assert(True)
    except:
        assert(False)

def testUpdateRoomThatDoesntExistRaisesException():
    repository = MockRoomsRepository()
    repository.rooms.clear()

    user = Employee(
        name="Test",
        emailAddress="test@test.com",
        position="Test",
        roles=[RoomAvailabilityManagement()]
    )

    room = Room(1, 1)

    useCase = UpdateRoomUseCase(repository)

    try:
        useCase.execute(user, room)
        assert(False)
    except:
        assert(True)