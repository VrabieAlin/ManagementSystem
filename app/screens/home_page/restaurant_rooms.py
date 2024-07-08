import sqlite3
from app.utils.constants import DataBase

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
    def __init__(self):
        self.init_db()

        self.rooms = []
        self.load_rooms()

    def init_db(self):
        self.conn = sqlite3.connect(DataBase.BD_NAME)
        self.cursor = self.conn.cursor()

        # Creare tabel rooms
        self.cursor.execute("""
                    CREATE TABLE IF NOT EXISTS rooms (
                        id INTEGER PRIMARY KEY,
                        name TEXT
                    )
                """)

        # Creare tabel objects
        self.cursor.execute("""
                    CREATE TABLE IF NOT EXISTS room_objects (
                        object_id INTEGER PRIMARY KEY,
                        owner_room_id INTEGER,
                        pos_x INTEGER,
                        pos_y INTEGER,
                        size_x INTEGER,
                        size_y INTEGER,
                        rotation REAL,
                        image_id INTEGER,
                        name TEXT,
                        FOREIGN KEY (owner_room_id) REFERENCES rooms (id)
                    )
                """)

        self.conn.commit()

    def load_rooms(self):
        # Get from rooms table
        self.cursor.execute("SELECT * FROM rooms")
        rooms = self.cursor.fetchall()
        for (room_id, room_name) in rooms:
            room = Room(name=room_name, id=room_id)
            self.load_room_objects(room)
            self.rooms.append(room)

    def load_room_objects(self, room):
        #Get object from objects table
        self.cursor.execute("SELECT * FROM room_objects WHERE owner_room_id = ?", (room.id,))
        objects = self.cursor.fetchall()

        for (object_id, owner_room_id, pos_x, pos_y, size_x, size_y, rotation, image_id, name) in objects:
            table = RoomObject()
            room.objects.append(table)
