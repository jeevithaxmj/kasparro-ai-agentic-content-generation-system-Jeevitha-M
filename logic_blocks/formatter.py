from typing import List


def format_bullets(items: List[str]) -> str:
    """
    Format a list of items into bullet points.
    """
    return "\n".join(f"- {item}" for item in items)


def format_price(price: int) -> str:
    """
    Format price into readable currency format.
    """
    return f"₹{price}"
