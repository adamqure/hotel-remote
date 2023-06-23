from datetime import datetime
import sqlite3
import pytest
from data.SQLiteDB.DAOs.SQLitePaymentMethodDataAccessObject import SQLitePaymentMethodDataAccessObject

from data.SQLiteDB.SQLiteDBConstants import DB_PATH
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

def testUpdateNonExistingPaymentMethodRaisesException(clearPaymentMethodTable):
    paymentMethod = PaymentMethod("Test", datetime.now(), None)
    paymentDao = SQLitePaymentMethodDataAccessObject()
    try:
        paymentDao.updatePaymentMethod(paymentMethod)
        assert(False)
    except:
        assert(True)

def testUpdatePaymentMethodSucceeds(clearPaymentMethodTable):
    paymentMethod = PaymentMethod("Test", datetime.now(), None)
    paymentDao = SQLitePaymentMethodDataAccessObject()
    paymentDao.createPaymentMethod(paymentMethod=paymentMethod)
    paymentMethod._creditCardNumber = "Test123"
    paymentDao.updatePaymentMethod(paymentMethod)

def testDeleteNonExistingPaymentMethodRaisesException(clearPaymentMethodTable):
    paymentDao = SQLitePaymentMethodDataAccessObject()

    try:
        paymentDao.deletePaymentMethod("Test")
        assert(False)
    except:
        assert(True)

def testDeleteExistingPaymentMethodSucceeds(clearPaymentMethodTable):
    paymentMethod = PaymentMethod("Test", datetime.now(), None)
    paymentDao = SQLitePaymentMethodDataAccessObject()
    paymentDao.createPaymentMethod(paymentMethod)
    paymentDao.deletePaymentMethod(paymentMethod)

def testCreateExistingPaymentMethodRaisesException(clearPaymentMethodTable):
    paymentMethod = PaymentMethod("Test", datetime.now(), None)
    paymentDao = SQLitePaymentMethodDataAccessObject()
    paymentDao.createPaymentMethod(paymentMethod)

    try:
        paymentDao.createPaymentMethod(paymentMethod)
        assert(False)
    except:
        assert(True)

def testCreatePaymentMethodSucceeds(clearPaymentMethodTable):
    paymentMethod = PaymentMethod("Test", datetime.now(), None)
    paymentDao = SQLitePaymentMethodDataAccessObject()
    paymentDao.createPaymentMethod(paymentMethod)