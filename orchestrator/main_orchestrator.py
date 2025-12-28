from agents.parser_agent import ParserAgent


class ContentOrchestrator:
    """
    Central controller that coordinates agents and logic blocks.
    """

    def __init__(self):
        self.parser_agent = ParserAgent()

    def run(self, raw_text: str):
        """
        Entry point for the agentic system.
        """
        product = self.parser_agent.parse(raw_text)
        return product
