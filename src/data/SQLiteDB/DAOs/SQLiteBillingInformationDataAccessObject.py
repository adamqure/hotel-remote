import sqlite3
from data.DAOs.BillingInformationDataAccessObject import BillingInformationDataAccessObject
from data.SQLiteDB.SQLiteDBConstants import DB_PATH
from domain.Entities.BillingInformation import BillingInformation


class SQLiteBillingInformationDataAccessObject(BillingInformationDataAccessObject):
    def createBillingInformation(self, billingInformation: BillingInformation):
        connection = sqlite3.connect(DB_PATH)
        try:
            cursor = connection.cursor()
            command = f"INSERT INTO BillingInformation (id, fullName, streetAddress1, streetAddress2, city, state, zipCode) VALUES (?, ?, ?, ?, ?, ?, ?)"
            cursor.execute(command, (str(billingInformation._id), billingInformation.fullName, billingInformation.stretAddress1, billingInformation.streetAddress2, billingInformation.city, billingInformation.state, billingInformation.zipCode))
            connection.commit()
        except Exception as e:
            print(f"Failed to create the new billing information")
            raise e
        finally:
            connection.close()

    def deleteBillingInformation(self, id: str):
        connection = sqlite3.connect(DB_PATH)
        try:
            cursor = connection.cursor()
            command = f"DELETE FROM BillingInformation WHERE id = \"{id}\";"
            cursor.execute(command)
            connection.commit()
        except Exception as e:
            print(f"Failed to delete the billing information")
            raise e
        finally:
            connection.close()

    def updateBillingInformation(self, billingInformation: BillingInformation):
        connection = sqlite3.connect(DB_PATH)
        try:
            cursor = connection.cursor()
            updateCommand = f"UPDATE BillingInformation SET id=?, fullName=?, streetAddress1=?, streetAddress2=?, city=?, state=?, zipCode=? WHERE id = ?"
            cursor.execute(updateCommand, (str(billingInformation._id), billingInformation.fullName, billingInformation.stretAddress1, billingInformation.streetAddress2, billingInformation.city, billingInformation.state, billingInformation.zipCode, billingInformation._id))
            connection.commit()
        except Exception as e:
            print(f"Failed to update billing information: {billingInformation}")
            raise e
        finally:
            connection.close()