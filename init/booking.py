__author__ = "5641727, Redelin, 6544078, Kervella"

"""Ein einfaches Buchhaltungssystem: Buchungen erstellen, stornieren und Rechnungen anzei-
gen"""

#hier quasi die buchungslogik
import tkinter as tk

"""vielleicht im ersten fenster sehen welche räume wann zur verfügung stehen, dann auswählen und im nächsten window
angaben machen"""

class Demo1:
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master)
        self.button1 = tk.Button(self.frame, text = 'New Window', width = 25, command = self.new_window)
        self.button1.pack()
        self.frame.pack()
    def new_window(self):
        self.newWindow = tk.Toplevel(self.master)
        self.app = Demo2(self.newWindow)

class Demo2:
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master)
        self.quitButton = tk.Button(self.frame, text = 'Quit', width = 25, command = self.close_windows)
        self.quitButton.pack()
        self.frame.pack()
    def close_windows(self):
        self.master.destroy()

def main(): 
    root = tk.Tk()
    app = Demo1(root)
    root.mainloop()

