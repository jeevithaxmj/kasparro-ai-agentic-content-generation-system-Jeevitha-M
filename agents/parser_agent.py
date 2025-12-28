from agents.product_model import ProductModel


class ParserAgent:
    """
    Responsible for converting raw product text into a structured ProductModel.
    """

    def parse(self, raw_text: str) -> ProductModel:
        """
        Parse unstructured product description text and return a ProductModel.
        This is a placeholder implementation.
        """

        # TODO: Replace with real parsing logic
        return ProductModel(
            name="Unknown",
            concentration="Unknown",
            skin_type=[],
            key_ingredients=[],
            benefits=[],
            how_to_use="",
            side_effects="",
            price=0
        )
