from app.core.contracts import ClusterResult
from app.engine.validation import validate_territory


def test_validation_marks_strong_cluster_valid():
    cluster = ClusterResult(
        cluster_id="c1",
        city_id="city",
        core_id="core",
        business_ids=["a", "b", "c"],
        raw_business_count=5,
        weighted_business_count=8.8,
        category_mix={"dermatologist": 2},
        density_score=0.9,
        radius_km=2.1,
        travel_efficiency=0.86,
        confidence_score=0.88,
        centroid=(1.0, 1.0),
    )
    validation = validate_territory(cluster, {"weighted_viable_count": 92, "travel_efficiency": 0.86})
    assert validation["status"] == "valid"
    assert validation["viability_score"] >= 0.78

