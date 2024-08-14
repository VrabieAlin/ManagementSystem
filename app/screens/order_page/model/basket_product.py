import pickle
from app.screens.order_page.model.product import Product
#from app.screens.order_page.view.elements.widgets.check_row.product_raw_view import ProductRawContainer
from app.utils.constants import Colors, ORDERED_PRODUCT_STATUS as PRODUCT_STATUS

class BasketProduct:
    def __init__(self, id, quantity, table_id, status, product):
        self.basket_id = id
        self.quantity = quantity
        self.table_id = table_id
        self.status = status
        self.product: Product = product
        self.widget = None

    @property
    def neserializabil(self):
        return self.widget

    TO DO: SA TRANSFORM OBIECTUL IN DICTIONAR! pentru a putea fi serializabil