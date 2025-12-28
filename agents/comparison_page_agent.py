from typing import Dict
from agents.product_model import ProductModel


class ComparisonPageAgent:
    """
    Agent responsible for generating a comparison page between
    the main product and a fictional competitor.
    """

    def generate(self, product: ProductModel) -> Dict:
        fictional_product = {
            "name": "RadiantSkin Vitamin C Serum",
            "concentration": "8%",
            "key_ingredients": ["Vitamin C", "Niacinamide"],
            "benefits": ["Brightening", "Even skin tone"],
            "price": 599
        }

        return {
            "page_type": "COMPARISON",
            "product_a": {
                "name": product.name,
                "concentration": product.concentration,
                "key_ingredients": product.key_ingredients,
                "benefits": product.benefits,
                "price": product.price
            },
            "product_b": fictional_product
        }
