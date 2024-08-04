import os
import sqlite3

from app.utils.constants import DataBase
from app.utils.utils import dict_factory


class DBManager():
    def __init__(self):
        # self.delete_db() # ASV: WARNING: ONLY FOR TESTS
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
                        `id` string not null primary key,
                        room_id INTEGER,
                        x INTEGER,
                        y INTEGER,
                        size_x INTEGER,
                        size_y INTEGER,
                        rotation REAL,
                        image TEXT,
                        FOREIGN KEY (room_id) REFERENCES rooms (id)
                    )
                """)

        # Creare tabel pt editor de locatie cu obiectele predefinite
        self.cursor.execute("""
                    CREATE TABLE IF NOT EXISTS location_editor_objects (
                        `id` integer not null primary key autoincrement,
                        `name` TEXT not null,
                        `category` TEXT not null,
                        `image` TEXT not null,
                         unique (`id`)
                    )
                """)

        self.conn.commit()

    def delete_db(self):
        # Ștergem fișierul de bază de date, dacă există
        if os.path.exists(DataBase.BD_NAME):
            os.remove(DataBase.BD_NAME)
#For testing: INSERT INTO test (text_column, integer_column, double_column) VALUES ('Some text', 42, 3.14);
