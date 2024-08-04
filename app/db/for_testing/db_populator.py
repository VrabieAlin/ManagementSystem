from app.db.db_manager import DBManager

class DBInserter:

    inserts = [
        "INSERT INTO rooms (id,name) VALUES (1,'Main Restaurant')",
        "INSERT INTO rooms (id,name) VALUES (2,'The Terrace')",

        "INSERT INTO categories (name) VALUES ('Burgers')",
        "INSERT INTO categories (name) VALUES ('Pizza')",
        "INSERT INTO categories (name) VALUES ('Drinks')",

        "INSERT INTO products (name, category_id, price) VALUES ('Hamburger', 1, 40.0)",
        "INSERT INTO products (name, category_id, price) VALUES ('Cheeseburger', 1, 43.0)",
        "INSERT INTO products (name, category_id, price) VALUES ('Capricciosa', 2, 40.0)",
        "INSERT INTO products (name, category_id, price) VALUES ('Quattro Stagioni', 2, 35.5)",
        "INSERT INTO products (name, category_id, price) VALUES ('Quatro Formaggi', 2, 30.99)",
        "INSERT INTO products (name, category_id, price) VALUES ('Delicio', 2, 45.0)",
        "INSERT INTO products (name, category_id, price) VALUES ('Cola', 3, 40.0)",
        "INSERT INTO products (name, category_id, price) VALUES ('Sprite', 3, 40.0)",
        "INSERT INTO products (name, category_id, price) VALUES ('Fanta 1', 3, 40.0)",
        "INSERT INTO products (name, category_id, price) VALUES ('Fanta 2', 3, 40.0)",
        "INSERT INTO products (name, category_id, price) VALUES ('Fanta 3', 3, 40.0)",
        "INSERT INTO products (name, category_id, price) VALUES ('Fanta 4', 3, 40.0)",
        "INSERT INTO products (name, category_id, price) VALUES ('Fanta 5', 3, 40.0)",
        "INSERT INTO products (name, category_id, price) VALUES ('Fanta 6', 3, 40.0)",
        "INSERT INTO products (name, category_id, price) VALUES ('Fanta 7', 3, 40.0)",
        "INSERT INTO products (name, category_id, price) VALUES ('Fanta 8', 3, 40.0)",
        "INSERT INTO products (name, category_id, price) VALUES ('Fanta 9', 3, 40.0)",
        "INSERT INTO products (name, category_id, price) VALUES ('Fanta 10', 3, 40.0)",
        "INSERT INTO products (name, category_id, price) VALUES ('Fanta 11', 3, 40.0)",
        "INSERT INTO products (name, category_id, price) VALUES ('Fanta 12', 3, 40.0)",
        "INSERT INTO products (name, category_id, price) VALUES ('Fanta 13', 3, 40.0)",
        "INSERT INTO products (name, category_id, price) VALUES ('Fanta 14', 3, 40.0)",
        "INSERT INTO products (name, category_id, price) VALUES ('Fanta 15', 3, 40.0)",
        "INSERT INTO products (name, category_id, price) VALUES ('Fanta 16', 3, 40.0)",
        "INSERT INTO products (name, category_id, price) VALUES ('Fanta 17', 3, 40.0)",
        "INSERT INTO products (name, category_id, price) VALUES ('Fanta 18', 3, 40.0)",
        "INSERT INTO products (name, category_id, price) VALUES ('Fanta 19', 3, 40.0)",
        "INSERT INTO products (name, category_id, price) VALUES ('Fanta 20', 3, 40.0)",
        "INSERT INTO products (name, category_id, price) VALUES ('Fanta 21', 3, 40.0)",
        "INSERT INTO products (name, category_id, price) VALUES ('Fanta 22', 3, 40.0)",
        "INSERT INTO products (name, category_id, price) VALUES ('Fanta 23', 3, 40.0)",
        "INSERT INTO products (name, category_id, price) VALUES ('Fanta 24', 3, 40.0)",
        "INSERT INTO products (name, category_id, price) VALUES ('Fanta 25', 3, 40.0)",
        "INSERT INTO products (name, category_id, price) VALUES ('Fanta 26', 3, 40.0)",
        "INSERT INTO products (name, category_id, price) VALUES ('Fanta 27', 3, 40.0)",
        "INSERT INTO products (name, category_id, price) VALUES ('Fanta 28', 3, 40.0)",
        "INSERT INTO products (name, category_id, price) VALUES ('Fanta 29', 3, 40.0)",
        "INSERT INTO products (name, category_id, price) VALUES ('Fanta 30', 3, 40.0)",
        "INSERT INTO products (name, category_id, price) VALUES ('Fanta 31', 3, 40.0)",
        "INSERT INTO products (name, category_id, price) VALUES ('Fanta 32', 3, 40.0)",
        "INSERT INTO products (name, category_id, price) VALUES ('Fanta 33', 3, 40.0)",
        "INSERT INTO products (name, category_id, price) VALUES ('Fanta 34', 3, 40.0)",
        "INSERT INTO products (name, category_id, price) VALUES ('Fanta 35', 3, 40.0)",
        "INSERT INTO products (name, category_id, price) VALUES ('Fanta 36', 3, 40.0)",
        "INSERT INTO products (name, category_id, price) VALUES ('Fanta 37', 3, 40.0)",
        "INSERT INTO products (name, category_id, price) VALUES ('Fanta 38', 3, 40.0)",
        "INSERT INTO products (name, category_id, price) VALUES ('Fanta 39', 3, 40.0)",
        "INSERT INTO products (name, category_id, price) VALUES ('Fanta 40', 3, 40.0)",
        "INSERT INTO products (name, category_id, price) VALUES ('Fanta 41', 3, 40.0)",
        "INSERT INTO products (name, category_id, price) VALUES ('Fanta 42', 3, 40.0)",
        "INSERT INTO products (name, category_id, price) VALUES ('Fanta 43', 3, 40.0)",
        "insert into `location_editor_objects` (`category`, `id`, `image`, `name`) select 'Mese' as `category`, '1' as `id`, 'big_round_table.png' as `image`, 'Masa rotunda mare' as `name` union all select 'Mese' as `category`, '2' as `id`, 'big_rectangular_table.png' as `image`, 'Masa patrata mare' as `name`"

    ]
    def __init__(self, db_manager: DBManager):
        self.db_manager = db_manager

    def populate_tables(self):
        conn = self.db_manager.conn
        cursor = self.db_manager.cursor
        for insert in self.inserts:
            cursor.execute(insert)
        conn.commit()

