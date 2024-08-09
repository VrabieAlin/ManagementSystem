from app.screens.order_page.model.category import Category
from app.screens.order_page.model.product import Product


class OrderDB:
    def __init__(self, main_window):
        self.main_window = main_window
        self.db_manager = self.main_window.db_manager

        self.categories = self.load_categories()
        self.products = self.load_products()

    def get_categories(self):
        return self.categories

    def load_categories(self):
        self.db_manager.cursor.execute("SELECT * FROM categories")
        categories = self.db_manager.cursor.fetchall()
        return [self._serialize_category(c) for c in categories]

    @staticmethod
    def _serialize_category(category):
        return Category(
            id=category.get('id', -1),
            name=category.get('name', "")
        )

    def get_products(self):
        return self.products

    def load_products(self):
        all_products = {}  # category: [products...]
        for category in self.categories:
            self.db_manager.cursor.execute("SELECT * FROM products WHERE category_id=?", (category.id,))
            products = self.db_manager.cursor.fetchall()
            products_serialized = [self._serialize_product(p) for p in products]
            products_serialized.sort(key=lambda product: product.order_in_list)  # sort products with order_in_list id
            all_products[category.id] = products_serialized
        return all_products

    @staticmethod
    def _serialize_product(product):
        return Product(
            id=product.get('id', -1),
            name=product.get('name', ""),
            price=product.get('price', 1),
            description=product.get('description', ""),
            recipe_id=product.get('recipe_id', -1),
            order_in_list=product.get('order_in_list', -1),
            category_id=product.get('category_id', -1)
        )