from __future__ import annotations

from app.core.config import config
from app.core.contracts import CanonicalBusiness


def score_business(business: CanonicalBusiness) -> CanonicalBusiness:
    weight = config.category_weights.get(business.category, 0.4)
    rating_score = min(business.sources[0].rating / 5, 1.0) * 0.2
    review_score = min(business.sources[0].review_count / 300, 1.0) * 0.1
    website_score = 0.08 if business.sources[0].website_present else 0.0
    completeness_score = business.sources[0].completeness * 0.12
    corridor_score = 0.1 if business.sources[0].premium_corridor else 0.0
    source_agreement = min(len(business.sources) / 3, 1.0) * 0.12
    quality = rating_score + review_score + website_score + completeness_score + corridor_score + source_agreement
    suitability_score = round(min(1.0, (weight / 1.2) + quality), 2)
    weighted_opportunity_score = round(suitability_score * weight * 10, 2)
    business.category_confidence = round(min(0.98, 0.62 + source_agreement + review_score), 2)
    business.suitability_score = suitability_score
    business.weighted_opportunity_score = weighted_opportunity_score
    business.quality_modifiers = {
        "rating_proxy": round(rating_score, 2),
        "review_proxy": round(review_score, 2),
        "website_presence": website_score,
        "business_completeness": round(completeness_score, 2),
        "source_agreement": round(source_agreement, 2),
        "premium_corridor": corridor_score,
    }
    return business


def score_businesses(businesses: list[CanonicalBusiness]) -> list[CanonicalBusiness]:
    return [score_business(business) for business in businesses]

