from typing import List, Union
from products import dao


class Product:
    def __init__(self, id: int, name: str, description: str, cost: float, qty: int = 0):
        self.id = id
        self.name = name
        self.description = description
        self.cost = cost
        self.qty = qty

    @classmethod
    def from_dict(cls, data: dict) -> "Product":
        return cls(data['id'], data['name'], data['description'], data['cost'], data['qty'])

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "cost": self.cost,
            "qty": self.qty,
        }


def list_products() -> List[Product]:
    """
    Fetches and returns a list of all products.
    """
    products_data = dao.list_products()
    return [Product.from_dict(product) for product in products_data]


def get_product(product_id: int) -> Union[Product, None]:
    """
    Fetches and returns a product by ID.
    Returns None if the product is not found.
    """
    product_data = dao.get_product(product_id)
    if product_data:
        return Product.from_dict(product_data)
    return None


def add_product(product_data: dict) -> None:
    """
    Adds a single product.
    """
    validate_product_data(product_data)
    dao.add_product(product_data)


def add_products(products_data: List[dict]) -> None:
    """
    Adds multiple products in a batch operation.
    """
    for product_data in products_data:
        validate_product_data(product_data)
    dao.add_products(products_data)


def update_qty(product_id: int, qty: int) -> None:
    """
    Updates the quantity of a product.
    Raises ValueError if the quantity is negative.
    """
    if qty < 0:
        raise ValueError("Quantity cannot be negative.")
    dao.update_qty(product_id, qty)


def validate_product_data(product_data: dict) -> None:
    """
    Validates the structure and content of product data.
    """
    required_keys = {'id', 'name', 'description', 'cost', 'qty'}
    if not required_keys.issubset(product_data):
        raise ValueError(f"Product data must contain keys: {required_keys}")
    if product_data['cost'] < 0 or product_data['qty'] < 0:
        raise ValueError("Cost and quantity must be non-negative.")
