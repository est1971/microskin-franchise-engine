"""International city fixtures — UK, Australia, EU, Scandinavia, APAC, MENA, Americas.

run_on_startup:
  • London, Sydney, Paris, Toronto, Bangkok, Kuala Lumpur → True
  • All others → False (lazy-load)
"""
from __future__ import annotations

INTERNATIONAL_CITY_FIXTURES = [

    # ══════════════════════════════════════════════════════════════════════════
    # UNITED KINGDOM
    # ══════════════════════════════════════════════════════════════════════════

    {
        "id": "gb-london",
        "country_code": "GB",
        "name": "London",
        "region": "Greater London",
        "metro": "Greater London",
        "population_context": 9600000,
        "maturity": "viable_now",
        "center": [51.5074, -0.1278],
        "launch_phase": "Foundation",
        "population_rank": 1,
        "run_on_startup": False,
        "cores": [
            {"id": "gb-lon-mayfair",      "name": "Mayfair / Marylebone",    "center": [51.5142, -0.1494], "corridors": ["Harley Street", "Wimpole Street", "New Cavendish Street"]},
            {"id": "gb-lon-chelsea",      "name": "Chelsea / Kensington",    "center": [51.4875, -0.1739], "corridors": ["Kings Road Chelsea", "Fulham Road Clinic Strip", "Brompton Road"]},
            {"id": "gb-lon-canary",       "name": "Canary Wharf / Shoreditch","center": [51.5054, -0.0235], "corridors": ["Canary Wharf South", "Shoreditch High Street", "Hoxton Square"]},
            {"id": "gb-lon-north",        "name": "North London / Hampstead","center": [51.5555, -0.1762], "corridors": ["Hampstead High Street", "Muswell Hill Broadway", "Highgate Village"]},
            {"id": "gb-lon-richmond",     "name": "Richmond / Wimbledon",    "center": [51.4480, -0.3010], "corridors": ["Richmond Hill Clinic Row", "Wimbledon Village", "Putney High Street"]},
            {"id": "gb-lon-city-east",    "name": "City / East London",      "center": [51.5200, -0.0800], "corridors": ["Liverpool Street Clinic Corridor", "Aldgate", "Wapping"]},
        ],
    },

    {
        "id": "gb-manchester",
        "country_code": "GB",
        "name": "Manchester",
        "region": "Greater Manchester",
        "metro": "Greater Manchester",
        "population_context": 2800000,
        "maturity": "viable_now",
        "center": [53.4808, -2.2426],
        "launch_phase": "Major Cities",
        "population_rank": 2,
        "run_on_startup": False,
        "cores": [
            {"id": "gb-man-spinningfields","name": "Spinningfields / Northern Quarter","center": [53.4808, -2.2490], "corridors": ["Deansgate Clinic Strip", "Bridge Street", "King Street"]},
            {"id": "gb-man-didsbury",     "name": "Didsbury / Altrincham",  "center": [53.4046, -2.2379], "corridors": ["Wilmslow Road Didsbury", "Altrincham High Street"]},
            {"id": "gb-man-salford-quays","name": "Salford Quays / Trafford","center": [53.4728, -2.2882], "corridors": ["Trafford Road", "White City Retail Park Corridor"]},
        ],
    },

    {
        "id": "gb-birmingham",
        "country_code": "GB",
        "name": "Birmingham",
        "region": "West Midlands",
        "metro": "West Midlands",
        "population_context": 2700000,
        "maturity": "viable_now",
        "center": [52.4862, -1.8904],
        "launch_phase": "Major Cities",
        "population_rank": 3,
        "run_on_startup": False,
        "cores": [
            {"id": "gb-bmi-edgbaston",    "name": "Edgbaston / Harborne",   "center": [52.4656, -1.9196], "corridors": ["Harley Street Bham (Hagley Road)", "Bristol Road Medical Mile"]},
            {"id": "gb-bmi-solihull",     "name": "Solihull",               "center": [52.4130, -1.7776], "corridors": ["Drury Lane Solihull", "Stratford Road Shirley"]},
            {"id": "gb-bmi-sutton",       "name": "Sutton Coldfield",       "center": [52.5641, -1.8242], "corridors": ["Beeches Road", "Birmingham Road Sutton"]},
        ],
    },

    {
        "id": "gb-glasgow",
        "country_code": "GB",
        "name": "Glasgow",
        "region": "Scotland",
        "metro": "Greater Glasgow",
        "population_context": 1830000,
        "maturity": "viable_now",
        "center": [55.8642, -4.2518],
        "launch_phase": "Major Cities",
        "population_rank": 4,
        "run_on_startup": False,
        "cores": [
            {"id": "gb-gla-west-end",     "name": "West End / Hillhead",    "center": [55.8726, -4.2921], "corridors": ["Byres Road", "Great Western Road Clinic Strip"]},
            {"id": "gb-gla-city-centre",  "name": "City Centre / Finnieston","center": [55.8642, -4.2638], "corridors": ["Sauchiehall Street", "Buchanan Street", "Finnieston"]},
            {"id": "gb-gla-southside",    "name": "Southside / Giffnock",   "center": [55.8090, -4.2729], "corridors": ["Kilmarnock Road", "Clarkston Road Giffnock"]},
        ],
    },

    {
        "id": "gb-leeds",
        "country_code": "GB",
        "name": "Leeds",
        "region": "West Yorkshire",
        "metro": "West Yorkshire",
        "population_context": 1900000,
        "maturity": "viable_now",
        "center": [53.8008, -1.5491],
        "launch_phase": "Major Cities",
        "population_rank": 5,
        "run_on_startup": False,
        "cores": [
            {"id": "gb-lds-headingley",   "name": "Headingley / Chapel Allerton","center": [53.8231, -1.5809], "corridors": ["Otley Road Leeds", "Chapel Allerton Strip"]},
            {"id": "gb-lds-harrogate",    "name": "Harrogate",              "center": [53.9929, -1.5418], "corridors": ["Parliament Street Harrogate", "Cold Bath Road"]},
        ],
    },

    {
        "id": "gb-edinburgh",
        "country_code": "GB",
        "name": "Edinburgh",
        "region": "Scotland",
        "metro": "Edinburgh",
        "population_context": 900000,
        "maturity": "viable_now",
        "center": [55.9533, -3.1883],
        "launch_phase": "Major Cities",
        "population_rank": 6,
        "run_on_startup": False,
        "cores": [
            {"id": "gb-edi-new-town",     "name": "New Town / Stockbridge", "center": [55.9560, -3.1998], "corridors": ["George Street", "Stockbridge Comely Bank", "Queensferry Road"]},
            {"id": "gb-edi-morningside",  "name": "Morningside / Bruntsfield","center": [55.9321, -3.2084], "corridors": ["Morningside Road", "Bruntsfield Place Clinic Strip"]},
        ],
    },

    {
        "id": "gb-liverpool",
        "country_code": "GB",
        "name": "Liverpool",
        "region": "Merseyside",
        "metro": "Merseyside",
        "population_context": 900000,
        "maturity": "viable_now",
        "center": [53.4084, -2.9916],
        "launch_phase": "Major Cities",
        "population_rank": 7,
        "run_on_startup": False,
        "cores": [
            {"id": "gb-lpl-bold-street",  "name": "Bold Street / Woolton",  "center": [53.4022, -2.9818], "corridors": ["Bold Street Clinic Row", "Allerton Road Woolton"]},
        ],
    },

    {
        "id": "gb-bristol",
        "country_code": "GB",
        "name": "Bristol",
        "region": "South West England",
        "metro": "Bristol",
        "population_context": 700000,
        "maturity": "viable_now",
        "center": [51.4545, -2.5879],
        "launch_phase": "Major Cities",
        "population_rank": 8,
        "run_on_startup": False,
        "cores": [
            {"id": "gb-brs-clifton",      "name": "Clifton / Cotham",       "center": [51.4574, -2.6189], "corridors": ["Whiteladies Road", "Clifton Village", "Cotham Hill"]},
            {"id": "gb-brs-south-ville",  "name": "Southville / Redland",   "center": [51.4420, -2.6020], "corridors": ["North Street Southville", "Gloucester Road Redland"]},
        ],
    },

    {
        "id": "gb-sheffield",
        "country_code": "GB",
        "name": "Sheffield",
        "region": "South Yorkshire",
        "metro": "Sheffield",
        "population_context": 750000,
        "maturity": "viable_now",
        "center": [53.3811, -1.4701],
        "launch_phase": "Major Cities",
        "population_rank": 9,
        "run_on_startup": False,
        "cores": [
            {"id": "gb-shf-broomhill",    "name": "Broomhill / Nether Edge", "center": [53.3781, -1.4929], "corridors": ["Broomhill Fulwood Road", "Nether Edge Abbeydale Road"]},
        ],
    },

    {
        "id": "gb-newcastle",
        "country_code": "GB",
        "name": "Newcastle",
        "region": "North East England",
        "metro": "Tyneside",
        "population_context": 920000,
        "maturity": "viable_now",
        "center": [54.9783, -1.6178],
        "launch_phase": "Major Cities",
        "population_rank": 10,
        "run_on_startup": False,
        "cores": [
            {"id": "gb-ncl-jesmond",      "name": "Jesmond / Gosforth",     "center": [55.0030, -1.6150], "corridors": ["Osborne Road Jesmond", "High Street Gosforth"]},
        ],
    },

    {
        "id": "gb-nottingham",
        "country_code": "GB",
        "name": "Nottingham",
        "region": "East Midlands",
        "metro": "Nottingham",
        "population_context": 760000,
        "maturity": "viable_now",
        "center": [52.9548, -1.1581],
        "launch_phase": "Major Cities",
        "population_rank": 11,
        "run_on_startup": False,
        "cores": [
            {"id": "gb-ntt-west-bridgford","name": "West Bridgford / Mapperley","center": [52.9297, -1.1345], "corridors": ["Bridgford Road", "Mapperley Plains Clinic Strip"]},
        ],
    },

    {
        "id": "gb-cardiff",
        "country_code": "GB",
        "name": "Cardiff",
        "region": "Wales",
        "metro": "Cardiff Metro",
        "population_context": 500000,
        "maturity": "viable_now",
        "center": [51.4816, -3.1791],
        "launch_phase": "Major Cities",
        "population_rank": 12,
        "run_on_startup": False,
        "cores": [
            {"id": "gb-cdf-pontcanna",    "name": "Pontcanna / Roath",      "center": [51.4940, -3.2090], "corridors": ["Cathedral Road Cardiff", "Wellfield Road Roath"]},
        ],
    },

    {
        "id": "gb-brighton",
        "country_code": "GB",
        "name": "Brighton",
        "region": "South East England",
        "metro": "Brighton",
        "population_context": 290000,
        "maturity": "viable_now",
        "center": [50.8225, -0.1372],
        "launch_phase": "Expansion",
        "population_rank": 13,
        "run_on_startup": False,
        "cores": [
            {"id": "gb-bgh-hove-clifton",  "name": "Hove / Seven Dials",    "center": [50.8273, -0.1681], "corridors": ["Church Road Hove", "Seven Dials Clinic Row"]},
        ],
    },

    {
        "id": "gb-leicester",
        "country_code": "GB",
        "name": "Leicester",
        "region": "East Midlands",
        "metro": "Leicester",
        "population_context": 540000,
        "maturity": "viable_now",
        "center": [52.6369, -1.1398],
        "launch_phase": "Expansion",
        "population_rank": 14,
        "run_on_startup": False,
        "cores": [
            {"id": "gb-lei-clarendon",    "name": "Clarendon Park / Stoneygate","center": [52.6193, -1.1280], "corridors": ["Queens Road Leicester", "London Road Medical Strip"]},
        ],
    },

    {
        "id": "gb-oxford",
        "country_code": "GB",
        "name": "Oxford",
        "region": "South East England",
        "metro": "Oxford",
        "population_context": 160000,
        "maturity": "viable_now",
        "center": [51.7520, -1.2577],
        "launch_phase": "Expansion",
        "population_rank": 15,
        "run_on_startup": False,
        "cores": [
            {"id": "gb-oxf-jericho",      "name": "Jericho / Summertown",   "center": [51.7640, -1.2720], "corridors": ["Banbury Road Clinic Strip", "Jericho Walton Street"]},
        ],
    },

    {
        "id": "gb-cambridge",
        "country_code": "GB",
        "name": "Cambridge",
        "region": "East of England",
        "metro": "Cambridge",
        "population_context": 130000,
        "maturity": "viable_now",
        "center": [52.2053, 0.1218],
        "launch_phase": "Expansion",
        "population_rank": 16,
        "run_on_startup": False,
        "cores": [
            {"id": "gb-cam-newnham",      "name": "Newnham / Trumpington",   "center": [52.1968, 0.1147], "corridors": ["Hills Road Cambridge", "Trumpington Street Clinic Row"]},
        ],
    },

    {
        "id": "gb-bath",
        "country_code": "GB",
        "name": "Bath",
        "region": "South West England",
        "metro": "Bath",
        "population_context": 95000,
        "maturity": "viable_now",
        "center": [51.3811, -2.3590],
        "launch_phase": "Expansion",
        "population_rank": 17,
        "run_on_startup": False,
        "cores": [
            {"id": "gb-bat-milsom",       "name": "Milsom Street / Lansdown","center": [51.3831, -2.3614], "corridors": ["Milsom Street", "Lansdown Road Clinic Strip"]},
        ],
    },

    {
        "id": "gb-southampton",
        "country_code": "GB",
        "name": "Southampton",
        "region": "South East England",
        "metro": "Southampton",
        "population_context": 700000,
        "maturity": "viable_now",
        "center": [50.9097, -1.4044],
        "launch_phase": "Expansion",
        "population_rank": 18,
        "run_on_startup": False,
        "cores": [
            {"id": "gb-sou-highfield",    "name": "Highfield / Shirley",    "center": [50.9263, -1.3972], "corridors": ["Highfield Avenue", "Shirley Road Clinic Strip"]},
        ],
    },

    # ══════════════════════════════════════════════════════════════════════════
    # AUSTRALIA
    # ══════════════════════════════════════════════════════════════════════════

    {
        "id": "au-sydney",
        "country_code": "AU",
        "name": "Sydney",
        "region": "New South Wales",
        "metro": "Greater Sydney",
        "population_context": 5300000,
        "maturity": "viable_now",
        "center": [-33.8688, 151.2093],
        "launch_phase": "Foundation",
        "population_rank": 1,
        "run_on_startup": False,
        "cores": [
            {"id": "au-syd-cbd",          "name": "CBD / Surry Hills",        "center": [-33.8810, 151.2097], "corridors": ["Pitt Street", "Crown Street Surry Hills", "Oxford Street"]},
            {"id": "au-syd-eastern",      "name": "Eastern Suburbs",          "center": [-33.8889, 151.2702], "corridors": ["New South Head Road", "Double Bay Knox Street", "Bondi Junction"]},
            {"id": "au-syd-lower-north",  "name": "Lower North Shore",        "center": [-33.8313, 151.1982], "corridors": ["Military Road Neutral Bay", "Willoughby Road Crows Nest", "Kirribilli"]},
            {"id": "au-syd-chatswood",    "name": "Chatswood / Lane Cove",    "center": [-33.7975, 151.1812], "corridors": ["Victoria Avenue Chatswood", "Lane Cove Village"]},
            {"id": "au-syd-northern",     "name": "Northern Beaches",         "center": [-33.7530, 151.2840], "corridors": ["Pittwater Road Mona Vale", "Manly Corso"]},
        ],
    },

    {
        "id": "au-melbourne",
        "country_code": "AU",
        "name": "Melbourne",
        "region": "Victoria",
        "metro": "Greater Melbourne",
        "population_context": 5200000,
        "maturity": "viable_now",
        "center": [-37.8136, 144.9631],
        "launch_phase": "Foundation",
        "population_rank": 2,
        "run_on_startup": False,
        "cores": [
            {"id": "au-mel-cbd",          "name": "CBD / Fitzroy",            "center": [-37.8136, 144.9631], "corridors": ["Collins Street", "Brunswick Street Fitzroy", "Chapel Street South Yarra"]},
            {"id": "au-mel-toorak",       "name": "Toorak / South Yarra",    "center": [-37.8478, 145.0159], "corridors": ["Toorak Road", "Malvern Road Clinic Strip"]},
            {"id": "au-mel-hawthorn",     "name": "Hawthorn / Camberwell",   "center": [-37.8225, 145.0396], "corridors": ["Glenferrie Road Hawthorn", "Burke Road Camberwell"]},
            {"id": "au-mel-bayside",      "name": "Bayside / Brighton",      "center": [-37.9011, 145.0040], "corridors": ["Church Street Brighton", "Bay Street Port Melbourne"]},
        ],
    },

    {
        "id": "au-brisbane",
        "country_code": "AU",
        "name": "Brisbane",
        "region": "Queensland",
        "metro": "Greater Brisbane",
        "population_context": 2600000,
        "maturity": "viable_now",
        "center": [-27.4698, 153.0251],
        "launch_phase": "Major Cities",
        "population_rank": 3,
        "run_on_startup": False,
        "cores": [
            {"id": "au-bri-new-farm",     "name": "New Farm / Teneriffe",    "center": [-27.4683, 153.0440], "corridors": ["Merthyr Road New Farm", "Vernon Terrace Teneriffe"]},
            {"id": "au-bri-paddington",   "name": "Paddington / Ascot",      "center": [-27.4627, 153.0063], "corridors": ["Latrobe Terrace Paddington", "Racecourse Road Ascot"]},
            {"id": "au-bri-gold-coast-corridor","name": "Gold Coast Corridor","center": [-28.0167, 153.4000], "corridors": ["Tedder Avenue Main Beach", "Cavill Avenue Surfers Paradise", "Broadbeach Mall"]},
        ],
    },

    {
        "id": "au-perth",
        "country_code": "AU",
        "name": "Perth",
        "region": "Western Australia",
        "metro": "Greater Perth",
        "population_context": 2100000,
        "maturity": "viable_now",
        "center": [-31.9505, 115.8605],
        "launch_phase": "Major Cities",
        "population_rank": 4,
        "run_on_startup": False,
        "cores": [
            {"id": "au-per-cottesloe",    "name": "Cottesloe / Claremont",   "center": [-31.9975, 115.7573], "corridors": ["Stirling Highway Claremont", "Cottesloe Beach Road"]},
            {"id": "au-per-subiaco",      "name": "Subiaco / Nedlands",      "center": [-31.9476, 115.8284], "corridors": ["Rokeby Road Subiaco", "Hampden Road Nedlands"]},
        ],
    },

    {
        "id": "au-adelaide",
        "country_code": "AU",
        "name": "Adelaide",
        "region": "South Australia",
        "metro": "Greater Adelaide",
        "population_context": 1400000,
        "maturity": "viable_now",
        "center": [-34.9285, 138.6007],
        "launch_phase": "Major Cities",
        "population_rank": 5,
        "run_on_startup": False,
        "cores": [
            {"id": "au-adl-north-adelaide","name": "North Adelaide",          "center": [-34.9044, 138.5999], "corridors": ["O'Connell Street", "Melbourne Street Clinic Strip"]},
            {"id": "au-adl-unley",        "name": "Unley / Norwood",          "center": [-34.9495, 138.6244], "corridors": ["Unley Road", "Magill Road Norwood"]},
        ],
    },

    {
        "id": "au-canberra",
        "country_code": "AU",
        "name": "Canberra",
        "region": "Australian Capital Territory",
        "metro": "Canberra",
        "population_context": 460000,
        "maturity": "viable_now",
        "center": [-35.2809, 149.1300],
        "launch_phase": "Expansion",
        "population_rank": 6,
        "run_on_startup": False,
        "cores": [
            {"id": "au-can-manuka",       "name": "Manuka / Deakin",         "center": [-35.3137, 149.1393], "corridors": ["Franklin Street Manuka", "Deakin Clinic Row"]},
        ],
    },

    # ══════════════════════════════════════════════════════════════════════════
    # GERMANY
    # ══════════════════════════════════════════════════════════════════════════

    {
        "id": "de-berlin",
        "country_code": "DE",
        "name": "Berlin",
        "region": "Berlin",
        "metro": "Berlin",
        "population_context": 3700000,
        "maturity": "viable_now",
        "center": [52.5200, 13.4050],
        "launch_phase": "Foundation",
        "population_rank": 1,
        "run_on_startup": False,
        "cores": [
            {"id": "de-ber-mitte",        "name": "Mitte / Prenzlauer Berg","center": [52.5303, 13.4116], "corridors": ["Friedrichstraße", "Schönhauser Allee", "Kastanienallee"]},
            {"id": "de-ber-charlottenburg","name": "Charlottenburg / Wilmersdorf","center": [52.5074, 13.3039], "corridors": ["Kurfürstendamm", "Tauentzienstraße", "Savignyplatz"]},
            {"id": "de-ber-mitte-west",   "name": "Schöneberg / Steglitz", "center": [52.4839, 13.3596], "corridors": ["Hauptstraße Schöneberg", "Schlossstraße Steglitz"]},
        ],
    },

    {
        "id": "de-munich",
        "country_code": "DE",
        "name": "Munich",
        "region": "Bavaria",
        "metro": "Munich",
        "population_context": 1600000,
        "maturity": "viable_now",
        "center": [48.1351, 11.5820],
        "launch_phase": "Foundation",
        "population_rank": 2,
        "run_on_startup": False,
        "cores": [
            {"id": "de-mun-maxvorstadt",  "name": "Maxvorstadt / Schwabing","center": [48.1524, 11.5693], "corridors": ["Leopoldstraße", "Maximilianstraße", "Türkenstraße"]},
            {"id": "de-mun-bogenhausen",  "name": "Bogenhausen / Schwabing-Ost","center": [48.1566, 11.6069], "corridors": ["Prinzregentenstraße", "Ismaninger Straße"]},
            {"id": "de-mun-haidhausen",   "name": "Haidhausen / Au",        "center": [48.1280, 11.6040], "corridors": ["Rosenheimer Straße", "Wörthstraße"]},
        ],
    },

    {
        "id": "de-hamburg",
        "country_code": "DE",
        "name": "Hamburg",
        "region": "Hamburg",
        "metro": "Hamburg",
        "population_context": 1900000,
        "maturity": "viable_now",
        "center": [53.5511, 9.9937],
        "launch_phase": "Foundation",
        "population_rank": 3,
        "run_on_startup": False,
        "cores": [
            {"id": "de-ham-eppendorf",    "name": "Eppendorf / Harvestehude","center": [53.5813, 9.9865], "corridors": ["Eppendorfer Landstraße", "Rothenbaumchaussee"]},
            {"id": "de-ham-blankenese",   "name": "Blankenese / Altona",    "center": [53.5627, 9.8086], "corridors": ["Blankeneser Hauptstraße", "Bahrenfelder Chaussee"]},
        ],
    },

    {
        "id": "de-frankfurt",
        "country_code": "DE",
        "name": "Frankfurt am Main",
        "region": "Hesse",
        "metro": "Rhine-Main Metro",
        "population_context": 780000,
        "maturity": "viable_now",
        "center": [50.1109, 8.6821],
        "launch_phase": "Major Cities",
        "population_rank": 4,
        "run_on_startup": False,
        "cores": [
            {"id": "de-fra-westend",      "name": "Westend / Nordend",      "center": [50.1218, 8.6690], "corridors": ["Bockenheimer Landstraße", "Berger Straße Nordend"]},
            {"id": "de-fra-sachsenhausen","name": "Sachsenhausen",          "center": [50.0984, 8.6835], "corridors": ["Schweizer Straße", "Textorstraße"]},
        ],
    },

    {
        "id": "de-cologne",
        "country_code": "DE",
        "name": "Cologne",
        "region": "North Rhine-Westphalia",
        "metro": "Cologne / Bonn",
        "population_context": 1100000,
        "maturity": "viable_now",
        "center": [50.9333, 6.9500],
        "launch_phase": "Major Cities",
        "population_rank": 5,
        "run_on_startup": False,
        "cores": [
            {"id": "de-col-innenstadt",   "name": "Innenstadt / Ehrenfeld",  "center": [50.9375, 6.9560], "corridors": ["Breite Straße", "Ehrenfelder Venloer Straße"]},
            {"id": "de-col-lindenthal",   "name": "Lindenthal",              "center": [50.9360, 6.9080], "corridors": ["Aachener Straße", "Dürener Straße Clinic Strip"]},
        ],
    },

    {
        "id": "de-stuttgart",
        "country_code": "DE",
        "name": "Stuttgart",
        "region": "Baden-Württemberg",
        "metro": "Stuttgart Metro",
        "population_context": 630000,
        "maturity": "viable_now",
        "center": [48.7758, 9.1829],
        "launch_phase": "Major Cities",
        "population_rank": 6,
        "run_on_startup": False,
        "cores": [
            {"id": "de-stu-main",         "name": "Stuttgart City Centre",   "center": [48.7758, 9.1829], "corridors": ["Königstraße", "Calwer Straße Clinic Strip"]},
        ],
    },

    {
        "id": "de-dusseldorf",
        "country_code": "DE",
        "name": "Düsseldorf",
        "region": "North Rhine-Westphalia",
        "metro": "Düsseldorf",
        "population_context": 640000,
        "maturity": "viable_now",
        "center": [51.2254, 6.7763],
        "launch_phase": "Major Cities",
        "population_rank": 7,
        "run_on_startup": False,
        "cores": [
            {"id": "de-dus-altstadt",     "name": "Altstadt / Pempelfort",   "center": [51.2297, 6.7848], "corridors": ["Königsallee", "Graf-Adolf-Straße", "Pempelforter Straße"]},
            {"id": "de-dus-oberbilk",     "name": "Oberkassel / Golzheim",   "center": [51.2337, 6.7497], "corridors": ["Luegallee Oberkassel", "Golzheimer Damm"]},
        ],
    },

    {
        "id": "de-leipzig",
        "country_code": "DE",
        "name": "Leipzig",
        "region": "Saxony",
        "metro": "Leipzig",
        "population_context": 620000,
        "maturity": "scaling",
        "center": [51.3397, 12.3731],
        "launch_phase": "Expansion",
        "population_rank": 8,
        "run_on_startup": False,
        "cores": [
            {"id": "de-lei-gohlis",       "name": "Gohlis / Plagwitz",       "center": [51.3540, 12.3562], "corridors": ["Karl-Liebknecht-Straße", "Gohlis Menckestraße"]},
        ],
    },

    {
        "id": "de-nuremberg",
        "country_code": "DE",
        "name": "Nuremberg",
        "region": "Bavaria",
        "metro": "Nuremberg Metro",
        "population_context": 530000,
        "maturity": "scaling",
        "center": [49.4521, 11.0767],
        "launch_phase": "Expansion",
        "population_rank": 9,
        "run_on_startup": False,
        "cores": [
            {"id": "de-nur-gostenhof",    "name": "Gostenhof / St. Johannis","center": [49.4561, 11.0620], "corridors": ["Fürther Straße", "Steinbühler Straße"]},
        ],
    },

    {
        "id": "de-hannover",
        "country_code": "DE",
        "name": "Hannover",
        "region": "Lower Saxony",
        "metro": "Hannover",
        "population_context": 540000,
        "maturity": "scaling",
        "center": [52.3759, 9.7320],
        "launch_phase": "Expansion",
        "population_rank": 10,
        "run_on_startup": False,
        "cores": [
            {"id": "de-han-list",         "name": "List / Nordstadt",        "center": [52.3867, 9.7418], "corridors": ["Lister Meile", "Bödekerstraße"]},
        ],
    },

    # ══════════════════════════════════════════════════════════════════════════
    # FRANCE
    # ══════════════════════════════════════════════════════════════════════════

    {
        "id": "fr-paris",
        "country_code": "FR",
        "name": "Paris",
        "region": "Île-de-France",
        "metro": "Greater Paris",
        "population_context": 12300000,
        "maturity": "viable_now",
        "center": [48.8566, 2.3522],
        "launch_phase": "Foundation",
        "population_rank": 1,
        "run_on_startup": False,
        "cores": [
            {"id": "fr-par-8e",           "name": "8e / 16e Arrondissement", "center": [48.8749, 2.3030], "corridors": ["Avenue Montaigne", "Rue du Faubourg Saint-Honoré", "Avenue Victor Hugo"]},
            {"id": "fr-par-saint-germain","name": "Saint-Germain-des-Prés",  "center": [48.8528, 2.3326], "corridors": ["Boulevard Saint-Germain", "Rue de Rennes Clinic Strip"]},
            {"id": "fr-par-marais",       "name": "Le Marais / République",  "center": [48.8594, 2.3602], "corridors": ["Rue de Bretagne", "Rue Oberkampf", "Rue Saint-Antoine"]},
            {"id": "fr-par-neuilly",      "name": "Neuilly-sur-Seine",       "center": [48.8837, 2.2680], "corridors": ["Avenue Charles de Gaulle Neuilly", "Boulevard Inkermann"]},
        ],
    },

    {
        "id": "fr-lyon",
        "country_code": "FR",
        "name": "Lyon",
        "region": "Auvergne-Rhône-Alpes",
        "metro": "Lyon Metro",
        "population_context": 1700000,
        "maturity": "viable_now",
        "center": [45.7640, 4.8357],
        "launch_phase": "Major Cities",
        "population_rank": 2,
        "run_on_startup": False,
        "cores": [
            {"id": "fr-lyo-presquile",    "name": "Presqu'île / Bellecour",  "center": [45.7491, 4.8315], "corridors": ["Rue de la République", "Cours Franklin Roosevelt"]},
            {"id": "fr-lyo-foch",         "name": "Foch / Masséna",          "center": [45.7779, 4.8575], "corridors": ["Avenue Foch", "Cours Masséna"]},
        ],
    },

    {
        "id": "fr-marseille",
        "country_code": "FR",
        "name": "Marseille",
        "region": "Provence-Alpes-Côte d'Azur",
        "metro": "Marseille Metro",
        "population_context": 1880000,
        "maturity": "viable_now",
        "center": [43.2965, 5.3698],
        "launch_phase": "Major Cities",
        "population_rank": 3,
        "run_on_startup": False,
        "cores": [
            {"id": "fr-mrs-endoume",      "name": "Endoume / Castellane",    "center": [43.2862, 5.3649], "corridors": ["Avenue du Prado", "Boulevard Castellane Clinic Strip"]},
        ],
    },

    {
        "id": "fr-toulouse",
        "country_code": "FR",
        "name": "Toulouse",
        "region": "Occitanie",
        "metro": "Toulouse Metro",
        "population_context": 1400000,
        "maturity": "viable_now",
        "center": [43.6047, 1.4442],
        "launch_phase": "Major Cities",
        "population_rank": 4,
        "run_on_startup": False,
        "cores": [
            {"id": "fr-tls-capitol",      "name": "Capitole / Côte Pavée",   "center": [43.6045, 1.4440], "corridors": ["Rue d'Alsace-Lorraine", "Allées Jean Jaurès"]},
        ],
    },

    {
        "id": "fr-nice",
        "country_code": "FR",
        "name": "Nice",
        "region": "Provence-Alpes-Côte d'Azur",
        "metro": "Nice Côte d'Azur",
        "population_context": 1000000,
        "maturity": "viable_now",
        "center": [43.7102, 7.2620],
        "launch_phase": "Major Cities",
        "population_rank": 5,
        "run_on_startup": False,
        "cores": [
            {"id": "fr-nic-promenade",    "name": "Promenade / Cimiez",      "center": [43.7102, 7.2690], "corridors": ["Promenade des Anglais Clinic Row", "Avenue de Cimiez"]},
        ],
    },

    {
        "id": "fr-bordeaux",
        "country_code": "FR",
        "name": "Bordeaux",
        "region": "Nouvelle-Aquitaine",
        "metro": "Bordeaux Metro",
        "population_context": 1000000,
        "maturity": "viable_now",
        "center": [44.8378, -0.5792],
        "launch_phase": "Major Cities",
        "population_rank": 6,
        "run_on_startup": False,
        "cores": [
            {"id": "fr-bdx-triangle-or",  "name": "Triangle d'Or / Caudéran","center": [44.8446, -0.5775], "corridors": ["Cours de l'Intendance", "Avenue de la Forêt Noire"]},
        ],
    },

    {
        "id": "fr-lille",
        "country_code": "FR",
        "name": "Lille",
        "region": "Hauts-de-France",
        "metro": "Métropole Européenne de Lille",
        "population_context": 1200000,
        "maturity": "viable_now",
        "center": [50.6292, 3.0573],
        "launch_phase": "Major Cities",
        "population_rank": 7,
        "run_on_startup": False,
        "cores": [
            {"id": "fr-lil-vieux-lille",  "name": "Vieux-Lille / Wazemmes", "center": [50.6397, 3.0612], "corridors": ["Rue de la Monnaie", "Rue Gambetta Clinic Row"]},
        ],
    },

    {
        "id": "fr-nantes",
        "country_code": "FR",
        "name": "Nantes",
        "region": "Pays de la Loire",
        "metro": "Nantes Metro",
        "population_context": 680000,
        "maturity": "scaling",
        "center": [47.2184, -1.5536],
        "launch_phase": "Expansion",
        "population_rank": 8,
        "run_on_startup": False,
        "cores": [
            {"id": "fr-nan-graslin",      "name": "Graslin / Bouffay",       "center": [47.2150, -1.5545], "corridors": ["Rue de Verdun", "Cours des 50 Otages"]},
        ],
    },

    {
        "id": "fr-montpellier",
        "country_code": "FR",
        "name": "Montpellier",
        "region": "Occitanie",
        "metro": "Montpellier Metro",
        "population_context": 620000,
        "maturity": "scaling",
        "center": [43.6108, 3.8767],
        "launch_phase": "Expansion",
        "population_rank": 9,
        "run_on_startup": False,
        "cores": [
            {"id": "fr-mpl-coeur",        "name": "Comédie / Antigone",      "center": [43.6110, 3.8780], "corridors": ["Rue de la Loge", "Avenue du Professeur Grasset Clinic Row"]},
        ],
    },

    # ══════════════════════════════════════════════════════════════════════════
    # SPAIN
    # ══════════════════════════════════════════════════════════════════════════

    {
        "id": "es-madrid",
        "country_code": "ES",
        "name": "Madrid",
        "region": "Community of Madrid",
        "metro": "Madrid Metro",
        "population_context": 6800000,
        "maturity": "viable_now",
        "center": [40.4168, -3.7038],
        "launch_phase": "Foundation",
        "population_rank": 1,
        "run_on_startup": False,
        "cores": [
            {"id": "es-mad-salamanca",    "name": "Salamanca / Almagro",     "center": [40.4249, -3.6820], "corridors": ["Calle Serrano", "Calle Velázquez", "Paseo de la Castellana"]},
            {"id": "es-mad-chamberi",     "name": "Chamberí / Malasaña",     "center": [40.4368, -3.7040], "corridors": ["Calle de Fuencarral", "Calle de Génova", "Calle Sagasta"]},
            {"id": "es-mad-pozuelo",      "name": "Pozuelo / La Moraleja",   "center": [40.4342, -3.8155], "corridors": ["Avenida de Europa Pozuelo", "La Moraleja Clinic Corridor"]},
        ],
    },

    {
        "id": "es-barcelona",
        "country_code": "ES",
        "name": "Barcelona",
        "region": "Catalonia",
        "metro": "Barcelona Metro",
        "population_context": 5600000,
        "maturity": "viable_now",
        "center": [41.3851, 2.1734],
        "launch_phase": "Foundation",
        "population_rank": 2,
        "run_on_startup": False,
        "cores": [
            {"id": "es-bcn-eixample",     "name": "Eixample / Sarrià",       "center": [41.3928, 2.1614], "corridors": ["Passeig de Gràcia", "Carrer de Balmes", "Via Augusta"]},
            {"id": "es-bcn-gracia",       "name": "Gràcia / Horta",          "center": [41.4063, 2.1529], "corridors": ["Carrer Gran de Gràcia", "Avinguda República Argentina"]},
            {"id": "es-bcn-barcelona-nord","name": "Sant Cugat / Vallès",    "center": [41.4735, 2.0847], "corridors": ["Rambla del Celler Sant Cugat", "Passeig de Can Magí"]},
        ],
    },

    {
        "id": "es-valencia",
        "country_code": "ES",
        "name": "Valencia",
        "region": "Valencia",
        "metro": "Valencia Metro",
        "population_context": 1800000,
        "maturity": "viable_now",
        "center": [39.4699, -0.3763],
        "launch_phase": "Major Cities",
        "population_rank": 3,
        "run_on_startup": False,
        "cores": [
            {"id": "es-vlc-pla-del-remei","name": "Pla del Remei / Gran Vía","center": [39.4696, -0.3762], "corridors": ["Calle Colón", "Gran Vía del Marqués del Turia", "Calle Jorge Juan"]},
        ],
    },

    {
        "id": "es-seville",
        "country_code": "ES",
        "name": "Seville",
        "region": "Andalusia",
        "metro": "Seville Metro",
        "population_context": 1500000,
        "maturity": "viable_now",
        "center": [37.3891, -5.9845],
        "launch_phase": "Major Cities",
        "population_rank": 4,
        "run_on_startup": False,
        "cores": [
            {"id": "es-svq-nervion",      "name": "Nervión / Los Remedios",  "center": [37.3793, -5.9725], "corridors": ["Calle Luis de Morales", "Avenida de la Palmera"]},
        ],
    },

    {
        "id": "es-bilbao",
        "country_code": "ES",
        "name": "Bilbao",
        "region": "Basque Country",
        "metro": "Bilbao Metro",
        "population_context": 1150000,
        "maturity": "viable_now",
        "center": [43.2630, -2.9350],
        "launch_phase": "Major Cities",
        "population_rank": 5,
        "run_on_startup": False,
        "cores": [
            {"id": "es-bil-abando",       "name": "Abando / Indautxu",       "center": [43.2635, -2.9336], "corridors": ["Gran Vía Diego López de Haro", "Calle Ercilla"]},
        ],
    },

    {
        "id": "es-malaga",
        "country_code": "ES",
        "name": "Málaga",
        "region": "Andalusia",
        "metro": "Málaga Metro",
        "population_context": 1060000,
        "maturity": "viable_now",
        "center": [36.7213, -4.4214],
        "launch_phase": "Major Cities",
        "population_rank": 6,
        "run_on_startup": False,
        "cores": [
            {"id": "es-mlg-soho",         "name": "SoHo / Marbella Corridor","center": [36.7185, -4.4266], "corridors": ["Calle Larios", "Paseo de la Farola", "Golden Mile Marbella"]},
        ],
    },

    # ══════════════════════════════════════════════════════════════════════════
    # PORTUGAL
    # ══════════════════════════════════════════════════════════════════════════

    {
        "id": "pt-lisbon",
        "country_code": "PT",
        "name": "Lisbon",
        "region": "Lisbon",
        "metro": "Lisbon Metro",
        "population_context": 3000000,
        "maturity": "viable_now",
        "center": [38.7223, -9.1393],
        "launch_phase": "Foundation",
        "population_rank": 1,
        "run_on_startup": False,
        "cores": [
            {"id": "pt-lis-chiado",       "name": "Chiado / Príncipe Real",  "center": [38.7107, -9.1428], "corridors": ["Rua Garrett", "Rua Dom Pedro V", "Avenida da Liberdade"]},
            {"id": "pt-lis-alcantara",    "name": "Alcântara / Campo de Ourique","center": [38.7048, -9.1733], "corridors": ["Rua Maria Pia Clinic Strip", "Rua Saraiva de Carvalho"]},
        ],
    },

    {
        "id": "pt-porto",
        "country_code": "PT",
        "name": "Porto",
        "region": "Porto",
        "metro": "Porto Metro",
        "population_context": 1900000,
        "maturity": "viable_now",
        "center": [41.1579, -8.6291],
        "launch_phase": "Major Cities",
        "population_rank": 2,
        "run_on_startup": False,
        "cores": [
            {"id": "pt-opo-baixa",        "name": "Baixa / Foz do Douro",    "center": [41.1496, -8.6104], "corridors": ["Rua de Santa Catarina", "Avenida da Boavista", "Passeio Alegre"]},
        ],
    },

    {
        "id": "pt-braga",
        "country_code": "PT",
        "name": "Braga",
        "region": "Braga",
        "metro": "Braga",
        "population_context": 200000,
        "maturity": "scaling",
        "center": [41.5454, -8.4265],
        "launch_phase": "Expansion",
        "population_rank": 3,
        "run_on_startup": False,
        "cores": [
            {"id": "pt-brg-main",         "name": "Braga City Centre",       "center": [41.5454, -8.4265], "corridors": ["Rua do Souto", "Avenida da Liberdade Braga"]},
        ],
    },

    # ══════════════════════════════════════════════════════════════════════════
    # ITALY
    # ══════════════════════════════════════════════════════════════════════════

    {
        "id": "it-rome",
        "country_code": "IT",
        "name": "Rome",
        "region": "Lazio",
        "metro": "Rome Metro",
        "population_context": 4300000,
        "maturity": "viable_now",
        "center": [41.9028, 12.4964],
        "launch_phase": "Foundation",
        "population_rank": 1,
        "run_on_startup": False,
        "cores": [
            {"id": "it-rom-parioli",      "name": "Parioli / Prati",         "center": [41.9264, 12.4791], "corridors": ["Viale Parioli", "Via Cola di Rienzo", "Via Candia"]},
            {"id": "it-rom-prati-vaticano","name": "Prati / Trionfale",      "center": [41.9063, 12.4618], "corridors": ["Via dei Gracchi", "Via Candia Clinic Strip"]},
            {"id": "it-rom-eur",          "name": "EUR / Appio Latino",      "center": [41.8335, 12.4739], "corridors": ["Viale dell'Umanesimo EUR", "Via Appia Nuova Clinic Corridor"]},
        ],
    },

    {
        "id": "it-milan",
        "country_code": "IT",
        "name": "Milan",
        "region": "Lombardy",
        "metro": "Milan Metro",
        "population_context": 3300000,
        "maturity": "viable_now",
        "center": [45.4654, 9.1859],
        "launch_phase": "Foundation",
        "population_rank": 2,
        "run_on_startup": False,
        "cores": [
            {"id": "it-mil-brera",        "name": "Brera / Porta Venezia",   "center": [45.4767, 9.1875], "corridors": ["Corso Venezia", "Via della Spiga", "Via Brera"]},
            {"id": "it-mil-magenta",      "name": "Magenta / CityLife",      "center": [45.4705, 9.1629], "corridors": ["Corso Magenta", "Piazzale Lotto CityLife"]},
            {"id": "it-mil-isola",        "name": "Isola / Porta Nuova",     "center": [45.4838, 9.1867], "corridors": ["Via Sassetti", "Corso Como", "Garibaldi Station Clinic Row"]},
        ],
    },

    {
        "id": "it-florence",
        "country_code": "IT",
        "name": "Florence",
        "region": "Tuscany",
        "metro": "Florence Metro",
        "population_context": 1000000,
        "maturity": "viable_now",
        "center": [43.7696, 11.2558],
        "launch_phase": "Major Cities",
        "population_rank": 3,
        "run_on_startup": False,
        "cores": [
            {"id": "it-fir-duomo",        "name": "Duomo / Oltrarno",        "center": [43.7697, 11.2557], "corridors": ["Via de' Tornabuoni", "Borgo San Jacopo", "Viale Milton"]},
        ],
    },

    {
        "id": "it-turin",
        "country_code": "IT",
        "name": "Turin",
        "region": "Piedmont",
        "metro": "Turin Metro",
        "population_context": 2300000,
        "maturity": "viable_now",
        "center": [45.0703, 7.6869],
        "launch_phase": "Major Cities",
        "population_rank": 4,
        "run_on_startup": False,
        "cores": [
            {"id": "it-tor-crocetta",     "name": "Crocetta / San Salvario", "center": [45.0597, 7.6787], "corridors": ["Corso Massimo d'Azeglio", "Via Lequio Clinic Strip"]},
        ],
    },

    {
        "id": "it-naples",
        "country_code": "IT",
        "name": "Naples",
        "region": "Campania",
        "metro": "Naples Metro",
        "population_context": 3200000,
        "maturity": "viable_now",
        "center": [40.8518, 14.2681],
        "launch_phase": "Major Cities",
        "population_rank": 5,
        "run_on_startup": False,
        "cores": [
            {"id": "it-nap-chiaia",       "name": "Chiaia / Posillipo",      "center": [40.8313, 14.2390], "corridors": ["Via Chiaia", "Riviera di Chiaia", "Via Posillipo Clinic Strip"]},
        ],
    },

    {
        "id": "it-bologna",
        "country_code": "IT",
        "name": "Bologna",
        "region": "Emilia-Romagna",
        "metro": "Bologna Metro",
        "population_context": 1000000,
        "maturity": "scaling",
        "center": [44.4949, 11.3426],
        "launch_phase": "Expansion",
        "population_rank": 6,
        "run_on_startup": False,
        "cores": [
            {"id": "it-blo-galvani",      "name": "Galvani / San Vitale",    "center": [44.4966, 11.3474], "corridors": ["Via d'Azeglio", "Via San Vitale Clinic Row"]},
        ],
    },

    # ══════════════════════════════════════════════════════════════════════════
    # POLAND
    # ══════════════════════════════════════════════════════════════════════════

    {
        "id": "pl-warsaw",
        "country_code": "PL",
        "name": "Warsaw",
        "region": "Masovian Voivodeship",
        "metro": "Warsaw Metro",
        "population_context": 1800000,
        "maturity": "viable_now",
        "center": [52.2297, 21.0122],
        "launch_phase": "Foundation",
        "population_rank": 1,
        "run_on_startup": False,
        "cores": [
            {"id": "pl-war-mokotow",      "name": "Mokotów / Żoliborz",      "center": [52.1930, 21.0079], "corridors": ["Aleje Niepodległości", "Puławska Clinic Strip", "Żoliborz Market"]},
            {"id": "pl-war-wilanow",      "name": "Wilanów / Ursynów",       "center": [52.1637, 21.0869], "corridors": ["Wilanowska Clinic Corridor", "Aleja KEN"]},
            {"id": "pl-war-srodmiescie",  "name": "Śródmieście / Powiśle",   "center": [52.2294, 21.0153], "corridors": ["Marszałkowska Clinic Row", "Nowy Świat"]},
        ],
    },

    {
        "id": "pl-krakow",
        "country_code": "PL",
        "name": "Kraków",
        "region": "Lesser Poland Voivodeship",
        "metro": "Kraków Metro",
        "population_context": 780000,
        "maturity": "viable_now",
        "center": [50.0647, 19.9450],
        "launch_phase": "Major Cities",
        "population_rank": 2,
        "run_on_startup": False,
        "cores": [
            {"id": "pl-kra-kazimierz",    "name": "Kazimierz / Krowodrza",   "center": [50.0522, 19.9506], "corridors": ["Ulica Karmelicka", "Aleje 3 Maja", "Ulica Długa Clinic Strip"]},
        ],
    },

    {
        "id": "pl-wroclaw",
        "country_code": "PL",
        "name": "Wrocław",
        "region": "Lower Silesian Voivodeship",
        "metro": "Wrocław Metro",
        "population_context": 640000,
        "maturity": "viable_now",
        "center": [51.1079, 17.0385],
        "launch_phase": "Major Cities",
        "population_rank": 3,
        "run_on_startup": False,
        "cores": [
            {"id": "pl-wro-srodmiescie",  "name": "Śródmieście / Krzyki",    "center": [51.1028, 17.0393], "corridors": ["Ulica Świdnicka", "Ulica Ślężna Clinic Corridor"]},
        ],
    },

    {
        "id": "pl-gdansk",
        "country_code": "PL",
        "name": "Gdańsk",
        "region": "Pomeranian Voivodeship",
        "metro": "Tricity Metro",
        "population_context": 760000,
        "maturity": "viable_now",
        "center": [54.3520, 18.6466],
        "launch_phase": "Major Cities",
        "population_rank": 4,
        "run_on_startup": False,
        "cores": [
            {"id": "pl-gda-wrzeszcz",     "name": "Wrzeszcz / Oliwa",        "center": [54.3769, 18.6220], "corridors": ["Aleja Grunwaldzka", "Ulica Obrońców Westerplatte"]},
        ],
    },

    {
        "id": "pl-poznan",
        "country_code": "PL",
        "name": "Poznań",
        "region": "Greater Poland Voivodeship",
        "metro": "Poznań Metro",
        "population_context": 550000,
        "maturity": "scaling",
        "center": [52.4064, 16.9252],
        "launch_phase": "Expansion",
        "population_rank": 5,
        "run_on_startup": False,
        "cores": [
            {"id": "pl-poz-grunwald",     "name": "Grunwald / Jeżyce",       "center": [52.4020, 16.8990], "corridors": ["Aleje Marcinkowskiego", "Ulica Głogowska Clinic Strip"]},
        ],
    },

    # ══════════════════════════════════════════════════════════════════════════
    # SCANDINAVIA
    # ══════════════════════════════════════════════════════════════════════════

    {
        "id": "se-stockholm",
        "country_code": "SE",
        "name": "Stockholm",
        "region": "Stockholm County",
        "metro": "Greater Stockholm",
        "population_context": 2400000,
        "maturity": "viable_now",
        "center": [59.3293, 18.0686],
        "launch_phase": "Foundation",
        "population_rank": 1,
        "run_on_startup": False,
        "cores": [
            {"id": "se-sto-ostermalm",    "name": "Östermalm / Lidingö",     "center": [59.3382, 18.0843], "corridors": ["Strandvägen", "Karlavägen Clinic Strip", "Lidingövägen"]},
            {"id": "se-sto-sodermalm",    "name": "Södermalm",               "center": [59.3121, 18.0634], "corridors": ["Götgatan", "Hornsgatan Clinic Row"]},
            {"id": "se-sto-danderyd",     "name": "Danderyd / Täby",         "center": [59.4017, 18.0325], "corridors": ["Mörbyleden", "Täby Centrum Corridor"]},
        ],
    },

    {
        "id": "se-gothenburg",
        "country_code": "SE",
        "name": "Gothenburg",
        "region": "Västra Götaland County",
        "metro": "Gothenburg",
        "population_context": 1000000,
        "maturity": "viable_now",
        "center": [57.7089, 11.9746],
        "launch_phase": "Major Cities",
        "population_rank": 2,
        "run_on_startup": False,
        "cores": [
            {"id": "se-got-avenyn",       "name": "Avenyn / Linnéstan",      "center": [57.7007, 11.9717], "corridors": ["Kungsportsavenyn", "Linnégatan Clinic Strip"]},
        ],
    },

    {
        "id": "se-malmo",
        "country_code": "SE",
        "name": "Malmö",
        "region": "Skåne County",
        "metro": "Malmö",
        "population_context": 380000,
        "maturity": "scaling",
        "center": [55.6050, 13.0038],
        "launch_phase": "Expansion",
        "population_rank": 3,
        "run_on_startup": False,
        "cores": [
            {"id": "se-mal-hyllie",       "name": "Hyllie / Limhamn",        "center": [55.5647, 12.9891], "corridors": ["Hyllie Stationstorg", "Limhamnsvägen Clinic Corridor"]},
        ],
    },

    {
        "id": "no-oslo",
        "country_code": "NO",
        "name": "Oslo",
        "region": "Oslo",
        "metro": "Greater Oslo",
        "population_context": 1100000,
        "maturity": "viable_now",
        "center": [59.9139, 10.7522],
        "launch_phase": "Foundation",
        "population_rank": 1,
        "run_on_startup": False,
        "cores": [
            {"id": "no-osl-frogner",      "name": "Frogner / Majorstuen",    "center": [59.9198, 10.7094], "corridors": ["Bogstadveien", "Frognerveien Clinic Strip", "Majorstuen"]},
            {"id": "no-osl-grunerlokka",  "name": "Grünerløkka / Sentrum",   "center": [59.9223, 10.7606], "corridors": ["Markveien", "Thorvald Meyers Gate"]},
        ],
    },

    {
        "id": "no-bergen",
        "country_code": "NO",
        "name": "Bergen",
        "region": "Vestland",
        "metro": "Bergen",
        "population_context": 290000,
        "maturity": "scaling",
        "center": [60.3913, 5.3221],
        "launch_phase": "Expansion",
        "population_rank": 2,
        "run_on_startup": False,
        "cores": [
            {"id": "no-ber-sentrum",      "name": "Bergen Sentrum",          "center": [60.3913, 5.3271], "corridors": ["Torgallmenningen", "Strandkaien Clinic Row"]},
        ],
    },

    {
        "id": "dk-copenhagen",
        "country_code": "DK",
        "name": "Copenhagen",
        "region": "Capital Region",
        "metro": "Greater Copenhagen",
        "population_context": 1380000,
        "maturity": "viable_now",
        "center": [55.6761, 12.5683],
        "launch_phase": "Foundation",
        "population_rank": 1,
        "run_on_startup": False,
        "cores": [
            {"id": "dk-cop-osterbro",     "name": "Østerbro / Frederiksberg","center": [55.6969, 12.5752], "corridors": ["Østerbrogade Clinic Strip", "Gammel Kongevej Frederiksberg"]},
            {"id": "dk-cop-nordhavn",     "name": "Nordhavn / Hellerup",     "center": [55.7146, 12.5858], "corridors": ["Tuborg Boulevard Hellerup", "Kalkbrænderihavnsgade"]},
        ],
    },

    {
        "id": "dk-aarhus",
        "country_code": "DK",
        "name": "Aarhus",
        "region": "Central Jutland",
        "metro": "Aarhus",
        "population_context": 350000,
        "maturity": "scaling",
        "center": [56.1629, 10.2039],
        "launch_phase": "Expansion",
        "population_rank": 2,
        "run_on_startup": False,
        "cores": [
            {"id": "dk-aar-troja",        "name": "Trøjborg / Østbyen",      "center": [56.1736, 10.2181], "corridors": ["Ny Munkegade", "Nordre Ringgade Clinic Row"]},
        ],
    },

    {
        "id": "fi-helsinki",
        "country_code": "FI",
        "name": "Helsinki",
        "region": "Uusimaa",
        "metro": "Greater Helsinki",
        "population_context": 1200000,
        "maturity": "viable_now",
        "center": [60.1699, 24.9384],
        "launch_phase": "Foundation",
        "population_rank": 1,
        "run_on_startup": False,
        "cores": [
            {"id": "fi-hel-eira",         "name": "Eira / Ullanlinna",       "center": [60.1556, 24.9402], "corridors": ["Merikatu Eira", "Bulevardi Clinic Strip"]},
            {"id": "fi-hel-punavuori",    "name": "Punavuori / Kruununhaka", "center": [60.1609, 24.9479], "corridors": ["Iso Roobertinkatu", "Korkeavuorenkatu"]},
        ],
    },

    {
        "id": "fi-tampere",
        "country_code": "FI",
        "name": "Tampere",
        "region": "Pirkanmaa",
        "metro": "Tampere",
        "population_context": 240000,
        "maturity": "scaling",
        "center": [61.4978, 23.7610],
        "launch_phase": "Expansion",
        "population_rank": 2,
        "run_on_startup": False,
        "cores": [
            {"id": "fi-tam-keskus",       "name": "Tampere Centre",          "center": [61.4978, 23.7620], "corridors": ["Hämeenkatu Clinic Row", "Satakunnankatu"]},
        ],
    },

    {
        "id": "ee-tallinn",
        "country_code": "EE",
        "name": "Tallinn",
        "region": "Harju County",
        "metro": "Tallinn",
        "population_context": 440000,
        "maturity": "scaling",
        "center": [59.4370, 24.7536],
        "launch_phase": "Foundation",
        "population_rank": 1,
        "run_on_startup": False,
        "cores": [
            {"id": "ee-tal-kadriorg",     "name": "Kadriorg / Kesklinn",     "center": [59.4402, 24.7771], "corridors": ["Narva Maantee Clinic Corridor", "Viru Väljak"]},
            {"id": "ee-tal-pirita",       "name": "Pirita / Ülemiste",       "center": [59.4566, 24.8158], "corridors": ["Pirita Tee", "Ülemiste City Clinic Row"]},
        ],
    },

    {
        "id": "ee-tartu",
        "country_code": "EE",
        "name": "Tartu",
        "region": "Tartu County",
        "metro": "Tartu",
        "population_context": 100000,
        "maturity": "emerging",
        "center": [58.3776, 26.7290],
        "launch_phase": "Expansion",
        "population_rank": 2,
        "run_on_startup": False,
        "cores": [
            {"id": "ee-tar-main",         "name": "Tartu City Centre",       "center": [58.3776, 26.7290], "corridors": ["Riia Maantee Clinic Strip", "Raekoja Plats"]},
        ],
    },

    # ══════════════════════════════════════════════════════════════════════════
    # THAILAND
    # ══════════════════════════════════════════════════════════════════════════

    {
        "id": "th-bangkok",
        "country_code": "TH",
        "name": "Bangkok",
        "region": "Bangkok",
        "metro": "Bangkok Metro",
        "population_context": 10700000,
        "maturity": "viable_now",
        "center": [13.7563, 100.5018],
        "launch_phase": "Foundation",
        "population_rank": 1,
        "run_on_startup": False,
        "cores": [
            {"id": "th-bkk-sukhumvit",    "name": "Sukhumvit",               "center": [13.7308, 100.5624], "corridors": ["Sukhumvit Road Clinic Mile", "Soi Tonglor", "Soi Ekkamai"]},
            {"id": "th-bkk-silom",        "name": "Silom / Sathorn",         "center": [13.7245, 100.5228], "corridors": ["Silom Road Medical Corridor", "Narathiwas Road", "Sathorn Clinic Strip"]},
            {"id": "th-bkk-ratchada",     "name": "Ratchadapisek / Ladprao", "center": [13.7725, 100.5671], "corridors": ["Ratchadapisek Road Clinic Row", "Phaholyothin Road"]},
            {"id": "th-bkk-ari",          "name": "Ari / Samsen",            "center": [13.7802, 100.5440], "corridors": ["Ari BTS Clinic Strip", "Phayathai Road"]},
            {"id": "th-bkk-petchburi",    "name": "Petchburi / Asoke",       "center": [13.7463, 100.5600], "corridors": ["Petchburi Road Clinic Corridor", "Asoke Clinic Row"]},
        ],
    },

    {
        "id": "th-chiang-mai",
        "country_code": "TH",
        "name": "Chiang Mai",
        "region": "Chiang Mai",
        "metro": "Chiang Mai",
        "population_context": 1800000,
        "maturity": "viable_now",
        "center": [18.7883, 98.9853],
        "launch_phase": "Major Cities",
        "population_rank": 2,
        "run_on_startup": False,
        "cores": [
            {"id": "th-cnx-nimmanhaemin",  "name": "Nimman / Santitham",     "center": [18.8029, 98.9674], "corridors": ["Nimmanhaemin Road Clinic Strip", "Maya Mall Corridor", "Huay Kaew Road"]},
        ],
    },

    {
        "id": "th-phuket",
        "country_code": "TH",
        "name": "Phuket",
        "region": "Phuket",
        "metro": "Phuket",
        "population_context": 420000,
        "maturity": "viable_now",
        "center": [7.8804, 98.3923],
        "launch_phase": "Major Cities",
        "population_rank": 3,
        "run_on_startup": False,
        "cores": [
            {"id": "th-hkt-patong",       "name": "Patong / Cherng Talay",   "center": [7.9038, 98.2966], "corridors": ["Bangla Road Patong", "Boat Avenue Cherng Talay", "Laguna Clinic Corridor"]},
        ],
    },

    {
        "id": "th-pattaya",
        "country_code": "TH",
        "name": "Pattaya",
        "region": "Chonburi",
        "metro": "Pattaya",
        "population_context": 350000,
        "maturity": "viable_now",
        "center": [12.9236, 100.8825],
        "launch_phase": "Major Cities",
        "population_rank": 4,
        "run_on_startup": False,
        "cores": [
            {"id": "th-pty-central",      "name": "Central Pattaya / Jomtien","center": [12.9246, 100.8830], "corridors": ["Second Road Clinic Strip", "Thappraya Road Jomtien"]},
        ],
    },

    # ══════════════════════════════════════════════════════════════════════════
    # MALAYSIA
    # ══════════════════════════════════════════════════════════════════════════

    {
        "id": "my-kuala-lumpur",
        "country_code": "MY",
        "name": "Kuala Lumpur",
        "region": "Federal Territory",
        "metro": "Klang Valley",
        "population_context": 7700000,
        "maturity": "viable_now",
        "center": [3.1390, 101.6869],
        "launch_phase": "Foundation",
        "population_rank": 1,
        "run_on_startup": False,
        "cores": [
            {"id": "my-kl-klcc",          "name": "KLCC / Bukit Bintang",    "center": [3.1469, 101.6962], "corridors": ["Jalan Ampang KLCC", "Bukit Bintang Clinic Corridor", "Jalan Conlay"]},
            {"id": "my-kl-bangsar",       "name": "Bangsar / Mont Kiara",    "center": [3.1191, 101.6717], "corridors": ["Jalan Bangsar Clinic Strip", "Solaris Mont Kiara", "Dutamas Jalan Kiara"]},
            {"id": "my-kl-damansara",     "name": "PJ / Damansara",          "center": [3.1193, 101.6243], "corridors": ["Jalan SS22 Damansara Jaya", "Jalan Ampang Hilir", "Empire Gallery Subang"]},
        ],
    },

    {
        "id": "my-penang",
        "country_code": "MY",
        "name": "Penang",
        "region": "Penang",
        "metro": "George Town",
        "population_context": 1800000,
        "maturity": "viable_now",
        "center": [5.4141, 100.3288],
        "launch_phase": "Major Cities",
        "population_rank": 2,
        "run_on_startup": False,
        "cores": [
            {"id": "my-pen-gurney",       "name": "Gurney Drive / Georgetown","center": [5.4327, 100.3110], "corridors": ["Gurney Plaza Clinic Corridor", "Jalan Tanjung Tokong"]},
        ],
    },

    {
        "id": "my-johor-bahru",
        "country_code": "MY",
        "name": "Johor Bahru",
        "region": "Johor",
        "metro": "Johor Bahru Metro",
        "population_context": 1800000,
        "maturity": "viable_now",
        "center": [1.4927, 103.7414],
        "launch_phase": "Major Cities",
        "population_rank": 3,
        "run_on_startup": False,
        "cores": [
            {"id": "my-jb-medini",        "name": "Medini / Tebrau",         "center": [1.4453, 103.6376], "corridors": ["Iskandar Puteri Clinic Corridor", "Tebrau Highway Strip"]},
        ],
    },

    # ══════════════════════════════════════════════════════════════════════════
    # JORDAN
    # ══════════════════════════════════════════════════════════════════════════

    {
        "id": "jo-amman",
        "country_code": "JO",
        "name": "Amman",
        "region": "Amman Governorate",
        "metro": "Greater Amman",
        "population_context": 4200000,
        "maturity": "viable_now",
        "center": [31.9522, 35.9304],
        "launch_phase": "Foundation",
        "population_rank": 1,
        "run_on_startup": False,
        "cores": [
            {"id": "jo-amm-abdoun",       "name": "Abdoun / Sweifieh",       "center": [31.9543, 35.8806], "corridors": ["Abdoun Clinic Corridor", "Sweifieh Wakalat Street", "Rainbow Street"]},
            {"id": "jo-amm-shmeisani",    "name": "Shmeisani / Tlaa Al Ali", "center": [31.9737, 35.9035], "corridors": ["Shmeisani Clinic Strip", "Tlaa Al Ali Medical Row"]},
            {"id": "jo-amm-fifth-circle",  "name": "5th Circle / Dabouq",   "center": [31.9800, 35.8639], "corridors": ["5th Circle Clinic Row", "Dabouq"]},
        ],
    },

    {
        "id": "jo-aqaba",
        "country_code": "JO",
        "name": "Aqaba",
        "region": "Aqaba Governorate",
        "metro": "Aqaba",
        "population_context": 200000,
        "maturity": "emerging",
        "center": [29.5320, 35.0063],
        "launch_phase": "Expansion",
        "population_rank": 2,
        "run_on_startup": False,
        "cores": [
            {"id": "jo-aqb-main",         "name": "Aqaba Downtown / Marina", "center": [29.5218, 35.0083], "corridors": ["Al Nahda Street Clinic Row", "Aqaba Marine Park Corridor"]},
        ],
    },

    # ══════════════════════════════════════════════════════════════════════════
    # CANADA
    # ══════════════════════════════════════════════════════════════════════════

    {
        "id": "ca-toronto",
        "country_code": "CA",
        "name": "Toronto",
        "region": "Ontario",
        "metro": "Greater Toronto Area",
        "population_context": 6700000,
        "maturity": "viable_now",
        "center": [43.6532, -79.3832],
        "launch_phase": "Foundation",
        "population_rank": 1,
        "run_on_startup": False,
        "cores": [
            {"id": "ca-tor-rosedale",     "name": "Rosedale / Yorkville",    "center": [43.6757, -79.3881], "corridors": ["Bloor Street West Yorkville", "Avenue Road Clinic Strip", "Hazelton Avenue"]},
            {"id": "ca-tor-forest-hill",  "name": "Forest Hill / Lytton Park","center": [43.6936, -79.4100], "corridors": ["Spadina Road Forest Hill", "Lytton Blvd Clinic Corridor"]},
            {"id": "ca-tor-etobicoke",    "name": "Etobicoke / Mississauga", "center": [43.5877, -79.6500], "corridors": ["Bloor Street Etobicoke", "Dundas Street West", "Erin Mills Town Centre"]},
            {"id": "ca-tor-north-york",   "name": "North York / Thornhill",  "center": [43.7684, -79.4130], "corridors": ["Yonge Street North York", "Bayview Avenue Clinic Row", "Highway 7 Thornhill"]},
        ],
    },

    {
        "id": "ca-vancouver",
        "country_code": "CA",
        "name": "Vancouver",
        "region": "British Columbia",
        "metro": "Metro Vancouver",
        "population_context": 2700000,
        "maturity": "viable_now",
        "center": [49.2827, -123.1207],
        "launch_phase": "Foundation",
        "population_rank": 2,
        "run_on_startup": False,
        "cores": [
            {"id": "ca-van-westside",     "name": "Westside / Kitsilano",    "center": [49.2655, -123.1659], "corridors": ["4th Avenue Kitsilano", "West Broadway Clinic Strip", "Kerrisdale 41st Ave"]},
            {"id": "ca-van-yaletown",     "name": "Yaletown / Coal Harbour",  "center": [49.2776, -123.1216], "corridors": ["Mainland Street Yaletown", "Davie Street", "Canada Place Clinic Row"]},
            {"id": "ca-van-burnaby",      "name": "Burnaby / Coquitlam",     "center": [49.2488, -122.9805], "corridors": ["Metrotown Kingsway", "Austin Avenue Coquitlam"]},
        ],
    },

    {
        "id": "ca-montreal",
        "country_code": "CA",
        "name": "Montreal",
        "region": "Quebec",
        "metro": "Greater Montreal",
        "population_context": 4300000,
        "maturity": "viable_now",
        "center": [45.5017, -73.5673],
        "launch_phase": "Foundation",
        "population_rank": 3,
        "run_on_startup": False,
        "cores": [
            {"id": "ca-mtl-outremont",    "name": "Outremont / Plateau",     "center": [45.5196, -73.6009], "corridors": ["Avenue Laurier Est", "Avenue du Mont-Royal", "Outremont Avenue"]},
            {"id": "ca-mtl-westmount",    "name": "Westmount / Côte-des-Neiges","center": [45.4847, -73.5978], "corridors": ["Sherbrooke Street West", "Queen Mary Road Clinic Strip"]},
        ],
    },

    {
        "id": "ca-calgary",
        "country_code": "CA",
        "name": "Calgary",
        "region": "Alberta",
        "metro": "Calgary",
        "population_context": 1600000,
        "maturity": "viable_now",
        "center": [51.0447, -114.0719],
        "launch_phase": "Major Cities",
        "population_rank": 4,
        "run_on_startup": False,
        "cores": [
            {"id": "ca-cal-mount-royal",  "name": "Mount Royal / Britannia", "center": [51.0195, -114.0840], "corridors": ["17th Avenue SW Clinic Strip", "Elbow Drive SW"]},
            {"id": "ca-cal-nw-corridor",  "name": "NW Calgary / Cochrane",   "center": [51.1281, -114.1949], "corridors": ["Shaganappi Trail NW", "Cochrane Downtown"]},
        ],
    },

    {
        "id": "ca-edmonton",
        "country_code": "CA",
        "name": "Edmonton",
        "region": "Alberta",
        "metro": "Edmonton",
        "population_context": 1500000,
        "maturity": "viable_now",
        "center": [53.5461, -113.4938],
        "launch_phase": "Major Cities",
        "population_rank": 5,
        "run_on_startup": False,
        "cores": [
            {"id": "ca-edm-whyte-ave",    "name": "Whyte Ave / Glenora",     "center": [53.5196, -113.4994], "corridors": ["82nd Avenue Whyte", "Glenora Clinic Corridor"]},
        ],
    },

    {
        "id": "ca-ottawa",
        "country_code": "CA",
        "name": "Ottawa",
        "region": "Ontario",
        "metro": "National Capital Region",
        "population_context": 1400000,
        "maturity": "viable_now",
        "center": [45.4215, -75.6972],
        "launch_phase": "Major Cities",
        "population_rank": 6,
        "run_on_startup": False,
        "cores": [
            {"id": "ca-ott-glebe",        "name": "The Glebe / Westboro",    "center": [45.3987, -75.6917], "corridors": ["Bank Street Glebe", "Richmond Road Westboro Clinic Strip"]},
        ],
    },

    # ══════════════════════════════════════════════════════════════════════════
    # MEXICO
    # ══════════════════════════════════════════════════════════════════════════

    {
        "id": "mx-mexico-city",
        "country_code": "MX",
        "name": "Mexico City",
        "region": "CDMX",
        "metro": "Valle de México",
        "population_context": 21600000,
        "maturity": "viable_now",
        "center": [19.4326, -99.1332],
        "launch_phase": "Foundation",
        "population_rank": 1,
        "run_on_startup": False,
        "cores": [
            {"id": "mx-mex-polanco",      "name": "Polanco / Lomas",          "center": [19.4334, -99.1913], "corridors": ["Presidente Masaryk", "Pedregal de San Ángel", "Avenida Presidente Masaryk"]},
            {"id": "mx-mex-condesa",      "name": "La Condesa / Roma Norte",  "center": [19.4152, -99.1652], "corridors": ["Avenida Ámsterdam", "Álvaro Obregón Clinic Strip", "Orizaba"]},
            {"id": "mx-mex-santa-fe",     "name": "Santa Fe / Interlomas",    "center": [19.3610, -99.2650], "corridors": ["Vasco de Quiroga Santa Fe", "Boulevar Miguel de Cervantes Saavedra"]},
        ],
    },

    {
        "id": "mx-guadalajara",
        "country_code": "MX",
        "name": "Guadalajara",
        "region": "Jalisco",
        "metro": "Guadalajara Metro",
        "population_context": 5200000,
        "maturity": "viable_now",
        "center": [20.6597, -103.3496],
        "launch_phase": "Major Cities",
        "population_rank": 2,
        "run_on_startup": False,
        "cores": [
            {"id": "mx-gdl-providencia",  "name": "Providencia / Chapalita", "center": [20.6808, -103.4089], "corridors": ["Avenida Providencia Clinic Strip", "López Mateos Norte"]},
            {"id": "mx-gdl-zapopan",      "name": "Zapopan / Andares",       "center": [20.6889, -103.4150], "corridors": ["Avenida Patria", "Andares Clinic Corridor"]},
        ],
    },

    {
        "id": "mx-monterrey",
        "country_code": "MX",
        "name": "Monterrey",
        "region": "Nuevo León",
        "metro": "Monterrey Metro",
        "population_context": 5300000,
        "maturity": "viable_now",
        "center": [25.6866, -100.3161],
        "launch_phase": "Major Cities",
        "population_rank": 3,
        "run_on_startup": False,
        "cores": [
            {"id": "mx-mty-san-pedro",    "name": "San Pedro Garza García",   "center": [25.6571, -100.3673], "corridors": ["Calzada del Valle", "Avenida Vasconcelos Clinic Strip", "Pedro Infante"]},
            {"id": "mx-mty-valle-oriente","name": "Valle Oriente / Santa Catarina","center": [25.6532, -100.2871], "corridors": ["Gómez Morín Clinic Corridor", "Revolución Avenue"]},
        ],
    },

    {
        "id": "mx-cancun",
        "country_code": "MX",
        "name": "Cancún",
        "region": "Quintana Roo",
        "metro": "Cancún Metro",
        "population_context": 1000000,
        "maturity": "viable_now",
        "center": [21.1619, -86.8515],
        "launch_phase": "Major Cities",
        "population_rank": 4,
        "run_on_startup": False,
        "cores": [
            {"id": "mx-cun-hotel-zone",   "name": "Hotel Zone / Downtown",   "center": [21.1380, -86.7800], "corridors": ["Kukulcán Boulevard Clinic Row", "Avenida Cobá Downtown"]},
        ],
    },

    {
        "id": "mx-puebla",
        "country_code": "MX",
        "name": "Puebla",
        "region": "Puebla",
        "metro": "Puebla Metro",
        "population_context": 3200000,
        "maturity": "scaling",
        "center": [19.0414, -98.2063],
        "launch_phase": "Expansion",
        "population_rank": 5,
        "run_on_startup": False,
        "cores": [
            {"id": "mx-pue-angelopolis",  "name": "Angelópolis / Lomas",     "center": [19.0195, -98.2340], "corridors": ["Boulevar Atlixcáyotl Clinic Corridor", "Periférico Ecológico"]},
        ],
    },

    # ══════════════════════════════════════════════════════════════════════════
    # BRAZIL
    # ══════════════════════════════════════════════════════════════════════════

    {
        "id": "br-sao-paulo",
        "country_code": "BR",
        "name": "São Paulo",
        "region": "São Paulo State",
        "metro": "Greater São Paulo",
        "population_context": 22400000,
        "maturity": "viable_now",
        "center": [-23.5505, -46.6333],
        "launch_phase": "Foundation",
        "population_rank": 1,
        "run_on_startup": False,
        "cores": [
            {"id": "br-spo-jardins",      "name": "Jardins / Itaim Bibi",    "center": [-23.5595, -46.6627], "corridors": ["Rua Oscar Freire", "Avenida Brigadeiro Faria Lima", "Haddock Lobo Clinic Strip"]},
            {"id": "br-spo-vila-madalena","name": "Vila Madalena / Pinheiros","center": [-23.5474, -46.6899], "corridors": ["Rua Wisard", "Avenida Pedroso de Moraes"]},
            {"id": "br-spo-morumbi",      "name": "Morumbi / Granja Viana",  "center": [-23.6153, -46.7176], "corridors": ["Avenida Giovanni Gronchi", "Estrada dos Romeiros Granja Viana"]},
            {"id": "br-spo-paulista",     "name": "Paulista / Higienópolis", "center": [-23.5631, -46.6544], "corridors": ["Avenida Paulista Clinic Corridor", "Rua da Consolação"]},
        ],
    },

    {
        "id": "br-rio-de-janeiro",
        "country_code": "BR",
        "name": "Rio de Janeiro",
        "region": "Rio de Janeiro State",
        "metro": "Greater Rio",
        "population_context": 13700000,
        "maturity": "viable_now",
        "center": [-22.9068, -43.1729],
        "launch_phase": "Foundation",
        "population_rank": 2,
        "run_on_startup": False,
        "cores": [
            {"id": "br-rio-ipanema",      "name": "Ipanema / Leblon",        "center": [-22.9839, -43.2039], "corridors": ["Rua Visconde de Pirajá Ipanema", "Rua Dias Ferreira Leblon", "Lagoa Rodrigo de Freitas"]},
            {"id": "br-rio-barra",        "name": "Barra da Tijuca / Recreio","center": [-23.0004, -43.3660], "corridors": ["Avenida das Américas Clinic Strip", "Barra Shopping Corridor"]},
            {"id": "br-rio-botafogo",     "name": "Botafogo / Flamengo",     "center": [-22.9461, -43.1913], "corridors": ["Rua Voluntários da Pátria Botafogo", "Praia do Flamengo"]},
        ],
    },

    {
        "id": "br-belo-horizonte",
        "country_code": "BR",
        "name": "Belo Horizonte",
        "region": "Minas Gerais",
        "metro": "RMBH",
        "population_context": 6000000,
        "maturity": "viable_now",
        "center": [-19.9167, -43.9345],
        "launch_phase": "Major Cities",
        "population_rank": 3,
        "run_on_startup": False,
        "cores": [
            {"id": "br-bhi-savassi",      "name": "Savassi / Lourdes",       "center": [-19.9400, -43.9350], "corridors": ["Rua Antônio de Albuquerque Savassi", "Avenida do Contorno Clinic Row"]},
        ],
    },

    {
        "id": "br-curitiba",
        "country_code": "BR",
        "name": "Curitiba",
        "region": "Paraná",
        "metro": "Curitiba Metro",
        "population_context": 3700000,
        "maturity": "viable_now",
        "center": [-25.4284, -49.2733],
        "launch_phase": "Major Cities",
        "population_rank": 4,
        "run_on_startup": False,
        "cores": [
            {"id": "br-cwb-batel",        "name": "Batel / Bigorrilho",      "center": [-25.4393, -49.2972], "corridors": ["Avenida do Batel", "Rua Mateus Leme Clinic Strip"]},
        ],
    },

    {
        "id": "br-porto-alegre",
        "country_code": "BR",
        "name": "Porto Alegre",
        "region": "Rio Grande do Sul",
        "metro": "Porto Alegre Metro",
        "population_context": 4300000,
        "maturity": "viable_now",
        "center": [-30.0346, -51.2177],
        "launch_phase": "Major Cities",
        "population_rank": 5,
        "run_on_startup": False,
        "cores": [
            {"id": "br-poa-moinhos",      "name": "Moinhos de Vento / Petrópolis","center": [-30.0231, -51.2028], "corridors": ["Rua Padre Chagas", "Avenida Independência Clinic Row"]},
        ],
    },

    {
        "id": "br-brasilia",
        "country_code": "BR",
        "name": "Brasília",
        "region": "Federal District",
        "metro": "Brasília",
        "population_context": 3100000,
        "maturity": "viable_now",
        "center": [-15.7942, -47.8822],
        "launch_phase": "Major Cities",
        "population_rank": 6,
        "run_on_startup": False,
        "cores": [
            {"id": "br-bsb-lago-sul",     "name": "Lago Sul / Sudoeste",     "center": [-15.8462, -47.8817], "corridors": ["SHIS QL Clinic Corridor", "SQSW Sudoeste Strip"]},
        ],
    },

    {
        "id": "br-fortaleza",
        "country_code": "BR",
        "name": "Fortaleza",
        "region": "Ceará",
        "metro": "Greater Fortaleza",
        "population_context": 4100000,
        "maturity": "viable_now",
        "center": [-3.7319, -38.5267],
        "launch_phase": "Expansion",
        "population_rank": 7,
        "run_on_startup": False,
        "cores": [
            {"id": "br-for-meireles",     "name": "Meireles / Aldeota",      "center": [-3.7283, -38.5042], "corridors": ["Avenida Beira Mar Clinic Corridor", "Rua Ildefonso Albano Aldeota"]},
        ],
    },

    {
        "id": "br-salvador",
        "country_code": "BR",
        "name": "Salvador",
        "region": "Bahia",
        "metro": "Salvador Metro",
        "population_context": 4000000,
        "maturity": "viable_now",
        "center": [-12.9714, -38.5014],
        "launch_phase": "Expansion",
        "population_rank": 8,
        "run_on_startup": False,
        "cores": [
            {"id": "br-ssd-pituba",       "name": "Pituba / Barra",          "center": [-13.0101, -38.4592], "corridors": ["Avenida ACM Pituba", "Avenida 7 de Setembro Barra"]},
        ],
    },
]
