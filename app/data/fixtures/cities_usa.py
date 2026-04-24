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
        "maturity": "viable_now",
        "center": [41.8781, -87.6298],
        "launch_phase": "Major Cities",
        "population_rank": 3,
        "run_on_startup": False,
        "cores": [
            {"id": "us-chi-gold-coast",   "name": "Gold Coast / Lincoln Park", "center": [41.9120, -87.6366], "corridors": ["Rush Street", "Oak Street", "Lincoln Park Medical Mile"]},
            {"id": "us-chi-river-north",  "name": "River North / Streeterville", "center": [41.8934, -87.6285], "corridors": ["Michigan Avenue", "Magnificent Mile", "Wacker Drive"]},
            {"id": "us-chi-northside",    "name": "North Side",                 "center": [41.9470, -87.6588], "corridors": ["Lakeview", "Roscoe Village", "Wrigleyville"]},
            {"id": "us-chi-oak-park",     "name": "Oak Park / Western Suburbs", "center": [41.8850, -87.8280], "corridors": ["Oak Park Lake Street", "Naperville Downtown", "Wheaton"]},
            {"id": "us-chi-north-shore",  "name": "North Shore",                "center": [42.0500, -87.6800], "corridors": ["Evanston Dempster", "Wilmette", "Winnetka"]},
        ],
    },

    # ── 4. Dallas–Fort Worth ──────────────────────────────────────────────────
    {
        "id": "us-dallas-fort-worth",
        "country_code": "US",
        "name": "Dallas–Fort Worth Metro",
        "region": "Texas",
        "metro": "Dallas–Fort Worth Metro",
        "population_context": 7600000,
        "maturity": "viable_now",
        "center": [32.7767, -96.7970],
        "launch_phase": "Major Cities",
        "population_rank": 4,
        "run_on_startup": False,
        "cores": [
            {"id": "us-dfw-uptown",    "name": "Uptown Dallas",          "center": [32.7980, -96.8097], "corridors": ["Oak Lawn Avenue", "Cedar Springs", "McKinney Avenue"]},
            {"id": "us-dfw-north",     "name": "North Dallas / Plano",   "center": [33.0198, -96.6989], "corridors": ["Preston Road Medical Corridor", "Legacy West", "Frisco Main"]},
            {"id": "us-dfw-southlake", "name": "Southlake / Keller",     "center": [32.9440, -97.1340], "corridors": ["Southlake Town Square", "Keller Main Street"]},
            {"id": "us-dfw-fort-worth","name": "Fort Worth Cultural",    "center": [32.7555, -97.3308], "corridors": ["Camp Bowie Boulevard", "University Drive", "West 7th"]},
        ],
    },

    # ── 5. Houston ────────────────────────────────────────────────────────────
    {
        "id": "us-houston",
        "country_code": "US",
        "name": "Houston Metro",
        "region": "Texas",
        "metro": "Houston Metro",
        "population_context": 7300000,
        "maturity": "viable_now",
        "center": [29.7604, -95.3698],
        "launch_phase": "Major Cities",
        "population_rank": 5,
        "run_on_startup": False,
        "cores": [
            {"id": "us-hou-galleria",    "name": "Galleria / Uptown",     "center": [29.7368, -95.4613], "corridors": ["Post Oak Boulevard", "Westheimer", "River Oaks Blvd"]},
            {"id": "us-hou-medical",     "name": "Medical Center / Midtown","center": [29.7069, -95.3962], "corridors": ["Main Street Medical", "Greenbriar Drive"]},
            {"id": "us-hou-memorial",    "name": "Memorial / Spring Branch","center": [29.7691, -95.5038], "corridors": ["Memorial Drive", "Spring Branch Gessner"]},
            {"id": "us-hou-the-woodlands","name": "The Woodlands",        "center": [30.1588, -95.4900], "corridors": ["Research Forest Drive", "Market Street", "Woodlands Pkwy"]},
        ],
    },

    # ── 6. Washington DC ──────────────────────────────────────────────────────
    {
        "id": "us-washington-dc",
        "country_code": "US",
        "name": "Washington DC Metro",
        "region": "DC / Maryland / Virginia",
        "metro": "Washington DC Metro",
        "population_context": 6400000,
        "maturity": "viable_now",
        "center": [38.9072, -77.0369],
        "launch_phase": "Major Cities",
        "population_rank": 6,
        "run_on_startup": False,
        "cores": [
            {"id": "us-dc-dupont",       "name": "Dupont Circle / Georgetown", "center": [38.9097, -77.0432], "corridors": ["Connecticut Avenue NW", "M Street NW Georgetown"]},
            {"id": "us-dc-bethesda",     "name": "Bethesda / Chevy Chase",     "center": [38.9847, -77.0947], "corridors": ["Wisconsin Avenue Bethesda", "Old Georgetown Road"]},
            {"id": "us-dc-arlington",    "name": "Arlington / McLean VA",       "center": [38.8814, -77.1057], "corridors": ["Clarendon Corridor", "McLean Tysons"]},
            {"id": "us-dc-reston",       "name": "Reston / Ashburn",           "center": [38.9590, -77.3570], "corridors": ["Reston Town Center", "Ashburn Village Blvd"]},
        ],
    },

    # ── 7. Miami ──────────────────────────────────────────────────────────────
    {
        "id": "us-miami",
        "country_code": "US",
        "name": "Miami Metro",
        "region": "Florida",
        "metro": "Miami Metro",
        "population_context": 6200000,
        "maturity": "viable_now",
        "center": [25.7617, -80.1918],
        "launch_phase": "Major Cities",
        "population_rank": 7,
        "run_on_startup": False,
        "cores": [
            {"id": "us-mia-brickell",    "name": "Brickell / Downtown",   "center": [25.7617, -80.1918], "corridors": ["Brickell Avenue", "Mary Brickell Village"]},
            {"id": "us-mia-south-beach", "name": "South Beach / Mid Beach","center": [25.7900, -80.1300], "corridors": ["Collins Avenue", "Lincoln Road", "Alton Road"]},
            {"id": "us-mia-coral-gables","name": "Coral Gables / Coconut Grove","center": [25.7218, -80.2684], "corridors": ["Miracle Mile", "US-1 Clinic Corridor"]},
            {"id": "us-mia-aventura",    "name": "Aventura / Hallandale",  "center": [25.9558, -80.1393], "corridors": ["Aventura Mall Corridor", "Hallandale Beach Blvd"]},
            {"id": "us-mia-boca",        "name": "Boca Raton / Delray",    "center": [26.3683, -80.1289], "corridors": ["Mizner Park", "Federal Highway Boca", "Atlantic Ave Delray"]},
        ],
    },

    # ── 8. Philadelphia ───────────────────────────────────────────────────────
    {
        "id": "us-philadelphia",
        "country_code": "US",
        "name": "Philadelphia Metro",
        "region": "Pennsylvania",
        "metro": "Philadelphia Metro",
        "population_context": 6200000,
        "maturity": "viable_now",
        "center": [39.9526, -75.1652],
        "launch_phase": "Major Cities",
        "population_rank": 8,
        "run_on_startup": False,
        "cores": [
            {"id": "us-phi-rittenhouse",  "name": "Rittenhouse / Center City",  "center": [39.9490, -75.1730], "corridors": ["Walnut Street", "Rittenhouse Square", "Broad Street Medical"]},
            {"id": "us-phi-main-line",    "name": "Main Line",                   "center": [40.0120, -75.3680], "corridors": ["Lancaster Avenue Main Line", "Ardmore", "Wayne"]},
            {"id": "us-phi-cherry-hill",  "name": "Cherry Hill NJ",              "center": [39.9357, -74.9913], "corridors": ["Haddonfield Road", "Route 70 Clinic Corridor"]},
        ],
    },

    # ── 9. Atlanta ────────────────────────────────────────────────────────────
    {
        "id": "us-atlanta",
        "country_code": "US",
        "name": "Atlanta Metro",
        "region": "Georgia",
        "metro": "Atlanta Metro",
        "population_context": 6200000,
        "maturity": "viable_now",
        "center": [33.7490, -84.3880],
        "launch_phase": "Major Cities",
        "population_rank": 9,
        "run_on_startup": False,
        "cores": [
            {"id": "us-atl-buckhead",    "name": "Buckhead",             "center": [33.8440, -84.3610], "corridors": ["Peachtree Road", "Paces Ferry", "Lenox Road"]},
            {"id": "us-atl-midtown",     "name": "Midtown Atlanta",      "center": [33.7847, -84.3888], "corridors": ["Peachtree Street Midtown", "10th Street"]},
            {"id": "us-atl-alpharetta",  "name": "Alpharetta / Roswell",  "center": [34.0754, -84.2941], "corridors": ["GA-400 Corridor", "Holcomb Bridge Road", "Old Alabama Road"]},
            {"id": "us-atl-sandy-springs","name": "Sandy Springs / Dunwoody","center": [33.9237, -84.3743], "corridors": ["Roswell Road Sandy Springs", "Perimeter Center"]},
        ],
    },

    # ── 10. Phoenix ───────────────────────────────────────────────────────────
    {
        "id": "us-phoenix",
        "country_code": "US",
        "name": "Phoenix Metro",
        "region": "Arizona",
        "metro": "Phoenix Metro",
        "population_context": 5100000,
        "maturity": "viable_now",
        "center": [33.4484, -112.0740],
        "launch_phase": "Major Cities",
        "population_rank": 10,
        "run_on_startup": False,
        "cores": [
            {"id": "us-phx-scottsdale",  "name": "Scottsdale",            "center": [33.4942, -111.9261], "corridors": ["Old Town Scottsdale", "McCormick Ranch", "North Scottsdale Rd"]},
            {"id": "us-phx-biltmore",    "name": "Phoenix Biltmore",      "center": [33.5100, -112.0260], "corridors": ["Camelback Road", "24th Street Corridor"]},
            {"id": "us-phx-chandler",    "name": "Chandler / Gilbert",    "center": [33.3062, -111.8413], "corridors": ["Chandler Fashion Center", "Gilbert Road Clinic Corridor"]},
        ],
    },

    # ── 11. Boston ────────────────────────────────────────────────────────────
    {
        "id": "us-boston",
        "country_code": "US",
        "name": "Boston Metro",
        "region": "Massachusetts",
        "metro": "Boston Metro",
        "population_context": 4900000,
        "maturity": "viable_now",
        "center": [42.3601, -71.0589],
        "launch_phase": "Major Cities",
        "population_rank": 11,
        "run_on_startup": False,
        "cores": [
            {"id": "us-bos-back-bay",     "name": "Back Bay / Beacon Hill",  "center": [42.3505, -71.0844], "corridors": ["Newbury Street", "Commonwealth Avenue", "Boylston Medical"]},
            {"id": "us-bos-chestnut-hill","name": "Chestnut Hill / Newton",  "center": [42.3250, -71.1614], "corridors": ["Hammond Street", "Newton Centre", "Chestnut Hill Ave"]},
            {"id": "us-bos-wellesley",    "name": "Wellesley / Needham",     "center": [42.2975, -71.2936], "corridors": ["Central Street Wellesley", "Highland Avenue Needham"]},
        ],
    },

    # ── 12. San Francisco Bay Area ────────────────────────────────────────────
    {
        "id": "us-san-francisco",
        "country_code": "US",
        "name": "San Francisco Bay Area",
        "region": "California",
        "metro": "San Francisco Bay Area",
        "population_context": 4700000,
        "maturity": "viable_now",
        "center": [37.7749, -122.4194],
        "launch_phase": "Major Cities",
        "population_rank": 12,
        "run_on_startup": False,
        "cores": [
            {"id": "us-sf-union-square",  "name": "Union Square / Pacific Heights","center": [37.7879, -122.4075], "corridors": ["Union Square", "Fillmore Street", "Sacramento Street"]},
            {"id": "us-sf-palo-alto",     "name": "Palo Alto / Menlo Park",        "center": [37.4419, -122.1430], "corridors": ["University Avenue Palo Alto", "El Camino Real", "Sand Hill Road"]},
            {"id": "us-sf-marin",         "name": "Marin County",                  "center": [37.9735, -122.5311], "corridors": ["Throckmorton Avenue Mill Valley", "Sir Francis Drake Blvd"]},
            {"id": "us-sf-walnut-creek",  "name": "Walnut Creek / Danville",       "center": [37.9058, -122.0596], "corridors": ["Broadway Walnut Creek", "Danville Hartz Ave"]},
        ],
    },

    # ── 13. Seattle ───────────────────────────────────────────────────────────
    {
        "id": "us-seattle",
        "country_code": "US",
        "name": "Seattle Metro",
        "region": "Washington",
        "metro": "Seattle Metro",
        "population_context": 4100000,
        "maturity": "viable_now",
        "center": [47.6062, -122.3321],
        "launch_phase": "Major Cities",
        "population_rank": 13,
        "run_on_startup": False,
        "cores": [
            {"id": "us-sea-capitol-hill", "name": "Capitol Hill / First Hill",  "center": [47.6253, -122.3130], "corridors": ["Broadway Capitol Hill", "First Hill Clinic Strip"]},
            {"id": "us-sea-bellevue",     "name": "Bellevue / Kirkland",        "center": [47.6101, -122.2015], "corridors": ["Bellevue Way NE", "NE 8th Street", "Kirkland Downtown"]},
            {"id": "us-sea-mercer-island","name": "Mercer Island / Issaquah",   "center": [47.5707, -122.2221], "corridors": ["Mercer Island SE 27th", "Issaquah Highlands"]},
        ],
    },

    # ── 14. Detroit ───────────────────────────────────────────────────────────
    {
        "id": "us-detroit",
        "country_code": "US",
        "name": "Detroit Metro",
        "region": "Michigan",
        "metro": "Detroit Metro",
        "population_context": 4400000,
        "maturity": "viable_now",
        "center": [42.3314, -83.0458],
        "launch_phase": "Expansion",
        "population_rank": 14,
        "run_on_startup": False,
        "cores": [
            {"id": "us-det-birmingham",  "name": "Birmingham / Troy",    "center": [42.5467, -83.2113], "corridors": ["Woodward Avenue Birmingham", "Big Beaver Road Troy"]},
            {"id": "us-det-royal-oak",   "name": "Royal Oak / Ferndale", "center": [42.4895, -83.1446], "corridors": ["Woodward Royal Oak", "Main Street Royal Oak"]},
            {"id": "us-det-ann-arbor",   "name": "Ann Arbor",            "center": [42.2808, -83.7430], "corridors": ["Main Street Ann Arbor", "State Street Medical District"]},
        ],
    },

    # ── 15. Minneapolis ───────────────────────────────────────────────────────
    {
        "id": "us-minneapolis",
        "country_code": "US",
        "name": "Minneapolis–St. Paul Metro",
        "region": "Minnesota",
        "metro": "Twin Cities Metro",
        "population_context": 3700000,
        "maturity": "viable_now",
        "center": [44.9778, -93.2650],
        "launch_phase": "Expansion",
        "population_rank": 15,
        "run_on_startup": False,
        "cores": [
            {"id": "us-msp-uptown",      "name": "Uptown / Edina",       "center": [44.9483, -93.2991], "corridors": ["Hennepin Avenue Uptown", "France Avenue Edina"]},
            {"id": "us-msp-wayzata",     "name": "Wayzata / Plymouth",   "center": [44.9740, -93.5149], "corridors": ["Wayzata Main Street", "Plymouth Road Clinic Corridor"]},
            {"id": "us-msp-woodbury",    "name": "Woodbury / Eagan",     "center": [44.9239, -92.9596], "corridors": ["Valley Creek Road", "Diffley Road Eagan"]},
        ],
    },

    # ── 16. San Diego ─────────────────────────────────────────────────────────
    {
        "id": "us-san-diego",
        "country_code": "US",
        "name": "San Diego Metro",
        "region": "California",
        "metro": "San Diego Metro",
        "population_context": 3300000,
        "maturity": "viable_now",
        "center": [32.7157, -117.1611],
        "launch_phase": "Expansion",
        "population_rank": 16,
        "run_on_startup": False,
        "cores": [
            {"id": "us-sd-la-jolla",     "name": "La Jolla / UTC",       "center": [32.8350, -117.2730], "corridors": ["Prospect Street La Jolla", "UTC Genesee Avenue"]},
            {"id": "us-sd-del-mar",      "name": "Del Mar / Rancho Santa Fe","center": [32.9595, -117.2653], "corridors": ["Del Mar Heights", "Rancho Santa Fe Road"]},
            {"id": "us-sd-downtown",     "name": "Downtown / Hillcrest", "center": [32.7321, -117.1494], "corridors": ["University Avenue Hillcrest", "5th Ave Gaslamp"]},
        ],
    },

    # ── 17. Tampa ─────────────────────────────────────────────────────────────
    {
        "id": "us-tampa",
        "country_code": "US",
        "name": "Tampa Bay Metro",
        "region": "Florida",
        "metro": "Tampa Bay Metro",
        "population_context": 3200000,
        "maturity": "viable_now",
        "center": [27.9506, -82.4572],
        "launch_phase": "Expansion",
        "population_rank": 17,
        "run_on_startup": False,
        "cores": [
            {"id": "us-tpa-south-tampa",  "name": "South Tampa",          "center": [27.9203, -82.4764], "corridors": ["MacDill Avenue", "South Howard Avenue", "Bayshore Boulevard"]},
            {"id": "us-tpa-st-pete",      "name": "St. Petersburg",       "center": [27.7676, -82.6403], "corridors": ["Central Avenue St Pete", "Tyrone Area"]},
            {"id": "us-tpa-clearwater",   "name": "Clearwater / Dunedin",  "center": [27.9654, -82.8001], "corridors": ["Cleveland Street Clearwater", "Alternate 19"]},
        ],
    },

    # ── 18. Denver ────────────────────────────────────────────────────────────
    {
        "id": "us-denver",
        "country_code": "US",
        "name": "Denver Metro",
        "region": "Colorado",
        "metro": "Denver Metro",
        "population_context": 2960000,
        "maturity": "viable_now",
        "center": [39.7392, -104.9903],
        "launch_phase": "Expansion",
        "population_rank": 18,
        "run_on_startup": False,
        "cores": [
            {"id": "us-den-cherry-creek", "name": "Cherry Creek",          "center": [39.7148, -104.9520], "corridors": ["Cherry Creek Drive", "1st Avenue Clinic Strip"]},
            {"id": "us-den-highlands",    "name": "Highlands / LoHi",      "center": [39.7634, -105.0090], "corridors": ["32nd Avenue", "Tennyson Street"]},
            {"id": "us-den-tech-center",  "name": "DTC / Greenwood Village","center": [39.6137, -104.8897], "corridors": ["Orchard Road", "Arapahoe Road DTC"]},
        ],
    },

    # ── 19. Portland OR ───────────────────────────────────────────────────────
    {
        "id": "us-portland",
        "country_code": "US",
        "name": "Portland Metro",
        "region": "Oregon",
        "metro": "Portland Metro",
        "population_context": 2500000,
        "maturity": "viable_now",
        "center": [45.5051, -122.6750],
        "launch_phase": "Expansion",
        "population_rank": 19,
        "run_on_startup": False,
        "cores": [
            {"id": "us-pdx-pearl",        "name": "Pearl District / NW",   "center": [45.5253, -122.6834], "corridors": ["NW 23rd Avenue", "Hoyt Street", "Pearl District"]},
            {"id": "us-pdx-lake-oswego",  "name": "Lake Oswego",           "center": [45.4212, -122.7061], "corridors": ["State Street Lake Oswego", "A Avenue"]},
            {"id": "us-pdx-beaverton",    "name": "Beaverton / Hillsboro", "center": [45.4871, -122.8037], "corridors": ["Canyon Road Beaverton", "Cedar Hills Blvd"]},
        ],
    },

    # ── 20. Baltimore ─────────────────────────────────────────────────────────
    {
        "id": "us-baltimore",
        "country_code": "US",
        "name": "Baltimore Metro",
        "region": "Maryland",
        "metro": "Baltimore Metro",
        "population_context": 2900000,
        "maturity": "viable_now",
        "center": [39.2904, -76.6122],
        "launch_phase": "Expansion",
        "population_rank": 20,
        "run_on_startup": False,
        "cores": [
            {"id": "us-bal-fed-hill",     "name": "Fed Hill / Harbor East", "center": [39.2820, -76.5980], "corridors": ["Light Street Corridor", "Harbor East"]},
            {"id": "us-bal-towson",       "name": "Towson / Hunt Valley",   "center": [39.4018, -76.6021], "corridors": ["York Road Towson", "Shawan Road Hunt Valley"]},
        ],
    },

    # ── 21. St. Louis ─────────────────────────────────────────────────────────
    {
        "id": "us-st-louis",
        "country_code": "US",
        "name": "St. Louis Metro",
        "region": "Missouri",
        "metro": "St. Louis Metro",
        "population_context": 2820000,
        "maturity": "viable_now",
        "center": [38.6270, -90.1994],
        "launch_phase": "Expansion",
        "population_rank": 21,
        "run_on_startup": False,
        "cores": [
            {"id": "us-stl-clayton",      "name": "Clayton / Ladue",       "center": [38.6473, -90.3242], "corridors": ["Maryland Avenue Clayton", "Ladue Road"]},
            {"id": "us-stl-chesterfield", "name": "Chesterfield",          "center": [38.6631, -90.5771], "corridors": ["Chesterfield Pkwy", "Long Road Clinic Corridor"]},
        ],
    },

    # ── 22. Charlotte ─────────────────────────────────────────────────────────
    {
        "id": "us-charlotte",
        "country_code": "US",
        "name": "Charlotte Metro",
        "region": "North Carolina",
        "metro": "Charlotte Metro",
        "population_context": 2700000,
        "maturity": "viable_now",
        "center": [35.2271, -80.8431],
        "launch_phase": "Expansion",
        "population_rank": 22,
        "run_on_startup": False,
        "cores": [
            {"id": "us-clt-south-park",   "name": "SouthPark",             "center": [35.1601, -80.8423], "corridors": ["Fairview Road", "Sharon Road SouthPark", "Morrison Blvd"]},
            {"id": "us-clt-myers-park",   "name": "Myers Park / Dilworth", "center": [35.2048, -80.8404], "corridors": ["Providence Road", "Selwyn Avenue"]},
            {"id": "us-clt-ballantyne",   "name": "Ballantyne / Pineville","center": [35.0596, -80.8626], "corridors": ["Ballantyne Commons Pkwy", "Pineville Matthews Road"]},
        ],
    },

    # ── 23. Orlando ───────────────────────────────────────────────────────────
    {
        "id": "us-orlando",
        "country_code": "US",
        "name": "Orlando Metro",
        "region": "Florida",
        "metro": "Orlando Metro",
        "population_context": 2700000,
        "maturity": "viable_now",
        "center": [28.5383, -81.3792],
        "launch_phase": "Expansion",
        "population_rank": 23,
        "run_on_startup": False,
        "cores": [
            {"id": "us-orl-dr-phillips",  "name": "Dr. Phillips / Windermere","center": [28.4500, -81.4960], "corridors": ["Sand Lake Road", "Dr Phillips Blvd", "Windermere Road"]},
            {"id": "us-orl-winter-park",  "name": "Winter Park",              "center": [28.5996, -81.3392], "corridors": ["Park Avenue Winter Park", "Fairbanks Avenue"]},
            {"id": "us-orl-lake-nona",    "name": "Lake Nona",                "center": [28.3589, -81.2359], "corridors": ["Narcoossee Road", "Tavistock Lakes Blvd"]},
        ],
    },

    # ── 24. Pittsburgh ────────────────────────────────────────────────────────
    {
        "id": "us-pittsburgh",
        "country_code": "US",
        "name": "Pittsburgh Metro",
        "region": "Pennsylvania",
        "metro": "Pittsburgh Metro",
        "population_context": 2370000,
        "maturity": "viable_now",
        "center": [40.4406, -79.9959],
        "launch_phase": "Expansion",
        "population_rank": 24,
        "run_on_startup": False,
        "cores": [
            {"id": "us-pit-shadyside",    "name": "Shadyside / Squirrel Hill","center": [40.4570, -79.9330], "corridors": ["Walnut Street Shadyside", "Forbes Avenue Squirrel Hill"]},
            {"id": "us-pit-sewickley",    "name": "Sewickley / Fox Chapel",   "center": [40.5414, -80.1831], "corridors": ["Beaver Street Sewickley", "Fox Chapel Road"]},
        ],
    },

    # ── 25. Sacramento ────────────────────────────────────────────────────────
    {
        "id": "us-sacramento",
        "country_code": "US",
        "name": "Sacramento Metro",
        "region": "California",
        "metro": "Sacramento Metro",
        "population_context": 2360000,
        "maturity": "viable_now",
        "center": [38.5816, -121.4944],
        "launch_phase": "Expansion",
        "population_rank": 25,
        "run_on_startup": False,
        "cores": [
            {"id": "us-sac-midtown",      "name": "Midtown Sacramento",    "center": [38.5721, -121.4800], "corridors": ["J Street Midtown", "Broadway Corridor"]},
            {"id": "us-sac-folsom",       "name": "Folsom / El Dorado Hills","center": [38.6780, -121.1761], "corridors": ["East Bidwell Street", "El Dorado Hills Town Center"]},
            {"id": "us-sac-roseville",    "name": "Roseville / Rocklin",   "center": [38.7521, -121.2880], "corridors": ["Douglas Boulevard", "Roseville Galleria Corridor"]},
        ],
    },

    # ── 26. Austin ────────────────────────────────────────────────────────────
    {
        "id": "us-austin",
        "country_code": "US",
        "name": "Austin Metro",
        "region": "Texas",
        "metro": "Austin Metro",
        "population_context": 2300000,
        "maturity": "viable_now",
        "center": [30.2672, -97.7431],
        "launch_phase": "Expansion",
        "population_rank": 26,
        "run_on_startup": False,
        "cores": [
            {"id": "us-aus-west-lake",    "name": "Westlake / Rollingwood","center": [30.2900, -97.8050], "corridors": ["Bee Cave Road", "Capital of Texas Hwy"]},
            {"id": "us-aus-domain",       "name": "The Domain / North Austin","center": [30.4022, -97.7251], "corridors": ["Domain BLVD", "Braker Lane Medical Corridor"]},
            {"id": "us-aus-south-lamar",  "name": "South Lamar / Travis Heights","center": [30.2413, -97.7694], "corridors": ["South Lamar Boulevard", "South Congress Avenue"]},
        ],
    },

    # ── 27. Cincinnati ────────────────────────────────────────────────────────
    {
        "id": "us-cincinnati",
        "country_code": "US",
        "name": "Cincinnati Metro",
        "region": "Ohio",
        "metro": "Cincinnati Metro",
        "population_context": 2255000,
        "maturity": "viable_now",
        "center": [39.1031, -84.5120],
        "launch_phase": "Expansion",
        "population_rank": 27,
        "run_on_startup": False,
        "cores": [
            {"id": "us-cin-hyde-park",    "name": "Hyde Park / Mt. Lookout","center": [39.1498, -84.4366], "corridors": ["Erie Avenue Hyde Park", "Columbia Parkway"]},
            {"id": "us-cin-blue-ash",     "name": "Blue Ash / Kenwood",     "center": [39.2320, -84.3782], "corridors": ["Reed Hartman Highway", "Kenwood Road Corridor"]},
        ],
    },

    # ── 28. Cleveland ─────────────────────────────────────────────────────────
    {
        "id": "us-cleveland",
        "country_code": "US",
        "name": "Cleveland Metro",
        "region": "Ohio",
        "metro": "Cleveland Metro",
        "population_context": 2057000,
        "maturity": "viable_now",
        "center": [41.4993, -81.6944],
        "launch_phase": "Expansion",
        "population_rank": 28,
        "run_on_startup": False,
        "cores": [
            {"id": "us-cle-beachwood",    "name": "Beachwood / Orange",    "center": [41.4647, -81.5133], "corridors": ["Chagrin Boulevard", "Richmond Road Beachwood"]},
            {"id": "us-cle-rocky-river",  "name": "Rocky River / Westlake","center": [41.4792, -81.8400], "corridors": ["Center Ridge Road", "Detroit Road Rocky River"]},
        ],
    },

    # ── 29. Indianapolis ──────────────────────────────────────────────────────
    {
        "id": "us-indianapolis",
        "country_code": "US",
        "name": "Indianapolis Metro",
        "region": "Indiana",
        "metro": "Indianapolis Metro",
        "population_context": 2100000,
        "maturity": "viable_now",
        "center": [39.7684, -86.1581],
        "launch_phase": "Expansion",
        "population_rank": 29,
        "run_on_startup": False,
        "cores": [
            {"id": "us-ind-meridian-north","name": "North Meridian Corridor","center": [39.8790, -86.1506], "corridors": ["Meridian Street North", "86th Street Clinic Strip"]},
            {"id": "us-ind-carmel",       "name": "Carmel / Fishers",      "center": [39.9784, -86.1180], "corridors": ["Carmel Main Street", "116th Street Carmel"]},
        ],
    },

    # ── 30. Columbus ──────────────────────────────────────────────────────────
    {
        "id": "us-columbus",
        "country_code": "US",
        "name": "Columbus Metro",
        "region": "Ohio",
        "metro": "Columbus Metro",
        "population_context": 2100000,
        "maturity": "viable_now",
        "center": [39.9612, -82.9988],
        "launch_phase": "Expansion",
        "population_rank": 30,
        "run_on_startup": False,
        "cores": [
            {"id": "us-col-upper-arlington","name": "Upper Arlington / Dublin","center": [40.0274, -83.0629], "corridors": ["Riverside Drive Upper Arlington", "Bridge Street Dublin"]},
            {"id": "us-col-new-albany",   "name": "New Albany / Gahanna",  "center": [40.0820, -82.8152], "corridors": ["New Albany Village Square", "Mill Run New Albany"]},
        ],
    },

    # ── 31. Nashville ─────────────────────────────────────────────────────────
    {
        "id": "us-nashville",
        "country_code": "US",
        "name": "Nashville Metro",
        "region": "Tennessee",
        "metro": "Nashville Metro",
        "population_context": 2010000,
        "maturity": "viable_now",
        "center": [36.1627, -86.7816],
        "launch_phase": "Expansion",
        "population_rank": 31,
        "run_on_startup": False,
        "cores": [
            {"id": "us-nas-green-hills",  "name": "Green Hills / Belle Meade","center": [36.1104, -86.8182], "corridors": ["Hillsboro Pike", "Richard Jones Road", "Belle Meade Blvd"]},
            {"id": "us-nas-brentwood",    "name": "Brentwood / Franklin",   "center": [35.9983, -86.7828], "corridors": ["Franklin Road Brentwood", "Main Street Franklin"]},
        ],
    },

    # ── 32. San Antonio ───────────────────────────────────────────────────────
    {
        "id": "us-san-antonio",
        "country_code": "US",
        "name": "San Antonio Metro",
        "region": "Texas",
        "metro": "San Antonio Metro",
        "population_context": 2600000,
        "maturity": "viable_now",
        "center": [29.4241, -98.4936],
        "launch_phase": "Expansion",
        "population_rank": 32,
        "run_on_startup": False,
        "cores": [
            {"id": "us-sat-north",        "name": "North San Antonio",     "center": [29.5580, -98.4936], "corridors": ["North Broadway", "Stone Oak Pkwy", "Huebner Road"]},
            {"id": "us-sat-alamo-heights","name": "Alamo Heights / Terrell Hills","center": [29.4826, -98.4556], "corridors": ["Broadway Street", "Austin Highway"]},
        ],
    },

    # ── 33. Las Vegas ─────────────────────────────────────────────────────────
    {
        "id": "us-las-vegas",
        "country_code": "US",
        "name": "Las Vegas Metro",
        "region": "Nevada",
        "metro": "Las Vegas Metro",
        "population_context": 2230000,
        "maturity": "viable_now",
        "center": [36.1699, -115.1398],
        "launch_phase": "Expansion",
        "population_rank": 33,
        "run_on_startup": False,
        "cores": [
            {"id": "us-lv-summerlin",     "name": "Summerlin",              "center": [36.1900, -115.3270], "corridors": ["Rampart Boulevard", "Desert Inn Road", "Summerlin Pkwy"]},
            {"id": "us-lv-henderson",     "name": "Henderson / Green Valley","center": [36.0397, -114.9817], "corridors": ["Green Valley Pkwy", "Stephanie Street Clinic Corridor"]},
            {"id": "us-lv-strip-north",   "name": "Las Vegas Strip / Medical Row","center": [36.1699, -115.1398], "corridors": ["Desert Inn Road Medical Corridor", "Karen Ave"]},
        ],
    },

    # ── 34. Salt Lake City ────────────────────────────────────────────────────
    {
        "id": "us-salt-lake-city",
        "country_code": "US",
        "name": "Salt Lake City Metro",
        "region": "Utah",
        "metro": "Salt Lake City Metro",
        "population_context": 1250000,
        "maturity": "viable_now",
        "center": [40.7608, -111.8910],
        "launch_phase": "Expansion",
        "population_rank": 34,
        "run_on_startup": False,
        "cores": [
            {"id": "us-slc-east-bench",   "name": "East Bench / Sugar House","center": [40.7376, -111.8480], "corridors": ["2100 South Clinic Strip", "1300 East Sugar House"]},
            {"id": "us-slc-murray",       "name": "Murray / Midvale",       "center": [40.6668, -111.8880], "corridors": ["State Street Murray", "Fashion Place Blvd"]},
        ],
    },

    # ── 35. Raleigh–Durham ────────────────────────────────────────────────────
    {
        "id": "us-raleigh-durham",
        "country_code": "US",
        "name": "Raleigh–Durham Metro",
        "region": "North Carolina",
        "metro": "Research Triangle",
        "population_context": 1400000,
        "maturity": "viable_now",
        "center": [35.7796, -78.6382],
        "launch_phase": "Expansion",
        "population_rank": 35,
        "run_on_startup": False,
        "cores": [
            {"id": "us-rdu-north-hills",  "name": "North Hills / Cary",    "center": [35.8509, -78.6270], "corridors": ["Six Forks Road North", "Kildaire Farm Road Cary"]},
            {"id": "us-rdu-chapel-hill",  "name": "Chapel Hill / Carrboro","center": [35.9132, -79.0558], "corridors": ["Franklin Street", "East Franklin Clinic Row"]},
        ],
    },

    # ── 36. Kansas City ───────────────────────────────────────────────────────
    {
        "id": "us-kansas-city",
        "country_code": "US",
        "name": "Kansas City Metro",
        "region": "Missouri / Kansas",
        "metro": "Kansas City Metro",
        "population_context": 2200000,
        "maturity": "viable_now",
        "center": [39.0997, -94.5786],
        "launch_phase": "Expansion",
        "population_rank": 36,
        "run_on_startup": False,
        "cores": [
            {"id": "us-kc-plaza",         "name": "Country Club Plaza / Brookside","center": [39.0406, -94.5905], "corridors": ["Ward Pkwy", "Brookside Boulevard", "47th Street Plaza"]},
            {"id": "us-kc-overland-park", "name": "Overland Park",         "center": [38.9822, -94.6708], "corridors": ["Metcalf Avenue", "Johnson Drive Overland Park"]},
        ],
    },

    # ── 37. Hartford ──────────────────────────────────────────────────────────
    {
        "id": "us-hartford",
        "country_code": "US",
        "name": "Hartford Metro",
        "region": "Connecticut",
        "metro": "Hartford Metro",
        "population_context": 1210000,
        "maturity": "viable_now",
        "center": [41.7658, -72.6851],
        "launch_phase": "Expansion",
        "population_rank": 37,
        "run_on_startup": False,
        "cores": [
            {"id": "us-hfd-west-hartford","name": "West Hartford",          "center": [41.7623, -72.7424], "corridors": ["LaSalle Road West Hartford", "Farmington Avenue Clinic Row"]},
            {"id": "us-hfd-glastonbury",  "name": "Glastonbury / Simsbury","center": [41.7026, -72.6070], "corridors": ["Glastonbury Main Street", "Simsbury Center"]},
        ],
    },

    # ── 38. Virginia Beach ────────────────────────────────────────────────────
    {
        "id": "us-virginia-beach",
        "country_code": "US",
        "name": "Virginia Beach / Norfolk Metro",
        "region": "Virginia",
        "metro": "Hampton Roads Metro",
        "population_context": 1800000,
        "maturity": "viable_now",
        "center": [36.8529, -75.9780],
        "launch_phase": "Expansion",
        "population_rank": 38,
        "run_on_startup": False,
        "cores": [
            {"id": "us-vb-hilltop",       "name": "Virginia Beach Hilltop","center": [36.8585, -76.0170], "corridors": ["Hilltop West Shopping Center", "First Colonial Road"]},
            {"id": "us-vb-chesapeake",    "name": "Chesapeake / Suffolk",  "center": [36.7682, -76.2452], "corridors": ["Greenbrier Pkwy", "Battlefield Blvd South"]},
        ],
    },

    # ── 39. Riverside–San Bernardino ─────────────────────────────────────────
    {
        "id": "us-riverside",
        "country_code": "US",
        "name": "Riverside–San Bernardino Metro",
        "region": "California",
        "metro": "Inland Empire",
        "population_context": 4600000,
        "maturity": "viable_now",
        "center": [33.9533, -117.3962],
        "launch_phase": "Expansion",
        "population_rank": 39,
        "run_on_startup": False,
        "cores": [
            {"id": "us-rie-rancho-cucamonga","name": "Rancho Cucamonga / Upland","center": [34.1064, -117.5931], "corridors": ["Foothill Blvd Rancho", "Haven Avenue Corridor"]},
            {"id": "us-rie-temecula",     "name": "Temecula / Murrieta",   "center": [33.4936, -117.1484], "corridors": ["Temecula Pkwy", "Murrieta Hot Springs Road"]},
        ],
    },

    # ── 40. Jacksonville ──────────────────────────────────────────────────────
    {
        "id": "us-jacksonville",
        "country_code": "US",
        "name": "Jacksonville Metro",
        "region": "Florida",
        "metro": "Jacksonville Metro",
        "population_context": 1600000,
        "maturity": "viable_now",
        "center": [30.3322, -81.6557],
        "launch_phase": "Expansion",
        "population_rank": 40,
        "run_on_startup": False,
        "cores": [
            {"id": "us-jax-san-marco",    "name": "San Marco / Avondale",  "center": [30.3022, -81.6499], "corridors": ["Atlantic Boulevard San Marco", "King Street Avondale"]},
            {"id": "us-jax-ponte-vedra",  "name": "Ponte Vedra / Jax Beach","center": [30.2399, -81.3873], "corridors": ["A1A Clinic Corridor", "Hodges Boulevard"]},
        ],
    },

    # ── 41. Richmond ──────────────────────────────────────────────────────────
    {
        "id": "us-richmond",
        "country_code": "US",
        "name": "Richmond Metro",
        "region": "Virginia",
        "metro": "Richmond Metro",
        "population_context": 1310000,
        "maturity": "viable_now",
        "center": [37.5407, -77.4360],
        "launch_phase": "Expansion",
        "population_rank": 41,
        "run_on_startup": False,
        "cores": [
            {"id": "us-ric-carytown",     "name": "Carytown / Museum District","center": [37.5502, -77.4775], "corridors": ["Cary Street", "Grove Avenue Clinic Strip"]},
            {"id": "us-ric-west-end",     "name": "West End / Short Pump",  "center": [37.6493, -77.6147], "corridors": ["Three Chopt Road", "Short Pump Town Center"]},
        ],
    },

    # ── 42. Louisville ────────────────────────────────────────────────────────
    {
        "id": "us-louisville",
        "country_code": "US",
        "name": "Louisville Metro",
        "region": "Kentucky",
        "metro": "Louisville Metro",
        "population_context": 1380000,
        "maturity": "viable_now",
        "center": [38.2527, -85.7585],
        "launch_phase": "Expansion",
        "population_rank": 42,
        "run_on_startup": False,
        "cores": [
            {"id": "us-lou-st-matthews",  "name": "St. Matthews / Middletown","center": [38.2540, -85.6554], "corridors": ["Shelbyville Road", "Breckinridge Lane Clinic Strip"]},
            {"id": "us-lou-cherokee",     "name": "Cherokee Gardens / Highlands","center": [38.2448, -85.7266], "corridors": ["Bardstown Road Highlands", "Baxter Avenue"]},
        ],
    },

    # ── 43. Oklahoma City ─────────────────────────────────────────────────────
    {
        "id": "us-oklahoma-city",
        "country_code": "US",
        "name": "Oklahoma City Metro",
        "region": "Oklahoma",
        "metro": "Oklahoma City Metro",
        "population_context": 1430000,
        "maturity": "viable_now",
        "center": [35.4676, -97.5164],
        "launch_phase": "Expansion",
        "population_rank": 43,
        "run_on_startup": False,
        "cores": [
            {"id": "us-okc-midtown",      "name": "Midtown / Nichols Hills","center": [35.4904, -97.5322], "corridors": ["Western Avenue Midtown", "63rd Street Nichols Hills"]},
            {"id": "us-okc-edmond",       "name": "Edmond",                "center": [35.6529, -97.4781], "corridors": ["Broadway Edmond", "Danforth Road Clinic Corridor"]},
        ],
    },

    # ── 44. Memphis ───────────────────────────────────────────────────────────
    {
        "id": "us-memphis",
        "country_code": "US",
        "name": "Memphis Metro",
        "region": "Tennessee",
        "metro": "Memphis Metro",
        "population_context": 1340000,
        "maturity": "viable_now",
        "center": [35.1495, -90.0490],
        "launch_phase": "Expansion",
        "population_rank": 44,
        "run_on_startup": False,
        "cores": [
            {"id": "us-mem-east-memphis", "name": "East Memphis / Germantown","center": [35.1298, -89.9213], "corridors": ["Poplar Avenue Medical Mile", "Forest Hill Irene"]},
        ],
    },

    # ── 45. New Orleans ───────────────────────────────────────────────────────
    {
        "id": "us-new-orleans",
        "country_code": "US",
        "name": "New Orleans Metro",
        "region": "Louisiana",
        "metro": "New Orleans Metro",
        "population_context": 1280000,
        "maturity": "viable_now",
        "center": [29.9511, -90.0715],
        "launch_phase": "Expansion",
        "population_rank": 45,
        "run_on_startup": False,
        "cores": [
            {"id": "us-nol-uptown",       "name": "Uptown New Orleans",    "center": [29.9402, -90.1120], "corridors": ["Magazine Street", "Prytania Street Clinic Row"]},
            {"id": "us-nol-metairie",     "name": "Metairie",              "center": [29.9980, -90.1660], "corridors": ["Veterans Memorial Blvd", "Causeway Boulevard"]},
        ],
    },

    # ── 46. Tucson ────────────────────────────────────────────────────────────
    {
        "id": "us-tucson",
        "country_code": "US",
        "name": "Tucson Metro",
        "region": "Arizona",
        "metro": "Tucson Metro",
        "population_context": 1050000,
        "maturity": "viable_now",
        "center": [32.2226, -110.9747],
        "launch_phase": "Expansion",
        "population_rank": 46,
        "run_on_startup": False,
        "cores": [
            {"id": "us-tus-foothills",    "name": "Foothills / Catalina",  "center": [32.3558, -110.9378], "corridors": ["Oracle Road Foothills", "Ina Road Clinic Corridor"]},
        ],
    },

    # ── 47. Fresno ────────────────────────────────────────────────────────────
    {
        "id": "us-fresno",
        "country_code": "US",
        "name": "Fresno Metro",
        "region": "California",
        "metro": "Fresno Metro",
        "population_context": 1000000,
        "maturity": "viable_now",
        "center": [36.7378, -119.7871],
        "launch_phase": "Expansion",
        "population_rank": 47,
        "run_on_startup": False,
        "cores": [
            {"id": "us-fre-fashion-fair",  "name": "Fashion Fair / Clovis","center": [36.7988, -119.8001], "corridors": ["Shaw Avenue Fresno", "Willow / Clovis Clinic Strip"]},
        ],
    },

    # ── 48. Albuquerque ───────────────────────────────────────────────────────
    {
        "id": "us-albuquerque",
        "country_code": "US",
        "name": "Albuquerque Metro",
        "region": "New Mexico",
        "metro": "Albuquerque Metro",
        "population_context": 920000,
        "maturity": "viable_now",
        "center": [35.0844, -106.6504],
        "launch_phase": "Expansion",
        "population_rank": 48,
        "run_on_startup": False,
        "cores": [
            {"id": "us-abq-rio-rancho",   "name": "Rio Rancho / NE Heights","center": [35.2329, -106.6630], "corridors": ["Paseo del Norte", "Unser Blvd Clinic Corridor"]},
        ],
    },

    # ── 49. Omaha ─────────────────────────────────────────────────────────────
    {
        "id": "us-omaha",
        "country_code": "US",
        "name": "Omaha Metro",
        "region": "Nebraska",
        "metro": "Omaha Metro",
        "population_context": 960000,
        "maturity": "viable_now",
        "center": [41.2565, -95.9345],
        "launch_phase": "Expansion",
        "population_rank": 49,
        "run_on_startup": False,
        "cores": [
            {"id": "us-oma-west-omaha",   "name": "West Omaha / Aksarben", "center": [41.2565, -96.0880], "corridors": ["Dodge Street West", "Aksarben Village Drive"]},
        ],
    },

    # ── 50. Honolulu ──────────────────────────────────────────────────────────
    {
        "id": "us-honolulu",
        "country_code": "US",
        "name": "Honolulu Metro",
        "region": "Hawaii",
        "metro": "Honolulu Metro",
        "population_context": 990000,
        "maturity": "viable_now",
        "center": [21.3069, -157.8583],
        "launch_phase": "Expansion",
        "population_rank": 50,
        "run_on_startup": False,
        "cores": [
            {"id": "us-hnl-ala-moana",    "name": "Ala Moana / Kahala",    "center": [21.2929, -157.8420], "corridors": ["Kapiolani Boulevard", "Kahala Mall Corridor"]},
            {"id": "us-hnl-kailua",       "name": "Kailua / Kaneohe",      "center": [21.3927, -157.7392], "corridors": ["Kailua Road", "Kamehameha Highway Kaneohe"]},
        ],
    },

    # ── 51. Baton Rouge ───────────────────────────────────────────────────────
    {
        "id": "us-baton-rouge",
        "country_code": "US",
        "name": "Baton Rouge Metro",
        "region": "Louisiana",
        "metro": "Baton Rouge Metro",
        "population_context": 858000,
        "maturity": "viable_now",
        "center": [30.4515, -91.1871],
        "launch_phase": "Expansion",
        "population_rank": 51,
        "run_on_startup": False,
        "cores": [
            {"id": "us-btr-perkins",      "name": "Perkins Road / Siegen",  "center": [30.3932, -91.1437], "corridors": ["Perkins Road Corridor", "Siegen Lane Clinic Strip"]},
        ],
    },

    # ── 52. Knoxville ─────────────────────────────────────────────────────────
    {
        "id": "us-knoxville",
        "country_code": "US",
        "name": "Knoxville Metro",
        "region": "Tennessee",
        "metro": "Knoxville Metro",
        "population_context": 869000,
        "maturity": "viable_now",
        "center": [35.9606, -83.9207],
        "launch_phase": "Expansion",
        "population_rank": 52,
        "run_on_startup": False,
        "cores": [
            {"id": "us-knx-west-knoxville","name": "West Knoxville / Turkey Creek","center": [35.9262, -84.0828], "corridors": ["Kingston Pike", "Turkey Creek Medical Center"]},
        ],
    },

    # ── 53. Greenville SC ─────────────────────────────────────────────────────
    {
        "id": "us-greenville-sc",
        "country_code": "US",
        "name": "Greenville–Spartanburg Metro",
        "region": "South Carolina",
        "metro": "Upstate SC Metro",
        "population_context": 920000,
        "maturity": "viable_now",
        "center": [34.8526, -82.3940],
        "launch_phase": "Expansion",
        "population_rank": 53,
        "run_on_startup": False,
        "cores": [
            {"id": "us-gvl-downtown",     "name": "Downtown Greenville",   "center": [34.8526, -82.3940], "corridors": ["Main Street Greenville", "Augusta Street Corridor"]},
        ],
    },
]
