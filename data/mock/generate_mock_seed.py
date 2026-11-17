import json
from pathlib import Path

DESTINATIONS = [
    {
        "id": "ooty",
        "name": "Ooty",
        "state": "Tamil Nadu",
        "lat": 11.4102,
        "lon": 76.6950,
        "best_season": "October to June",
        "approx_daily_budget_inr": 3500,
        "recommended_duration_days": 3,
        "overview": "Queen of Nilgiri Hill Stations famous for tea estates, colonial gardens, and toy train.",
        "image_url": "https://images.unsplash.com/photo-1589308078059-be1415eab4c3?w=800"
    },
    {
        "id": "munnar",
        "name": "Munnar",
        "state": "Kerala",
        "lat": 10.0889,
        "lon": 77.0595,
        "best_season": "September to May",
        "approx_daily_budget_inr": 3800,
        "recommended_duration_days": 3,
        "overview": "Idyllic hill retreat wrapped in sprawling emerald tea plantations and misty peaks.",
        "image_url": "https://images.unsplash.com/photo-1602216056096-3b40cc0c9944?w=800"
    },
    {
        "id": "goa",
        "name": "Goa",
        "state": "Goa",
        "lat": 15.2993,
        "lon": 74.1240,
        "best_season": "November to February",
        "approx_daily_budget_inr": 4500,
        "recommended_duration_days": 4,
        "overview": "Sun-soaked coastal paradise famed for beaches, Portuguese architecture, and nightlife.",
        "image_url": "https://images.unsplash.com/photo-1512343879784-a960bf40e7f2?w=800"
    },
    {
        "id": "manali",
        "name": "Manali",
        "state": "Himachal Pradesh",
        "lat": 32.2396,
        "lon": 77.1887,
        "best_season": "October to June",
        "approx_daily_budget_inr": 4000,
        "recommended_duration_days": 4,
        "overview": "High-altitude Himalayan resort town renowned for snow sports, pine valleys, and cafes.",
        "image_url": "https://images.unsplash.com/photo-1605649487212-47bdab064df7?w=800"
    },
    {
        "id": "coorg",
        "name": "Coorg",
        "state": "Karnataka",
        "lat": 12.4244,
        "lon": 75.7382,
        "best_season": "October to April",
        "approx_daily_budget_inr": 3600,
        "recommended_duration_days": 3,
        "overview": "The Scotland of India, home to coffee groves, spice hills, and cascading waterfalls.",
        "image_url": "https://images.unsplash.com/photo-1596401057633-54a8fe8ef647?w=800"
    },
    {
        "id": "kodaikanal",
        "name": "Kodaikanal",
        "state": "Tamil Nadu",
        "lat": 10.2381,
        "lon": 77.4892,
        "best_season": "September to May",
        "approx_daily_budget_inr": 3200,
        "recommended_duration_days": 3,
        "overview": "Princess of Hill Stations set around a star-shaped lake, pine forests, and granite cliffs.",
        "image_url": "https://images.unsplash.com/photo-1582510003544-4d00b7f74220?w=800"
    },
    {
        "id": "udaipur",
        "name": "Udaipur",
        "state": "Rajasthan",
        "lat": 24.5854,
        "lon": 73.7125,
        "best_season": "October to March",
        "approx_daily_budget_inr": 4200,
        "recommended_duration_days": 3,
        "overview": "City of Lakes steeped in royal Mewar Rajput palaces, serene waters, and vintage alleys.",
        "image_url": "https://images.unsplash.com/photo-1599661046289-e31897846e41?w=800"
    },
    {
        "id": "jaipur",
        "name": "Jaipur",
        "state": "Rajasthan",
        "lat": 26.9124,
        "lon": 75.7873,
        "best_season": "October to March",
        "approx_daily_budget_inr": 3800,
        "recommended_duration_days": 3,
        "overview": "The Pink City celebrated for grand forts, astronomical observatories, and vibrant bazaars.",
        "image_url": "https://images.unsplash.com/photo-1477587458883-47145ed94245?w=800"
    },
    {
        "id": "varanasi",
        "name": "Varanasi",
        "state": "Uttar Pradesh",
        "lat": 25.3176,
        "lon": 82.9739,
        "best_season": "October to March",
        "approx_daily_budget_inr": 2800,
        "recommended_duration_days": 3,
        "overview": "One of the world's oldest living cities, sacred Ganges river ghats, and spiritual rituals.",
        "image_url": "https://images.unsplash.com/photo-1561361513-2d000a50f0dc?w=800"
    },
    {
        "id": "wayanad",
        "name": "Wayanad",
        "state": "Kerala",
        "lat": 11.6854,
        "lon": 76.1320,
        "best_season": "October to May",
        "approx_daily_budget_inr": 3400,
        "recommended_duration_days": 3,
        "overview": "Verdant spice country with prehistoric caves, waterfalls, and mist-laden trekking routes.",
        "image_url": "https://images.unsplash.com/photo-1544735716-392fe2489ffa?w=800"
    },
    {
        "id": "rishikesh",
        "name": "Rishikesh",
        "state": "Uttarakhand",
        "lat": 30.0869,
        "lon": 78.2676,
        "best_season": "September to April",
        "approx_daily_budget_inr": 3000,
        "recommended_duration_days": 3,
        "overview": "Yoga capital of the world and white-water river rafting hub at the Himalayan foothills.",
        "image_url": "https://images.unsplash.com/photo-1588095240986-e8d193d537f8?w=800"
    },
    {
        "id": "leh",
        "name": "Leh",
        "state": "Ladakh",
        "lat": 34.1526,
        "lon": 77.5771,
        "best_season": "May to September",
        "approx_daily_budget_inr": 5000,
        "recommended_duration_days": 5,
        "overview": "Stunning high-altitude cold desert with ancient Tibetan monasteries and azure lakes.",
        "image_url": "https://images.unsplash.com/photo-1506744038136-46273834b3fb?w=800"
    },
    {
        "id": "darjeeling",
        "name": "Darjeeling",
        "state": "West Bengal",
        "lat": 27.0410,
        "lon": 88.2663,
        "best_season": "March to May & October to December",
        "approx_daily_budget_inr": 3600,
        "recommended_duration_days": 3,
        "overview": "Queen of the Hills commanding vistas of Mt. Kanchenjunga, tea gardens, and toy trains.",
        "image_url": "https://images.unsplash.com/photo-1544735716-392fe2489ffa?w=800"
    },
    {
        "id": "agra",
        "name": "Agra",
        "state": "Uttar Pradesh",
        "lat": 27.1767,
        "lon": 78.0081,
        "best_season": "October to March",
        "approx_daily_budget_inr": 3500,
        "recommended_duration_days": 2,
        "overview": "Mughal capital and proud home of the Taj Mahal, Agra Fort, and rich cultural monuments.",
        "image_url": "https://images.unsplash.com/photo-1564507592333-c60657eea523?w=800"
    },
    {
        "id": "bengaluru",
        "name": "Bengaluru",
        "state": "Karnataka",
        "lat": 12.9716,
        "lon": 77.5946,
        "best_season": "Throughout the year",
        "approx_daily_budget_inr": 4000,
        "recommended_duration_days": 3,
        "overview": "Garden City of India and Silicon Valley blending royal palaces, craft breweries, and tech parks.",
        "image_url": "https://images.unsplash.com/photo-1596176530529-78163a4f7af2?w=800"
    }
]

# Generate curated authentic places per destination
DEST_PLACES = {
    "udaipur": [
        ("City Palace", "heritage", 400, 120, 4.8, True, "09:00", "17:30", "palace,mewar,royalty,museum,architecture"),
        ("Lake Pichola Boat Ride", "nature", 500, 75, 4.7, False, "09:00", "18:00", "boating,lake,sunset,palace_view"),
        ("Jag Mandir", "heritage", 200, 60, 4.5, False, "10:00", "18:00", "island_palace,marble,courtyard,view"),
        ("Saheliyon Ki Bari", "nature", 100, 60, 4.4, False, "09:00", "19:00", "gardens,fountains,marble_elephants,greenery"),
        ("Bagore Ki Haveli & Museum", "museum", 100, 90, 4.6, True, "09:30", "19:00", "museum,dharohar_dance,turbans,puppets"),
        ("Sajjangarh Monsoon Palace", "heritage", 150, 90, 4.3, False, "09:00", "18:30", "hilltop,sunset,panoramic_view,wildlife"),
        ("Jagdish Temple", "temple", 20, 45, 4.6, True, "05:30", "22:00", "vishnu,carvings,spiritual,architecture"),
        ("Vintage Car Museum", "museum", 250, 60, 4.3, True, "09:00", "21:00", "vintage_cars,rolls_royce,heritage"),
        ("Fateh Sagar Lake", "nature", 50, 75, 4.5, False, "08:00", "20:00", "lake,promenade,boating,chhatris"),
        ("Ambrai Ghat Evening Walk", "scenic", 0, 60, 4.8, False, "06:00", "22:00", "ghat,evening_lights,pichola,peaceful"),
        ("Hathi Pol Bazaar", "shopping", 200, 90, 4.2, False, "10:30", "20:30", "handicrafts,miniature_paintings,leather"),
        ("Jheel's Ginger Coffee & Bakery", "food", 350, 45, 4.6, True, "08:30", "22:00", "cafe,lakeview,bakery,breakfast"),
    ],
    "jaipur": [
        ("Amber Fort & Palace", "heritage", 500, 150, 4.8, False, "08:00", "17:30", "sheesh_mahal,fort,mughal,elephant"),
        ("Hawa Mahal", "heritage", 200, 60, 4.6, True, "09:00", "17:00", "palace_of_winds,windows,honeycomb,architecture"),
        ("City Palace Jaipur", "heritage", 700, 120, 4.7, True, "09:30", "17:00", "courtyards,peacock_gate,royal_attire"),
        ("Jantar Mantar", "heritage", 200, 75, 4.6, False, "09:00", "17:00", "astronomy,sundial,unesco,science"),
        ("Nahargarh Fort Sunset Point", "heritage", 150, 90, 4.6, False, "10:00", "18:00", "viewpoint,sunset,city_lights,fort"),
        ("Albert Hall Museum", "museum", 300, 90, 4.5, True, "09:00", "17:00", "artifacts,egyptian_mummy,miniatures"),
        ("Govind Dev Ji Temple", "temple", 0, 45, 4.8, True, "05:00", "21:00", "spiritual,krishna,aarti,peace"),
        ("Bapu Bazaar & Johari Bazaar", "shopping", 300, 120, 4.4, False, "11:00", "21:00", "textiles,jootis,jewelry,spices"),
        ("LMB (Laxmi Mishtan Bhandar)", "food", 450, 60, 4.4, True, "09:00", "22:00", "ghewar,thali,rajasthani,sweets"),
        ("Galta Ji (Monkey Temple)", "temple", 50, 75, 4.3, False, "06:00", "19:00", "natural_spring,kunds,monkeys,rock"),
        ("Jal Mahal (Water Palace)", "scenic", 0, 45, 4.5, False, "06:00", "20:00", "lake_palace,photography,promenade"),
    ],
    "ooty": [
        ("Ooty Botanical Gardens", "nature", 80, 90, 4.4, False, "07:00", "18:30", "flowers,glasshouse,exotic_plants,terraces"),
        ("Nilgiri Mountain Railway", "heritage", 250, 180, 4.8, True, "07:00", "16:00", "toy_train,unesco,steam,scenic"),
        ("Doddabetta Peak", "nature", 50, 60, 4.4, False, "09:00", "18:00", "highest_peak,clouds,telescope,view"),
        ("Pykara Lake & Waterfalls", "nature", 120, 90, 4.4, False, "09:30", "17:30", "boating,pine_forest,shola,rapids"),
        ("Ooty Tea Factory & Museum", "museum", 100, 60, 4.3, True, "09:00", "18:30", "tea_making,tasting,chocolate,processing"),
        ("Rose Garden", "nature", 60, 60, 4.4, False, "08:30", "18:00", "roses,floral,walking,photography"),
        ("Avalanche Lake Sanctuary", "nature", 200, 120, 4.6, False, "09:00", "15:00", "trout_fishing,pristine,magnolia,woods"),
        ("St. Stephen's Church", "heritage", 20, 45, 4.3, True, "10:00", "17:00", "gothic,timber,colonial,cemetery"),
        ("Commercial Road Chocolate Walk", "food", 250, 60, 4.5, True, "10:00", "21:00", "homemade_chocolate,fudge,bakeries"),
        ("Ooty Lake Boating", "nature", 150, 75, 4.2, False, "09:00", "18:00", "rowing,eucalyptus,cycling,fun"),
    ],
    "munnar": [
        ("Tea Museum & Estate", "museum", 150, 90, 4.5, True, "09:00", "17:00", "tea_production,history,tasting,estate"),
        ("Eravikulam National Park", "nature", 200, 150, 4.7, False, "07:30", "16:00", "nilgiri_tahr,anamudi,hills,neelakurinji"),
        ("Mattupetty Dam & Lake", "nature", 100, 75, 4.3, False, "09:30", "17:00", "boating,reflections,scenic,elephants"),
        ("Kundala Lake & Echo Point", "nature", 80, 60, 4.3, False, "08:30", "18:00", "pedal_boat,echo,pine_groves,mist"),
        ("Pothamedu View Point", "nature", 0, 45, 4.5, False, "06:00", "18:30", "sunset,tea_valleys,cardamom,hills"),
        ("Attukal Waterfalls", "nature", 0, 60, 4.4, False, "08:00", "18:00", "cascades,trek,monsoon,lush"),
        ("Blossom International Park", "nature", 50, 60, 4.2, False, "09:00", "19:00", "gardens,roller_skating,river,walk"),
        ("KFDC Floriculture Centre", "nature", 50, 45, 4.3, True, "09:00", "17:00", "orchids,greenhouse,rare_plants"),
        ("Rapsy Restaurant (Kerala Food)", "food", 250, 45, 4.4, True, "08:00", "21:30", "biryani,parotta,beef_roast,kerala"),
    ],
    "goa": [
        ("Basilica of Bom Jesus", "heritage", 0, 60, 4.7, True, "09:00", "18:30", "unesco,st_francis,baroque,church"),
        ("Fort Aguada & Lighthouse", "heritage", 50, 90, 4.5, False, "09:30", "18:00", "portuguese_fort,mandovi,sea_view"),
        ("Palolem Beach", "nature", 0, 120, 4.8, False, "06:00", "22:00", "crescent_beach,kayaking,dolphins,shacks"),
        ("Dudhsagar Waterfalls Trek", "nature", 500, 240, 4.7, False, "06:00", "16:00", "four_tier,jeep_safari,rail_bridge,river"),
        ("Anjuna Flea Market", "shopping", 100, 120, 4.3, False, "09:00", "19:00", "bohemian,souvenirs,music,clothing"),
        ("Fontainhas Latin Quarter Walk", "heritage", 0, 90, 4.6, False, "08:00", "20:00", "colorful_houses,tiled_alleys,cafes"),
        ("Chapora Fort", "heritage", 0, 60, 4.4, False, "08:00", "18:00", "dil_chahta_hai,sunset,vagator_view"),
        ("Se Cathedral", "heritage", 0, 60, 4.6, True, "07:30", "18:00", "golden_bell,manueline,tuscany,unesco"),
        ("Fisherman's Wharf", "food", 800, 90, 4.6, True, "12:00", "23:00", "goan_curry,seafood,riverside,cocktails"),
        ("Calangute & Baga Water Sports", "adventure", 1200, 120, 4.3, False, "09:00", "17:00", "parasailing,jet_ski,banana_ride"),
    ],
    "manali": [
        ("Hadimba Devi Temple", "temple", 50, 60, 4.6, True, "08:00", "18:00", "wooden_pagoda,cedar_forest,mahabharata"),
        ("Solang Valley Adventure Hub", "nature", 500, 180, 4.7, False, "09:00", "17:00", "paragliding,snow,ropeway,zorbing"),
        ("Rohtang Pass", "nature", 500, 240, 4.8, False, "06:00", "16:00", "high_pass,glacier,pir_panjal,snow"),
        ("Jogini Waterfall Trek", "nature", 0, 120, 4.7, False, "08:00", "17:00", "trekking,apple_orchards,streams,pools"),
        ("Old Manali Cafe Street", "food", 450, 90, 4.6, True, "09:00", "23:00", "israeli_food,live_music,woodfire_pizza"),
        ("Vashisht Hot Water Springs", "temple", 0, 60, 4.4, False, "07:00", "20:00", "sulphur_bath,sage_vashisht,himalayan"),
        ("Naggar Castle & Gallery", "heritage", 100, 75, 4.5, True, "09:00", "18:00", "wood_stone,roerich_paintings,beas_valley"),
        ("Mall Road Shopping", "shopping", 200, 90, 4.3, False, "10:00", "21:00", "kullu_shawls,wooden_crafts,streetfood"),
    ],
    "coorg": [
        ("Abbey Falls", "nature", 50, 60, 4.3, False, "09:00", "17:00", "waterfall,coffee_plantations,lush,hanging_bridge"),
        ("Raja's Seat", "nature", 30, 60, 4.4, False, "06:00", "20:00", "sunset,mist,gardens,kodagu_kings"),
        ("Namdroling Golden Temple", "temple", 50, 75, 4.7, True, "09:00", "18:00", "tibetan_monastery,golden_buddha,peace"),
        ("Dubare Elephant Camp", "wildlife", 200, 120, 4.3, False, "09:00", "16:30", "elephants,river_cauvery,bathing,wildlife"),
        ("Barapole River Rafting", "adventure", 1200, 150, 4.6, False, "08:00", "15:00", "whitewater_rapids,river,monsoon_rush"),
        ("Coffee Estate Plantation Tour", "food", 300, 90, 4.6, False, "09:30", "17:00", "coffee_tasting,cardamom,estate_walk"),
        ("Talacauvery & Brahmagiri", "temple", 20, 90, 4.6, False, "06:00", "18:30", "river_origin,sacred_kund,brahmagiri_hills"),
        ("Madikeri Fort & Museum", "heritage", 40, 60, 4.2, True, "10:00", "17:30", "granite_elephants,prison,palace,history"),
    ],
    "kodaikanal": [
        ("Kodaikanal Lake Boating", "nature", 150, 75, 4.5, False, "08:30", "18:00", "star_shaped,pedal_boat,cycling,lake_promenade"),
        ("Coaker's Walk", "nature", 30, 60, 4.5, False, "07:00", "19:00", "valley_view,mist,cliffside_path,telescope"),
        ("Pillar Rocks", "nature", 20, 45, 4.3, False, "09:00", "17:30", "granite_boulders,chasm,cloudscape,dramatic"),
        ("Dolphin's Nose Trek", "adventure", 50, 120, 4.6, False, "08:00", "17:00", "rock_promontory,deep_gorge,trekking,thrill"),
        ("Bryant Park", "nature", 50, 60, 4.3, False, "09:00", "18:00", "horticulture,hybrids,glasshouse,roses"),
        ("Silver Cascade Falls", "nature", 0, 45, 4.2, False, "07:00", "18:00", "waterfall,monkeys,fruit_stalls,roadside"),
        ("Shembaganur Museum of Natural History", "museum", 50, 60, 4.3, True, "10:00", "17:00", "taxidermy,orchids,anthropology,fauna"),
    ],
    "varanasi": [
        ("Dashashwamedh Ghat Evening Ganga Aarti", "spiritual", 0, 90, 4.9, False, "18:00", "20:30", "ganga_aarti,lamps,priests,spiritual_energy"),
        ("Kashi Vishwanath Temple", "temple", 50, 90, 4.9, True, "03:00", "23:00", "jyotirlinga,shiva,corridor,gold_spire"),
        ("Sunrise Boat Ride on Ganges", "nature", 300, 90, 4.8, False, "05:30", "08:00", "morning_mist,ghats,rituals,sunrise"),
        ("Sarnath Deer Park & Stupa", "heritage", 100, 120, 4.7, False, "08:00", "18:00", "dhamek_stupa,buddha_first_sermon,ashoka"),
        ("Sarnath Archaeological Museum", "museum", 50, 75, 4.6, True, "09:00", "17:00", "ashokan_lion_capital,buddhist_art"),
        ("Manikarnika Ghat", "spiritual", 0, 45, 4.5, False, "00:00", "23:59", "cremation_ghat,cycle_of_life,sacred_flames"),
        ("Banarasi Silk Weaving Center", "shopping", 200, 60, 4.5, True, "10:00", "20:00", "silk_sarees,gold_zari,handloom,artisans"),
        ("Blue Lassi Shop", "food", 120, 30, 4.7, True, "09:00", "22:00", "creamy_lassi,earthen_pot,clay_cup,fruits"),
    ],
    "wayanad": [
        ("Edakkal Caves", "heritage", 50, 120, 4.6, False, "09:00", "16:00", "neolithic_petroglyphs,steep_climb,rock_art"),
        ("Banasura Sagar Dam", "nature", 100, 90, 4.4, False, "09:00", "17:30", "earth_dam,speedboating,islands,scenic"),
        ("Chembra Peak & Heart Lake", "adventure", 200, 180, 4.7, False, "07:00", "14:00", "heart_shaped_lake,hard_trek,clouds"),
        ("Wayanad Wildlife Sanctuary", "wildlife", 300, 120, 4.4, False, "07:00", "17:00", "jeep_safari,deer,elephants,forest"),
        ("Soochipara Waterfalls", "nature", 80, 90, 4.5, False, "09:00", "17:00", "three_tiered,rock_climbing,pool,falls"),
        ("Karapuzha Dam & Adventure Park", "adventure", 150, 90, 4.3, False, "09:30", "18:00", "zipline,lake_view,lawn,boating"),
        ("Pookode Lake", "nature", 50, 60, 4.3, False, "09:00", "17:30", "freshwater_lake,lotus,aquarium,pedal_boats"),
    ],
    "rishikesh": [
        ("Triveni Ghat Evening Maha Aarti", "spiritual", 0, 75, 4.8, False, "17:30", "20:00", "ganga_aarti,holy_dip,bhajans,lamps"),
        ("Ganga White Water Rafting", "adventure", 1000, 150, 4.9, False, "08:00", "16:00", "rapids,roller_coaster,cliff_jumping,ganga"),
        ("Lakshman Jhula & Ram Jhula", "heritage", 0, 60, 4.5, False, "06:00", "22:00", "suspension_bridge,temples,river_breeze"),
        ("Beatles Ashram (Chaurasi Kutia)", "heritage", 150, 90, 4.6, False, "09:00", "16:30", "meditation_caves,graffiti,transcendental"),
        ("Neer Garh Waterfall Trek", "nature", 50, 90, 4.5, False, "08:00", "17:30", "cascades,natural_spring,rock_pools"),
        ("Little Buddha Cafe", "food", 400, 60, 4.6, True, "08:00", "23:00", "ganga_view,shakshuka,momos,bohemian"),
        ("Parmarth Niketan Ashram", "spiritual", 0, 60, 4.7, True, "06:00", "20:00", "yoga,gardens,peace,ganga_puja"),
    ],
    "leh": [
        ("Pangong Tso Lake", "nature", 300, 240, 4.9, False, "06:00", "18:00", "color_changing_lake,3_idiots,azure,mountains"),
        ("Nubra Valley & Hunder Sand Dunes", "nature", 300, 240, 4.8, False, "06:00", "18:00", "double_humped_camel,desert,cold_desert"),
        ("Thiksey Monastery", "heritage", 50, 90, 4.8, True, "07:00", "18:00", "maitreya_buddha,potala_style,monks,prayer"),
        ("Leh Palace", "heritage", 100, 75, 4.4, True, "08:00", "18:00", "namgyal_dynasty,tibetan_architecture,town_view"),
        ("Shanti Stupa", "spiritual", 0, 60, 4.7, False, "05:00", "21:00", "peace_pagoda,sunset,panoramic_leh,relics"),
        ("Hall of Fame Museum", "museum", 100, 75, 4.7, True, "09:00", "19:00", "indian_army,kargil_war,siachen_gear"),
        ("Magnetic Hill", "nature", 0, 45, 4.3, False, "06:00", "18:00", "gravity_defying,optical_illusion,highway"),
    ],
    "darjeeling": [
        ("Tiger Hill Sunrise Point", "nature", 50, 75, 4.8, False, "04:00", "07:00", "sunrise,kanchenjunga,golden_rays,peak"),
        ("Darjeeling Himalayan Toy Train", "heritage", 300, 120, 4.7, True, "08:00", "16:00", "unesco,steam_locomotive,batasia_loop"),
        ("Batasia Loop & War Memorial", "heritage", 30, 45, 4.5, False, "05:00", "18:00", "spiral_railway,garden,gorkha_soldiers"),
        ("Happy Valley Tea Estate", "food", 150, 75, 4.5, False, "09:00", "16:30", "tea_bushes,plucking,muscatel,tasting"),
        ("Himalayan Mountaineering Institute & Zoo", "museum", 110, 120, 4.6, True, "08:30", "16:30", "red_panda,snow_leopard,everest_gear"),
        ("Glenary's Bakery & Pub", "food", 450, 60, 4.6, True, "07:00", "22:00", "british_bakery,apple_pie,roast_chicken"),
        ("Peace Pagoda & Japanese Temple", "spiritual", 0, 60, 4.5, True, "04:30", "19:00", "buddhist_shrine,drums,pine_forest"),
    ],
    "agra": [
        ("Taj Mahal", "heritage", 250, 150, 4.9, True, "06:00", "18:30", "wonder_of_world,shah_jahan,white_marble"),
        ("Agra Fort", "heritage", 150, 120, 4.7, True, "06:00", "18:00", "red_sandstone,mughal_palaces,diwan_i_aam"),
        ("Fatehpur Sikri", "heritage", 100, 150, 4.7, False, "06:00", "18:00", "buland_darwaza,akbar,salim_chishti"),
        ("Mehtab Bagh", "nature", 50, 60, 4.4, False, "06:00", "18:30", "moonlight_garden,taj_view_across_yamuna"),
        ("Itmad-ud-Daulah (Baby Taj)", "heritage", 50, 60, 4.5, True, "06:00", "18:00", "pietra_dura,marble_lattice,nur_jahan"),
        ("Panchi Petha Emporium", "food", 150, 30, 4.4, True, "09:00", "21:30", "petha,anghoori,pan_petha,dalmoth"),
    ],
    "bengaluru": [
        ("Bangalore Palace", "heritage", 400, 90, 4.4, True, "09:00", "17:30", "tudor_architecture,woodcarvings,royal"),
        ("Lalbagh Botanical Garden", "nature", 50, 105, 4.5, False, "06:00", "19:00", "glasshouse,fossil_tree,lotus_pond"),
        ("Cubbon Park", "nature", 20, 90, 4.5, False, "06:00", "20:00", "greenery,bamboo,jogging,library"),
        ("Visvesvaraya Industrial & Tech Museum", "museum", 100, 120, 4.6, True, "09:30", "18:00", "science,interactive,engines,kids"),
        ("Vidyarthi Bhavan", "food", 200, 45, 4.6, True, "06:30", "20:00", "masala_dosa,filter_coffee,traditional"),
        ("Bannerghatta Biological Park", "wildlife", 350, 180, 4.3, False, "09:00", "16:30", "safari,tigers,butterfly_park,zoo"),
        ("Bull Temple & Bugle Rock", "temple", 30, 45, 4.4, False, "06:00", "20:00", "nandi_monolith,dravidian,rock_garden"),
        ("Commercial Street & Brigade Road", "shopping", 300, 120, 4.3, False, "10:30", "21:00", "shopping,fashion,street_food,pub_city"),
    ]
}


def build_mock_files():
    out_dir = Path("data/mock")
    out_dir.mkdir(parents=True, exist_ok=True)

    dest_dict = {d["id"]: d for d in DESTINATIONS}
    with open(out_dir / "destinations.json", "w", encoding="utf-8") as f:
        json.dump(DESTINATIONS, f, indent=2)

    places = []
    pid_counter = 1
    for dest_id, items in DEST_PLACES.items():
        dest = dest_dict.get(dest_id)
        if not dest:
            continue
        base_lat = dest["lat"]
        base_lon = dest["lon"]

        for idx, (name, cat, cost, dur, rating, indoor, o_t, c_t, tags) in enumerate(items):
            # Deterministic offset based on idx
            lat_off = (idx % 4 - 1.5) * 0.02
            lon_off = (idx // 4 - 1.5) * 0.02
            places.append({
                "id": f"PLC_{pid_counter:04d}",
                "name": name,
                "destination_id": dest_id,
                "destination_name": dest["name"],
                "state": dest["state"],
                "country_code": "IN",
                "lat": round(base_lat + lat_off, 5),
                "lon": round(base_lon + lon_off, 5),
                "category": cat,
                "avg_cost_inr": cost,
                "avg_visit_duration_min": dur,
                "rating": rating,
                "popularity": round(rating / 5.0, 2),
                "crowd_level": 0.6 if rating > 4.5 else 0.4,
                "open_time": o_t,
                "close_time": c_t,
                "is_indoor": indoor,
                "best_season": dest["best_season"],
                "tags": tags,
                "image_url": dest["image_url"],
                "data_source": "curated_mock_seed"
            })
            pid_counter += 1

    with open(out_dir / "places.json", "w", encoding="utf-8") as f:
        json.dump(places, f, indent=2)

    print(f"Generated {len(DESTINATIONS)} destinations and {len(places)} curated places in data/mock/")


if __name__ == "__main__":
    build_mock_files()

