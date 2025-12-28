from agents.parser_agent import ParserAgent
from agents.faq_page_agent import FAQPageAgent


class ContentOrchestrator:
    """
    Central controller that coordinates agents and logic blocks.
    """

    def __init__(self):
        self.parser_agent = ParserAgent()
        self.faq_agent = FAQPageAgent()

    def run(self, raw_product_data: dict):
        """
        Entry point for the agentic system.
        """
        product = self.parser_agent.parse(raw_product_data)
        faq_page = self.faq_agent.generate(product)

        return {
            "faq_page": faq_page
        }
