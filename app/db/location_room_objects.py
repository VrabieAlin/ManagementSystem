class LocationRoomObject:
    def __init__(self, db_manager):
        self.db_manager = db_manager

    def load_room_objects(self, room):
        # Get object from objects table
        self.db_manager.cursor.execute("SELECT * FROM room_objects WHERE owner_room_id = ?", (room.id,))
        objects = self.db_manager.cursor.fetchall()

        for (object_id, owner_room_id, pos_x, pos_y, size_x, size_y, rotation, image_id, name) in objects:
            table = LocationRoomObject()
            room.objects.append(table)