class RoomObject():
    def __init__(self, **kwargs):
        self.id = -1
        self.owner_room_id = -1
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
    def __init__(self, db_manager):
        self.db_manager = db_manager

        self.rooms = []
        self.load_rooms()


    def load_rooms(self):
        # Get from rooms table
        self.db_manager.cursor.execute("SELECT * FROM rooms")
        rooms = self.db_manager.cursor.fetchall()
        for (room_id, room_name) in rooms:
            room = Room(name=room_name, id=room_id)
            self.load_room_objects(room)
            self.rooms.append(room)

    def load_room_objects(self, room):
        #Get object from objects table
        self.db_manager.cursor.execute("SELECT * FROM room_objects WHERE owner_room_id = ?", (room.id,))
        objects = self.db_manager.cursor.fetchall()

        for (object_id, owner_room_id, pos_x, pos_y, size_x, size_y, rotation, image_id, name) in objects:
            table = RoomObject()
            room.objects.append(table)
