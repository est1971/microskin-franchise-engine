# Sandbox Validation Log

Validation runs executed in sandbox mode with recursive repair expectations.

## Calibration importer

- Command: `/Users/davidrobinson/Documents/Playground/.venv/bin/python scripts/import_calibration.py`
- Exit code: `0`

```text

```

## Sandbox smoke app

- Command: `/Users/davidrobinson/Documents/Playground/.venv/bin/python scripts/smoke_app.py`
- Exit code: `0`

```text
Smoke OK: territory-cluster-us-new-york-us-ny-manhattan-1
```

## Pytest

- Command: `/Users/davidrobinson/Documents/Playground/.venv/bin/pytest`
- Exit code: `0`

```text
============================= test session starts ==============================
platform darwin -- Python 3.14.0, pytest-9.0.3, pluggy-1.6.0
rootdir: /Users/davidrobinson/Documents/Playground
configfile: pyproject.toml
testpaths: tests
plugins: asyncio-1.3.0, anyio-4.13.0
asyncio: mode=Mode.AUTO, debug=False, asyncio_default_fixture_loop_scope=None, asyncio_default_test_loop_scope=function
collected 8 items

tests/integration/test_api.py ...                                        [ 37%]
tests/integration/test_pipeline.py ..                                    [ 62%]
tests/ui/test_ui_contract.py .                                           [ 75%]
tests/unit/test_scoring.py .                                             [ 87%]
tests/unit/test_validation.py .                                          [100%]

============================== 8 passed in 0.57s ===============================
```

## Guardian Completion Event

- Critical validation status: `PASS`
- End-to-end sandbox flow executed.
