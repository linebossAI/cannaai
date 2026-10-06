from services.privacy import is_allowed_source, sanitize_lead


def calculate_fit_score(lead):
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


def qualify_lead(lead):
    if not is_allowed_source(
        lead.get("source_type"),
        lead.get("is_public", False)
    ):
        return None

    if not lead.get("business_name"):
        return None

    cleaned = sanitize_lead(lead)
    cleaned["fit_score"] = calculate_fit_score(cleaned)

    return cleaned


def demo_leads():
    leads = [
        {
            "business_name": "Example Cannabis Dispensary",
            "business_category": "dispensary",
            "website": "https://example.com",
            "public_source": "public_web",
            "source_url": "https://example.com",
            "reason": "Cannabis retailer that could benefit from AI business tools",
            "source_type": "public_web",
            "is_public": True,
        },
        {
            "business_name": "Example Cannabis Brand",
            "business_category": "cannabis_brand",
            "website": "https://examplebrand.com",
            "public_source": "public_reddit",
            "source_url": "https://reddit.com",
            "reason": "Public discussion indicates an active cannabis business",
            "source_type": "public_reddit",
            "is_public": True,
        },
    ]

    return [
        qualified
        for lead in leads
        if (qualified := qualify_lead(lead)) is not None
    ]


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
