from domain.Entities.People.Person import Person

class Guest(Person):
    def __init__(self, name, emailAddress, paymentMethod, reservations = []):
        self._paymentMethod = paymentMethod
        self.reservations = reservations
        super().__init__(name, emailAddress)

    def makeReservation(reservation):
        pass

    def updateReservation(reservation):
        pass

    def cancelReservation(reservation):
        pass

    def addPaymentMethod(paymentMethod):
        pass

    def removePaymentMethod(paymentMethod):
        pass

    def updatePaymentMethod(paymentMethod):
        pass
