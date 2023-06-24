import uuid
from domain.Entities.PaymentMethod import PaymentMethod
from domain.Entities.People.Person import Person

class Guest(Person):
    def __init__(self, name, emailAddress, paymentMethod: PaymentMethod, reservations = [], id: uuid = None):
        self._paymentMethod = paymentMethod
        self.reservations = reservations

        if id == None:
            self._id = uuid.uuid4()
        else:
            self._id = id

        super().__init__(name, emailAddress, self._id)

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
