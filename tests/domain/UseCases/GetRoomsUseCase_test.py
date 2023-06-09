from datetime import datetime
from domain.Entities.EmployeeRoles.ReservationManagement import ReservationManagement
from domain.Entities.EmployeeRoles.RoomAvailabilityManagement import RoomAvailabilityManagement
from domain.Entities.People.Employee import Employee
from domain.Entities.Room import Room
from domain.Repositories.RoomsRepository import RoomsRepository
from domain.UseCases.GetRoomsUseCase import GetRoomsUseCase


class MockRoomsRepository(RoomsRepository):
    rooms: list[Room] = []
    def getRoomList(self) -> list[Room]:
        return self.rooms
    
    def getRoomsAvailableForDates(self, dates: list[datetime]) -> list[Room]:
        pass

    def getRoomsWithCapacity(self, capacity: int) -> list[Room]:
        return filter(lambda room: room.capacity >= capacity, self.rooms)
    
def testGetRoomListWithRoomManagementRoleSucceeds():
    repository = MockRoomsRepository()
    repository.rooms.append(
        Room(
            number=1, floor=1
        )
    )

    repository.rooms.append(
        Room(
            number=2, floor=1
        )
    )

    user = Employee(
        name="Test",
        emailAddress="test@test.com",
        position="Test",
        roles=[RoomAvailabilityManagement()]
    )

    useCase = GetRoomsUseCase(repository=repository)
    response = useCase.execute(user)
    assert(len(response) == 2)

def testGetRoomListWithNoRolesRaisesException():
    repository = MockRoomsRepository()

    user = Employee(
        name="Test",
        emailAddress="test@test.com",
        position="Test",
        roles=[]
    )

    useCase = GetRoomsUseCase(repository=repository)
    try:
        response = useCase.execute(user)
        assert(False)
    except:
        assert(True)
