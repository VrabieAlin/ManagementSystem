from box import Box


class RoomObjects:

    def __init__(self, db_manager):
        self.db_manager = db_manager

    def save_objects_for_room(self, objects):
        data = [(o.id,1, o.x, o.y, 100, 100, 100, o.image) for o in objects]
        self.db_manager.cursor.executemany(
            "INSERT OR REPLACE INTO room_objects (id,room_id,x,y,size_x,size_y,rotation, image) VALUES(?,?,?,?,?,?,?,?)", data)
        self.db_manager.conn.commit()

    def get_objects_for_room(self, room_id):
        self.db_manager.cursor.execute("SELECT * FROM room_objects WHERE room_id = ?",(room_id,))
        rows = self.db_manager.cursor.fetchall()
        return [self._serialize(r) for r in rows]

    @staticmethod
    def _serialize(object):
        return Box(object)
