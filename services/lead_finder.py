"""
Privacy-first lead discovery foundation for CannabisAI.

This module does not scrape platforms yet.
It provides the data structure and qualification layer that
future public-source integrations will use.
"""

from services.privacy import is_allowed_source, sanitize_lead


def qualify_lead(lead):
    """
    Determine whether a potential lead contains enough
    legitimate business information to be considered.
    """

    source_type = lead.get("source_type")
    is_public = lead.get("is_public", False)

    if not is_allowed_source(source_type, is_public):
        return None

    if not lead.get("business_name"):
        return None

    cleaned = sanitize_lead(lead)

    cleaned["fit_score"] = calculate_fit_score(cleaned)

    return cleaned


def calculate_fit_score(lead):
    """
    Initial placeholder scoring system.

    This will eventually use the AI model and business-specific
    criteria.
    """

    score = 0

    if lead.get("business_name"):
        score += 25

    if lead.get("website"):
        score += 25

    if lead.get("business_category"):
        score += 25

    if lead.get("public_source"):
        score += 25

    return score


def lead_finder_status():
    return {
        "status": "foundation_ready",
        "sources": [
            "public_reddit",
            "public_telegram",
            "public_web",
        ],
        "automatic_outreach": False,
        "privacy_first": True,
    }
