__author__ = "5641727, Redelin, 6544078, Kervella"
"""Kundenverwaltung (Kundennummer, gemachte Buchungen, bezahlte und offene Rechnun-
gen)
Für VIP-Kunden (dies sind Kunden, die schon mindestens 4-mal das Hotel besucht haben) gibt
es verschiedene Vorteile (überlegen Sie selbst welche, als Idee: Vergünstigung beim Preis, kos-
tenloses Frühstück, freien Eintritt ins SPAR, kostenloser Zimmerupgrade falls entsprechende
Zimmer frei sind ... Ihre Entscheidung)."""

import sqlite3 as sl

class Crm:
    """ class that defines CRM database."""

    def __init__(self):
        """ Creates SQLite connector to crm.db database and cursor to manage sql execution"""

        self.con = sl.connect('crm.db')
        self.cursor = self.con.cursor()

    def close_table(self):
        """ Closes table"""

        dropTableStatement = "DROP TABLE USER"
        self.cursor.execute(dropTableStatement)
        self.con.close()

    def create_table(self):
        """ Creates Table"""

        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS USER (
                name TEXT NOT NULL,
                email TEXT NOT NULL PRIMARY KEY
                number_stays INTEGER DEFAULT 0,
                bill NUMERIC DEFAULT 0,                
            );
        """)

    def insert_name(self, name, email):
        """ To initialize new user"""

        sql = 'INSERT INTO USER (name, email) values(?, ?)'
        data = (name, email)
        
        self.cursor.execute(sql, data)

    def get_entry_by_email(self, email):
        """ Email is unique key. Retrieves user info by email adress"""

        mail = (email,)
        data = self.cursor.execute("SELECT * FROM USER WHERE email == ?", mail)
        for row in data:
            print("This is the row with email "+ email+": "+str(row))