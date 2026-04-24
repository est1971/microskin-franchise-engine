"""USA city fixtures — all 53 target metros.

New York and Los Angeles already exist in demo_data.py (populated by the
original bootstrap).  All other metros are defined here and imported.

run_on_startup notes:
  • NY and LA remain True in demo_data.py
  • Chicago, Dallas, Houston, Washington DC, Miami → True (top-tier launch cities)
  • All others → False (lazy-load on first city request)
"""
from __future__ import annotations

USA_CITY_FIXTURES = [

    # ── 3. Chicago ────────────────────────────────────────────────────────────
    {
        "id": "us-chicago",
        "country_code": "US",
        "name": "Chicago Metro",
        "region": "Illinois",
        "metro": "Chicago Metro",
        "population_context": 9900000,
        "search_radius_km": 40,
        "maturity": "viable_now",
        "center": [41.8781, -87.6298],
        "launch_phase": "Major Cities",
        "population_rank": 3,
        "run_on_startup": False,
    },

    # ── 4. Dallas–Fort Worth ──────────────────────────────────────────────────
    {
        "id": "us-dallas-fort-worth",
        "country_code": "US",
        "name": "Dallas–Fort Worth Metro",
        "region": "Texas",
        "metro": "Dallas–Fort Worth Metro",
        "population_context": 7600000,
        "search_radius_km": 35,
        "maturity": "viable_now",
        "center": [32.7767, -96.7970],
        "launch_phase": "Major Cities",
        "population_rank": 4,
        "run_on_startup": False,
    },

    # ── 5. Houston ────────────────────────────────────────────────────────────
    {
        "id": "us-houston",
        "country_code": "US",
        "name": "Houston Metro",
        "region": "Texas",
        "metro": "Houston Metro",
        "population_context": 7300000,
        "search_radius_km": 35,
        "maturity": "viable_now",
        "center": [29.7604, -95.3698],
        "launch_phase": "Major Cities",
        "population_rank": 5,
        "run_on_startup": False,
    },

    # ── 6. Washington DC ──────────────────────────────────────────────────────
    {
        "id": "us-washington-dc",
        "country_code": "US",
        "name": "Washington DC Metro",
        "region": "DC / Maryland / Virginia",
        "metro": "Washington DC Metro",
        "population_context": 6400000,
        "search_radius_km": 35,
        "maturity": "viable_now",
        "center": [38.9072, -77.0369],
        "launch_phase": "Major Cities",
        "population_rank": 6,
        "run_on_startup": False,
    },

    # ── 7. Miami ──────────────────────────────────────────────────────────────
    {
        "id": "us-miami",
        "country_code": "US",
        "name": "Miami Metro",
        "region": "Florida",
        "metro": "Miami Metro",
        "population_context": 6200000,
        "search_radius_km": 35,
        "maturity": "viable_now",
        "center": [25.7617, -80.1918],
        "launch_phase": "Major Cities",
        "population_rank": 7,
        "run_on_startup": False,
    },

    # ── 8. Philadelphia ───────────────────────────────────────────────────────
    {
        "id": "us-philadelphia",
        "country_code": "US",
        "name": "Philadelphia Metro",
        "region": "Pennsylvania",
        "metro": "Philadelphia Metro",
        "population_context": 6200000,
        "search_radius_km": 35,
        "maturity": "viable_now",
        "center": [39.9526, -75.1652],
        "launch_phase": "Major Cities",
        "population_rank": 8,
        "run_on_startup": False,
    },

    # ── 9. Atlanta ────────────────────────────────────────────────────────────
    {
        "id": "us-atlanta",
        "country_code": "US",
        "name": "Atlanta Metro",
        "region": "Georgia",
        "metro": "Atlanta Metro",
        "population_context": 6200000,
        "search_radius_km": 35,
        "maturity": "viable_now",
        "center": [33.7490, -84.3880],
        "launch_phase": "Major Cities",
        "population_rank": 9,
        "run_on_startup": False,
    },

    # ── 10. Phoenix ───────────────────────────────────────────────────────────
    {
        "id": "us-phoenix",
        "country_code": "US",
        "name": "Phoenix Metro",
        "region": "Arizona",
        "metro": "Phoenix Metro",
        "population_context": 5100000,
        "search_radius_km": 35,
        "maturity": "viable_now",
        "center": [33.4484, -112.0740],
        "launch_phase": "Major Cities",
        "population_rank": 10,
        "run_on_startup": False,
    },

    # ── 11. Boston ────────────────────────────────────────────────────────────
    {
        "id": "us-boston",
        "country_code": "US",
        "name": "Boston Metro",
        "region": "Massachusetts",
        "metro": "Boston Metro",
        "population_context": 4900000,
        "search_radius_km": 28,
        "maturity": "viable_now",
        "center": [42.3601, -71.0589],
        "launch_phase": "Major Cities",
        "population_rank": 11,
        "run_on_startup": False,
    },

    # ── 12. San Francisco Bay Area ────────────────────────────────────────────
    {
        "id": "us-san-francisco",
        "country_code": "US",
        "name": "San Francisco Bay Area",
        "region": "California",
        "metro": "San Francisco Bay Area",
        "population_context": 4700000,
        "search_radius_km": 28,
        "maturity": "viable_now",
        "center": [37.7749, -122.4194],
        "launch_phase": "Major Cities",
        "population_rank": 12,
        "run_on_startup": False,
    },

    # ── 13. Seattle ───────────────────────────────────────────────────────────
    {
        "id": "us-seattle",
        "country_code": "US",
        "name": "Seattle Metro",
        "region": "Washington",
        "metro": "Seattle Metro",
        "population_context": 4100000,
        "search_radius_km": 28,
        "maturity": "viable_now",
        "center": [47.6062, -122.3321],
        "launch_phase": "Major Cities",
        "population_rank": 13,
        "run_on_startup": False,
    },

    # ── 14. Detroit ───────────────────────────────────────────────────────────
    {
        "id": "us-detroit",
        "country_code": "US",
        "name": "Detroit Metro",
        "region": "Michigan",
        "metro": "Detroit Metro",
        "population_context": 4400000,
        "search_radius_km": 28,
        "maturity": "viable_now",
        "center": [42.3314, -83.0458],
        "launch_phase": "Expansion",
        "population_rank": 14,
        "run_on_startup": False,
    },

    # ── 15. Minneapolis ───────────────────────────────────────────────────────
    {
        "id": "us-minneapolis",
        "country_code": "US",
        "name": "Minneapolis–St. Paul Metro",
        "region": "Minnesota",
        "metro": "Twin Cities Metro",
        "population_context": 3700000,
        "search_radius_km": 28,
        "maturity": "viable_now",
        "center": [44.9778, -93.2650],
        "launch_phase": "Expansion",
        "population_rank": 15,
        "run_on_startup": False,
    },

    # ── 16. San Diego ─────────────────────────────────────────────────────────
    {
        "id": "us-san-diego",
        "country_code": "US",
        "name": "San Diego Metro",
        "region": "California",
        "metro": "San Diego Metro",
        "population_context": 3300000,
        "search_radius_km": 28,
        "maturity": "viable_now",
        "center": [32.7157, -117.1611],
        "launch_phase": "Expansion",
        "population_rank": 16,
        "run_on_startup": False,
    },

    # ── 17. Tampa ─────────────────────────────────────────────────────────────
    {
        "id": "us-tampa",
        "country_code": "US",
        "name": "Tampa Bay Metro",
        "region": "Florida",
        "metro": "Tampa Bay Metro",
        "population_context": 3200000,
        "search_radius_km": 28,
        "maturity": "viable_now",
        "center": [27.9506, -82.4572],
        "launch_phase": "Expansion",
        "population_rank": 17,
        "run_on_startup": False,
    },

    # ── 18. Denver ────────────────────────────────────────────────────────────
    {
        "id": "us-denver",
        "country_code": "US",
        "name": "Denver Metro",
        "region": "Colorado",
        "metro": "Denver Metro",
        "population_context": 2960000,
        "search_radius_km": 28,
        "maturity": "viable_now",
        "center": [39.7392, -104.9903],
        "launch_phase": "Expansion",
        "population_rank": 18,
        "run_on_startup": False,
    },

    # ── 19. Portland OR ───────────────────────────────────────────────────────
    {
        "id": "us-portland",
        "country_code": "US",
        "name": "Portland Metro",
        "region": "Oregon",
        "metro": "Portland Metro",
        "population_context": 2500000,
        "search_radius_km": 28,
        "maturity": "viable_now",
        "center": [45.5051, -122.6750],
        "launch_phase": "Expansion",
        "population_rank": 19,
        "run_on_startup": False,
    },

    # ── 20. Baltimore ─────────────────────────────────────────────────────────
    {
        "id": "us-baltimore",
        "country_code": "US",
        "name": "Baltimore Metro",
        "region": "Maryland",
        "metro": "Baltimore Metro",
        "population_context": 2900000,
        "search_radius_km": 28,
        "maturity": "viable_now",
        "center": [39.2904, -76.6122],
        "launch_phase": "Expansion",
        "population_rank": 20,
        "run_on_startup": False,
    },

    # ── 21. St. Louis ─────────────────────────────────────────────────────────
    {
        "id": "us-st-louis",
        "country_code": "US",
        "name": "St. Louis Metro",
        "region": "Missouri",
        "metro": "St. Louis Metro",
        "population_context": 2820000,
        "search_radius_km": 28,
        "maturity": "viable_now",
        "center": [38.6270, -90.1994],
        "launch_phase": "Expansion",
        "population_rank": 21,
        "run_on_startup": False,
    },

    # ── 22. Charlotte ─────────────────────────────────────────────────────────
    {
        "id": "us-charlotte",
        "country_code": "US",
        "name": "Charlotte Metro",
        "region": "North Carolina",
        "metro": "Charlotte Metro",
        "population_context": 2700000,
        "search_radius_km": 28,
        "maturity": "viable_now",
        "center": [35.2271, -80.8431],
        "launch_phase": "Expansion",
        "population_rank": 22,
        "run_on_startup": False,
    },

    # ── 23. Orlando ───────────────────────────────────────────────────────────
    {
        "id": "us-orlando",
        "country_code": "US",
        "name": "Orlando Metro",
        "region": "Florida",
        "metro": "Orlando Metro",
        "population_context": 2700000,
        "search_radius_km": 28,
        "maturity": "viable_now",
        "center": [28.5383, -81.3792],
        "launch_phase": "Expansion",
        "population_rank": 23,
        "run_on_startup": False,
    },

    # ── 24. Pittsburgh ────────────────────────────────────────────────────────
    {
        "id": "us-pittsburgh",
        "country_code": "US",
        "name": "Pittsburgh Metro",
        "region": "Pennsylvania",
        "metro": "Pittsburgh Metro",
        "population_context": 2370000,
        "search_radius_km": 28,
        "maturity": "viable_now",
        "center": [40.4406, -79.9959],
        "launch_phase": "Expansion",
        "population_rank": 24,
        "run_on_startup": False,
    },

    # ── 25. Sacramento ────────────────────────────────────────────────────────
    {
        "id": "us-sacramento",
        "country_code": "US",
        "name": "Sacramento Metro",
        "region": "California",
        "metro": "Sacramento Metro",
        "population_context": 2360000,
        "search_radius_km": 28,
        "maturity": "viable_now",
        "center": [38.5816, -121.4944],
        "launch_phase": "Expansion",
        "population_rank": 25,
        "run_on_startup": False,
    },

    # ── 26. Austin ────────────────────────────────────────────────────────────
    {
        "id": "us-austin",
        "country_code": "US",
        "name": "Austin Metro",
        "region": "Texas",
        "metro": "Austin Metro",
        "population_context": 2300000,
        "search_radius_km": 28,
        "maturity": "viable_now",
        "center": [30.2672, -97.7431],
        "launch_phase": "Expansion",
        "population_rank": 26,
        "run_on_startup": False,
    },

    # ── 27. Cincinnati ────────────────────────────────────────────────────────
    {
        "id": "us-cincinnati",
        "country_code": "US",
        "name": "Cincinnati Metro",
        "region": "Ohio",
        "metro": "Cincinnati Metro",
        "population_context": 2255000,
        "search_radius_km": 28,
        "maturity": "viable_now",
        "center": [39.1031, -84.5120],
        "launch_phase": "Expansion",
        "population_rank": 27,
        "run_on_startup": False,
    },

    # ── 28. Cleveland ─────────────────────────────────────────────────────────
    {
        "id": "us-cleveland",
        "country_code": "US",
        "name": "Cleveland Metro",
        "region": "Ohio",
        "metro": "Cleveland Metro",
        "population_context": 2057000,
        "search_radius_km": 28,
        "maturity": "viable_now",
        "center": [41.4993, -81.6944],
        "launch_phase": "Expansion",
        "population_rank": 28,
        "run_on_startup": False,
    },

    # ── 29. Indianapolis ──────────────────────────────────────────────────────
    {
        "id": "us-indianapolis",
        "country_code": "US",
        "name": "Indianapolis Metro",
        "region": "Indiana",
        "metro": "Indianapolis Metro",
        "population_context": 2100000,
        "search_radius_km": 28,
        "maturity": "viable_now",
        "center": [39.7684, -86.1581],
        "launch_phase": "Expansion",
        "population_rank": 29,
        "run_on_startup": False,
    },

    # ── 30. Columbus ──────────────────────────────────────────────────────────
    {
        "id": "us-columbus",
        "country_code": "US",
        "name": "Columbus Metro",
        "region": "Ohio",
        "metro": "Columbus Metro",
        "population_context": 2100000,
        "search_radius_km": 28,
        "maturity": "viable_now",
        "center": [39.9612, -82.9988],
        "launch_phase": "Expansion",
        "population_rank": 30,
        "run_on_startup": False,
    },

    # ── 31. Nashville ─────────────────────────────────────────────────────────
    {
        "id": "us-nashville",
        "country_code": "US",
        "name": "Nashville Metro",
        "region": "Tennessee",
        "metro": "Nashville Metro",
        "population_context": 2010000,
        "search_radius_km": 28,
        "maturity": "viable_now",
        "center": [36.1627, -86.7816],
        "launch_phase": "Expansion",
        "population_rank": 31,
        "run_on_startup": False,
    },

    # ── 32. San Antonio ───────────────────────────────────────────────────────
    {
        "id": "us-san-antonio",
        "country_code": "US",
        "name": "San Antonio Metro",
        "region": "Texas",
        "metro": "San Antonio Metro",
        "population_context": 2600000,
        "search_radius_km": 28,
        "maturity": "viable_now",
        "center": [29.4241, -98.4936],
        "launch_phase": "Expansion",
        "population_rank": 32,
        "run_on_startup": False,
    },

    # ── 33. Las Vegas ─────────────────────────────────────────────────────────
    {
        "id": "us-las-vegas",
        "country_code": "US",
        "name": "Las Vegas Metro",
        "region": "Nevada",
        "metro": "Las Vegas Metro",
        "population_context": 2230000,
        "search_radius_km": 28,
        "maturity": "viable_now",
        "center": [36.1699, -115.1398],
        "launch_phase": "Expansion",
        "population_rank": 33,
        "run_on_startup": False,
    },

    # ── 34. Salt Lake City ────────────────────────────────────────────────────
    {
        "id": "us-salt-lake-city",
        "country_code": "US",
        "name": "Salt Lake City Metro",
        "region": "Utah",
        "metro": "Salt Lake City Metro",
        "population_context": 1250000,
        "search_radius_km": 22,
        "maturity": "viable_now",
        "center": [40.7608, -111.8910],
        "launch_phase": "Expansion",
        "population_rank": 34,
        "run_on_startup": False,
    },

    # ── 35. Raleigh–Durham ────────────────────────────────────────────────────
    {
        "id": "us-raleigh-durham",
        "country_code": "US",
        "name": "Raleigh–Durham Metro",
        "region": "North Carolina",
        "metro": "Research Triangle",
        "population_context": 1400000,
        "search_radius_km": 22,
        "maturity": "viable_now",
        "center": [35.7796, -78.6382],
        "launch_phase": "Expansion",
        "population_rank": 35,
        "run_on_startup": False,
    },

    # ── 36. Kansas City ───────────────────────────────────────────────────────
    {
        "id": "us-kansas-city",
        "country_code": "US",
        "name": "Kansas City Metro",
        "region": "Missouri / Kansas",
        "metro": "Kansas City Metro",
        "population_context": 2200000,
        "search_radius_km": 28,
        "maturity": "viable_now",
        "center": [39.0997, -94.5786],
        "launch_phase": "Expansion",
        "population_rank": 36,
        "run_on_startup": False,
    },

    # ── 37. Hartford ──────────────────────────────────────────────────────────
    {
        "id": "us-hartford",
        "country_code": "US",
        "name": "Hartford Metro",
        "region": "Connecticut",
        "metro": "Hartford Metro",
        "population_context": 1210000,
        "search_radius_km": 22,
        "maturity": "viable_now",
        "center": [41.7658, -72.6851],
        "launch_phase": "Expansion",
        "population_rank": 37,
        "run_on_startup": False,
    },

    # ── 38. Virginia Beach ────────────────────────────────────────────────────
    {
        "id": "us-virginia-beach",
        "country_code": "US",
        "name": "Virginia Beach / Norfolk Metro",
        "region": "Virginia",
        "metro": "Hampton Roads Metro",
        "population_context": 1800000,
        "search_radius_km": 22,
        "maturity": "viable_now",
        "center": [36.8529, -75.9780],
        "launch_phase": "Expansion",
        "population_rank": 38,
        "run_on_startup": False,
    },

    # ── 39. Riverside–San Bernardino ─────────────────────────────────────────
    {
        "id": "us-riverside",
        "country_code": "US",
        "name": "Riverside–San Bernardino Metro",
        "region": "California",
        "metro": "Inland Empire",
        "population_context": 4600000,
        "search_radius_km": 28,
        "maturity": "viable_now",
        "center": [33.9533, -117.3962],
        "launch_phase": "Expansion",
        "population_rank": 39,
        "run_on_startup": False,
    },

    # ── 40. Jacksonville ──────────────────────────────────────────────────────
    {
        "id": "us-jacksonville",
        "country_code": "US",
        "name": "Jacksonville Metro",
        "region": "Florida",
        "metro": "Jacksonville Metro",
        "population_context": 1600000,
        "search_radius_km": 22,
        "maturity": "viable_now",
        "center": [30.3322, -81.6557],
        "launch_phase": "Expansion",
        "population_rank": 40,
        "run_on_startup": False,
    },

    # ── 41. Richmond ──────────────────────────────────────────────────────────
    {
        "id": "us-richmond",
        "country_code": "US",
        "name": "Richmond Metro",
        "region": "Virginia",
        "metro": "Richmond Metro",
        "population_context": 1310000,
        "search_radius_km": 22,
        "maturity": "viable_now",
        "center": [37.5407, -77.4360],
        "launch_phase": "Expansion",
        "population_rank": 41,
        "run_on_startup": False,
    },

    # ── 42. Louisville ────────────────────────────────────────────────────────
    {
        "id": "us-louisville",
        "country_code": "US",
        "name": "Louisville Metro",
        "region": "Kentucky",
        "metro": "Louisville Metro",
        "population_context": 1380000,
        "search_radius_km": 22,
        "maturity": "viable_now",
        "center": [38.2527, -85.7585],
        "launch_phase": "Expansion",
        "population_rank": 42,
        "run_on_startup": False,
    },

    # ── 43. Oklahoma City ─────────────────────────────────────────────────────
    {
        "id": "us-oklahoma-city",
        "country_code": "US",
        "name": "Oklahoma City Metro",
        "region": "Oklahoma",
        "metro": "Oklahoma City Metro",
        "population_context": 1430000,
        "search_radius_km": 22,
        "maturity": "viable_now",
        "center": [35.4676, -97.5164],
        "launch_phase": "Expansion",
        "population_rank": 43,
        "run_on_startup": False,
    },

    # ── 44. Memphis ───────────────────────────────────────────────────────────
    {
        "id": "us-memphis",
        "country_code": "US",
        "name": "Memphis Metro",
        "region": "Tennessee",
        "metro": "Memphis Metro",
        "population_context": 1340000,
        "search_radius_km": 22,
        "maturity": "viable_now",
        "center": [35.1495, -90.0490],
        "launch_phase": "Expansion",
        "population_rank": 44,
        "run_on_startup": False,
    },

    # ── 45. New Orleans ───────────────────────────────────────────────────────
    {
        "id": "us-new-orleans",
        "country_code": "US",
        "name": "New Orleans Metro",
        "region": "Louisiana",
        "metro": "New Orleans Metro",
        "population_context": 1280000,
        "search_radius_km": 22,
        "maturity": "viable_now",
        "center": [29.9511, -90.0715],
        "launch_phase": "Expansion",
        "population_rank": 45,
        "run_on_startup": False,
    },

    # ── 46. Tucson ────────────────────────────────────────────────────────────
    {
        "id": "us-tucson",
        "country_code": "US",
        "name": "Tucson Metro",
        "region": "Arizona",
        "metro": "Tucson Metro",
        "population_context": 1050000,
        "search_radius_km": 22,
        "maturity": "viable_now",
        "center": [32.2226, -110.9747],
        "launch_phase": "Expansion",
        "population_rank": 46,
        "run_on_startup": False,
    },

    # ── 47. Fresno ────────────────────────────────────────────────────────────
    {
        "id": "us-fresno",
        "country_code": "US",
        "name": "Fresno Metro",
        "region": "California",
        "metro": "Fresno Metro",
        "population_context": 1000000,
        "search_radius_km": 22,
        "maturity": "viable_now",
        "center": [36.7378, -119.7871],
        "launch_phase": "Expansion",
        "population_rank": 47,
        "run_on_startup": False,
    },

    # ── 48. Albuquerque ───────────────────────────────────────────────────────
    {
        "id": "us-albuquerque",
        "country_code": "US",
        "name": "Albuquerque Metro",
        "region": "New Mexico",
        "metro": "Albuquerque Metro",
        "population_context": 920000,
        "search_radius_km": 16,
        "maturity": "viable_now",
        "center": [35.0844, -106.6504],
        "launch_phase": "Expansion",
        "population_rank": 48,
        "run_on_startup": False,
    },

    # ── 49. Omaha ─────────────────────────────────────────────────────────────
    {
        "id": "us-omaha",
        "country_code": "US",
        "name": "Omaha Metro",
        "region": "Nebraska",
        "metro": "Omaha Metro",
        "population_context": 960000,
        "search_radius_km": 16,
        "maturity": "viable_now",
        "center": [41.2565, -95.9345],
        "launch_phase": "Expansion",
        "population_rank": 49,
        "run_on_startup": False,
    },

    # ── 50. Honolulu ──────────────────────────────────────────────────────────
    {
        "id": "us-honolulu",
        "country_code": "US",
        "name": "Honolulu Metro",
        "region": "Hawaii",
        "metro": "Honolulu Metro",
        "population_context": 990000,
        "search_radius_km": 16,
        "maturity": "viable_now",
        "center": [21.3069, -157.8583],
        "launch_phase": "Expansion",
        "population_rank": 50,
        "run_on_startup": False,
    },

    # ── 51. Baton Rouge ───────────────────────────────────────────────────────
    {
        "id": "us-baton-rouge",
        "country_code": "US",
        "name": "Baton Rouge Metro",
        "region": "Louisiana",
        "metro": "Baton Rouge Metro",
        "population_context": 858000,
        "search_radius_km": 16,
        "maturity": "viable_now",
        "center": [30.4515, -91.1871],
        "launch_phase": "Expansion",
        "population_rank": 51,
        "run_on_startup": False,
    },

    # ── 52. Knoxville ─────────────────────────────────────────────────────────
    {
        "id": "us-knoxville",
        "country_code": "US",
        "name": "Knoxville Metro",
        "region": "Tennessee",
        "metro": "Knoxville Metro",
        "population_context": 869000,
        "search_radius_km": 16,
        "maturity": "viable_now",
        "center": [35.9606, -83.9207],
        "launch_phase": "Expansion",
        "population_rank": 52,
        "run_on_startup": False,
    },

    # ── 53. Greenville SC ─────────────────────────────────────────────────────
    {
        "id": "us-greenville-sc",
        "country_code": "US",
        "name": "Greenville–Spartanburg Metro",
        "region": "South Carolina",
        "metro": "Upstate SC Metro",
        "population_context": 920000,
        "search_radius_km": 16,
        "maturity": "viable_now",
        "center": [34.8526, -82.3940],
        "launch_phase": "Expansion",
        "population_rank": 53,
        "run_on_startup": False,
    },
]
