"""
Product knowledge service for CannabisAI.
"""

PRODUCTS = [
    {
        "name": "Blue Dream",
        "type": "Flower",
        "category": "Sativa-leaning hybrid",
        "description": "Demo product for development."
    },
    {
        "name": "OG Kush",
        "type": "Flower",
        "category": "Indica-leaning hybrid",
        "description": "Demo product for development."
    },
    {
        "name": "Citrus Haze",
        "type": "Flower",
        "category": "Sativa",
        "description": "Demo product for development."
    }
]


def handle_products(message):
    """Return product information."""
    response = "Here are the current products:\n\n"

    for product in PRODUCTS:
        response += (
            f"• {product['name']} — "
            f"{product['type']} — "
            f"{product['category']}\n"
        )

    return response
