__author__ = "5641727, Redelin, 6544078, Kervella"
import sqlite3
from employee import Employee

conn = sqlite3.connect('employee_database.db')

c = conn.cursor()

c.execute("""CREATE TABLE IF NOT EXISTS employees (
           ID text,
            first test,
            last text,
           role text
            )""")

def insert_emp(emp):
    with conn:
        c.execute("INSERT INTO employees VALUES (:ID, :first, :last, :role)", {'ID': emp.ID, 'first': emp.first, 'last': emp.last, 'role': emp.role})

def update_role(emp, role):
    with conn:
        c.execute("""UPDATE employees SET role = :role
                    WHERE ID = :ID """,
                  {'ID': emp.ID, 'role': role})


def get_empl_by_ID(IDs):
    c.execute("SELECT * FROM employees WHERE ID = :ID", {'ID': IDs})
    return c.fetchall()

def remove_emp(emp):
    with conn:
        c.execute("DELETE from employees WHERE ID = :ID",{'ID': emp.ID})

def new_employee():
    new_emp = Employee(input("ID: "), input("Firstname: "), input("Lastname: "), input("Role: "))
    return new_emp
    

def add_emp():
    new_emp = new_employee()
    insert_emp(new_emp)

    
def close_table():
        """ Closes table"""

        conn.close()
        print("The Databank has been closed.")
        print("If you want to add a new person to the system, please restart the Class.")


empl = get_empl_by_ID('68')
print(empl)





