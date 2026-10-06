"""
CannabisAI LeadFinder.

Customer Mode helps a cannabis brand discover relevant public communities
and potential customer opportunities.

Developer Mode will be added separately for CannabisAI's internal use.
"""

from services.privacy import is_allowed_source, sanitize_lead


def calculate_fit_score(opportunity):
    score = 0

    if opportunity.get("community_name"):
        score += 20

    if opportunity.get("platform"):
        score += 20

    if opportunity.get("topic"):
        score += 20

    if opportunity.get("source_url"):
        score += 20

    if opportunity.get("reason"):
        score += 20

    return score


def qualify_opportunity(opportunity):
    if not is_allowed_source(
        opportunity.get("source_type"),
        opportunity.get("is_public", False),
    ):
        return None

    if not opportunity.get("community_name"):
        return None

    cleaned = sanitize_lead({
        "business_name": opportunity.get("community_name"),
        "business_category": opportunity.get("topic"),
        "website": opportunity.get("source_url"),
        "public_source": opportunity.get("platform"),
        "source_url": opportunity.get("source_url"),
        "reason": opportunity.get("reason"),
    })

    cleaned["community_name"] = opportunity.get("community_name")
    cleaned["platform"] = opportunity.get("platform")
    cleaned["topic"] = opportunity.get("topic")
    cleaned["fit_score"] = calculate_fit_score(opportunity)

    return cleaned


def customer_lead_finder_status():
    return {
        "mode": "customer",
        "purpose": "find relevant public cannabis communities and customer opportunities",
        "sources": [
            "public_reddit",
            "public_telegram",
            "public_web",
        ],
        "automatic_outreach": False,
        "privacy_first": True,
        "developer_mode": "separate",
    }


CUSTOMER_TARGETS = {
    "flower": [
        "flower",
        "premium flower",
        "indica",
        "sativa",
        "hybrid",
    ],
    "edibles": [
        "edibles",
        "gummies",
        "infused",
        "edible",
    ],
    "vapes": [
        "vape",
        "vapes",
        "cartridge",
        "cart",
        "disposable",
    ],
    "concentrates": [
        "concentrates",
        "live resin",
        "rosin",
        "wax",
        "dabs",
    ],
    "cannabis_brand": [
        "cannabis brand",
        "weed brand",
        "cannabis company",
        "marijuana brand",
    ],
}


def find_target_matches(text):
    text = text.lower()
    matches = []

    for category, keywords in CUSTOMER_TARGETS.items():
        if any(keyword in text for keyword in keywords):
            matches.append(category)

    return matches
