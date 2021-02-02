
__author__ = "5641727, Redelin, 6544078, Kervella"
"""Zimmerverwaltung (Zimmerart (Suite, DZ, EZ, ...), Belegung, Zuordnung zu Kunden, freie Zim-
mer für einen bestimmten Zeitraum anzeigen)"""

# Ab hier sind meine Vorschläge

def initialise_room():
    """Initialization of all the rooms, only at the beginning
    """
    rooms =[]    
    for i in range (1,5):
        for x in range (1,4):
            if x == 2:
                room = {'number': i*100+x, 'sort': 'dual', 'booked': False}
                rooms.append(room)
            elif x == 3:
                room = {'number': i*100+x, 'sort': 'suite', 'booked': False}
                rooms.append(room)     
            else:
                room = {'number': i*100+x, 'sort': 'indiv', 'booked': False}
                rooms.append(room)      
    return rooms

def check_room(rooms):
    """creating two distincts lists of booked and non-booked rooms
    rooms: list
    """
    free_rooms = []
    booked_rooms = []    
    for element in rooms:
        if element['booked'] == False:
            free_rooms.append(element)
        else:
            booked_rooms.append(element)
    return free_rooms, booked_rooms

                

def booking():
    """Ability to book a room
    """
    room_choice = int(input("Room you want to book: "))
    for x in rooms:
        if room_choice == x['number']:
            if x['booked'] == True:
                print("The room is already booked!")
            else:
                x['booked'] = True

rooms = initialise_room()
free_rooms = check_room(rooms)[0]
booked_rooms = check_room(rooms)[1]

"""
while True:  #zum testen     
    print("----------------")    #Übersicht
    print("Rooms:\n", rooms)
    print("----------------")
    print("Free rooms:\n", free_rooms)
    print("----------------")
    print("Booked rooms:\n", booked_rooms)
    print("----------------")


    booking()
    free_rooms = check_room(rooms)[0]
    booked_rooms = check_room(rooms)[1]
    print(booked_rooms)
    """