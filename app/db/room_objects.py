class RoomObjects:

    def __init__(self, db_manager):
        self.db_manager = db_manager

    def save_objects_for_room(self, objects):
        data = [(1, o.x, o.y, 100, 100, 100, o.image) for o in objects]
        self.db_manager.cursor.executemany(
            "INSERT INTO room_objects (owner_room_id,x,y,size_x,size_y,rotation, image) VALUES(?,?,?,?,?,?,?)", data)
        self.db_manager.conn.commit()
