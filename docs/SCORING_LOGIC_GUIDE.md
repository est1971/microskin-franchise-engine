# Scoring Logic Guide

Every canonical business receives:

- category classification
- category confidence
- suitability score
- weighted opportunity score

Default weights:

- dermatologist: `1.2`
- aesthetic clinic: `1.0`
- med spa: `0.9`
- hospital dermatology department: `0.8`
- PMU artist: `0.7`
- premium salon: `0.5`

Quality modifiers include rating, review volume, website presence, record completeness, premium corridor signal, and multi-source agreement.

