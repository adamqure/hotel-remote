from domain.Entities.BillingInformation import BillingInformation
from domain.Entities.PaymentMethod import PaymentMethod


class PaymentMethodBillingInformationJoiningDataAccessObject:
    def getBillingInformationForPaymentMethod(self, paymentMethod: PaymentMethod) -> BillingInformation:
        pass

    def deletePaymentMethodBillingInformationJoin(self, paymentMethod: PaymentMethod, billingInformation: BillingInformation):
        pass

    def createPaymentMethodBillingInformationJoin(self, paymentMethod: PaymentMethod, billingInformation: BillingInformation):
        pass