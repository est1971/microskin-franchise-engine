# Country Profile Guide

Country profiles are configuration-first and should define:

- postal system type
- administrative hierarchy
- preferred geometry snapping order
- normalization and transliteration settings
- market maturity defaults
- category mapping adjustments
- naming convention
- export convention

Seed examples are stored in `app/data/fixtures/demo_data.py`. Add new markets by introducing a country profile first, then city fixtures or live adapters.

