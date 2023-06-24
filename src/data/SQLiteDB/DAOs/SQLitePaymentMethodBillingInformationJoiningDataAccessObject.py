import sqlite3
from data.DAOs.PaymentMethodBillingInformationJoiningDataAccessObject import PaymentMethodBillingInformationJoiningDataAccessObject
from data.SQLiteDB.SQLiteDBConstants import DB_PATH
from domain.Entities.BillingInformation import BillingInformation
from domain.Entities.PaymentMethod import PaymentMethod


class SQLitePaymentMethodBillingInformationJoiningDataAccessObject(PaymentMethodBillingInformationJoiningDataAccessObject):
    def getBillingInformationForPaymentMethod(self, paymentMethod: PaymentMethod) -> BillingInformation:
        connection = sqlite3.connect(DB_PATH)
        try:
            cursor = connection.cursor()
            command = f"SELECT BillingInformation.id as id, fullName, streetAddress1, streetAddress2, city, state, zipCode FROM PaymentMethodBillingInformationJoining JOIN BillingInformation ON PaymentMethodBillingInformationJoining.billingInformationID = BillingInformation.id WHERE PaymentMethodBillingInformationJoining.paymentMethodID = \"{str(paymentMethod._id)}\""
            cursor.execute(command)
            dataObjects = cursor.fetchall()

            if len(dataObjects) == 0:
                raise f"Failed to find billing information that matches payment method {paymentMethod}"
            
            billingInformationData = dataObjects[0]

            return BillingInformation(
                id=billingInformationData[0],
                fullName=billingInformationData[1],
                streetAddress1=billingInformationData[2],
                streetAddress2=billingInformationData[3],
                city=billingInformationData[4],
                state=billingInformationData[5],
                zipCode=billingInformationData[6]
            )
        except Exception as e:
            print(f"Failed to get the payment Method")
            raise e
        finally:
            connection.close()

    def deletePaymentMethodBillingInformationJoin(self, paymentMethod: PaymentMethod, billingInformation: BillingInformation):
        connection = sqlite3.connect(DB_PATH)
        try:
            cursor = connection.cursor()
            command = f"DELETE FROM PaymentMethodBillingInformationJoining WHERE paymentMethodID = ? AND billingInformationID = ?"
            cursor.execute(command, (str(paymentMethod._id),str(billingInformation._id)))
            connection.commit()
        except Exception as e:
            print(f"Failed to delete join")
            raise e
        finally:
            connection.close()

    def createPaymentMethodBillingInformationJoin(self, paymentMethod: PaymentMethod, billingInformation: BillingInformation):
        connection = sqlite3.connect(DB_PATH)
        try:
            cursor = connection.cursor()
            command = f"INSERT INTO PaymentMethodBillingInformationJoining (paymentMethodID, billingInformationID) VALUES (?, ?)"
            cursor.execute(command, (str(paymentMethod._id), str(billingInformation._id)))
            connection.commit()
        except Exception as e:
            print(f"Failed to create join")
            raise e
        finally:
            connection.close()