__author__ = "5641727, Redelin, 6544078, Kervella"

Wir entwickeln ein Programm zur Unterstützung einer Hotelrezeption.

Folgende Funktionnen sollen enthalten halten:
1. Buchungsfunktion mit Unterscheidung zwischen regulären Kunden und VIP Kunden, die mit einem Rabatt
begünstigt werden.
2. Eine Funktion zur Kreation eines persönlichen Dienstplan für Mitarbeiter
3. Eine Funktion die die eingelesenen Kunden-Daten in einer Datenbank speichert damit das Hotel die Daten für einen
nächsten Besuch haben kann.

Um diese Funktionen zu gewährleisten haben wir mehrere kleinere Dateien erstellt:

1. databank employee.py: Eine Datenbank mit allen Mitarbeitern, in Form einer Klasse "empl_databank", mit der Möglichkeit eine neue Mitarbeiterin oder 
Mitarbeiter hinzuzufügen, ihn/sie zu entfernen, seine/ihre Daten aktualisieren oder ihn/sie aufzurufen.
Die Datenbank ist mit der Klasse "Employee" verbunden um neue Mitarbeiter im Format
{ID: , Firstname:, Lastname:, Role: } zu bekommen.
Die Funktionen dafür sind folgende:
	empl.databank.add_emp()
	empl.databank.remove_emp()
	empl.databank.update_role(emp, role)
	empl.databank.get_empl_by_ID(IDs)
	empl.databank.close_table(): schließt die Datenbank nach der Benutzung

2. rooms.py: Eine Datenbank mit allen Zimmer und den jeweiligen Status des Zimmers.
Folgende Funktionen sind dort vorhanden:
	initialise_room(): erstellt 12 Zimmer in drei Kategorien: Single-, Double-Room oder Suite
	check_room(): erstellt zwei Listen mit den gebuchten Zimmer in einer und die verfügbaren Zimmer in der anderen Liste.
	booking(): Fragt nach dem Wunschzimmer und überprüft ob dieser schon gebucht worden ist. Ändert nur den Status des Zimmers.
	
3. crm.py: Noch eine letzte Datenbank mit den Kunden Informationen.
Diese Datenbank soll dem Programm ermöglichen Daten anzulegen um spätere Buchungen zu vereinfachen oder VIPs zu erkennen.
Es werden immer Name, email, Anzahl der gebuchten Tage und Rechnungen gespeichert.
	__init__(self): initialisiert die Verbindung zwischen Datenbank und Klasse
	create_table(self): erstellt die Datenbank falls diese noch nicht erstellt worden ist.
	insert_name(self, name, email): speichert die Daten ab
	get_entry_by_email(self, email): ermöglicht, durch die Email, einen direkt Abruf von Daten
	close_table(self): schließt die Datenbank nach der Benutzung
	
4. employee.py beinhaltet eine Klasse zur Formatierung der Employees im Programm.

5. booking.py: Ein Buchhaltungssystem zur Buchung von räumen und erstellung von Rechnungen.
Die Klasse soll dem Programm ermöglichen durch tkinter einen besseren Überblick über dem Ablauf der Buchung darzustellen
	__init__(self, root): initialisiert die Klasse mit der Datenbank Verbindung
	enter_info(self): ermöglicht dem User Informationen direkt in die Datenbank hinzuzufügen
	select_room(self): ermöglicht dem User ein Zimmer auszuwählen
	calendar(self): Zeigt nur ein Kalendar
	close_windows(self): schließt das Fenster nach den Eingaben
	main(): benutzt die Klasse in einem Loop
	
6. schedule.py 	soll eine Klasse zur erstellung möglicher Dienstpläne sein.
Durch eine Datenbank soll, anhand einer Email, die Dienstpläne für die jeweiligen Mitarbeiter ausgedruckt werden.
	__init__(self): erstellt die Verbindung zwischen der Klasse und der Datenbank
	create_table(self): erstellt die Datenbank
	insert_name(self, name, email): fügt der Datenbank eine neue Person hinzu
	get_entry_by_email(self, email): Anhand einer Email werden die zugehörigen Daten ausgedruckt
	
-------------------------
UNFERTIGE PUNKTE

Die richtige Implementierung der jeweiligen Funktionen und eine ablauf zur Benutzung fehlen. Wir haben es nicht geschafft alle Datenbanken so zu verknüpfen dass ein Ablauf alle Funktionnen Sinn ergibt.
So wäre die Idee folgende:
Zuerst werden die Datenbanken erstellt und zugeordnet. Zu dem Zeitpunkt wäre noch nichts angelegt und man könnte dies ändern um das Programm realistischer zu gestalten. Danach wäre ein Mitarbeiter in der Lage durch 
spezifische Befehle die Booking.py Datei aufzurufen und zu benutzen um eine Buchung durchzuführen. Des weiteren sollte man die Informationen der Kunden in der Datenbank, mithilfe von crm.py, angelegen.
Zuletzt müsste ein Mitarbeiter, mithilfe von schedule.py, in der Lage sein ein Diensplan zu erstellen und diesen dann auszudrücken.
	