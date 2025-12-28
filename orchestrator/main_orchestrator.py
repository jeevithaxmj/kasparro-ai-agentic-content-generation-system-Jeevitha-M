import json
from agents.parser_agent import ParserAgent
from agents.faq_page_agent import FAQPageAgent
from agents.product_page_agent import ProductPageAgent
from agents.comparison_page_agent import ComparisonPageAgent


class ContentOrchestrator:
    """
    Central controller that coordinates agents and produces final outputs.
    """

    def __init__(self):
        self.parser_agent = ParserAgent()
        self.faq_agent = FAQPageAgent()
        self.product_page_agent = ProductPageAgent()
        self.comparison_agent = ComparisonPageAgent()

    def run(self, raw_product_data: dict):
        product = self.parser_agent.parse(raw_product_data)

        faq_page = self.faq_agent.generate(product)
        product_page = self.product_page_agent.generate(product)
        comparison_page = self.comparison_agent.generate(product)

        return faq_page, product_page, comparison_page


if __name__ == "__main__":
    raw_product_data = {
        "Product Name": "GlowBoost Vitamin C Serum",
        "Concentration": "10% Vitamin C",
        "Skin Type": ["Oily", "Combination"],
        "Key Ingredients": ["Vitamin C", "Hyaluronic Acid"],
        "Benefits": ["Brightening", "Fades dark spots"],
        "How to Use": "Apply 2–3 drops in the morning before sunscreen",
        "Side Effects": "Mild tingling for sensitive skin",
        "Price": 699
    }

    orchestrator = ContentOrchestrator()
    faq, product, comparison = orchestrator.run(raw_product_data)

    with open("output/faq.json", "w") as f:
        json.dump(faq, f, indent=2)

    with open("output/product_page.json", "w") as f:
        json.dump(product, f, indent=2)

    with open("output/comparison_page.json", "w") as f:
        json.dump(comparison, f, indent=2)

        
