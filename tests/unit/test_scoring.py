from app.core.contracts import BusinessRecord
from app.engine.reconciliation import reconcile_businesses
from app.engine.scoring import score_businesses


def test_scoring_increases_with_quality_and_sources():
    records = [
        BusinessRecord(
            record_id="a",
            source="google_places",
            source_confidence=0.8,
            city_id="x",
            country_code="US",
            name="Park Dermatology",
            address="123 Park Ave",
            region="NY",
            city="New York",
            latitude=1.0,
            longitude=1.0,
            category_hint="dermatologist",
            rating=4.8,
            review_count=300,
            website_present=True,
            premium_corridor=True,
            completeness=0.95,
            stale=False,
            metadata={},
        ),
        BusinessRecord(
            record_id="b",
            source="overture",
            source_confidence=0.7,
            city_id="x",
            country_code="US",
            name="Park Dermatology",
            address="123 Park Ave",
            region="NY",
            city="New York",
            latitude=1.0,
            longitude=1.0,
            category_hint="dermatologist",
            rating=4.7,
            review_count=250,
            website_present=True,
            premium_corridor=True,
            completeness=0.9,
            stale=False,
            metadata={},
        ),
    ]
    scored = score_businesses(reconcile_businesses(records))
    assert len(scored) == 1
    assert scored[0].weighted_opportunity_score > 10
    assert scored[0].category_confidence >= 0.7

