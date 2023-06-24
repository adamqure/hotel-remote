import sqlite3
from data.DAOs.PaymentMethodDataAccessObject import PaymentMethodDataAccessObject
from data.SQLiteDB.SQLiteDBConstants import DB_PATH
from domain.Entities.PaymentMethod import PaymentMethod


class SQLitePaymentMethodDataAccessObject(PaymentMethodDataAccessObject):
    def updatePaymentMethod(self, paymentMethod: PaymentMethod):
        connection = sqlite3.connect(DB_PATH)
        try:
            cursor = connection.cursor()
            command = f"UPDATE PaymentMethod SET id=?, creditCardNumber=?, expirationMonth=?, expirationYear=? WHERE id = ?"
            cursor.execute(command, (str(paymentMethod._id), paymentMethod._creditCardNumber, paymentMethod._expirationDate.date().month, paymentMethod._expirationDate.date().year, str(paymentMethod._id)))
            connection.commit()
        except Exception as e:
            print(f"Failed to create the new payment method")
            raise e
        finally:
            connection.close()

    def deletePaymentMethod(self, id: str):
        connection = sqlite3.connect(DB_PATH)
        try:
            cursor = connection.cursor()
            command = f"DELETE FROM PaymentMethod WHERE id = \"{id}\";"
            cursor.execute(command)
            connection.commit()
        except Exception as e:
            print(f"Failed to delete the payment method")
            raise e
        finally:
            connection.close()

    def createPaymentMethod(self, paymentMethod: PaymentMethod):
        connection = sqlite3.connect(DB_PATH)
        try:
            cursor = connection.cursor()
            command = f"INSERT INTO PaymentMethod (id, creditCardNumber, expirationMonth, expirationYear) VALUES (?, ?, ?, ?)"
            cursor.execute(command, (str(paymentMethod._id), paymentMethod._creditCardNumber, paymentMethod._expirationDate.date().month, paymentMethod._expirationDate.date().year))
            connection.commit()
        except Exception as e:
            print(f"Failed to create the new payment method")
            raise e
        finally:
            connection.close()