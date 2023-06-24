import datetime
import uuid

from domain.Entities.BillingInformation import BillingInformation


class PaymentMethod:
    def __init__(self, cardNumber, expirationDate: datetime, billingInformation: BillingInformation, id: uuid = None):
        self._creditCardNumber = cardNumber
        self._expirationDate = expirationDate
        self._billingInformation = billingInformation

        if id == None:
            self._id = uuid.uuid4()
        else:
            self._id = uuid.UUID(id)

    def getBillingInformation(self) -> BillingInformation:
        return self._billingInformation
