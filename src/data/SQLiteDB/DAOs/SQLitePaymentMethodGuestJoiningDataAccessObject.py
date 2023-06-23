import datetime
import sqlite3
from data.DAOs.PaymentMethodGuestJoiningDataAccessObject import PaymentMethodGuestJoiningDataAccessObject
from data.SQLiteDB.SQLiteDBConstants import DB_PATH
from domain.Entities.PaymentMethod import PaymentMethod
from domain.Entities.People.Guest import Guest


class SQLitePaymentMethodGuestJoiningDataAccessObject(PaymentMethodGuestJoiningDataAccessObject):
    def createPaymentMethodGuestJoin(self, paymentMethod: PaymentMethod, guest: Guest):
        connection = sqlite3.connect(DB_PATH)
        try:
            cursor = connection.cursor()
            command = f"INSERT INTO PaymentMethodGuestJoining (guestID, paymentMethodID) VALUES (?, ?)"
            cursor.execute(command, (str(guest._id), str(paymentMethod._id)))
            connection.commit()
        except Exception as e:
            print(f"Failed to create join")
            raise e
        finally:
            connection.close()

    def deletePaymentMethodGuestJoin(self, paymentMethod: PaymentMethod, guest: Guest):
        connection = sqlite3.connect(DB_PATH)
        try:
            cursor = connection.cursor()
            command = f"DELETE FROM PaymentMethodGuestJoining WHERE guestID = ? AND paymentMethodID = ?"
            cursor.execute(command, (str(guest._id), str(paymentMethod._id)))
            connection.commit()
        except Exception as e:
            print(f"Failed to delete join")
            raise e
        finally:
            connection.close()

    def getPaymentMethodForGuest(self, guest: Guest) -> PaymentMethod:
        connection = sqlite3.connect(DB_PATH)
        try:
            cursor = connection.cursor()
            command = f"SELECT PaymentMethod.id as id, creditCardNumber, expirationMonth, expirationYear FROM PaymentMethodGuestJoining JOIN PaymentMethod ON PaymentMethodGuestJoining.paymentMethodID = PaymentMethod.id WHERE PaymentMethodGuestJoining.guestID = \"{str(guest._id)}\""
            cursor.execute(command)
            
            dataObjects = cursor.fetchall()
            if len(dataObjects) == 0:
                raise f"Failed to find Payment Method that matches guest {guest}"
            
            paymentMethodData = dataObjects[0]
            return PaymentMethod(
                cardNumber=paymentMethodData[1],
                expirationDate=datetime.datetime(year=paymentMethodData[3], month= paymentMethodData[2], day= 1),
                billingInformation=None,
                id=paymentMethodData[0]
            )
        except Exception as e:
            print(f"Failed to get Payment Method for guest {guest}")
            raise e
        finally:
            connection.close()