from domain.Entities.People.Guest import Guest


class GuestDataAccessObject:
    def createGuest(self, guest: Guest):
        pass

    def getAllGuests(self) -> list[Guest]:
        pass

    def deleteGuest(self, id: str):
        pass

    def updateGuest(self, guest: Guest):
        pass

