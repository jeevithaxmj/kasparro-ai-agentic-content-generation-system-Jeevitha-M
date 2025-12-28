from typing import Dict
from agents.product_model import ProductModel


class ProductPageAgent:
    """
    Agent responsible for generating the product description page.
    """

    def generate(self, product: ProductModel) -> Dict:
        return {
            "page_type": "PRODUCT",
            "product_name": product.name,
            "concentration": product.concentration,
            "skin_type": product.skin_type,
            "key_ingredients": product.key_ingredients,
            "benefits": product.benefits,
            "how_to_use": product.how_to_use,
            "side_effects": product.side_effects,
            "price": product.price
        }
