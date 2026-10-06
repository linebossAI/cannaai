"""
Inventory management service for CannabisAI.
"""

INVENTORY = {
    "Blue Dream": 24,
    "OG Kush": 8,
    "Citrus Haze": 3
}

LOW_STOCK_THRESHOLD = 5


def handle_inventory(message):
    """Return inventory status."""

    response = "Current inventory:\n\n"

    for product, quantity in INVENTORY.items():
        if quantity <= LOW_STOCK_THRESHOLD:
            status = "⚠️ LOW STOCK"
        else:
            status = "OK"

        response += f"• {product}: {quantity} units — {status}\n"

    return response
