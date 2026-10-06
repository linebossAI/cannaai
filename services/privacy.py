"""
Privacy guardrails for CannabisAI.

This module defines the rules that data must pass before it can
be used by CannabisAI services.
"""

BLOCKED_DATA_TYPES = {
    "password",
    "session_cookie",
    "authentication_token",
    "private_message",
    "private_group_data",
}


def is_allowed_source(source_type, is_public=True):
    """
    Check whether a source is eligible for LeadFinder.

    LeadFinder is restricted to publicly available sources.
    """

    if not is_public:
        return False

    if source_type in {
        "private_group",
        "private_channel",
        "private_message",
    }:
        return False

    return True


def is_allowed_field(field_name):
    """
    Prevent unnecessary sensitive or credential data from entering
    the LeadFinder system.
    """

    return field_name not in BLOCKED_DATA_TYPES


def sanitize_lead(lead):
    """
    Keep only the business-relevant fields we currently need.
    """

    allowed_fields = {
        "business_name",
        "business_category",
        "website",
        "public_source",
        "source_url",
        "reason",
        "fit_score",
    }

    return {
        key: value
        for key, value in lead.items()
        if key in allowed_fields
    }


def privacy_notice():
    """
    Return the core privacy principle used by LeadFinder.
    """

    return (
        "CannabisAI LeadFinder uses public business information only, "
        "minimizes collected data, and requires human approval for outreach."
    )
