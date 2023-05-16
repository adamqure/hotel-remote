class PaymentMethod:
    def __init__(self, cardNumber, expirationDate, securityCode, billingInformation):
        self._creditCardNumber = cardNumber
        self._expirationDate = expirationDate
        self._securityCode = securityCode
        self._billingInformation = billingInformation

    def processPayment(charge):
        pass

    def processRefund(credit):
        pass