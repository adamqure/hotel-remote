from datetime import datetime
import sqlite3
import pytest
from data.SQLiteDB.DAOs.SQLiteBillingInformationDataAccessObject import SQLiteBillingInformationDataAccessObject
from data.SQLiteDB.DAOs.SQLitePaymentMethodBillingInformationJoiningDataAccessObject import SQLitePaymentMethodBillingInformationJoiningDataAccessObject
from data.SQLiteDB.DAOs.SQLitePaymentMethodDataAccessObject import SQLitePaymentMethodDataAccessObject

from data.SQLiteDB.SQLiteDBConstants import DB_PATH
from domain.Entities.BillingInformation import BillingInformation
from domain.Entities.PaymentMethod import PaymentMethod


@pytest.fixture
def clearPaymentMethodTable():
    connection = sqlite3.connect(DB_PATH)
    try:
        cursor = connection.cursor()
        cursor.execute("DROP TABLE PaymentMethod")
        cursor.execute("CREATE TABLE \"PaymentMethod\" (\"id\"	TEXT NOT NULL UNIQUE, \"creditCardNumber\"	TEXT NOT NULL, \"expirationMonth\"	INTEGER NOT NULL, \"expirationYear\"	INTEGER NOT NULL, PRIMARY KEY(\"id\"))")
    except Exception as e:
        print("Failed to drop the Payment Method table")
        print(e)
    finally:
        connection.close()

@pytest.fixture
def clearBillingInformationTable():
    connection = sqlite3.connect(DB_PATH)
    try:
        cursor = connection.cursor()
        cursor.execute("DROP TABLE BillingInformation")
        cursor.execute("CREATE TABLE \"BillingInformation\" (\"id\"	TEXT NOT NULL UNIQUE, \"fullName\"	TEXT NOT NULL, \"streetAddress1\"	TEXT NOT NULL, \"streetAddress2\"	TEXT, \"city\"	TEXT NOT NULL, \"state\"	TEXT NOT NULL, \"zipCode\"	TEXT NOT NULL, PRIMARY KEY(\"id\"))")
    except Exception as e:
        print("Failed to drop the Billing Information table")
        print(e)
    finally:
        connection.close()

def testGetBillingInformationForNonexistentPaymentMethodRaisesException(clearPaymentMethodTable, clearBillingInformationTable):
    connection = sqlite3.connect(DB_PATH)

    billingInformation = BillingInformation("Test", "Test", None, "Test", "Test", "00000")

    billingInfoDao = SQLiteBillingInformationDataAccessObject()
    billingInfoDao.createBillingInformation(billingInformation)

    paymentMethod = PaymentMethod("Test", datetime.now(), None)

    joinDao = SQLitePaymentMethodBillingInformationJoiningDataAccessObject()
    joinDao.createPaymentMethodBillingInformationJoin(paymentMethod=paymentMethod, billingInformation=billingInformation)

    try:
        joinDao.getBillingInformationForPaymentMethod(paymentMethod=paymentMethod)
        assert(False)
    except:
        assert(True)

def testGetBillingInformationForExistingPaymentMethodSuccessful(clearPaymentMethodTable, clearBillingInformationTable):
    connection = sqlite3.connect(DB_PATH)

    billingInformation = BillingInformation("Test", "Test", None, "Test", "Test", "00000")

    billingInfoDao = SQLiteBillingInformationDataAccessObject()
    billingInfoDao.createBillingInformation(billingInformation)

    paymentMethod = PaymentMethod("Test", datetime.now(), None)

    paymentDao = SQLitePaymentMethodDataAccessObject()
    paymentDao.createPaymentMethod(paymentMethod=paymentMethod)

    joinDao = SQLitePaymentMethodBillingInformationJoiningDataAccessObject()
    joinDao.createPaymentMethodBillingInformationJoin(paymentMethod=paymentMethod, billingInformation=billingInformation)

    billingInfo = joinDao.getBillingInformationForPaymentMethod(paymentMethod=paymentMethod)
    assert(billingInfo._id == billingInformation._id)


def testGetBillingInformationForPaymentMethodWithNoBillingInformationRaisesException(clearPaymentMethodTable, clearBillingInformationTable):
    connection = sqlite3.connect(DB_PATH)

    billingInformation = BillingInformation("Test", "Test", None, "Test", "Test", "00000")

    paymentMethod = PaymentMethod("Test", datetime.now(), None)

    paymentDao = SQLitePaymentMethodDataAccessObject()
    paymentDao.createPaymentMethod(paymentMethod=paymentMethod)

    joinDao = SQLitePaymentMethodBillingInformationJoiningDataAccessObject()
    joinDao.createPaymentMethodBillingInformationJoin(paymentMethod=paymentMethod, billingInformation=billingInformation)

    try:
        joinDao.getBillingInformationForPaymentMethod(paymentMethod=paymentMethod)
        assert(False)
    except:
        assert(True)

def testDeleteJoinWithNoBillingInformationRaisesException(clearPaymentMethodTable, clearBillingInformationTable):
    billingInformation = BillingInformation("Test", "Test", None, "Test", "Test", "00000")
    paymentMethod = PaymentMethod("Test", datetime.now(), None)

    joinDao = SQLitePaymentMethodBillingInformationJoiningDataAccessObject()

    try:
        joinDao.deletePaymentMethodBillingInformationJoin(paymentMethod, None)
        assert(False)
    except:
        assert(True)

def testDeleteJoinWithNoPaymentMethodRaisesException(clearPaymentMethodTable, clearBillingInformationTable):
    billingInformation = BillingInformation("Test", "Test", None, "Test", "Test", "00000")
    paymentMethod = PaymentMethod("Test", datetime.now(), None)

    joinDao = SQLitePaymentMethodBillingInformationJoiningDataAccessObject()

    try:
        joinDao.deletePaymentMethodBillingInformationJoin(None, billingInformation)
        assert(False)
    except:
        assert(True)

def testDeleteJoinSuccessful(clearPaymentMethodTable, clearBillingInformationTable):
    billingInformation = BillingInformation("Test", "Test", None, "Test", "Test", "00000")
    paymentMethod = PaymentMethod("Test", datetime.now(), None)

    joinDao = SQLitePaymentMethodBillingInformationJoiningDataAccessObject()
    joinDao.createPaymentMethodBillingInformationJoin(paymentMethod, billingInformation)
    joinDao.deletePaymentMethodBillingInformationJoin(paymentMethod, billingInformation)

def testCreateJoinSuccessful(clearPaymentMethodTable, clearBillingInformationTable):
    billingInformation = BillingInformation("Test", "Test", None, "Test", "Test", "00000")
    paymentMethod = PaymentMethod("Test", datetime.now(), None)

    joinDao = SQLitePaymentMethodBillingInformationJoiningDataAccessObject()
    joinDao.createPaymentMethodBillingInformationJoin(paymentMethod, billingInformation)