# Source Adapter Guide

Adapters live in `app/engine/adapters.py` and return `BusinessRecord` objects. The current stack demonstrates:

- `google_places`
- `overture`
- `mapbox_search`

To add a provider:

1. Create a new adapter class extending `ProviderAdapter`.
2. Normalize fields into the shared `BusinessRecord` contract.
3. Preserve provider payload details in `metadata` for provenance.
4. Add the adapter to `adapter_stack()`.
5. Re-run validation to confirm reconciliation and scoring still pass.

