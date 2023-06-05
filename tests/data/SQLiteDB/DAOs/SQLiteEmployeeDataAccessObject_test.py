import pytest
import sqlite3
import json
import jsonpickle
from data.SQLiteDB.DAOs.SQLiteEmployeeDataAccessObject import SQLiteEmployeeDataAccessObject
from data.SQLiteDB.SQLiteDBConstants import DB_PATH
from domain.Entities.EmployeeRoles.EmployeeRole import EmployeeRole
from domain.Entities.People.Employee import Employee

@pytest.fixture
def clearEmployeeTable():
    connection = sqlite3.connect(DB_PATH)
    try:
        cursor = connection.cursor()
        cursor.execute("DROP TABLE Employee")
        cursor.execute("CREATE TABLE \"Employee\" (\"id\"	TEXT NOT NULL UNIQUE,\"name\"	TEXT NOT NULL,\"emailAddress\"	TEXT NOT NULL,\"employeeID\"	TEXT NOT NULL, \"position\"	TEXT NOT NULL, \"roles\"	TEXT, PRIMARY KEY(\"id\"))")
    except Exception as e:
        print("Failed to drop the employee table")
        print(e)
    finally:
        connection.close()


@pytest.fixture
def newEmployee():
    connection = sqlite3.connect(DB_PATH)
    try:
        cursor = connection.cursor()
        newEmployee = Employee(
            name="Test",
            emailAddress="test@test.com",
            position="Test Position",
            roles=[EmployeeRole("TestRole")],
            employeeID="123456"
        )
        command = f"INSERT INTO Employee (id, name, emailAddress, employeeID, position, roles) VALUES (?, ?, ?, ?, ?, ?)"
        cursor.execute(command, (str(newEmployee._id), newEmployee._name, newEmployee._emailAddress, newEmployee.employeeID, newEmployee.position, jsonpickle.encode(newEmployee.getRoles())))
        connection.commit()
    except Exception as e:
        print("Failed to create a new employee")
        print(e)
    finally:
        connection.close()

@pytest.fixture
def newEmployees():
    connection = sqlite3.connect(DB_PATH)
    try:
        cursor = connection.cursor()
        newEmployees = []
        newEmployees.append(
            Employee(
                name="Test",
                emailAddress="test@test.com",
                position="Test Position",
                roles=[EmployeeRole("TestRole")],
                employeeID="123456"
            )
        )

        newEmployees.append(
            Employee(
                name="Test2",
                emailAddress="test@test.com",
                position="Test Position",
                roles=[EmployeeRole("TestRole")],
                employeeID="111111"
            )
        )

        for newEmployee in newEmployees:
            command = f"INSERT INTO Employee (id, name, emailAddress, employeeID, position, roles) VALUES (?, ?, ?, ?, ?, ?)"
            cursor.execute(command, (str(newEmployee._id), newEmployee._name, newEmployee._emailAddress, newEmployee.employeeID, newEmployee.position, jsonpickle.encode(newEmployee.getRoles())))
            connection.commit()

    except Exception as e:
        print("Failed to create a new employee")
        print(e)
    finally:
        connection.close()

def testFetchEmployeeFoundReturnsProperEmployee(clearEmployeeTable, newEmployee):
    dao = SQLiteEmployeeDataAccessObject()
    result = dao.getEmployee("123456")
    assert(result.employeeID == "123456")

def testFetchEmployeeNotExistsRaisesException(): 
    try:
        dao = SQLiteEmployeeDataAccessObject()
        result = dao.getEmployee("111111")
        assert(False)
    except:
        assert(True)

def testFetchAllEmployeesReturnsEmployee(clearEmployeeTable, newEmployee):
    dao = SQLiteEmployeeDataAccessObject()
    result = dao.getAllEmployees()
    assert(len(result) == 1)
    assert(result[0].employeeID == "123456")

def testFetchAllEmployeesReturnsMultipleEmployees(clearEmployeeTable, newEmployees):
    dao = SQLiteEmployeeDataAccessObject()
    result = dao.getAllEmployees()
    assert(len(result) == 2)
    assert(result[0].employeeID == "123456")
    assert(result[1].employeeID == "111111")