# Make a dictionary containing the necessary input fields specific to each topic
topic_fields = {
    "311 CALL TYPE": None,
    "311 NOTEBOOK UPDATE": None,
    "ADDRESS VALIDATION": None,
    "AUTO CITYVIEW TEST": None,
    "CHATTY": None,
    "CONSTITUENT SERVICES - INTAKE": None,
    "CONSUMER FRAUD": None,
    "DAMAGE BY CITY CREW": [
        "damage_crew1",
        "damage_crew2",
        "damage_crew3",
        "damage_crew4",
        "damage_crew5",
        "vehicle_type1",
        "vehicle_type2"
    ],
    "DOCUMENTATION ONLY": None,
    "EMAIL TO SERVICE REQUEST": None,
    "FLOOD RISK MAP UPDATE": None,
    "MANUAL CITYVIEW TEST": None,
    "RECYCLE ADDRESS": None,
    "SEWER BILLING (SHELLY) REFUND/ADJUSTMENT/CREDIT": None,
    "VITA INFORMATION": None,
    "BIOSOLIDS - SPILL ON THE ROADWAY": [
        "spill_bio1"
    ],
    "ODOR COMPLAINT - BIOSOLIDS": [
        "odor_bio1"
    ],
    "REQUEST FOR INFORMATION - BIOSOLIDS": [
        "request_bio1",
        "request_bio2"
    ],
    "URGENT COMPLAINTS - BIOSOLIDS": None,
    "ABANDONED OR INOPERABLE VEHICLE (PRIVATE PROPERTY ONLY)": [
        "abandoned_vehicle1",
        "abandoned_vehicle2",
        "abandoned_vehicle3",
        "abandoned_vehicle4",
        "abandoned_vehicle5",
        "abandoned_vehicle6"
    ],
    "CONSTRUCTION SITE HOURS COMPLAINT": [
        "contractor1",
        "contractor2",
        "contractor3"
    ],
    "HOUSING VIOLATIONS": [
        "housing_violation1",
        "housing_violation2",
        "housing_violation3",
        "housing_violation4",
        "housing_violation5",
    ],
    "ILLEGAL DUMPING": [
        "illegal_dumping1",
        "illegal_dumping2"
    ],
    "ILLEGAL OPERATION OF A SHORT-TERM VACATION RENTAL": None,
    "ILLEGAL SIGN": [
        "issue_location1"
    ],
    "OVERGROWTH PRIVATE PROPERTY": [
        "property_overgrowth1",
        "property_overgrowth2",
        "property_overgrowth3",
        "property_overgrowth4"
    ],
    "ZONING VIOLATIONS": None,
    "DRIVER CALL IN": None,
    "LONG TERM WORK ORDER - DESIGN ENGINEERING": None,
    "SHORT TERM WORK ORDER - DESIGN ENGINEERING": None,
    "CUSTODIAL SERVICE REQUEST": [
        "custodial1",
        "city_building1",
        "city_building2"
    ],
    "ELECTRICAL OR LIGHTING SERVICE REQUEST": [
        "electrical1",
        "city_building1",
        "city_building2"
    ],
    "ELEVATOR SERVICE REQUEST": [
        "elevator_building1",
        "city_building1"
    ],
    "EVENT SETUP REQUEST": [
        "event_setup1",
        "event_setup2",
        "event_setup3",
        "event_setup4"
    ],
    "FURNITURE MOVE OR WORKSPACE RECONFIGURATION": [
        "furniture_move1",
        "furniture_move2",
        "furniture_move3",
        "furniture_move4",
        "furniture_move5",
        "furniture_move6",
        "furniture_move7",
        "furniture_move8",
        "furniture_move9"
    ],
    "HEATING AND AIR CONDITIONING SERVICE REQUEST": [
        "hvac1",
        "hvac2",
        "hvac3",
        "city_building1",
        "city_building2"
    ],
    "LOCKSMITH/ACCESS CONTROL SERVICE REQUEST": [
        "city_building1",
        "city_building2",
        "access_building1"
    ],
    "PARKING AND PARKING LOT ACCESS SERVICE REQUEST": [
        "access_parking1",
        "access_parking2"
    ],
    "PEST CONTROL REQUEST": [
        "city_building1",
        "city_building2"
    ],
    "PLUMBING SERVICE REQUEST": [
        "city_building1",
        "city_building2",
        "plumbing1"
    ],
    "ROOF LEAK OR ROOF REPAIR SERVICE REQUEST": [
        "city_building1",
        "city_building2",
        "roof_leak1"
    ],
    "SURPLUS PROPERTY PICK-UP REQUEST": [
        "furniture_surplus1",
        "furniture_surplus2",
        "furniture_surplus3"
    ],
    "CONTRACTOR COMPLAINT": [
        "contractor1",
        "contractor2",
        "contractor3"
    ],
    "DRIVER SAFETY COMPLAINT": [
        "vehicle_type1",
        "vehicle_type2",
        "driver_safety1",
        "driver_safety2",
        "driver_safety3",
        "driver_safety4"
    ],
    "FEEDBACK AND QUESTIONS": None,
    "INQUIRY ON CLOSED SERVICE REQUEST": None,
    "SUPERVISOR CALL BACK": None,
    "SUPERVISOR CALL BACK SEWER": None,
    "FUELING SYSTEM ASSISTANCE": None,
    "VEHICLE SERVICE - ROUTINE MAINTENANCE": None,
    "WEBSITE ERRORS": None,
    "RADIO SERVICE REQUEST": None,
    "NEIGHBORHOOD SERVICES QUALITY OF LIFE": [
        "PhoneNumber",
        "ContactPerson",
        "EmailAddress"
    ],
    "PUBLIC PARK WORK REQUEST": [
        "parks_maint1",
        "parks_maint2"
    ],
    "RIVERFRONT EVENT (500+)": None,
    "DISTRESSED PAVEMENT": [
        "distressed_pavement1"
    ],
    "SPECIAL EVENTS/WORK ZONE STREET CLOSURES": None,
    "STREET CLEANUP": [
        "street_cleanup1",
        "street_cleanup2"
    ],
    "DRAINAGE JOB/WORK ORDER INQUIRY": [
        "workorder_inquiry1",
        "workorder_inquiry2",
        "ContactPerson"
    ],
    "EROSION, DRAINAGE ON A CONSTRUCTION SITE": [
        "issue_location1"
    ],
    "STORMWATER FACILITY INSPECTION": [
        "stormwater_facility1",
        "stormwater_facility2",
        "stormwater_facility3",
        "stormwater_facility4"
    ],
    "BAD ODOR COMPLAINT (SEWER ONLY)": [
        "bad_odor1",
        "bad_odor2",
        "bad_odor3",
        "bad_odor4"
    ],
    "EROSION AND DRAINAGE": [
        "drainage_issue1",
        "drainage_issue2",
        "drainage_issue3",
        "drainage_issue4",
        "drainage_issue5"
    ],
    "FLOODING": [
        "flooding1",
        "flooding2",
        "flooding3",
        "flooding4"
    ],
    "GRINDER PUMP STATION REPAIR": [
        "grinder_pump1",
        "grinder_pump2",
        "grinder_pump3"
    ],
    "MANHOLE PROBLEM": [
        "manhole1"
    ],
    "SEWER BACKUP": [
        "sewer_backup1",
        "sewer_backup2",
        "sewer_backup3"
    ],
    "SEWER BILLING - 311 REVIEW": None,
    "SIZE DRIVEWAY PIPE/TILE": None,
    "STORM DRAINAGE PROBLEM": [
        "stormdrain_problem1",
        "stormdrain_problem2"
    ],
    "STORM DRAINAGE VIOLATION (LEAVES)": [
        "stormdrain_violation1",
        "stormdrain_violation2"
    ],
    "STORM GRATES": [
        "stormgrate1",
        "stormgrate2"
    ],
    "SUNKEN SURFACE AREA": [
        "sunken_surface1",
        "sunken_surface2"
    ],
    "WATER POLLUTION": [
        "water_pollution1",
        "water_pollution2",
        "water_pollution3"
    ],
    "ALLEY MAINTENANCE": [
        "alley_maint1"
    ],
    "DEAD ANIMAL PICKUP": [
        "dead_animal1",
        "dead_animal2"
    ],
    "DRIVEWAY": [
        "driveway1",
        "driveway2"
    ],
    "GRAFFITI REMOVAL": [
        "graffiti_removal1",
        "graffiti_removal2"
    ],
    "GUARDRAIL REQUEST OR REPAIR": [
        "guardrail1",
        "guardrail2"
    ],
    "POTHOLES": [
        "pothole1",
        "pothole2",
        "pothole3",
        "pothole4",
        "pothole5"
    ],
    "ROADSIDE MOWING": [
        "roadside_mowing1"
    ],
    "ROADWAY SIGHT OBSTRUCTION": [
        "site_obstruction1",
        "site_obstruction2",
        "site_obstruction3",
        "direction1"
    ],
    "SIDEWALKS": [
        "sidewalk1",
        "sidewalk2",
        "issue_location1"
    ],
    "SNOW AND ICE REMOVAL": [
        "streetlocation",
        "snow_removal1",
        "snow_removal2",
        "snow_removal3"
    ],
    "STEEL/METAL PLATES IN ROADWAY": [
        "metal_plate1"
    ],
    "STREET LANE MARKINGS": [
        "lane_markers1",
        "lane_markers2"
    ],
    "STREET LIGHTS (NOT TRAFFIC SIGNALS)": [
        "street_lights1",
        "street_lights2",
        "street_lights3",
        "street_lights4"
    ],
    "STREET SWEEPING": [
        "street_sweeping1",
        "street_sweeping2"
    ],
    "TIRES - ROADSIDE": [
        "tire_pickup1",
        "tire_pickup2"
    ],
    "VETERANS BRIDGE FLAG MAINTENANCE": [
        "flag_maint1"
    ],
    "LONG TERM WORK ORDER - TRAFFIC OPERATIONS": None,
    "SHORT TERM WORK ORDER - TRAFFIC OPERATIONS": None,
    "FLASHING BEACONS": [
        "flash_beacon1",
        "flash_beacon2",
        "flash_beacon3"
    ],
    "TRAFFIC CALMING": [
        "traffic_calming1"
    ],
    "TRAFFIC CONTROL FOR WORK ZONE": [
        "work_zone1",
        "work_zone2"
    ],
    "TRAFFIC SIGNALS": [
        "direction1",
        "traffic_signal1",
        "traffic_signal2",
        "traffic_signal3"
    ],
    "TRAFFIC SIGNS": [
        "traffic_sign1",
        "traffic_sign2"
    ],
    "TREE CONCERN OR QUESTION": [
        "tree_location1",
        "tree_concern2"
    ],
    "TREE FALLEN/BRANCH": [
        "fallen_tree1",
        "fallen_tree2",
        "fallen_tree3",
        "fallen_tree4"
    ],
    "TREE PRUNING": [
        "tree_location1",
        "tree_pruning1"
    ],
    "TREE REMOVAL": [
        "tree_location1",
        "tree_removal1"
    ],
    "BAGGED YARD WASTE": [
        "material_location1"
    ],
    "BRUSH COLLECTION": [
        "material_location1"
    ],
    "BULK TRASH": [
        "CityviewStatus",
        "material_location1"
    ],
    "GARBAGE AND RECYCLING ASSISTANCE": [
        "garbage_assistance1"
    ],
    "GARBAGE CONTAINER REMOVAL": [
        "garbage_removal1"
    ],
    "LITTER - PRIVATE PROPERTY": [
        "property_litter1",
        "property_litter2",
        "property_litter3",
        "property_litter4",
        "property_litter5",
        "property_litter6",
    ],
    "LOOSE LEAF COLLECTION": [
        "loose_leaf1"
    ],
    "MISSED GARBAGE": [
        "incidentTime",
        "missed_garbage"
    ],
    "MISSED RECYCLE": None,
    "NEW GARBAGE CONTAINER": [
        "new_bin1",
        "new_bin2",
        "new_bin3",
        "new_bin4",
        "new_bin5"
    ],
    "NEW RECYCLE CONTAINER": [
        "new_bin1",
        "new_bin2",
        "new_bin3",
        "new_bin4",
        "new_bin5"            
    ],
    "RECYCLE CONTAINER REMOVAL": [
        "recycle_removal1"
    ],
    "RECYCLE CONTAINER REPAIR": [
        "bin_repair1"
    ]
}

# Make a dictionary containing the possible values for the fields that aren't arbitrary
field_values = {
    "abandoned_vehicle4": [
        "Yes", 
        "No"
    ],
    "abandoned_vehicle5": [
        "Yes", 
        "No"
    ],
    "abandoned_vehicle6": [
        "Yes", 
        "No"
    ],
    "housing_violation2": [
        "Yes", 
        "No", 
        "Unknown"
    ],
    "housing_violation3": [
        "Yes", 
        "No"
    ],
    "housing_violation4": [
        "Yes", 
        "No", 
        "Unknown"
    ],
    "illegal_dumping1": [
        "Yes", 
        "No", 
        "Unknown"
    ],
    "illegal_dumping2": [
        "Yes", 
        "No"
    ],
    "property_overgrowth1": [
        "Occupied", 
        "Vacant", 
        "Unknown"
    ],
    "property_overgrowth2": [
        "Yes", 
        "No", 
        "Unknown"
    ],
    "property_overgrowth3": [
        "Yes", 
        "No"
    ],
    "custodial1": [
        "Restock paper supplies",
        "Spill cleanup requested",
        "General cleaning requested",
        "Deep clean or refinish requested",
        "Other request"
    ],
    "city_building1": [
        "Avondale Community Center",
        "Bessie Smith Cultural Center",
        "Brainerd Golf Cart Bldg",
        "Brainerd Golf Course Club House",
        "Brainerd Golf Course Maintenance Building",
        "Brown Acres Club House",
        "Brown Acres Maintenance Building",
        "Chris Ramsey Community Center",
        "Chris Ramsey Pool",
        "Carver Community Center",
        "Carver Pool",
        "Champions Club Tennis Center",
        "City Council Building",
        "City Hall",
        "City Hall Annex",
        "City Hall Midtown",
        "Development Resource Center",
        "Dr. Carol B. Berz Family Justice Center",
        "East Chattanooga Community Center",
        "East Lake Community Center",
        "Eastdale Community Center",
        "Fleet Fueling Station - Amnicola",
        "Fleet Fueling Station - 12th Street",
        "Fleet Garage - 12th Street",
        "Fleet Garage - Amnicola",
        "Fleet Tire Shop - Amnicola",
        "Fleet Tire Shop - 12th Street",
        "Frances B Wyatt Arts & Craft Bldg",
        "Frances B Wyatt Community Center",
        "Facilities Management Building",
        "Glenwood Community Center",
        "Heritage House",
        "Hixson Community Center",
        "John A Patten Community Center",
        "Lindsay Street Building",
        "North Chattanooga Community Center",
        "North River Civic Center",
        "Philip Grymes Outdoor Chattanooga Center",
        "Shepherd Community Center",
        "South Chattanooga Indoor Pool",
        "Summit Complex Maintenance Building",
        "The Summit Softball Complex A",
        "The Summit Softball Complex B",
        "The Summit Softball Complex C",
        "Traffic Operations Building",
        "Tyner Community Center",
        "Warner Park Concession - Cooke Field",
        "Warner Park Fieldhouse",
        "Warner Park Frost Stadium",
        "Warner Park Pool",
        "Washington Hills Community Center",
        "Watkins Street Facility",
        "Watkins Street Warehouse",
        "WellAdvantage Health and Wellness Center",
        "Other City Building"
    ],
    "electrical1": [
        "Power Outage",
        "Light Burned Out",
        "Receptacle or swith issue", # Should be "switch", but this typo was present on the editcase.php page
        "Tripped circuit breaker",
        "New electrical service request",
        "Other request"
    ],
    "furniture_move1": [
        "Yes",
        "No",
        "Unknown"
    ],
    "furniture_move2": [
        "Desk",
        "Table",
        "Chairs",
        "Cubical",
        "Filing Cabinet",
        "Other Furniture"
    ],
    "furniture_move3": [
        "Yes",
        "No",
        "Unknown"
    ],
    "furniture_move6": [
        "Yes",
        "No",
        "Unknown"
    ],
    "furniture_move8": [
        "Yes",
        "No",
        "Unknown"
    ],
    "hvac1": [
        "Occupant Comfort (Too Hot)",
        "Occupant Comfort (Too Cold)",
        "Equipment Malfunction"
    ],
    "access_parking1": [
        "Parking Lot A (City Hall or City Council)",
        "Parking Lot B (City Hall)",
        "Parking Lot C (City Hall)",
        "Parking Lot D (City Hall)",
        "King Street Parking Lot (DRC)",
        "CARTA Parking Garage (DRC)",
        "Annex Parking Lot (City Hall Annex)",
        "Other Parking Lot"
    ],
    "plumbing1": [
        "Plumbing Leak (Emergency)",
        "Plumbing Leak (Non-Emergency)",
        "Sewage Backup (Emergency)",
        "Plumbing Fixture Maintenance",
        "Other Plumbing Issue"
    ],
    "furniture_surplus2": [
        "Yes",
        "No",
        "Unknown"
    ],
    "vehicle_type2": [
        "Brush truck",
        "Garbage truck",
        "Passenger vehicle",
        "Pickup truck",
        "Other vehicle"
    ],
    "driver_safety3": [
        "Yes",
        "No"
    ],
    "driver_safety4": [
        "Blocked intersection",
        "Aggressive driving",
        "Illegally parked",
        "Not using signals",
        "Ran stop light",
        "Ran stop sign",
        "Reckless driving",
        "Seat belt violation",
        "Following too closely",
        "Speeding",
        "Other"
    ],
    "parks_maint1": [
        "Coolidge Park",
        "Greenway Farm",
        "Miller Park",
        "Montague Park Sculpture Fields",
        "Renaissance Park",
        "Ross's Landing",
        "Tennessee Riverpark",
        "Walnut Street Bridge",
        "Warner Park",
        "Avondale Park",
        "Batters Place Tennis Courts",
        "Benham Williams Park",
        "Boulevard Park",
        "Brainerd Park",
        "Caruthers Park",
        "Carver Park",
        "Champions Club",
        "Chattanooga Chew Chew",
        "Chattown Skate Park",
        "Church Street Park",
        "Delong Park",
        "DuPont Park",
        "East Chattanooga Park",
        "East Lake Center Park",
        "East Lake Park",
        "Eastdale Park",
        "Fort Negley Park",
        "Frances B Wyatt Park",
        "Frederick Park",
        "Glenwood Park",
        "Harris Johnson Park",
        "Hill City Park",
        "Hixson Ballfields",
        "Hixson Park",
        "Inspiration Park",
        "Jack Benson Heritage Park",
        "Jefferson Park",
        "John A Patten Park",
        "Lake Hills Park",
        "Lakeside Ballfields",
        "Lookout Valley Park",
        "Main Terrain Park",
        "Memorial Auditorium Mini Park",
        "Milliken Park",
        "Mountain Creek Road Park",
        "Murray Hills Park",
        "North Chattanooga Park",
        "North River Soccer Complex",
        "Overlook Park",
        "Park City Park",
        "Patten Parkway",
        "Perkins Park",
        "Phillips Park",
        "Piney Woods",
        "Portland Park",
        "Pringle Park",
        "Ridgedale Safewalk",
        "Rivermont Park",
        "Riverside Park",
        "Riverview Bird Sanctuary",
        "Riverview Park",
        "Roy Nelms Park",
        "Shepherd Park",
        "South Chattanooga Park",
        "Southside Community Park",
        "St. Elmo Park",
        "Stringers Ridge",
        "Sylvan Park",
        "Tacoa Park",
        "Tatum Park",
        "Ted Bryant Park",
        "The Sinks Disc Golf Course",
        "TN Aquarium Plaza",
        "Tyner Park",
        "Urban Art Garden",
        "Washington Hills Park",
        "Watkins Street Park",
        "Westside Park",
        "Whiteside Park"
    ],
    "street_cleanup1": [
        "Accident debris",
        "Construction material",
        "Garbage or furniture",
        "Tree limbs",
        "Other"
    ],
    "street_cleanup2": [
        "Yes",
        "No"
    ],
    "stormwater_facility1": [
        "Yes",
        "No"
    ],
    "bad_odor4": [
        "Yes",
        "No",
        "Unknown"
    ],
    "drainage_issue1": [
        "Under construction",
        "Already developed"
    ],
    "flooding1": [
        "Yes",
        "No",
        "Don't Know"
    ],
    "flooding2": [
        "Yes",
        "No"
    ],
    "flooding4": [
        "Yes",
        "No"
    ],
    "grinder_pump1": [
        "Yes",
        "No",
        "Unknown"
    ],
    "grinder_pump2": [
        "Yes",
        "No",
        "Unknown"
    ],
    "grinder_pump3": [
        "Yes",
        "No"
    ],
    "manhole1": [
        "Water overflowing",
        "Lid or cover missing",
        "Lid or cover broken loose or rattling",
        "Lid or cover askew",
        "Lid or cover set aside",
        "Surface around manhole in need of repair",
        "Height adjustment needed"
    ],
    "sewer_backup1": [
        "Inside",
        "Outside"
    ],
    "stormdrain_problem1": [
        "Roadside structure",
        "Manhole",
        "Catch Basin",
        "Curb Inlet",
        "Section of Pipe"
    ],
    "stormdrain_problem2": [
        "In front",
        "Behind",
        "Beside",
        "Other"
    ],
    "stormdrain_violation1": [
        "Ditch",
        "Street",
        "Other"
    ],
    "stormdrain_violation2": [
        "Yes",
        "No"
    ],
    "stormgrate1": [
        "Broken",
        "Missing",
        "Flipped-Up",
        "Fallen In"
    ],
    "stormgrate2": [
        "Yes",
        "No"
    ],
    "sunken_surface1": [
        "Yes",
        "No",
        "Don't Know"
    ],
    "alley_maint1": [
        "Pothole or Surface",
        "Litter",
        "Overgrowth",
        "Other"
    ],
    "driveway1": [
        "Yes",
        "No",
        "Don't Know"
    ],
    "driveway2": [
        "Concrete",
        "Asphalt",
        "Don't Know"
    ],
    "graffiti_removal1": [
        "Public",
        "Private",
        "Unknown"
    ],
    "guardrail1": [
        "New Guardrail",
        "Guardrail Repair"
    ],
    "pothole1": [
        "Alley",
        "Bike Lane",
        "Intersection",
        "Shoulder",
        "Street"
    ],
    "pothole2": [
        "Depressions in the pavement",
        "Pothole",
        "Rough pavement",
        "Sinkhole",
        "Other"
    ],
    "pothole3": [
        "Yes",
        "No"
    ],
    "pothole4": [
        "Yes",
        "No"
    ],
    "pothole5": [
        "Yes",
        "No",
        "Unknown"
    ],
    "roadside_mowing1": [
        "Yes",
        "No",
        "Unknown"        
    ],
    "site_obstruction1": [
        "Curve",
        "Embankment",
        "Fence",
        "Parked vehicle",
        "Sign",
        "Wall",
        "Other"
    ],
    "direction1": [
        "North",
        "East",
        "South",
        "West"
    ],
    "sidewalk2": [
        "Yes",
        "No"
    ],
    "streetlocation": [
        "Alley",
        "bike lane",
        "intersection",
        "shoulder",
        "street",
        "bridge",
        "curve",
        "hill",
        "tunnel"
    ],
    "snow_removal1": [
        "Yes",
        "No"
    ],
    "snow_removal2": [
        "Yes",
        "No",
        "Unknown"
    ],
    "snow_removal3": [
        "Bridge",
        "Curve",
        "Hill",
        "Intersection",
        "Tunnel",
        "Other"
    ],
    "metal_plate1": [
        "Shifted plates",
        "Loud noises",
        "Dangerous conditions",
        "Other issue"
    ],
    "lane_markers1": [
        "Repaint faded lines or symbols",
        "paint new symbols",
        "Make a change to existing lines or symbols"
    ],
    "lane_markers2": [
        "Stop bars",
        "Yield bars",
        "White skip lines",
        "Yellow skip lines",
        "White solid lines",
        "Yellow solid lines",
        "Bike symbols",
        "Turn arrows",
        "Parking stalls",
        "Other"
    ],
    "street_lights1": [
        "New",
        "Broken"
    ],
    "street_sweeping1": [
        "Yes",
        "No"
    ],
    "tire_pickup1": [
        "Less than 10",
        "10-24",
        "25-50",
        "More than 50"
    ],
    "tire_pickup2": [
        "Yes",
        "No"
    ],
    "flash_beacon1": [
        "School/Overhead/Pedestrian"
    ],
    "traffic_signal1": [
        "Signal change",
        "New traffic signal",
        "Traffic signal bulb out",
        "Traffic signal damaged",
        "Traffic signal malfunction",
        "Traffic signal timing"
    ],
    "traffic_sign1": [
        "New Sign",
        "Change Sign",
        "Sign Damage",
    ],
    "traffic_sign2": [
        "Missing",
        "Down",
        "Illegible"
    ],
    "tree_location1": [
        "Alley",
        "City Park",
        "Ditch",
        "Median",
        "Private Property",
        "Roadway",
        "Sidewalk",
        "Other location"
    ],
    "tree_concern2": [
        "Yes",
        "No"
    ],
    "fallen_tree1": [
        "Yes",
        "No"
    ],
    "fallen_tree3": [
        "Roadway (blocking traffic)",
        "Roadside (not blocking traffic)",
        "Sidewalk",
        "Bike Lane",
        "Alley",
        "Park",
        "Lodged in a tree or other structure"
    ],
    "fallen_tree4": [
        "Yes",
        "No",
        "Unknown"
    ],
    "tree_pruning1": [
        "Blocking business signs",
        "Blocking traffic signal",
        "Tree limbs hitting vehicle",
        "Remove dead or broken branches"
    ],
    "material_location1": [
        "Front",
        "Side Street",
        "Rear",
        "Across the Street"
    ],
    "CityviewStatus": [
        "New",
        "Open",
        "In Progress",
        "Closed"
    ],
    "garbage_assistance1": [
        "Back door",
        "Side Door",
        "Fence",
        "Gate",
        "Carport",
        "Other"
    ],
    "street_litter2": [
        "On the roadway",
        "One the side of the road", # Should be "on", but this typo is on the editcase.php page
        "On the sidewalk",
        "Other location"
    ],
    "property_litter1": [
        "Private property",
        "Alley",
        "Roadside",
        "Street",
        "Sidewalk",
        "Other"
    ],
    "property_litter3": [
        "Yes",
        "No"
    ],
    "property_litter4": [
        "Yes",
        "No"
    ],
    "missed_garbage": [
        "Yes",
        "No"
    ],
    "new_bin2": [
        "Yes",
        "No"
    ],
    "new_bin3": [
        "Yes",
        "No"
    ],
    "new_bin4": [
        "Yes",
        "No"
    ],
    "new_bin5": [
        "Yes",
        "No"
    ],
    "bin_repair1": [
        "Lid",
        "Wheel",
        "Body"
    ],
    "damage_crew1": [
        "Yes",
        "No"
    ],
    "spill_bio1": [
        "Biosolids spilled into roadways",
        "Biosolids tracking onto roadways",
        "Truck overturned"
    ],
    "odor_bio1": [
        "Yes",
        "No"
    ],
    "request_bio1": [
        "What is in the product?",
        "How do I get Biosolids?",
        "Are you spreading in my area?",
        "Other question"
    ]
}

def get_topic_field_info():
    return topic_fields, field_values