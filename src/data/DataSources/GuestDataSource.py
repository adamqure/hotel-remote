from data.DAOs.BillingInformationDataAccessObject import BillingInformationDataAccessObject
from data.DAOs.GuestDataAccessObject import GuestDataAccessObject
from data.DAOs.PaymentMethodBillingInformationJoiningDataAccessObject import PaymentMethodBillingInformationJoiningDataAccessObject
from data.DAOs.PaymentMethodDataAccessObject import PaymentMethodDataAccessObject
from data.DAOs.PaymentMethodGuestJoiningDataAccessObject import PaymentMethodGuestJoiningDataAccessObject
from data.SQLiteDB.DAOs.SQLiteBillingInformationDataAccessObject import SQLiteBillingInformationDataAccessObject
from data.SQLiteDB.DAOs.SQLiteGuestDataAccessObject import SQLiteGuestDataAccessObject
from data.SQLiteDB.DAOs.SQLitePaymentMethodBillingInformationJoiningDataAccessObject import SQLitePaymentMethodBillingInformationJoiningDataAccessObject
from data.SQLiteDB.DAOs.SQLitePaymentMethodDataAccessObject import SQLitePaymentMethodDataAccessObject
from data.SQLiteDB.DAOs.SQLitePaymentMethodGuestJoiningDataAccessObject import SQLitePaymentMethodGuestJoiningDataAccessObject
from domain.Entities.People.Guest import Guest


class GuestDataSource:
    def __init__(
        self, 
        guestDAO: GuestDataAccessObject = SQLiteGuestDataAccessObject(),
        paymentMethodDAO: PaymentMethodDataAccessObject = SQLitePaymentMethodDataAccessObject(),
        billingInformationDAO: BillingInformationDataAccessObject = SQLiteBillingInformationDataAccessObject(),
        paymentMethodBillingInfoJoinDAO: PaymentMethodBillingInformationJoiningDataAccessObject = SQLitePaymentMethodBillingInformationJoiningDataAccessObject(),
        paymentMethodGuestJoinDAO: PaymentMethodGuestJoiningDataAccessObject = SQLitePaymentMethodGuestJoiningDataAccessObject()
    ):
        self._guestDAO = guestDAO
        self._paymentMethodDAO = paymentMethodDAO
        self._billingInformationDAO = billingInformationDAO
        self._paymentMethodBillingInfoJoinDAO = paymentMethodBillingInfoJoinDAO
        self._paymentMethodGuestJoinDAO = paymentMethodGuestJoinDAO

    def createGuest(self, guest: Guest):
        self._billingInformationDAO.createBillingInformation(
            guest._paymentMethod.getBillingInformation()
        )

        self._paymentMethodDAO.createPaymentMethod(
            guest._paymentMethod
        )

        self._paymentMethodBillingInfoJoinDAO.createPaymentMethodBillingInformationJoin(guest._paymentMethod, guest._paymentMethod.getBillingInformation())

        self._guestDAO.createGuest(
            guest
        )

        self._paymentMethodGuestJoinDAO.createPaymentMethodGuestJoin(guest._paymentMethod, guest)

    def updateGuest(self, guest: Guest):
        self._billingInformationDAO.updateBillingInformation(
            guest._paymentMethod.getBillingInformation()
        )

        self._paymentMethodDAO.updatePaymentMethod(
            guest._paymentMethod
        )

        self._guestDAO.updateGuest(
            guest
        )