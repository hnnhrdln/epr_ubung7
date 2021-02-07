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


emp_1 = Employee('75A', 'John', 'Doe', 'Deskmanager')
emp_2 = Employee('89P', 'Fred', 'Parker', 'Frontdesk')

insert_emp(emp_1)
insert_emp(emp_2)

empl = get_empl_by_ID('75A')
print(empl)


conn.close()
