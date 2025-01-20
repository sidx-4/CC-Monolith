import json
import products
from cart import dao
from products import Product


class Cart:
    def __init__(self, id: int, username: str, contents: list[Product], cost: float):
        self.id = id
        self.username = username
        self.contents = contents
        self.cost = cost

    def load(data):
        return Cart(data['id'], data['username'], data['contents'], data['cost'])


def get_cart(username: str) -> list:
    cart_details = dao.get_cart(username)
    if cart_details is None:
        return []

    # Process cart details and retrieve all products in a single loop
    items = []
    for cart_detail in cart_details:
        contents = cart_detail['contents']
        evaluated_contents = eval(contents)  # Convert stringified list into a Python list
        
        # Fetch product details for all product IDs in evaluated_contents
        for product_id in evaluated_contents:
            product_details = products.get_product(product_id)  # Fetch product details
            items.append(product_details)
    
    return items


def add_to_cart(username: str, product_id: int):
    dao.add_to_cart(username, product_id)


def remove_from_cart(username: str, product_id: int):
    dao.remove_from_cart(username, product_id)


def delete_cart(username: str):
    dao.delete_cart(username)
