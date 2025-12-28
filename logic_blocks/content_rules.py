from typing import List


def validate_skin_type(product_skin_types: List[str], user_skin_type: str) -> bool:
    """
    Check if the product is suitable for the user's skin type.
    """
    return user_skin_type.lower() in [s.lower() for s in product_skin_types]


def has_required_benefits(product_benefits: List[str], required_benefits: List[str]) -> bool:
    """
    Check if the product contains all required benefits.
    """
    product_benefits_lower = [b.lower() for b in product_benefits]
    return all(benefit.lower() in product_benefits_lower for benefit in required_benefits)
