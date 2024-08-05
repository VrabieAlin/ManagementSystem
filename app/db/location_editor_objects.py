from box import Box


class LocationEditorObjects:
    def __init__(self, db_manager):
        self.db_manager = db_manager

    def load_default_objects(self):
        self.db_manager.cursor.execute("SELECT * from location_editor_objects")
        objects = self.db_manager.cursor.fetchall()
        return [Box(o) for o in objects]