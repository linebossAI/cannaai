"""
CannabisAI AI Assistant

This module is responsible for understanding a user's request
and routing it to the appropriate CannabisAI business service.
"""

from services.products import handle_products
from services.inventory import handle_inventory
from services.marketing import handle_marketing
from services.compliance import handle_compliance
from services.business import handle_business


def get_response(message):
    """
    Main CannabisAI assistant router.

    Takes a user's message and determines which business
    service should handle it.
    """

    message = message.strip()

    if not message:
        return "Ask me something about the business."

    text = message.lower()

    if any(word in text for word in [
        "product",
        "products",
        "flower",
        "strain",
        "menu"
    ]):
        return handle_products(message)

    if any(word in text for word in [
        "inventory",
        "stock",
        "restock",
        "low stock"
    ]):
        return handle_inventory(message)

    if any(word in text for word in [
        "marketing",
        "caption",
        "instagram",
        "promotion",
        "promo",
        "advertising"
    ]):
        return handle_marketing(message)

    if any(word in text for word in [
        "compliance",
        "compliant",
        "legal",
        "claim"
    ]):
        return handle_compliance(message)

    if any(word in text for word in [
        "business",
        "sales",
        "owner",
        "manager",
        "performance"
    ]):
        return handle_business(message)

    if any(word in text for word in [
        "hello",
        "hi",
        "hey"
    ]):
        return (
            "What's good 👋 I'm CannabisAI.\n\n"
            "I can help with products, inventory, marketing, "
            "compliance, and business operations."
        )

    return (
        "I'm CannabisAI, your business assistant.\n\n"
        "Try asking me about:\n"
        "• Products\n"
        "• Inventory\n"
        "• Marketing\n"
        "• Compliance\n"
        "• Business performance"
    )
