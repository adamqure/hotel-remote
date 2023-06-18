from domain.Entities.PaymentMethod import PaymentMethod
from domain.Entities.People.Guest import Guest


class PaymentMethodGuestJoiningDataAccessObject:
    def createPaymentMethodGuestJoin(self, paymentMethod: PaymentMethod, guest: Guest):
        pass

    def deletePaymentMethodGuestJoin(self, paymentMethod: PaymentMethod, guest: Guest):
        pass

    def getPaymentMethodForGuest(self, guest: Guest) -> PaymentMethod:
        pass