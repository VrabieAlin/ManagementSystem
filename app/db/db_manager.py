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
