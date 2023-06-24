from datetime import datetime
import sqlite3
import pytest
from data.SQLiteDB.DAOs.SQLiteGuestDataAccessObject import SQLiteGuestDataAccessObject
from data.SQLiteDB.DAOs.SQLitePaymentMethodDataAccessObject import SQLitePaymentMethodDataAccessObject
from data.SQLiteDB.DAOs.SQLitePaymentMethodGuestJoiningDataAccessObject import SQLitePaymentMethodGuestJoiningDataAccessObject

from data.SQLiteDB.SQLiteDBConstants import DB_PATH
from domain.Entities.PaymentMethod import PaymentMethod
from domain.Entities.People.Guest import Guest

@pytest.fixture
def clearJoinTable():
    connection = sqlite3.connect(DB_PATH)
    try:
        cursor = connection.cursor()
        cursor.execute("DROP TABLE PaymentMethodGuestJoining")
        cursor.execute("CREATE TABLE \"PaymentMethodGuestJoining\" (\"id\"	INTEGER NOT NULL UNIQUE, \"guestID\"	TEXT NOT NULL, \"paymentMethodID\"	TEXT NOT NULL UNIQUE, PRIMARY KEY(\"id\" AUTOINCREMENT))")
    except Exception as e:
        print("Failed to drop the Guest table")
        print(e)
    finally:
        connection.close()

@pytest.fixture
def clearGuestTable():
    connection = sqlite3.connect(DB_PATH)
    try:
        cursor = connection.cursor()
        cursor.execute("DROP TABLE Guest")
        cursor.execute("CREATE TABLE \"Guest\" (\"id\"	TEXT NOT NULL UNIQUE, \"name\"	TEXT NOT NULL, \"emailAddress\"	TEXT NOT NULL, PRIMARY KEY(\"id\"))")
    except Exception as e:
        print("Failed to drop the Guest table")
        print(e)
    finally:
        connection.close()

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

def testCreateJoinWithNoGuestRaisesException(clearGuestTable, clearPaymentMethodTable):
    guest = Guest(
        name="Test",
        emailAddress="test@test.com",
        paymentMethod=None
    )

    paymentMethod = PaymentMethod("Test", datetime.now(), None)

    guestDao = SQLiteGuestDataAccessObject()
    paymentDao = SQLitePaymentMethodDataAccessObject()
    paymentDao.createPaymentMethod(paymentMethod)

    joinDao = SQLitePaymentMethodGuestJoiningDataAccessObject()

    try:
        joinDao.createPaymentMethodGuestJoin(paymentMethod, None)
        assert(False)
    except:
        assert(True)

def testCreateJoinWithNoPaymentMethodRaisesException(clearGuestTable, clearPaymentMethodTable):
    guest = Guest(
        name="Test",
        emailAddress="test@test.com",
        paymentMethod=None
    )

    paymentMethod = PaymentMethod("Test", datetime.now(), None)

    guestDao = SQLiteGuestDataAccessObject()
    paymentDao = SQLitePaymentMethodDataAccessObject()
    guestDao.createGuest(guest)

    joinDao = SQLitePaymentMethodGuestJoiningDataAccessObject()

    try:
        joinDao.createPaymentMethodGuestJoin(None, guest)
        assert(False)
    except:
        assert(True)

def testCreateJoinSuccessful(clearGuestTable, clearPaymentMethodTable):
    guest = Guest(
        name="Test",
        emailAddress="test@test.com",
        paymentMethod=None
    )

    paymentMethod = PaymentMethod("Test", datetime.now(), None)

    guestDao = SQLiteGuestDataAccessObject()
    paymentDao = SQLitePaymentMethodDataAccessObject()
    paymentDao.createPaymentMethod(paymentMethod)

    joinDao = SQLitePaymentMethodGuestJoiningDataAccessObject()
    joinDao.createPaymentMethodGuestJoin(paymentMethod, guest)


def testDeleteJoinWithNoGuestRaisesException(clearGuestTable, clearPaymentMethodTable):
    guest = Guest(
        name="Test",
        emailAddress="test@test.com",
        paymentMethod=None
    )

    paymentMethod = PaymentMethod("Test", datetime.now(), None)

    guestDao = SQLiteGuestDataAccessObject()
    paymentDao = SQLitePaymentMethodDataAccessObject()
    paymentDao.createPaymentMethod(paymentMethod)

    joinDao = SQLitePaymentMethodGuestJoiningDataAccessObject()

    try:
        joinDao.deletePaymentMethodGuestJoin(paymentMethod, None)
        assert(False)
    except:
        assert(True)

def testDeleteNonExistingJoinRaisesException(clearGuestTable, clearPaymentMethodTable):
    guest = Guest(
        name="Test",
        emailAddress="test@test.com",
        paymentMethod=None
    )

    paymentMethod = PaymentMethod("Test", datetime.now(), None)

    guestDao = SQLiteGuestDataAccessObject()
    paymentDao = SQLitePaymentMethodDataAccessObject()
    paymentDao.createPaymentMethod(paymentMethod)

    joinDao = SQLitePaymentMethodGuestJoiningDataAccessObject()

    try:
        joinDao.deletePaymentMethodGuestJoin(paymentMethod, guest)
        assert(False)
    except:
        assert(True)

def testDeleteExistingJoinSuccessful(clearGuestTable, clearPaymentMethodTable):
    guest = Guest(
        name="Test",
        emailAddress="test@test.com",
        paymentMethod=None
    )

    paymentMethod = PaymentMethod("Test", datetime.now(), None)

    guestDao = SQLiteGuestDataAccessObject()
    paymentDao = SQLitePaymentMethodDataAccessObject()
    paymentDao.createPaymentMethod(paymentMethod)

    joinDao = SQLitePaymentMethodGuestJoiningDataAccessObject()
    joinDao.createPaymentMethodGuestJoin(paymentMethod, guest)
    joinDao.deletePaymentMethodGuestJoin(paymentMethod, guest)

def testDeleteJoinWithNoPaymentMethodRaisesException(clearGuestTable, clearPaymentMethodTable):
    guest = Guest(
        name="Test",
        emailAddress="test@test.com",
        paymentMethod=None
    )

    paymentMethod = PaymentMethod("Test", datetime.now(), None)

    guestDao = SQLiteGuestDataAccessObject()
    paymentDao = SQLitePaymentMethodDataAccessObject()
    paymentDao.createPaymentMethod(paymentMethod)

    joinDao = SQLitePaymentMethodGuestJoiningDataAccessObject()

    try:
        joinDao.createPaymentMethodGuestJoin(None, guest)
        assert(False)
    except:
        assert(True)

def testGetPaymentMethodForGuestWithNoGuestRaisesException(clearGuestTable, clearPaymentMethodTable):
    guest = Guest(
        name="Test",
        emailAddress="test@test.com",
        paymentMethod=None
    )

    paymentMethod = PaymentMethod("Test", datetime.now(), None)

    guestDao = SQLiteGuestDataAccessObject()
    paymentDao = SQLitePaymentMethodDataAccessObject()
    paymentDao.createPaymentMethod(paymentMethod)

    joinDao = SQLitePaymentMethodGuestJoiningDataAccessObject()

    try:
        joinDao.getPaymentMethodForGuest(None)
        assert(False)
    except:
        assert(True)

def testGetPaymentMethodForGuestWithNoPaymentMethodRaisesException(clearGuestTable, clearPaymentMethodTable):
    guest = Guest(
        name="Test",
        emailAddress="test@test.com",
        paymentMethod=None
    )

    paymentMethod = PaymentMethod("Test", datetime.now(), None)

    guestDao = SQLiteGuestDataAccessObject()
    paymentDao = SQLitePaymentMethodDataAccessObject()

    joinDao = SQLitePaymentMethodGuestJoiningDataAccessObject()
    joinDao.createPaymentMethodGuestJoin(paymentMethod, guest)

    try:
        joinDao.getPaymentMethodForGuest(guest)
        assert(False)
    except:
        assert(True)

def testGetPaymentMethodForGuestSuccessful(clearGuestTable, clearPaymentMethodTable):
    guest = Guest(
        name="Test",
        emailAddress="test@test.com",
        paymentMethod=None
    )

    paymentMethod = PaymentMethod("Test", datetime.now(), None)

    guestDao = SQLiteGuestDataAccessObject()
    paymentDao = SQLitePaymentMethodDataAccessObject()
    paymentDao.createPaymentMethod(paymentMethod)

    joinDao = SQLitePaymentMethodGuestJoiningDataAccessObject()
    joinDao.createPaymentMethodGuestJoin(paymentMethod, guest)

    result = joinDao.getPaymentMethodForGuest(guest)
    assert(result._id == paymentMethod._id)
