from box import Box


class LocationRoom:

    def __init__(self, db_manager):
        self.db_manager = db_manager

    def load_rooms(self):
        # Get from rooms table
        self.db_manager.cursor.execute("SELECT * FROM rooms")
        rooms = self.db_manager.cursor.fetchall()
        return [self._serialize(r) for r in rooms]

    @staticmethod
    def _serialize(room):
        if 'name' not in room:
            room.name = ""
        if 'id' not in room:
            room.id = -1
        return Box(room)