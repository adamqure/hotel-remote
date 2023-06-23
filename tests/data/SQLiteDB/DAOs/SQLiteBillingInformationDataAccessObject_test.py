import sqlite3

import pytest
from data.SQLiteDB.DAOs.SQLiteBillingInformationDataAccessObject import SQLiteBillingInformationDataAccessObject

from data.SQLiteDB.SQLiteDBConstants import DB_PATH
from domain.Entities.BillingInformation import BillingInformation


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

@pytest.fixture
def newBillingInformation():
    connection = sqlite3.connect(DB_PATH)

    billingInfo = BillingInformation(
        id="Test",
        fullName="Test",
        streetAddress1="Test",
        streetAddress2=None,
        city="Test",
        state="Test",
        zipCode="00000"
    )

    try:
        cursor = connection.cursor()
        command = f"INSERT INTO BillingInformation (id, fullName, streetAddress1, streetAddress2, city, state, zipCode) VALUES (?, ?, ?, ?, ?, ?, ?)"
        cursor.execute(command, (billingInfo._id, billingInfo.fullName, billingInfo.stretAddress1, billingInfo.streetAddress2, billingInfo.city, billingInfo.state, billingInfo.zipCode))
        connection.commit()
    except Exception as e:
        print("Failed to create the Billing Information")
        print(e)
    finally:
        connection.close()

def selectBillingInfo(id: str):
    connection = sqlite3.connect(DB_PATH)

    try:
        cursor = connection.cursor()
        command = f"SELECT * FROM BillingInformation WHERE id = {str}"
        result = cursor.execute(command)
        return result
    except Exception as e:
        print("Failed to get the Billing Information")
        print(e)
    finally:
        connection.close()

def testCreateExistingBillingInfoRaisesException(clearBillingInformationTable, newBillingInformation):
    billingInfo = BillingInformation(
        id="Test",
        fullName="Test",
        streetAddress1="Test",
        streetAddress2=None,
        city="Test",
        state="Test",
        zipCode="00000"
    )

    dao = SQLiteBillingInformationDataAccessObject()
    try:
        dao.createBillingInformation(billingInfo)
        assert(False)
    except:
        assert(True)

def testCreateBillingInformationSucceeds(clearBillingInformationTable):
    billingInfo = BillingInformation(
        id="Test",
        fullName="Test",
        streetAddress1="Test",
        streetAddress2=None,
        city="Test",
        state="Test",
        zipCode="00000"
    )

    dao = SQLiteBillingInformationDataAccessObject()
    try:
        dao.createBillingInformation(billingInfo)
        assert(True)
    except:
        assert(False)

def testDeleteNonExistingBillingInfoRaisesException(clearBillingInformationTable):
    dao = SQLiteBillingInformationDataAccessObject()
    try:
        dao.deleteBillingInformation("Test")
        assert(False)
    except:
        assert(True)

def testDeleteExistingBillingInfoSucceeds(clearBillingInformationTable, newBillingInformation):
    dao = SQLiteBillingInformationDataAccessObject()
    try:
        dao.deleteBillingInformation("Test")
        assert(True)
    except:
        assert(False)

def testUpdateNonExistingBillingInfoRaisesException(clearBillingInformationTable):
    billingInfo = BillingInformation(
        id="Test",
        fullName="Test",
        streetAddress1="Test",
        streetAddress2=None,
        city="Test",
        state="Test",
        zipCode="00000"
    )

    dao = SQLiteBillingInformationDataAccessObject()
    try:
        dao.updateBillingInformation(billingInfo)
        assert(False)
    except:
        assert(True)

def testUpdateExistingBillingInfoRaisesException(clearBillingInformationTable, newBillingInformation):
    billingInfo = BillingInformation(
        id="Test",
        fullName="Test",
        streetAddress1="Test",
        streetAddress2="Test",
        city="Test",
        state="Test",
        zipCode="00000"
    )

    dao = SQLiteBillingInformationDataAccessObject()
    try:
        dao.updateBillingInformation(billingInfo)
        assert(True)
    except:
        assert(False)