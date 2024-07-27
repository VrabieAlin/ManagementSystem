from box import Box
class OrderDB():
    def __init__(self, main_window):
        self.main_window = main_window
        #TO DO: chech if db_manager is present and valid
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
        if 'name' not in category:
            category.name = ""
        if 'id' not in category:
            category.id = -1
        return Box(category)

    def get_products(self):
        return self.products
    def load_products(self):
        all_products = {} # catgory: [products...]
        for category in self.categories:
            self.db_manager.cursor.execute("SELECT * FROM products WHERE category_id=?", (category.id,))
            products = self.db_manager.cursor.fetchall()
            products_serialized = [self._serialize_category(p) for p in products]
            products_serialized.sort(key=lambda product: product.order_in_list) #sort products with order_in_list id
            all_products[category.id] = products_serialized
        return all_products

    @staticmethod
    def _serialize_product(product):
        if 'id' not in product:
            product.id = -1
        if 'name' not in product:
            product.name = ""
        if 'price' not in product:
            product.price = 1
        if 'description' not in product:
            product.description = ""
        if 'recipe_id' not in product:
            product.recipe_id = -1
        if 'order_in_list' not in product: #position in order list if the customer want a custom order
            product.order_in_list = -1
        if 'category_id' not in product:
            product.category_id = -1

        return Box(product)



