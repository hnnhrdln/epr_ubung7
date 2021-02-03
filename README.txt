Hab weiter über die Datenstruktur nachgedacht. 
Würde gerne 3 Databases machen, aka Tables

1) rooms

*number* | sort  | booked | price |
---------------------------------
  101    | indiv | 1      | 100   |
....
-> gegebenen falls  hier booked entfernen, da booked ehr tag bezogen ist
ich denke rooms sollte einfach nur ein inventar der vorhandenen räume sein
die verwaltung der buchungen dann in schedule 
-> in booking.py dann alle räume anzeigen, sobald einer festgelegt ist die 
anzeige des kalenders anpassen

2) crm

*email* |  name |  number_stays | bill  | 
-----------------------------------------
abc@def | Peter |   2           | 300   |
....
-> eg bill am ende des aufenthalts zahlen oder sort

3) schedule

day     | room  | booked  | employee| booked_by |
-------------------------------------------------
2021-1-2| 101   |  1      | Frank   | abc@def   |
...
-> SQLite hat kein Bool. 0=false, 1=true
-> im kalender farblich darstellen an welchen tagen booked == false, also der raum frei ist
nur diese zeiten buchen lassen
-> wie das mit einem zeitraum gehen woll, weiß ich noch nicht ganz, aber man kann auf jeden fall 
einen tag auswählen, der wird als Datetime zurückgegeben und dann in schedule booked auf true
und in crm number_stays +1 und bill + price vom raum 

