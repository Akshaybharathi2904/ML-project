import os
import random
import numpy as np
import pandas as pd
from pathlib import Path
from typing import Dict, List, Tuple
from src.utils.geo import build_distance_and_time_matrices
from src.utils.config import load_config, get_project_root

# Set deterministic seeds
RANDOM_SEED = 42
np.random.seed(RANDOM_SEED)
random.seed(RANDOM_SEED)

CATEGORIES = [
    "heritage",
    "nature",
    "beach",
    "temple",
    "adventure",
    "food",
    "shopping",
    "museum",
    "wildlife",
    "hill_station",
]

SEASONS = ["winter", "monsoon", "summer", "all"]

CITY_COORDINATES = {
    "Bengaluru": {"lat": 12.9716, "lon": 77.5946, "state": "Karnataka"},
    "Mysuru": {"lat": 12.2958, "lon": 76.6394, "state": "Karnataka"},
    "Coorg": {"lat": 12.4244, "lon": 75.7382, "state": "Karnataka"},
    "Hampi": {"lat": 15.3350, "lon": 76.4600, "state": "Karnataka"},
    "Gokarna": {"lat": 14.5479, "lon": 74.3188, "state": "Karnataka"},
    "Chennai": {"lat": 13.0827, "lon": 80.2707, "state": "Tamil Nadu"},
    "Madurai": {"lat": 9.9252, "lon": 78.1198, "state": "Tamil Nadu"},
    "Coimbatore": {"lat": 11.0168, "lon": 76.9558, "state": "Tamil Nadu"},
    "Ooty": {"lat": 11.4102, "lon": 76.6950, "state": "Tamil Nadu"},
    "Kodaikanal": {"lat": 10.2381, "lon": 77.4892, "state": "Tamil Nadu"},
    "Kochi": {"lat": 9.9312, "lon": 76.2673, "state": "Kerala"},
    "Munnar": {"lat": 10.0889, "lon": 77.0595, "state": "Kerala"},
    "Alleppey": {"lat": 9.4981, "lon": 76.3388, "state": "Kerala"},
    "Wayanad": {"lat": 11.6854, "lon": 76.1320, "state": "Kerala"},
    "Thiruvananthapuram": {"lat": 8.5241, "lon": 76.9366, "state": "Kerala"},
}

SEED_PLACES = [
    # Bengaluru
    ("Bangalore Palace", "Bengaluru", "heritage", 400, 90, 4.4, "09:00", "17:30", "history,architecture,royal"),
    ("Lalbagh Botanical Garden", "Bengaluru", "nature", 50, 105, 4.5, "06:00", "19:00", "flowers,glasshouse,lake,walk"),
    ("Cubbon Park", "Bengaluru", "nature", 20, 90, 4.5, "06:00", "20:00", "greenery,biking,bamboo,jogging"),
    ("Visvesvaraya Industrial & Tech Museum", "Bengaluru", "museum", 100, 120, 4.6, "09:30", "18:00", "science,interactive,kids,engines"),
    ("Commercial Street", "Bengaluru", "shopping", 250, 120, 4.3, "10:30", "21:00", "fashion,streetfood,bargains,souvenirs"),
    ("Vidyarthi Bhavan", "Bengaluru", "food", 200, 45, 4.6, "06:30", "20:00", "dosa,traditional,filter_coffee,breakfast"),
    ("Bannerghatta National Park", "Bengaluru", "wildlife", 350, 180, 4.3, "09:00", "16:30", "safari,tigers,zoo,butterfly_park"),
    ("Bull Temple (Nandi Temple)", "Bengaluru", "temple", 30, 45, 4.4, "06:00", "20:00", "spiritual,drakeshwara,sculpture,ancient"),
    # Mysuru
    ("Mysore Palace", "Mysuru", "heritage", 150, 120, 4.8, "10:00", "17:30", "illumination,royal,durbar,grand"),
    ("Chamundeshwari Temple", "Mysuru", "temple", 50, 60, 4.6, "07:30", "21:00", "hilltop,panoramic,spiritual,goddess"),
    ("Brindavan Gardens", "Mysuru", "nature", 80, 120, 4.2, "06:00", "20:00", "musical_fountain,dam,evening,lighting"),
    ("Mysore Sand Sculpture Museum", "Mysuru", "museum", 70, 45, 4.2, "08:30", "18:30", "art,sand,unique,crafts"),
    ("Devaraja Market", "Mysuru", "shopping", 100, 75, 4.4, "06:30", "20:30", "flowers,spices,sandalwood,incense"),
    ("St. Philomena's Cathedral", "Mysuru", "heritage", 40, 45, 4.4, "05:00", "18:00", "gothic,stained_glass,church,architecture"),
    # Coorg
    ("Abbey Falls", "Coorg", "nature", 50, 60, 4.3, "09:00", "17:00", "waterfall,coffee_plantations,lush,trek"),
    ("Raja's Seat", "Coorg", "hill_station", 30, 60, 4.4, "06:00", "20:00", "sunset,gardens,mist,panoramic_view"),
    ("Dubare Elephant Camp", "Coorg", "wildlife", 200, 120, 4.3, "09:00", "16:30", "elephants,river_crossing,bathing,wildlife"),
    ("Namdroling Golden Temple", "Coorg", "temple", 50, 75, 4.7, "09:00", "18:00", "tibetan,monastery,peace,buddha"),
    ("Barapole River Rafting", "Coorg", "adventure", 1200, 150, 4.6, "08:00", "15:00", "whitewater,rapids,adrenaline,river"),
    ("Coorg Coffee Plantation Tour", "Coorg", "food", 300, 90, 4.6, "09:30", "17:00", "coffee_tasting,estate,pepper,spices"),
    # Hampi
    ("Virupaksha Temple", "Hampi", "temple", 50, 75, 4.8, "06:00", "18:00", "unesco,tungabhadra,ancient,carvings"),
    ("Vijaya Vittala Temple & Stone Chariot", "Hampi", "heritage", 100, 120, 4.9, "08:30", "17:30", "iconic,musical_pillars,unesco,stone_carving"),
    ("Matanga Hill Sunrise Trek", "Hampi", "adventure", 0, 90, 4.8, "05:00", "18:30", "sunrise,boulders,panoramic,hiking"),
    ("Queen's Bath & Royal Enclosure", "Hampi", "heritage", 40, 75, 4.5, "08:00", "18:00", "indo_islamic,aqueducts,ruins,history"),
    ("Hampi Bouldering & Sanapur Lake", "Hampi", "adventure", 300, 120, 4.6, "07:00", "18:00", "coracle_ride,climbing,cliff_jumping,lake"),
    # Gokarna
    ("Om Beach", "Gokarna", "beach", 0, 120, 4.7, "05:00", "20:00", "om_shape,waves,cafe,rocky_coast"),
    ("Kudle Beach", "Gokarna", "beach", 0, 105, 4.6, "05:00", "21:00", "sunset,shacks,beachside_yoga,swimming"),
    ("Mahabaleshwar Temple", "Gokarna", "temple", 20, 60, 4.7, "06:00", "20:30", "atmalinga,sacred,dravidian,rituals"),
    ("Paradise Beach Trek", "Gokarna", "adventure", 0, 120, 4.6, "06:00", "18:00", "cliff_trekking,hidden_cove,secluded,camping"),
    ("Namaste Cafe", "Gokarna", "food", 450, 60, 4.4, "08:00", "22:00", "seafood,beachview,continental,chilled"),
    # Chennai
    ("Marina Beach", "Chennai", "beach", 0, 90, 4.4, "05:00", "22:00", "longest_beach,sundal,lighthouse,breeze"),
    ("Kapaleeshwarar Temple", "Chennai", "temple", 20, 60, 4.8, "06:00", "21:00", "dravidian,gopuram,mylapore,tank"),
    ("Fort St. George & Museum", "Chennai", "museum", 60, 90, 4.3, "09:00", "17:00", "colonial_history,weapons,coins,british"),
    ("DakshinaChitra Heritage Museum", "Chennai", "heritage", 175, 120, 4.7, "10:00", "18:00", "south_indian_houses,crafts,folk_art,culture"),
    ("Murugan Idli Shop", "Chennai", "food", 180, 45, 4.5, "07:00", "22:30", "ghee_podi_idli,chutneys,south_indian,breakfast"),
    ("Pondy Bazaar", "Chennai", "shopping", 300, 120, 4.3, "10:00", "21:30", "t_nagar,silk_sarees,jewelry,street_market"),
    # Madurai
    ("Meenakshi Amman Temple", "Madurai", "temple", 50, 150, 4.9, "05:00", "21:30", "thousand_pillar_hall,gopurams,spiritual,unesco_candidate"),
    ("Thirumalai Nayakkar Mahal", "Madurai", "heritage", 50, 75, 4.5, "09:00", "17:00", "celestial_pavilions,light_show,pillars,palace"),
    ("Gandhi Memorial Museum", "Madurai", "museum", 20, 60, 4.4, "10:00", "17:45", "freedom_struggle,bloodstained_cloth,history,peace"),
    ("Madurai Famous Jigarthanda", "Madurai", "food", 120, 30, 4.7, "09:00", "23:00", "jigarthanda,dessert,icecream,local_specialty"),
    # Coimbatore
    ("Adiyogi Shiva Statue", "Coimbatore", "temple", 0, 90, 4.8, "06:00", "20:00", "isha_foundation,gigantic,laser_show,meditation"),
    ("Gedee Car Museum", "Coimbatore", "museum", 100, 75, 4.6, "09:00", "18:30", "vintage_cars,automotive_history,rare,technology"),
    ("Marudhamalai Temple", "Coimbatore", "temple", 30, 60, 4.6, "06:00", "20:30", "hilltop,lord_murugan,scenic,ayurvedic_herbs"),
    ("Brookefields Mall", "Coimbatore", "shopping", 400, 120, 4.3, "10:00", "22:00", "brands,food_court,cinema,modern"),
    # Ooty
    ("Ooty Botanical Gardens", "Ooty", "nature", 80, 90, 4.4, "07:00", "18:30", "fossil_tree,terraces,exotic_plants,flowers"),
    ("Doddabetta Peak", "Ooty", "hill_station", 30, 60, 4.4, "09:00", "18:00", "highest_peak,telescope_house,clouds,viewpoint"),
    ("Nilgiri Mountain Railway", "Ooty", "heritage", 250, 180, 4.8, "07:00", "16:00", "toy_train,unesco,tunnels,steam_locomotive"),
    ("Pykara Lake & Waterfalls", "Ooty", "nature", 120, 90, 4.4, "09:30", "17:30", "boating,pine_forests,shola,serene"),
    ("Ooty Chocolate Factory Tour", "Ooty", "food", 150, 45, 4.5, "09:00", "19:00", "homemade_chocolates,fudge,tasting,sweets"),
    # Kodaikanal
    ("Kodaikanal Lake Boating", "Kodaikanal", "nature", 150, 75, 4.5, "08:30", "18:00", "star_shaped,pedal_boat,cycling,lake_promenade"),
    ("Coaker's Walk", "Kodaikanal", "hill_station", 30, 60, 4.5, "07:00", "19:00", "valley_view,mist,cliffside_path,telescope"),
    ("Pillar Rocks", "Kodaikanal", "nature", 20, 45, 4.3, "09:00", "17:30", "granite_boulders,chasm,cloudscape,dramatic"),
    ("Dolphin's Nose Trek", "Kodaikanal", "adventure", 50, 120, 4.6, "08:00", "17:00", "rock_promontory,deep_gorge,trekking,thrill"),
    # Kochi
    ("Fort Kochi & Chinese Fishing Nets", "Kochi", "heritage", 0, 90, 4.6, "06:00", "19:00", "cantilever,sunset,colonial_alleys,harbor"),
    ("Mattancherry Dutch Palace", "Kochi", "museum", 25, 60, 4.3, "09:45", "16:45", "murals,kerala_architecture,history,kings"),
    ("Jew Town & Paradesi Synagogue", "Kochi", "shopping", 30, 75, 4.5, "10:00", "18:00", "antiques,spices,chandeliers,quaint_cafes"),
    ("Kerala Kathakali Centre", "Kochi", "heritage", 400, 90, 4.8, "17:00", "20:00", "classical_dance,makeup_demonstration,theater,music"),
    ("Kashi Art Cafe", "Kochi", "food", 350, 60, 4.6, "08:30", "21:00", "art_gallery,chocolate_cake,coffee,bohemian"),
    # Munnar
    ("Tea Museum & Tata Tea Estate", "Munnar", "museum", 150, 90, 4.5, "09:00", "17:00", "tea_processing,tasting,plantations,green"),
    ("Eravikulam National Park", "Munnar", "wildlife", 200, 150, 4.7, "07:30", "16:00", "nilgiri_tahr,anamudi_peak,neelakurinji,hills"),
    ("Mattupetty Dam & Lake", "Munnar", "nature", 100, 75, 4.3, "09:30", "17:00", "speedboat,elephant_sightings,reflections,scenic"),
    ("Anamudi Shola Trekking", "Munnar", "adventure", 500, 180, 4.7, "08:00", "15:00", "high_altitude,cloud_forest,biodiversity,hiking"),
    # Alleppey
    ("Alleppey Backwaters Houseboat Cruise", "Alleppey", "nature", 1500, 240, 4.9, "11:00", "18:00", "kettuvallam,paddy_fields,canals,coconut_groves"),
    ("Marari Beach", "Alleppey", "beach", 0, 100, 4.6, "05:00", "20:00", "serene,hammocks,fishermen,peaceful"),
    ("Alleppey Lighthouse & Beach", "Alleppey", "heritage", 40, 60, 4.3, "09:00", "18:00", "panoramic_sea_view,museum,pier_ruins,history"),
    ("Thaff Delicacy (Kerala Meals)", "Alleppey", "food", 250, 45, 4.5, "11:30", "22:00", "karimeen_pollichathu,kerala_parotta,biryani,spicy"),
    # Wayanad
    ("Edakkal Caves", "Wayanad", "heritage", 50, 120, 4.6, "09:00", "16:00", "neolithic_petroglyphs,steep_climb,rock_art,ancient"),
    ("Banasura Sagar Dam", "Wayanad", "adventure", 100, 90, 4.4, "09:00", "17:30", "earth_dam,speedboating,islands,scenic"),
    ("Chembra Peak & Heart Lake", "Wayanad", "adventure", 200, 180, 4.7, "07:00", "14:00", "heart_shaped_lake,hard_trek,clouds,panoramic"),
    ("Wayanad Wildlife Sanctuary (Muthanga)", "Wayanad", "wildlife", 300, 120, 4.4, "07:00", "17:00", "jeep_safari,deer,elephants,dense_forest"),
    # Thiruvananthapuram
    ("Padmanabhaswamy Temple", "Thiruvananthapuram", "temple", 50, 90, 4.9, "05:00", "19:30", "richest_temple,chera_style,gold,vaults,sacred"),
    ("Kovalam Lighthouse Beach", "Thiruvananthapuram", "beach", 0, 120, 4.7, "05:00", "21:00", "red_white_lighthouse,crescent_beach,surfing,cafes"),
    ("Napier Museum & Art Gallery", "Thiruvananthapuram", "museum", 50, 75, 4.4, "10:00", "16:45", "indo_saracenic,raja_ravi_varma,bronze,wood_carvings"),
    ("Poovar Island Mangrove Cruise", "Thiruvananthapuram", "nature", 800, 100, 4.6, "08:00", "18:00", "estuary,mangroves,golden_sand,floating_restaurant"),
]

# Modifiers and descriptors to expand places across South Indian cities realistically
NAME_PATTERNS = [
    ("{city} Eco Nature Park", "nature", "eco_park,walking_trail,birds,lush"),
    ("{city} Heritage Art Walk & Crafts Center", "shopping", "handicrafts,local_artisans,pottery,fabrics"),
    ("{city} Traditional Spice Market", "shopping", "spices,cardamom,pepper,tea_leaves"),
    ("{city} Hill Viewpoint & Sunrise Point", "hill_station", "mist,cloudline,photography,sunrise"),
    ("{city} Ancient Shiva & Vishnu Temple", "temple", "ancient_gopuram,chola_architecture,prayers"),
    ("{city} Royal Fort & Bastion", "heritage", "stone_walls,cannons,architecture,lookout"),
    ("{city} Local Food Street & Delicacies", "food", "traditional_thali,dosa,street_food,snacks"),
    ("{city} Forest Canopy Walk & Trek", "adventure", "zipline,suspension_bridge,dense_forest,thrill"),
    ("{city} Biodiversity Wildlife Reserve", "wildlife", "spotted_deer,hornbill,native_fauna,safari"),
    ("{city} City History & Cultural Museum", "museum", "antiquities,numismatics,folk_heritage,sculptures"),
    ("{city} Hidden Waterfalls & Natural Pool", "nature", "cascades,natural_spring,rock_pools,swimming"),
    ("{city} Rock Climbing & Boulder Arena", "adventure", "bouldering,outdoor_activity,gear,climbing"),
    ("{city} Coastal Cove & Fishermen Promenade", "beach", "seaside,waves,coconut_water,sunset"),
    ("{city} Botanical Orchid Garden", "nature", "rare_flora,greenhouse,fragrance,shaded_paths"),
    ("{city} Traditional Silk & Handloom Center", "shopping", "kanchipuram_silk,weaving,authentic,souvenirs"),
    ("{city} Sacred River Ghat & Ritual Grounds", "temple", "holy_dip,evening_aarti,lamps,peaceful"),
    ("{city} Organic Tea & Spice Estate", "food", "estate_walk,fresh_brews,cardamom,cinnamon"),
    ("{city} Mountain Biking & Valley Trail", "adventure", "offroad,trails,endurance,mountain_views"),
]


def generate_places(target_count: int = 300) -> pd.DataFrame:
    """Generate ~300 realistic places located across 15 South Indian cities."""
    records = []
    pid = 1

    # 1. Add handcrafted authentic seed places
    for name, city, cat, cost, duration, rating, o_time, c_time, tags in SEED_PLACES:
        base_coord = CITY_COORDINATES[city]
        # Slight jitter (within ~3-5 km of city center)
        lat = round(base_coord["lat"] + np.random.uniform(-0.04, 0.04), 5)
        lon = round(base_coord["lon"] + np.random.uniform(-0.04, 0.04), 5)
        pop = round(np.clip(rating / 5.0 + np.random.uniform(-0.1, 0.1), 0.3, 0.98), 2)
        crowd = round(np.clip(pop * 0.9 + np.random.uniform(-0.15, 0.15), 0.15, 0.95), 2)
        season = random.choice(SEASONS)

        records.append({
            "id": f"P{pid:03d}",
            "name": name,
            "city": city,
            "state": base_coord["state"],
            "lat": lat,
            "lon": lon,
            "category": cat,
            "avg_cost_inr": cost,
            "avg_visit_duration_min": duration,
            "rating": round(float(rating), 1),
            "popularity": pop,
            "crowd_level": crowd,
            "open_time": o_time,
            "close_time": c_time,
            "best_season": season,
            "tags": tags,
        })
        pid += 1

    # 2. Synthesize additional places to reach target_count
    cities = list(CITY_COORDINATES.keys())
    while pid <= target_count:
        city = cities[(pid - 1) % len(cities)]
        pattern, cat, tag_str = random.choice(NAME_PATTERNS)
        
        # Coastal cities get more beach options, hill cities get hill_station
        if cat == "beach" and city not in ["Chennai", "Gokarna", "Kochi", "Alleppey", "Thiruvananthapuram"]:
            cat = "nature"
            tag_str = "waterfront,lake,breeze,nature_walk"

        name = pattern.format(city=city)
        if any(r["name"] == name for r in records):
            name = f"{name} #{random.randint(2, 9)}"

        base_coord = CITY_COORDINATES[city]
        lat = round(base_coord["lat"] + np.random.uniform(-0.08, 0.08), 5)
        lon = round(base_coord["lon"] + np.random.uniform(-0.08, 0.08), 5)

        # Category-appropriate costs and durations
        if cat in ["food", "shopping"]:
            cost = int(np.random.choice([100, 200, 350, 500, 750]))
            duration = int(np.random.choice([45, 60, 90]))
        elif cat in ["adventure"]:
            cost = int(np.random.choice([300, 600, 900, 1400]))
            duration = int(np.random.choice([90, 120, 150, 180]))
        elif cat in ["temple"]:
            cost = int(np.random.choice([0, 20, 50, 100]))
            duration = int(np.random.choice([45, 60, 75]))
        elif cat in ["heritage", "museum"]:
            cost = int(np.random.choice([30, 50, 100, 200]))
            duration = int(np.random.choice([60, 90, 120]))
        else:
            cost = int(np.random.choice([0, 50, 100, 250, 400]))
            duration = int(np.random.choice([60, 90, 120]))

        rating = round(float(np.clip(np.random.normal(4.2, 0.35), 3.2, 5.0)), 1)
        pop = round(float(np.clip(rating / 5.2 + np.random.uniform(-0.15, 0.15), 0.2, 0.95)), 2)
        crowd = round(float(np.clip(pop * 0.85 + np.random.uniform(-0.2, 0.2), 0.1, 0.95)), 2)
        open_hour = random.choice([6, 7, 8, 9, 10])
        close_hour = random.choice([17, 18, 19, 20, 21])
        open_time = f"{open_hour:02d}:00"
        close_time = f"{close_hour:02d}:00"
        season = random.choice(SEASONS)

        records.append({
            "id": f"P{pid:03d}",
            "name": name,
            "city": city,
            "state": base_coord["state"],
            "lat": lat,
            "lon": lon,
            "category": cat,
            "avg_cost_inr": cost,
            "avg_visit_duration_min": duration,
            "rating": rating,
            "popularity": pop,
            "crowd_level": crowd,
            "open_time": open_time,
            "close_time": close_time,
            "best_season": season,
            "tags": tag_str,
        })
        pid += 1

    df = pd.DataFrame(records)
    return df


def generate_users(num_users: int = 1000, cold_start_ratio: float = 0.15) -> pd.DataFrame:
    """
    Generate synthetic users with latent category interest weights,
    budget tier, pace preference, and designated cold-start partition.
    """
    users = []
    budget_tiers = ["low", "medium", "luxury"]
    paces = ["relaxed", "moderate", "packed"]

    num_cold_start = int(num_users * cold_start_ratio)
    cold_start_indices = set(range(num_users - num_cold_start, num_users))

    for uid in range(1, num_users + 1):
        # Latent preference Dirichlet distribution over categories (sparsified)
        raw_weights = np.random.exponential(scale=1.0, size=len(CATEGORIES))
        # Zero out categories the user has low affinity for
        raw_weights[raw_weights < np.median(raw_weights)] *= 0.15
        pref_vec = raw_weights / np.sum(raw_weights)
        pref_dict = {f"pref_{cat}": round(float(w), 4) for cat, w in zip(CATEGORIES, pref_vec)}

        budget = np.random.choice(budget_tiers, p=[0.4, 0.45, 0.15])
        pace = np.random.choice(paces, p=[0.3, 0.5, 0.2])
        is_cold = (uid - 1) in cold_start_indices

        user_row = {
            "id": f"U{uid:04d}",
            "budget_level": budget,
            "pace": pace,
            "is_cold_start": is_cold,
            **pref_dict,
        }
        users.append(user_row)

    return pd.DataFrame(users)


def generate_ratings(
    places_df: pd.DataFrame,
    users_df: pd.DataFrame,
    target_ratings: int = 30000
) -> pd.DataFrame:
    """
    Generate user-place ratings based on dot product of latent preference and place category,
    quality bias, popularity bias, and realistic noise.
    
    Cold-start users have 0 ratings in the standard training pool.
    """
    ratings = []
    cat_to_col = {cat: f"pref_{cat}" for cat in CATEGORIES}

    # Only active (non cold-start) users generate training ratings
    active_users = users_df[~users_df["is_cold_start"]].copy().reset_index(drop=True)
    n_active = len(active_users)
    n_places = len(places_df)

    ratings_per_user = target_ratings // n_active
    places_records = places_df.to_dict(orient="records")

    for _, user in active_users.iterrows():
        uid = user["id"]
        # Sample places with probability proportional to popularity
        pops = np.array([p["popularity"] for p in places_records])
        probs = pops / pops.sum()
        
        # User reviews between max(5, ratings_per_user - 10) and (ratings_per_user + 15) places
        k_places = np.random.randint(max(8, ratings_per_user - 10), ratings_per_user + 15)
        k_places = min(k_places, n_places)
        chosen_indices = np.random.choice(n_places, size=k_places, replace=False, p=probs)

        for p_idx in chosen_indices:
            p = places_records[p_idx]
            cat = p["category"]
            cat_pref = user[cat_to_col[cat]]

            # Latent affinity signal: 2.5 baseline + preference match + place quality bonus + random noise
            pref_boost = cat_pref * 6.0  # Range approx 0 to 2
            quality_boost = (p["rating"] - 3.5) * 0.8  # Range approx -0.5 to 1.2
            noise = np.random.normal(0, 0.45)

            score = 2.4 + pref_boost + quality_boost + noise
            rating = int(np.clip(np.round(score), 1, 5))

            ratings.append({
                "user_id": uid,
                "place_id": p["id"],
                "rating": rating,
                "timestamp": int(1700000000 + np.random.randint(0, 30000000))
            })

    # Also generate a separate ground-truth test evaluation set for the cold-start users
    # so we can rigorously evaluate cold-start NDCG/RMSE later
    cold_users = users_df[users_df["is_cold_start"]].copy().reset_index(drop=True)
    cold_ratings = []
    for _, user in cold_users.iterrows():
        uid = user["id"]
        k_places = np.random.randint(8, 16)
        chosen_indices = np.random.choice(n_places, size=k_places, replace=False)
        for p_idx in chosen_indices:
            p = places_records[p_idx]
            cat = p["category"]
            cat_pref = user[cat_to_col[cat]]
            score = 2.4 + cat_pref * 6.0 + (p["rating"] - 3.5) * 0.8 + np.random.normal(0, 0.4)
            rating = int(np.clip(np.round(score), 1, 5))
            cold_ratings.append({
                "user_id": uid,
                "place_id": p["id"],
                "rating": rating,
                "timestamp": int(1700000000 + np.random.randint(0, 30000000))
            })

    ratings_df = pd.DataFrame(ratings)
    cold_ratings_df = pd.DataFrame(cold_ratings)
    return ratings_df, cold_ratings_df


def main():
    root = get_project_root()
    processed_dir = root / "data" / "processed"
    raw_dir = root / "data" / "raw"
    processed_dir.mkdir(parents=True, exist_ok=True)
    raw_dir.mkdir(parents=True, exist_ok=True)

    config = load_config()
    print("Generating places dataset (South India: Tamil Nadu, Kerala, Karnataka)...")
    places_df = generate_places(target_count=config["data"].get("num_places", 300))
    places_path = root / config["data"]["places_csv"]
    places_df.to_csv(places_path, index=False)
    print(f" Saved {len(places_df)} places to {places_path}")

    print("Generating users dataset with latent profiles and cold-start tags...")
    users_df = generate_users(
        num_users=config["data"].get("num_users", 1000),
        cold_start_ratio=config["data"].get("cold_start_ratio", 0.15)
    )
    users_path = root / config["data"]["users_csv"]
    users_df.to_csv(users_path, index=False)
    print(f" Saved {len(users_df)} users (Cold-start count: {users_df['is_cold_start'].sum()}) to {users_path}")

    print("Generating ratings dataset (~30,000 interactions)...")
    ratings_df, cold_ratings_df = generate_ratings(
        places_df, users_df,
        target_ratings=config["data"].get("num_ratings", 30000)
    )
    ratings_path = root / config["data"]["ratings_csv"]
    ratings_df.to_csv(ratings_path, index=False)
    
    cold_ratings_path = processed_dir / "cold_start_eval_ratings.csv"
    cold_ratings_df.to_csv(cold_ratings_path, index=False)
    print(f" Saved {len(ratings_df)} training ratings to {ratings_path}")
    print(f" Saved {len(cold_ratings_df)} held-out cold-start ratings to {cold_ratings_path}")

    print("Building and caching Haversine distance and travel time matrices...")
    dist_df, time_df = build_distance_and_time_matrices(
        places_df,
        avg_speed_kmh=config["travel_model"]["avg_speed_kmh"],
        traffic_factor=config["travel_model"]["traffic_factor"],
        min_transfer_min=config["travel_model"]["min_transfer_time_min"]
    )
    dist_path = root / config["data"]["distance_matrix_csv"]
    time_path = root / config["data"]["travel_time_matrix_csv"]
    dist_df.to_csv(dist_path)
    time_df.to_csv(time_path)
    print(f" Saved distance matrix {dist_df.shape} to {dist_path}")
    print(f" Saved travel time matrix {time_df.shape} to {time_path}")
    print("Data generation complete!")


if __name__ == "__main__":
    main()

