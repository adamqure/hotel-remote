from data.DAOs.EmployeeDataAccessObject import EmployeeDataAccessObject
from domain.Entities.People.Employee import Employee
from data.SQLiteDB.SQLiteDBConstants import DB_PATH
import sqlite3
import jsonpickle

class SQLiteEmployeeDataAccessObject(EmployeeDataAccessObject):
    def getEmployee(self, id: str):
        connection = sqlite3.connect(DB_PATH)
        try:
            cursor = connection.cursor()
            selectCommand = f"SELECT * FROM Employee WHERE employeeID = {id};"
            cursor.execute(selectCommand)
            result = cursor.fetchall()
            if len(result) == 0:
                raise f"Failed to find employee that matches id {id}"
            
            employeeData = result[0]
            return Employee(
                name=employeeData[1],
                emailAddress=employeeData[2],
                position=employeeData[4],
                roles=jsonpickle.decode(employeeData[5]),
                employeeID=employeeData[3],
                id=employeeData[0]
            )
        except Exception as e:
            raise f"Failed to find employee that matches id {id}: {e}"
        finally:        
            connection.close()  

    def getAllEmployees(self) -> list[Employee]:
        connection = sqlite3.connect(DB_PATH)
        try:
            cursor = connection.cursor()
            selectCommand = f"SELECT * FROM Employee"
            cursor.execute(selectCommand)
            dataObjects = cursor.fetchall()
            result: list[Employee] = []
            for employeeData in dataObjects:
                result.append(
                    Employee(
                        name=employeeData[1],
                        emailAddress=employeeData[2],
                        position=employeeData[4],
                        roles=jsonpickle.decode(employeeData[5]),
                        employeeID=employeeData[3],
                        id=employeeData[0]
                    )
                )
            return result
        except:
            raise f"Failed to fetch employee list"
        finally:        
            connection.close()  

    def updateEmployee(self, employee: Employee):
        connection = sqlite3.connect(DB_PATH)
        try:
            cursor = connection.cursor()
            updateCommand = f"UPDATE Employee SET id = ?, name = ?, emailAddress = ?, employeeID = ?, position = ?, roles = ? WHERE id = ?"
            cursor.execute(updateCommand, (str(employee._id), employee._name, employee._emailAddress, employee.employeeID, employee.position, jsonpickle.encode(employee.getRoles()), str(employee._id)))
            connection.commit()
        except Exception as e:
            print(f"Failed to update employee: {employee}")
            raise e
        finally:
            connection.close()

    def addEmployee(self, employee: Employee):
        connection = sqlite3.connect(DB_PATH)
        try:
            cursor = connection.cursor()
            command = f"INSERT INTO Employee (id, name, emailAddress, employeeID, position, roles) VALUES (?, ?, ?, ?, ?, ?)"
            cursor.execute(command, (str(employee._id), employee._name, employee._emailAddress, employee.employeeID, employee.position, jsonpickle.encode(employee.getRoles())))
            connection.commit()
        except Exception as e:
            print(f"Failed to create the new employee")
            raise e
        finally:
            connection.close()

    def deleteEmployee(self, id: str):
        connection = sqlite3.connect(DB_PATH)
        try:
            cursor = connection.cursor()
            command = f"DELETE FROM Employee WHERE id = \"{id}\";"
            cursor.execute(command)
            connection.commit()
        except Exception as e:
            print(f"Failed to delete the employee")
            raise e
        finally:
            connection.close()