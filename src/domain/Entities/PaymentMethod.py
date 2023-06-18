import datetime
import uuid


class PaymentMethod:
    def __init__(self, cardNumber, expirationDate: datetime, billingInformation, id: uuid = None):
        self._creditCardNumber = cardNumber
        self._expirationDate = expirationDate
        self._billingInformation = billingInformation

        if id == None:
            self._id = uuid.uuid4()
        else:
            self._id = id

    def processPayment(charge):
        pass

    def processRefund(credit):
        pass