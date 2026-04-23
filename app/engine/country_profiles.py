from __future__ import annotations

from app.core.contracts import CountryProfile
from app.data.fixtures.demo_data import COUNTRY_FIXTURES


def load_country_profiles() -> dict[str, CountryProfile]:
    profiles: dict[str, CountryProfile] = {}
    for country in COUNTRY_FIXTURES:
        profiles[country["code"]] = CountryProfile(
            code=country["code"],
            name=country["name"],
            postal_system_type=country["profile"]["postal_system_type"],
            admin_hierarchy=country["profile"]["admin_hierarchy"],
            preferred_geometry_snap_hierarchy=country["profile"]["preferred_geometry_snap_hierarchy"],
            normalization=country["profile"]["normalization"],
            market_defaults=country["profile"]["market_defaults"],
            category_mapping_adjustments=country["profile"]["category_mapping_adjustments"],
            naming_convention=country["profile"]["naming_convention"],
            export_convention=country["profile"]["export_convention"],
        )
    return profiles

