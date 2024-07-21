from box import Box
class OrderDB():
    def __init__(self, main_window):
        self.main_window = main_window
        #TO DO: chech if db_manager is present and valid
        self.db_manager = self.main_window.db_manager

    def load_categories(self):
        # Get from rooms table
        self.db_manager.cursor.execute("SELECT * FROM categories")
        categories = self.db_manager.cursor.fetchall()
        return [self._serialize(c) for c in categories]

    @staticmethod
    def _serialize(category):
        if 'name' not in category:
            category.name = ""
        if 'id' not in category:
            category.id = -1
        return Box(category)