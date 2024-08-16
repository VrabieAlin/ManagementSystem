class Product:
    def __init__(self, id, name, price, description, recipe_id, order_in_list, category_id):
        self.id = id
        self.name = name
        self.price = price
        self.description = description
        self.recipe_id = recipe_id
        self.order_in_list = order_in_list
        self.category_id = category_id

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'price': self.price,
            'description': self.description,
            'recipe_id': self.recipe_id,
            'order_in_list': self.order_in_list,
            'category_id': self.category_id
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            id=data.get('id', -1),
            name=data.get('name', ''),
            price=data.get('price', 0.0),
            description=data.get('description', ''),
            recipe_id=data.get('recipe_id', -1),
            order_in_list=data.get('order_in_list', -1),
            category_id=data.get('category_id', -1)
        )