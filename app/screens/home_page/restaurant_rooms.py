class RoomObject():
    def __init__(self, **kwargs):
        self.id = -1
        self.name = ""
        self.pos_x = 0
        self.pos_y = 0
        self.size_x = 1
        self.size_y = 1
        self.rotation = 0
        self.image_id = 0

class Room():
    def __init__(self, **kwargs):
        self.objects = []
        if 'name' in kwargs:
            self.name = kwargs['name']
        else:
            self.name = ""

        if 'id' in kwargs:
            self.id = kwargs['id']
        else:
            self.id = -1



#To do: to move this file in other location
class RoomsManager():
    def __init__(self):
        #SQLite db connection...
        self.rooms = []
        self.load_rooms()


    def load_rooms(self):
        #Get from rooms table
        room1 = Room(name="Room1", id="1")
        self.load_room_objects(room1)

        room2 = Room(name="Room2", id="2")
        self.load_room_objects(room2)

        room3 = Room(name="Room3", id="3")
        self.load_room_objects(room3)

        room4 = Room(name="Room4", id="4")
        self.load_room_objects(room4)

        room5 = Room(name="Room5", id="5")
        self.load_room_objects(room5)

        room6 = Room(name="Room6", id="6")
        self.load_room_objects(room6)

        room7 = Room(name="Room7", id="7")
        self.load_room_objects(room7)

        room8 = Room(name="Room8", id="8")
        self.load_room_objects(room8)

        room9 = Room(name="Room9", id="9")
        self.load_room_objects(room9)

        room10 = Room(name="Room10", id="10")
        self.load_room_objects(room10)

        self.rooms.append(room1)
        self.rooms.append(room2)
        self.rooms.append(room3)
        self.rooms.append(room4)
        self.rooms.append(room5)
        self.rooms.append(room6)
        self.rooms.append(room7)
        self.rooms.append(room8)
        self.rooms.append(room9)
        self.rooms.append(room10)

    def load_room_objects(self, room):
        #Get object from objects table
        table1 = RoomObject()
        table2 = RoomObject()
        table3 = RoomObject()

        room.objects.append(table1)
        room.objects.append(table2)
        room.objects.append(table3)