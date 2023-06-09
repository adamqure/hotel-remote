from datetime import datetime
from domain.Entities.EmployeeRoles.RoomAvailabilityManagement import RoomAvailabilityManagement
from domain.Entities.People.Employee import Employee
from domain.Entities.Room import Room
from domain.Repositories.RoomsRepository import RoomsRepository
from domain.UseCases.RoomManagement.DeleteRoomUseCase import DeleteRoomUseCase


class MockRoomsRepository(RoomsRepository):
    rooms: list[Room] = []
    def getRoomList(self) -> list[Room]:
        return self.rooms

    def deleteRoom(self, room: Room):
        if room in self.rooms:
            self.rooms.remove(room)
        else:
            raise f"Room does not exist: {room}"
        
def testDeleteRoomWithoutPermissionsRaisesException():
    user = Employee(
        name="Test",
        emailAddress="test@test.com",
        position="Test",
        roles=[]
    )

    room = Room(1, 1)
    
    try:
        useCase = DeleteRoomUseCase(MockRoomsRepository())
        useCase.execute(user, room)
        assert(False)
    except:
        assert(True)

def testDeleteRoomWithoutEnoughParametersRaisesException():
    user = Employee(
        name="Test",
        emailAddress="test@test.com",
        position="Test",
        roles=[RoomAvailabilityManagement()]
    )
    
    try:
        useCase = DeleteRoomUseCase(MockRoomsRepository())
        useCase.execute(user)
        assert(False)
    except:
        assert(True)

def testDeleteRoomAlreadyExistsIsDeleted():
    repository = MockRoomsRepository()
    repository.rooms.append(Room(1, 1))

    user = Employee(
        name="Test",
        emailAddress="test@test.com",
        position="Test",
        roles=[RoomAvailabilityManagement()]
    )

    room = Room(1, 1)

    useCase = DeleteRoomUseCase(repository)

    try:
        useCase.execute(user, room)
        assert(len(repository.getRoomList()) == 0)
    except:
        assert(False)

def testDeleteNonExistingRoomRaisesException():
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

    useCase = DeleteRoomUseCase(MockRoomsRepository())

    try:
        useCase.execute(user, room)
        assert(False)
    except:
        assert(True)