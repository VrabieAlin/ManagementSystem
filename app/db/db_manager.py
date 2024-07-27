import sqlite3

from app.utils.constants import DataBase
from app.utils.utils import dict_factory


class DBManager():
    def __init__(self):
        self.init_db()

    def init_db(self):
        self.conn = sqlite3.connect(DataBase.BD_NAME)
        self.conn.row_factory = dict_factory
        self.cursor = self.conn.cursor()

        # Creare tabel rooms
        self.cursor.execute("""
                    CREATE TABLE IF NOT EXISTS rooms (
                        id INTEGER PRIMARY KEY,
                        name TEXT
                    )
                """)

        # Creare tabel categories
        self.cursor.execute("""
                            CREATE TABLE IF NOT EXISTS categories (
                                id INTEGER PRIMARY KEY,
                                name TEXT
                            )
                        """)

        # Creare tabel products of each category
        self.cursor.execute("""
                        CREATE TABLE IF NOT EXISTS products (
                            id INTEGER PRIMARY KEY,
                            category_id INTEGER DEFAULT -1,
                            name TEXT DEFAULT '',
                            price DOUBLE DEFAULT -1,
                            description TEXT DEFAULT '',
                            recipe_id INTEGER DEFAULT -1,
                            order_in_list INTEGER DEFAULT -1
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

#For testing: INSERT INTO test (text_column, integer_column, double_column) VALUES ('Some text', 42, 3.14);
