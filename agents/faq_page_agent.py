from typing import List, Dict
from agents.product_model import ProductModel


class FAQPageAgent:
    """
    Agent responsible for generating FAQ page content in structured form.
    """

    def generate(self, product: ProductModel) -> Dict:
        faqs: List[Dict[str, str]] = [
            {
                "question": f"What is {product.name}?",
                "answer": f"{product.name} is a skincare product formulated with key ingredients such as {', '.join(product.key_ingredients)}."
            },
            {
                "question": "Who can use this product?",
                "answer": f"This product is suitable for {', '.join(product.skin_type)} skin types."
            },
            {
                "question": "How should I use this product?",
                "answer": product.how_to_use
            },
            {
                "question": "Are there any side effects?",
                "answer": product.side_effects
            },
            {
                "question": "What are the main benefits?",
                "answer": ", ".join(product.benefits)
            }
        ]

        return {
            "page_type": "FAQ",
            "product_name": product.name,
            "faqs": faqs
        }
