__author__ = "5641727, Redelin, 6544078, Kervella"

"""Was ich mir gedacht habe:
die schedule.db enthält eine tabelle mit folgenden spalten:

day     | room | booked | employee|
-------------------------------------------
2021-1-2| 101  | true   | Peter   | -> Raum 101 ist am 2.1.21 belegt. Peter arbeitet

[Btw, der Dienstplan muss doch exportiert und importiert werden können...
das geht aber gut mit SQLite]
"""

import sqlite3 as sl

class Schedule:
    """ class that defines schedule database."""

    def __init__(self):
        """ Creates SQLite connector to schedule.db database and cursor to manage sql execution"""

        self.con = sl.connect('schedule.db')
        self.cursor = self.con.cursor()

    def close_table(self):
        """ Closes table"""

        dropTableStatement = "DROP TABLE SCHEDULE"
        self.cursor.execute(dropTableStatement)
        self.con.close()

    def create_table(self):
        """ Creates Table"""

        self.cursor.execute("""
            CREATE TABLE SCHEDULE (
                day DATETIME, 
                room NUMBER,
                booked BOOLEAN,
                employee TEXT
            );
        """)

    def insert_name(self, name, email):
        """ To initialize new user"""

        sql = 'INSERT INTO SCHEDULE (name, email) values(?, ?)'
        data = (name, email)
        
        self.cursor.execute(sql, data)

    def get_entry_by_email(self, email):
        """ Email is unique key. Retrieves user info by email adress"""

        mail = (email,)
        data = self.cursor.execute("SELECT * FROM SCHEDULE WHERE email == ?", mail)
        for row in data:
            print("This is the row with email "+ email+": "+str(row))