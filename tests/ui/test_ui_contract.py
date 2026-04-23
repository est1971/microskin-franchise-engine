from pathlib import Path


def test_ui_contains_required_views():
    html = Path("app/templates/index.html").read_text(encoding="utf-8")
    required = [
        "Global market view",
        "Country analysis",
        "City intelligence",
        "Territory detail & calculator",
        "Admin review",
        "Export center",
    ]
    for item in required:
        assert item in html

