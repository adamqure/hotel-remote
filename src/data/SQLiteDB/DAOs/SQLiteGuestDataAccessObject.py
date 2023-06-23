import sqlite3
from data.DAOs.GuestDataAccessObject import GuestDataAccessObject
from data.SQLiteDB.SQLiteDBConstants import DB_PATH
from domain.Entities.People.Guest import Guest


class SQLiteGuestDataAccessObject(GuestDataAccessObject):
    def createGuest(self, guest: Guest):
        connection = sqlite3.connect(DB_PATH)
        try:
            cursor = connection.cursor()
            command = f"INSERT INTO Guest (id, name, emailAddress) VALUES (?, ?, ?)"
            cursor.execute(command, (str(guest._id), guest._name, guest._emailAddress))
            connection.commit()
        except Exception as e:
            print(f"Failed to create the new guest")
            raise e
        finally:
            connection.close()

    def getAllGuests(self) -> list[Guest]:
        connection = sqlite3.connect(DB_PATH)
        try:
            cursor = connection.cursor()
            selectCommand = f"SELECT * FROM Guest"
            cursor.execute(selectCommand)
            dataObjects = cursor.fetchall()
            result: list[Guest] = []
            for guestData in dataObjects:
                result.append(
                    Guest(
                        name=guestData[1],
                        emailAddress=guestData[2],
                        paymentMethod=None,
                        reservations=[],
                        id=guestData[0]
                    )
                )
            return result
        except:
            raise f"Failed to fetch guest list"
        finally:        
            connection.close()  

    def deleteGuest(self, id: str):
        connection = sqlite3.connect(DB_PATH)
        try:
            cursor = connection.cursor()
            command = f"DELETE FROM Guest WHERE id = \"{id}\";"
            cursor.execute(command)
            connection.commit()
        except Exception as e:
            print(f"Failed to delete the guest")
            raise e
        finally:
            connection.close()

    def updateGuest(self, guest: Guest):
        connection = sqlite3.connect(DB_PATH)
        try:
            cursor = connection.cursor()
            updateCommand = f"UPDATE Guest SET id=?, name=?, emailAddress=? WHERE id=?"
            cursor.execute(updateCommand, (str(guest._id), guest._name, guest._emailAddress, str(guest._id)))
            connection.commit()
        except Exception as e:
            print(f"Failed to update guest: {guest}")
            raise e
        finally:
            connection.close()
