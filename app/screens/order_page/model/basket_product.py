import pickle
from app.screens.order_page.model.product import Product
#from app.screens.order_page.view.elements.widgets.check_row.product_raw_view import ProductRawContainer
from app.utils.constants import Colors, ORDERED_PRODUCT_STATUS as PRODUCT_STATUS

class BasketProduct:
    def __init__(self, id, quantity, table_id, status, product, notes=""):
        self.basket_id = id
        self.quantity = quantity
        self.table_id = table_id
        self.status = status
        self.product: Product = product
        self.notes = notes

    def to_dict(self):
        # Convertirea într-un dicționar
        return {'basket_id': self.basket_id,
                'quantity': self.quantity,
                'table_id': self.table_id,
                'status': self.status,
                'notes': self.notes,
                'product': self.product.to_dict()
                }

    @classmethod
    def from_dict(cls, data):
        product_data = data.get('product', {})
        product = Product.from_dict(product_data)
        return cls(
            id=data.get('basket_id', -1),
            quantity=data.get('quantity', 0),
            table_id=data.get('table_id', -1),
            status=data.get('status', ''),
            notes=data.get('notes', ''),
            product=product
        )