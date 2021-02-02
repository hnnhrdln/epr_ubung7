__author__ = "5641727, Redelin, 6544078, Kervella"

"""Ein einfaches Buchhaltungssystem: Buchungen erstellen, stornieren und Rechnungen anzei-
gen"""

#hier quasi die buchungslogik
import tkinter as tk
from tkinter import ttk
from tkcalendar import Calendar,DateEntry
import datetime

"""vielleicht im ersten fenster sehen welche räume wann zur verfügung stehen, dann auswählen und im nächsten window
angaben machen"""


class Demo2:
    def __init__(self, root):
        self.root = root

        self.frame = tk.Frame(self.root)
        self.frame_bottom = tk.Frame(self.root)

        self.quit_button = tk.Button(self.frame, text = 'Quit', width = 25, command = self.close_windows)
        self.calendar_button = tk.Button(self.frame, text = "Calendar", command = self.calendar)
        self.enter_person = tk.Button(self.frame, text = "Enter Your Info", command = self.enter_info)

        self.quit_button.pack(side= "bottom")
        self.calendar_button.pack()
        self.enter_person.pack()
        self.frame.pack()

    def enter_info(self):
        name_var = tk.StringVar()
        email_var = tk.StringVar()

        def submit():
            name=name_var.get()
            email = email_var.get()
            print("Name entered " +name)
            print("Email entered " +email)

            name_var.set("")
            email_var.set("")

            window.destroy()  

        window = tk.Toplevel(self.root)
        
        tk.Label(window, text = "Please enter your information").grid(row=0,column = 0)
        tk.Label(window, text = "Your Name").grid(row = 1, column = 0)
        tk.Entry(window, textvariable = name_var).grid(row = 1, column = 1)
        tk.Label(window, text = "Your Email Adress").grid(row = 2, column = 0)
        tk.Entry(window, textvariable = email_var).grid(row = 2, column = 1)

        tk.Button(window,text = 'Submit', command = submit).grid(row = 3, column = 0)
        

    def close_windows(self):
        self.root.destroy()

    def calendar(self):
        def print_sel():
            print(cal.selection_get())
            cal.see(datetime.date(year=2021, month=2, day=2))

        top = tk.Toplevel(self.root)

        today = datetime.date.today()

        maxdate = datetime.date(year=2022, month=1, day=1)
        mindate = today + datetime.timedelta(days=5)
        print(mindate, maxdate)

        cal = Calendar(top, font="Arial 14", selectmode='day', locale='en_US',
                    mindate=mindate, maxdate=maxdate, disabledforeground='red',
                    cursor="hand1", year=2018, month=2, day=5)
        cal.pack(fill="both", expand=True)
        ttk.Button(top, text="ok", command=print_sel).pack()


def main(): 
    root = tk.Tk()
    Demo2(root)
    root.mainloop()

if __name__ == '__main__':
    main()


