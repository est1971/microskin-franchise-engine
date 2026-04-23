from app.services.pipeline import global_summary, run_city_pipeline


def test_pipeline_detects_multi_core_and_territories():
    result = run_city_pipeline("us-new-york")
    assert result.city_analysis["suggested_economic_cores"] >= 4
    assert len(result.clusters) >= 3
    assert len(result.territories) >= 3
    assert any(item.validation_status.startswith("valid") for item in result.territories)


def test_global_summary_population_warning_present():
    summary = global_summary()
    assert summary["population_logic_warning_count"] >= 1

