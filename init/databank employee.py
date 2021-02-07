__author__ = "5641727, Redelin, 6544078, Kervella"

import sqlite3
from employee import Employee

class empl_databank:

    conn = sqlite3.connect('employee_database.db')

    c = conn.cursor()

    sqlite3.connect('employee_database.db').cursor().execute("""CREATE TABLE IF NOT EXISTS employees (
               ID text,
                first test,
                last text,
               role text
                )""")

    def insert_emp(emp):
        """Insert employee into databank
        emp: tuple
        """
        with sqlite3.connect('employee_database.db'):
            sqlite3.connect('employee_database.db').cursor().execute("INSERT INTO employees VALUES (:ID, :first, :last, :role)", {'ID': emp.ID, 'first': emp.first, 'last': emp.last, 'role': emp.role})

    def update_role(emp, role):
        """update an employees' role
        emp: tuple
        role: string
        """
        with sqlite3.connect('employee_database.db'):
            sqlite3.connect('employee_database.db').cursor().execute("""UPDATE employees SET role = :role
                        WHERE ID = :ID """,
                      {'ID': emp.ID, 'role': role})


    def get_empl_by_ID(IDs):
        """returns an employees' data
        ID: string
        """
        sqlite3.connect('employee_database.db').cursor().execute("SELECT * FROM employees WHERE ID = :ID", {'ID': IDs})
        return sqlite3.connect('employee_database.db').cursor().fetchall()

    def remove_emp(emp):
        """removes an employee from the batabank
        emp: tuple
        """
        with sqlite3.connect('employee_database.db'):
            sqlite3.connect('employee_database.db').cursor().execute("DELETE from employees WHERE ID = :ID",{'ID': emp.ID})

    def new_employee():
        """create a new employee
        """
        new_emp = Employee(input("ID: "), input("Firstname: "), input("Lastname: "), input("Role: "))
        return new_emp
        

    def add_emp():
        """reunites two functions from above to gain time whilst refering to them
        """
        new_emp = empl_databank.new_employee()
        empl_databank.insert_emp(new_emp)

        
    def close_table():
            """ Closes table"""

            sqlite3.connect('employee_database.db').cursor().close()
            print("The Databank has been closed.")
            print("If you want to add a new person to the system, please restart the Class.")







