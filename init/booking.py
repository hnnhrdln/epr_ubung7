__author__ = "5641727, Redelin, 6544078, Kervella"

"""Ein einfaches Buchhaltungssystem: Buchungen erstellen, stornieren und Rechnungen anzei-
gen"""

#hier quasi die buchungslogik
import tkinter as tk
from tkinter import ttk
from tkcalendar import Calendar,DateEntry
import datetime
import rooms
from crm import Crm

#vielleicht im ersten fenster sehen welche räume wann zur verfügung stehen, dann auswählen und im nächsten window
#angaben machen


class Booking:
    def __init__(self, root):

        # Initializing CRM database class
        self.crm = Crm()
        # TK root
        self.root = root
        # Header
        self.room_header = tk.Label(self.root, text = "Welcome to our cozy hotel!\nPlease see our available rooms:")
        self.room_header.pack()
        # 
        self.select_room()
        self.enter_info()
        self.calendar()
        # Closing Window/Programm
        self.quit_button = tk.Button(self.root, text = 'Quit', width = 25, command = self.close_windows)
        self.quit_button.pack()
    

    def enter_info(self):
        """ Lets User enter information. Gets added to database"""

        name_var = tk.StringVar()
        email_var = tk.StringVar()

        def submit():
            name=name_var.get()
            email = email_var.get()
            print("Name entered " +name)
            print("Email entered " +email)

            self.crm.insert_name(name, email)
            self.crm.get_entry_by_email(email)

            name_var.set("")
            email_var.set("")

            window.destroy()  

        window = self.root
        
        tk.Label(window, text = "Please enter your information").pack()
        tk.Label(window, text = "Your Name").pack()
        tk.Entry(window, textvariable = name_var).pack()
        tk.Label(window, text = "Your Email Adress").pack()
        tk.Entry(window, textvariable = email_var).pack()

        tk.Button(window,text = 'Submit', command = submit).pack()
        
    def select_room(self):
        """ Lets User select free room"""

        selected = tk.IntVar()
        frame1 = self.root

        def bla():
            print(selected.get())
            selected_now = selected.get()
            selected_label = tk.Label(self.root, text=selected_now, bg="orange")
            selected_label.pack()

        for e in rooms.free_rooms:
            R = tk.Radiobutton(frame1, text = e['sort']+" room number "+str(e['number']),
             value = e['number'], variable= selected, command = bla)
            R.pack()

    def close_windows(self):
        """ Closes window. Stops programm execution."""

        self.root.destroy()

    def calendar(self):
        """ So far only displays calendar."""

        def print_sel():
            print(cal.selection_get())
            cal.see(datetime.date(year=2021, month=2, day=2))

        top = self.root

        today = datetime.date.today()

        maxdate = datetime.date(year=2022, month=1, day=1)
        mindate = today + datetime.timedelta(days=5)
        print(mindate, maxdate)

        cal = Calendar(top, font="Arial 14", selectmode='day', locale='en_US',
                    mindate=mindate, maxdate=maxdate, disabledforeground='red',
                    cursor="hand1", year=2018, month=2, day=5)
        cal.pack()
        ttk.Button(top, text="ok", command=print_sel).pack()


def main(): 
    root = tk.Tk()
    Booking(root)
    #print(rooms.rooms)

    root.mainloop()


if __name__ == '__main__':
    main()


