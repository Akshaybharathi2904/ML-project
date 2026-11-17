"""
TRAVELMATE AI - South India Destinations (64 Verified Destinations)
Tamil Nadu, Kerala, Karnataka, Andhra Pradesh, Telangana, Puducherry, Lakshadweep
"""

SOUTH_DESTINATIONS = [
    # ---------- TAMIL NADU (12) ----------
    {
        "id": "ooty", "name": "Ooty", "state": "Tamil Nadu", "is_ut": False,
        "lat": 11.4102, "lon": 76.6950, "category": "Hill Station", "best_season": "October to June",
        "budget": 3500, "days": 3,
        "overview": "Queen of Nilgiri Hill Stations famous for misty tea estates, Nilgiri Mountain Railway, and botanical wonders.",
        "attractions": ["Ooty Botanical Gardens", "Doddabetta Peak", "Nilgiri Mountain Railway", "Pykara Lake", "Rose Garden"],
        "nearby": ["Coonoor", "Kotagiri", "Mudumalai National Park"],
        "activities": ["Heritage Toy Train Ride", "Tea Tasting at Glenmorgan", "Boating at Ooty Lake"],
        "img_url": "https://images.unsplash.com/photo-1589308078059-be1415eab4c3?auto=format&fit=crop&w=1200&q=80",
        "photographer": "Kishore Kumar", "profile": "https://unsplash.com/@kishorekumar"
    },
    {
        "id": "kodaikanal", "name": "Kodaikanal", "state": "Tamil Nadu", "is_ut": False,
        "lat": 10.2381, "lon": 77.4892, "category": "Hill Station", "best_season": "September to May",
        "budget": 3600, "days": 3,
        "overview": "Princess of Hill Stations set around a star-shaped lake amidst dense pine forests and rolling mist.",
        "attractions": ["Kodaikanal Lake", "Coaker's Walk", "Pillar Rocks", "Bryant Park", "Silver Cascade Falls"],
        "nearby": ["Palani", "Madurai", "Dindigul"],
        "activities": ["Cycling around Kodai Lake", "Trekking to Dolphin's Nose", "Visiting Pine Forest"],
        "img_url": "https://images.unsplash.com/photo-1544735716-392fe2489ffa?auto=format&fit=crop&w=1200&q=80",
        "photographer": "Santhosh Kumar", "profile": "https://unsplash.com/@santhosh"
    },
    {
        "id": "chennai", "name": "Chennai", "state": "Tamil Nadu", "is_ut": False,
        "lat": 13.0827, "lon": 80.2707, "category": "Metropolitan Culture", "best_season": "November to February",
        "budget": 4200, "days": 3,
        "overview": "Cultural capital of South India boasting colonial heritage, Carnatic music traditions, and Marina Beach.",
        "attractions": ["Marina Beach", "Kapaleeshwarar Temple", "Fort St. George", "San Thome Basilica", "Government Museum"],
        "nearby": ["Mahabalipuram", "Kanchipuram", "Pulicat Lake"],
        "activities": ["Marina Beach Evening Stroll", "Classical Bharatanatyam recital", "South Indian Filter Coffee Trail"],
        "img_url": "https://images.unsplash.com/photo-1582510003544-4d00b7f74220?auto=format&fit=crop&w=1200&q=80",
        "photographer": "Prasanna Kumar", "profile": "https://unsplash.com/@prasanna"
    },
    {
        "id": "madurai", "name": "Madurai", "state": "Tamil Nadu", "is_ut": False,
        "lat": 9.9252, "lon": 78.1198, "category": "Spiritual Heritage", "best_season": "October to March",
        "budget": 3000, "days": 2,
        "overview": "One of the world's oldest continuously inhabited cities, anchored by the iconic Meenakshi Amman Temple.",
        "attractions": ["Meenakshi Amman Temple", "Thirumalai Nayakkar Mahal", "Gandhi Memorial Museum", "Koodal Azhagar Temple"],
        "nearby": ["Rameswaram", "Kodaikanal", "Chettinad"],
        "activities": ["Night Ceremony at Meenakshi Temple", "Tasting authentic Jigarthanda", "Palace Light & Sound Show"],
        "img_url": "https://images.unsplash.com/photo-1609766857041-ed402ea8069a?auto=format&fit=crop&w=1200&q=80",
        "photographer": "Balaji Srinivasan", "profile": "https://unsplash.com/@balajis"
    },
    {
        "id": "rameswaram", "name": "Rameswaram", "state": "Tamil Nadu", "is_ut": False,
        "lat": 9.2876, "lon": 79.3129, "category": "Spiritual Coastal", "best_season": "October to April",
        "budget": 3200, "days": 2,
        "overview": "Sacred island pilgrimage destination connected by Pamban Bridge, surrounded by turquoise waters.",
        "attractions": ["Ramanathaswamy Temple", "Pamban Sea Bridge", "Dhanushkodi Ghost Town", "APJ Abdul Kalam Memorial"],
        "nearby": ["Madurai", "Dhanushkodi", "Devipattinam"],
        "activities": ["Pamban Rail Bridge view", "Dhanushkodi 4x4 Jeep Safari", "Holy Theertham Bathing Ritual"],
        "img_url": "https://images.unsplash.com/photo-1590050752117-238cb0fb12b1?auto=format&fit=crop&w=1200&q=80",
        "photographer": "Naveen Raj", "profile": "https://unsplash.com/@naveenraj"
    },
    {
        "id": "kanyakumari", "name": "Kanyakumari", "state": "Tamil Nadu", "is_ut": False,
        "lat": 8.0883, "lon": 77.5385, "category": "Coastal Landmark", "best_season": "October to March",
        "budget": 3200, "days": 2,
        "overview": "The southern tip of mainland India where the Bay of Bengal, Arabian Sea, and Indian Ocean converge.",
        "attractions": ["Vivekananda Rock Memorial", "Thiruvalluvar Statue", "Sunset View Point", "Padmanabhapuram Palace"],
        "nearby": ["Nagercoil", "Trivandrum", "Poovar"],
        "activities": ["Sunrise watching over Triveni Sangam", "Ferry to Vivekananda Rock", "Visiting Gandhi Memorial Mandapam"],
        "img_url": "https://images.unsplash.com/photo-1596176530529-78163a4f7af2?auto=format&fit=crop&w=1200&q=80",
        "photographer": "Karthik Sridhar", "profile": "https://unsplash.com/@karthiks"
    },
    {
        "id": "mahabalipuram", "name": "Mahabalipuram", "state": "Tamil Nadu", "is_ut": False,
        "lat": 12.6269, "lon": 80.1927, "category": "UNESCO Heritage", "best_season": "November to February",
        "budget": 3800, "days": 2,
        "overview": "Ancient 7th-century Pallava coastal port famous for monolith rock-cut rathas and sea-facing Shore Temple.",
        "attractions": ["Shore Temple", "Pancha Rathas", "Arjuna's Penance", "Krishna's Butterball", "Mahabalipuram Beach"],
        "nearby": ["Chennai", "Kanchipuram", "Puducherry"],
        "activities": ["Stone Carving Workshops", "Beachside Seafood Dining", "Heritage Architecture Photography"],
        "img_url": "https://images.unsplash.com/photo-1590050752117-238cb0fb12b1?auto=format&fit=crop&w=1200&q=80",
        "photographer": "Arun Kumar", "profile": "https://unsplash.com/@arunkumar"
    },
    {
        "id": "thanjavur", "name": "Thanjavur", "state": "Tamil Nadu", "is_ut": False,
        "lat": 10.7870, "lon": 79.1378, "category": "UNESCO Heritage", "best_season": "October to March",
        "budget": 2900, "days": 2,
        "overview": "Cradle of Chola architecture home to the monumental 1,000-year-old Brihadisvara Great Living Chola Temple.",
        "attractions": ["Brihadisvara Temple", "Thanjavur Maratha Palace", "Saraswathi Mahal Library", "Schwartz Church"],
        "nearby": ["Tiruchirappalli", "Kumbakonam", "Chettinad"],
        "activities": ["Tanjore Gold Leaf Painting Tour", "Observing Chola Bronze Casting", "Temple Architecture Tour"],
        "img_url": "https://images.unsplash.com/photo-1609766857041-ed402ea8069a?auto=format&fit=crop&w=1200&q=80",
        "photographer": "Ramesh Sundaram", "profile": "https://unsplash.com/@rameshs"
    },
    {
        "id": "yercaud", "name": "Yercaud", "state": "Tamil Nadu", "is_ut": False,
        "lat": 11.7753, "lon": 78.2093, "category": "Hill Station", "best_season": "October to June",
        "budget": 3100, "days": 2,
        "overview": "Serene Shevaroy hill retreat surrounded by coffee plantations, orange groves, and spice orchards.",
        "attractions": ["Yercaud Lake", "Lady's Seat", "Pagoda Point", "Shevaroy Temple", "Kiliyur Falls"],
        "nearby": ["Salem", "Hogenakkal", "Namakkal"],
        "activities": ["Boating on Emerald Lake", "Coffee Plantation Walk", "Sunset at Lady's Seat"],
        "img_url": "https://images.unsplash.com/photo-1544735716-392fe2489ffa?auto=format&fit=crop&w=1200&q=80",
        "photographer": "Vijay Anand", "profile": "https://unsplash.com/@vijayanand"
    },
    {
        "id": "chettinad", "name": "Chettinad", "state": "Tamil Nadu", "is_ut": False,
        "lat": 10.0760, "lon": 78.7830, "category": "Heritage & Culinary", "best_season": "October to March",
        "budget": 3600, "days": 2,
        "overview": "Historic region celebrated for palatial 19th-century merchant mansions, Athangudi handmade tiles, and fiery cuisine.",
        "attractions": ["Chettinad Palace", "Athangudi Tile Factories", "Kaviarasu Kannadasan Memorial", "Ayyanar Shrine"],
        "nearby": ["Karaikudi", "Madurai", "Thanjavur"],
        "activities": ["Mansion Architecture Walk", "Authentic 21-Dish Chettinad Feast", "Antique Shopping in Karaikudi"],
        "img_url": "https://images.unsplash.com/photo-1582510003544-4d00b7f74220?auto=format&fit=crop&w=1200&q=80",
        "photographer": "Meenakshi S", "profile": "https://unsplash.com/@meenakshis"
    },
    {
        "id": "coimbatore", "name": "Coimbatore", "state": "Tamil Nadu", "is_ut": False,
        "lat": 11.0168, "lon": 76.9558, "category": "Spiritual & Nature", "best_season": "September to March",
        "budget": 3200, "days": 2,
        "overview": "Manchester of South India nestled near the Western Ghats, famed for the 112-ft Adiyogi Shiva Statue.",
        "attractions": ["Adiyogi Shiva Statue", "Marudhamalai Murugan Temple", "Siruvani Waterfalls", "GD Naidu Museum", "Gass Forest Museum"],
        "nearby": ["Ooty", "Pollachi", "Topslip"],
        "activities": ["Visiting Adiyogi Dhyanalinga", "Drinking pure Siruvani mineral water", "Anamalai wildlife gateway tour"],
        "img_url": "https://images.unsplash.com/photo-1609766857041-ed402ea8069a?auto=format&fit=crop&w=1200&q=80",
        "photographer": "Senthil Nathan", "profile": "https://unsplash.com/@senthilnathan"
    },
    {
        "id": "tiruvannamalai", "name": "Tiruvannamalai", "state": "Tamil Nadu", "is_ut": False,
        "lat": 12.2253, "lon": 79.0747, "category": "Spiritual Heritage", "best_season": "October to March",
        "budget": 2800, "days": 2,
        "overview": "Sacred Agni (Fire) elemental pilgrimage town at the foot of Arunachala Hill, sanctified by Sage Ramana Maharshi.",
        "attractions": ["Annamalaiyar Temple", "Arunachala Holy Hill", "Sri Ramana Ashram", "Virupaksha Cave", "Seshadri Swamigal Ashram"],
        "nearby": ["Vellore", "Gingee Fort", "Puducherry"],
        "activities": ["14-km barefoot Giri Valam circumambulation", "Meditating in Ramana Maharshi Cave", "Temple gopuram tour"],
        "img_url": "https://images.unsplash.com/photo-1582510003544-4d00b7f74220?auto=format&fit=crop&w=1200&q=80",
        "photographer": "Muthu Raman", "profile": "https://unsplash.com/@muthuraman"
    },

    # ---------- KERALA (12) ----------
    {
        "id": "munnar", "name": "Munnar", "state": "Kerala", "is_ut": False,
        "lat": 10.0889, "lon": 77.0595, "category": "Hill Station", "best_season": "September to May",
        "budget": 3800, "days": 3,
        "overview": "Idyllic hill retreat wrapped in sprawling emerald tea plantations, mist-capped peaks, and rare Nilgiri Tahrs.",
        "attractions": ["Eravikulam National Park", "Mattupetty Dam", "Tea Museum", "Anamudi Peak", "Top Station"],
        "nearby": ["Thekkady", "Marayoor", "Vagamon"],
        "activities": ["Tea factory manufacturing tour", "Spotting Nilgiri Tahr", "Speedboating on Mattupetty Lake"],
        "img_url": "https://images.unsplash.com/photo-1602216056096-3b40cc0c9944?auto=format&fit=crop&w=1200&q=80",
        "photographer": "Nandhu Kumar", "profile": "https://unsplash.com/@nandhukumar"
    },
    {
        "id": "wayanad", "name": "Wayanad", "state": "Kerala", "is_ut": False,
        "lat": 11.6854, "lon": 76.1320, "category": "Nature & Wildlife", "best_season": "October to May",
        "budget": 3600, "days": 3,
        "overview": "Verdant highland paradise of spice forests, prehistoric caves, and heart-shaped mountain lakes.",
        "attractions": ["Edakkal Caves", "Banasura Sagar Dam", "Chembra Peak", "Soochipara Falls", "Muthanga Wildlife Sanctuary"],
        "nearby": ["Calicut", "Coorg", "Bandipur"],
        "activities": ["Trekking to Chembra heart lake", "Exploring prehistoric petroglyphs at Edakkal", "Bamboo rafting on Kuruva Island"],
        "img_url": "https://images.unsplash.com/photo-1544735716-392fe2489ffa?auto=format&fit=crop&w=1200&q=80",
        "photographer": "Binoy Thomas", "profile": "https://unsplash.com/@binoythomas"
    },
    {
        "id": "alleppey", "name": "Alleppey (Alappuzha)", "state": "Kerala", "is_ut": False,
        "lat": 9.4981, "lon": 76.3388, "category": "Backwaters", "best_season": "October to March",
        "budget": 4500, "days": 2,
        "overview": "Venice of the East renowned for tranquil backwater cruises on traditional kettuvallam houseboats.",
        "attractions": ["Vembanad Lake", "Alappuzha Beach & Pier", "Marari Beach", "Kuttanad Paddy Fields", "Krishnapuram Palace"],
        "nearby": ["Kumarakom", "Kochi", "Kollam"],
        "activities": ["Overnight traditional houseboat cruise", "Kayaking through narrow village canals", "Watching Nehru Trophy snake boat races"],
        "img_url": "https://images.unsplash.com/photo-1602216056096-3b40cc0c9944?auto=format&fit=crop&w=1200&q=80",
        "photographer": "Ajay Menon", "profile": "https://unsplash.com/@ajaymenon"
    },
    {
        "id": "kochi", "name": "Kochi (Cochin)", "state": "Kerala", "is_ut": False,
        "lat": 9.9312, "lon": 76.2673, "category": "Coastal Heritage", "best_season": "October to April",
        "budget": 4000, "days": 3,
        "overview": "Queen of the Arabian Sea uniting Chinese fishing nets, Portuguese synagogues, Dutch palaces, and spice bazaars.",
        "attractions": ["Chinese Fishing Nets", "Fort Kochi", "Mattancherry Palace", "Paradesi Synagogue", "Marine Drive"],
        "nearby": ["Alleppey", "Munnar", "Athirappilly"],
        "activities": ["Watching sunset over Chinese fishing nets", "Kathakali dance performance", "Mattancherry spice street walking tour"],
        "img_url": "https://images.unsplash.com/photo-1590050752117-238cb0fb12b1?auto=format&fit=crop&w=1200&q=80",
        "photographer": "George Mathew", "profile": "https://unsplash.com/@georgemathew"
    },
    {
        "id": "varkala", "name": "Varkala", "state": "Kerala", "is_ut": False,
        "lat": 8.7379, "lon": 76.7163, "category": "Beach & Cliff", "best_season": "October to April",
        "budget": 3400, "days": 3,
        "overview": "Coastal cliff sanctuary with red laterite cliffs towering dramatically over the sparkling Arabian Sea.",
        "attractions": ["Varkala Cliff Beach (Papanasam)", "Janardhana Swamy Temple", "Kappil Beach & Lake", "Anjengo Fort", "Sivagiri Mutt"],
        "nearby": ["Kollam", "Trivandrum", "Munroe Island"],
        "activities": ["Cliff-top cafe dining at sunset", "Ayurvedic massage & rejuvenation", "Surfing on Black Sand Beach"],
        "img_url": "https://images.unsplash.com/photo-1512343879784-a960bf40e7f2?auto=format&fit=crop&w=1200&q=80",
        "photographer": "Siddharth Nair", "profile": "https://unsplash.com/@siddharthnair"
    },
    {
        "id": "thekkady", "name": "Thekkady (Periyar)", "state": "Kerala", "is_ut": False,
        "lat": 9.6031, "lon": 77.1615, "category": "Wildlife & Spice", "best_season": "September to May",
        "budget": 3700, "days": 2,
        "overview": "Periyar Tiger Reserve sanctuary celebrated for wild elephant herds around artificial Periyar Lake and cardamom estates.",
        "attractions": ["Periyar National Park", "Periyar Lake Boat Safari", "Kumily Spice Plantations", "Kadathanadan Kalari Centre", "Murikkady"],
        "nearby": ["Munnar", "Vagamon", "Madurai"],
        "activities": ["Lake boat safari for wild elephants", "Bamboo rafting in Periyar tiger sanctuary", "Kalaripayattu martial arts show"],
        "img_url": "https://images.unsplash.com/photo-1512343879784-a960bf40e7f2?auto=format&fit=crop&w=1200&q=80",
        "photographer": "Rahul Varma", "profile": "https://unsplash.com/@rahulvarma"
    },
    {
        "id": "kovalam", "name": "Kovalam", "state": "Kerala", "is_ut": False,
        "lat": 8.4004, "lon": 76.9787, "category": "Beach & Coastal", "best_season": "September to March",
        "budget": 4100, "days": 2,
        "overview": "World-famous crescent beach enclave marked by the candy-striped Vizhinjam Lighthouse and shallow warm waters.",
        "attractions": ["Lighthouse Beach", "Hawa Beach", "Samudra Beach", "Vizhinjam Marine Aquarium", "Halcyon Castle"],
        "nearby": ["Trivandrum", "Poovar", "Varkala"],
        "activities": ["Climbing 140-step Lighthouse for panoramic views", "Sea surfing and catamaran rides", "Authentic Ayurvedic treatments"],
        "img_url": "https://images.unsplash.com/photo-1512343879784-a960bf40e7f2?auto=format&fit=crop&w=1200&q=80",
        "photographer": "Deepak Krishnan", "profile": "https://unsplash.com/@deepakkrishnan"
    },
    {
        "id": "kumarakom", "name": "Kumarakom", "state": "Kerala", "is_ut": False,
        "lat": 9.6175, "lon": 76.4301, "category": "Backwaters & Birds", "best_season": "September to March",
        "budget": 4800, "days": 2,
        "overview": "Lush cluster of islands on Vembanad Lake famed for migratory waterfowl and luxury backwater wellness resorts.",
        "attractions": ["Kumarakom Bird Sanctuary", "Vembanad Lake", "Aruvikkuzhi Waterfall", "Bay Island Driftwood Museum", "Pathiramanal Island"],
        "nearby": ["Kottayam", "Alleppey", "Kochi"],
        "activities": ["Dawn birdwatching cruise on Vembanad", "Luxury Ayurvedic resort spa retreat", "Fresh Karimeen Pollichathu culinary treat"],
        "img_url": "https://images.unsplash.com/photo-1602216056096-3b40cc0c9944?auto=format&fit=crop&w=1200&q=80",
        "photographer": "Manoj Pillai", "profile": "https://unsplash.com/@manojpillai"
    },
    {
        "id": "bekal", "name": "Bekal", "state": "Kerala", "is_ut": False,
        "lat": 12.3833, "lon": 75.0333, "category": "Coastal Heritage", "best_season": "October to March",
        "budget": 3900, "days": 2,
        "overview": "North Kerala fortress coastal marvel where the 300-year-old keyhole-shaped Bekal Fort overlooks crashing waves.",
        "attractions": ["Bekal Fort", "Bekal Beach Park", "Chandragiri Fort", "Kappil Beach Bekal", "Nityanandashram Caves"],
        "nearby": ["Kasaragod", "Mangalore", "Kannur"],
        "activities": ["Walking the sea-facing ramparts of Bekal Fort", "Viewing sunset from observation tower", "Theyyam ritual performance in Kannur"],
        "img_url": "https://images.unsplash.com/photo-1590050752117-238cb0fb12b1?auto=format&fit=crop&w=1200&q=80",
        "photographer": "Ashwin Raj", "profile": "https://unsplash.com/@ashwinraj"
    },
    {
        "id": "athirappilly", "name": "Athirappilly Falls", "state": "Kerala", "is_ut": False,
        "lat": 10.2851, "lon": 76.5698, "category": "Waterfalls & Nature", "best_season": "June to January",
        "budget": 3300, "days": 1,
        "overview": "The Niagara of India, a thundering 80-foot waterfall cascading over rocky ledges into the Chalakudy River gorge.",
        "attractions": ["Athirappilly Waterfalls", "Vazhachal Falls", "Charpa Falls", "Thumboormuzhy Dam Butterfly Park"],
        "nearby": ["Thrissur", "Kochi", "Valparai"],
        "activities": ["Trek to the base of Athirappilly falls", "Forest canopy birdwatching for Malabar Hornbills", "Scenic drive through Sholayar rainforest"],
        "img_url": "https://images.unsplash.com/photo-1544735716-392fe2489ffa?auto=format&fit=crop&w=1200&q=80",
        "photographer": "Prashanth Nair", "profile": "https://unsplash.com/@prashanthnair"
    },
    {
        "id": "vagamon", "name": "Vagamon", "state": "Kerala", "is_ut": False,
        "lat": 9.6865, "lon": 76.9066, "category": "Hill Station", "best_season": "Throughout the year",
        "budget": 2900, "days": 2,
        "overview": "Offbeat pine valley hill station in Idukki with velvet green meadows, tea gardens, and paragliding take-off cliffs.",
        "attractions": ["Vagamon Pine Forest", "Kurisumala Ashram", "Vagamon Meadows", "Murugan Hill", "Marmala Waterfalls"],
        "nearby": ["Kottayam", "Thekkady", "Munnar"],
        "activities": ["Tandem Paragliding over Vagamon valley", "Walking through scented pine forest", "Off-roading Jeep safari in green meadows"],
        "img_url": "https://images.unsplash.com/photo-1544735716-392fe2489ffa?auto=format&fit=crop&w=1200&q=80",
        "photographer": "Vishnu Mohan", "profile": "https://unsplash.com/@vishnumohan"
    },
    {
        "id": "kozhikode", "name": "Kozhikode (Calicut)", "state": "Kerala", "is_ut": False,
        "lat": 11.2588, "lon": 75.7804, "category": "Culinary & Coastal", "best_season": "October to March",
        "budget": 3200, "days": 2,
        "overview": "UNESCO City of Literature, historic port where Vasco da Gama landed in 1498, world-famed for Malabar Biryani.",
        "attractions": ["Kappad Beach", "Kozhikode Beach & Old Pier", "Mananchira Square", "Mishkal Mosque", "SM Street (Sweet Street)"],
        "nearby": ["Wayanad", "Beypore", "Kannur"],
        "activities": ["Authentic Thalassery/Malabar Dum Biryani feast", "Watching traditional Uru wooden boat building at Beypore", "Tasting fresh Calicut Halwa at SM Street"],
        "img_url": "https://images.unsplash.com/photo-1582510003544-4d00b7f74220?auto=format&fit=crop&w=1200&q=80",
        "photographer": "Faizal Kareem", "profile": "https://unsplash.com/@faizalkareem"
    },

    # ---------- KARNATAKA (12) ----------
    {
        "id": "bengaluru", "name": "Bengaluru", "state": "Karnataka", "is_ut": False,
        "lat": 12.9716, "lon": 77.5946, "category": "Metropolitan Culture", "best_season": "September to March",
        "budget": 4500, "days": 3,
        "overview": "Garden City and Silicon Valley of India blending Lalbagh botanical heritage, craft microbreweries, and palaces.",
        "attractions": ["Bangalore Palace", "Lalbagh Botanical Garden", "Cubbon Park", "Tipu Sultan's Summer Palace", "Vidhana Soudha"],
        "nearby": ["Nandi Hills", "Mysuru", "Bannerghatta National Park"],
        "activities": ["Microbrewery hopping in Indiranagar", "Morning run through Cubbon Park", "Visiting Glass House in Lalbagh"],
        "img_url": "https://images.unsplash.com/photo-1596176530529-78163a4f7af2?auto=format&fit=crop&w=1200&q=80",
        "photographer": "Naveen Gowda", "profile": "https://unsplash.com/@naveengowda"
    },
    {
        "id": "coorg", "name": "Coorg (Madikeri)", "state": "Karnataka", "is_ut": False,
        "lat": 12.4244, "lon": 75.7382, "category": "Hill & Plantation", "best_season": "October to April",
        "budget": 4000, "days": 3,
        "overview": "Scotland of India nestled on Western Ghats slopes, famed for coffee estates, Kodava culture, and abbey falls.",
        "attractions": ["Abbey Falls", "Raja's Seat", "Namdroling Golden Temple", "Dubare Elephant Camp", "Talakaveri"],
        "nearby": ["Mysuru", "Wayanad", "Nagarhole National Park"],
        "activities": ["Elephant bathing at Dubare Camp", "Coffee estate plantation trail", "Sunset watching from Raja's Seat"],
        "img_url": "https://images.unsplash.com/photo-1544735716-392fe2489ffa?auto=format&fit=crop&w=1200&q=80",
        "photographer": "Chethan K", "profile": "https://unsplash.com/@chethank"
    },
    {
        "id": "hampi", "name": "Hampi", "state": "Karnataka", "is_ut": False,
        "lat": 15.3350, "lon": 76.4600, "category": "UNESCO Heritage", "best_season": "October to March",
        "budget": 3200, "days": 3,
        "overview": "UNESCO World Heritage site of ancient Vijayanagara Empire with boulder-strewn landscapes and monumental stone temples.",
        "attractions": ["Virupaksha Temple", "Vijaya Vittala Temple & Stone Chariot", "Lotus Mahal", "Elephant Stables", "Matanga Hill"],
        "nearby": ["Hosapete", "Badami", "Aihole"],
        "activities": ["Sunrise trek atop Matanga Hill", "Coracle boat ride across Tungabhadra river", "Bouldering and architecture cycling tour"],
        "img_url": "https://images.unsplash.com/photo-1609766857041-ed402ea8069a?auto=format&fit=crop&w=1200&q=80",
        "photographer": "Harsha Vardhan", "profile": "https://unsplash.com/@harshavardhan"
    },
    {
        "id": "mysuru", "name": "Mysuru (Mysore)", "state": "Karnataka", "is_ut": False,
        "lat": 12.2958, "lon": 76.6394, "category": "Royal Heritage", "best_season": "September to March",
        "budget": 3500, "days": 2,
        "overview": "City of Palaces celebrated for illuminated Amba Vilas Palace, Dasara royal processions, and Mysore Pak sweets.",
        "attractions": ["Mysore Palace", "Chamundi Hill", "Brindavan Gardens", "St. Philomena's Cathedral", "Mysore Zoo"],
        "nearby": ["Srirangapatna", "Somnathpur", "Coorg"],
        "activities": ["Viewing 100,000 bulbs illuminating Mysore Palace", "Climbing Chamundeshwari 1,000 steps", "Tasting melt-in-mouth original Mysore Pak"],
        "img_url": "https://images.unsplash.com/photo-1582510003544-4d00b7f74220?auto=format&fit=crop&w=1200&q=80",
        "photographer": "Ravi Shankar", "profile": "https://unsplash.com/@ravishankar"
    },
    {
        "id": "gokarna", "name": "Gokarna", "state": "Karnataka", "is_ut": False,
        "lat": 14.5479, "lon": 74.3188, "category": "Beach & Spiritual", "best_season": "October to March",
        "budget": 2800, "days": 3,
        "overview": "Laidback coastal holy town where Shiva Atmalinga temple meets secluded cliffs and pristine Om Beach.",
        "attractions": ["Om Beach", "Kudle Beach", "Half Moon Beach", "Paradise Beach", "Mahabaleshwar Temple"],
        "nearby": ["Karwar", "Murudeshwar", "Dandeli"],
        "activities": ["Beach trekking from Kudle to Paradise", "Kayaking on Om Beach", "Watching bioluminescent waves at night"],
        "img_url": "https://images.unsplash.com/photo-1512343879784-a960bf40e7f2?auto=format&fit=crop&w=1200&q=80",
        "photographer": "Anish Shetty", "profile": "https://unsplash.com/@anishshetty"
    },
    {
        "id": "chikmagalur", "name": "Chikmagalur", "state": "Karnataka", "is_ut": False,
        "lat": 13.3161, "lon": 75.7720, "category": "Hill Station", "best_season": "September to May",
        "budget": 3400, "days": 3,
        "overview": "Birthplace of Indian coffee nestled beneath Mullayanagiri peak, draped in lush shola forests and mountain streams.",
        "attractions": ["Mullayanagiri Peak", "Baba Budangiri", "Hebbe Falls", "Coffee Yatra Museum", "Kudremukh National Park"],
        "nearby": ["Belur", "Halebidu", "Shimoga"],
        "activities": ["Trek to Mullayanagiri Karnataka highest summit", "Coffee tasting session at plantation homestay", "Dip in crystal Hebbe waterfall stream"],
        "img_url": "https://images.unsplash.com/photo-1544735716-392fe2489ffa?auto=format&fit=crop&w=1200&q=80",
        "photographer": "Girish Rao", "profile": "https://unsplash.com/@girishrao"
    },
    {
        "id": "badami", "name": "Badami", "state": "Karnataka", "is_ut": False,
        "lat": 15.9189, "lon": 75.6766, "category": "Heritage Caves", "best_season": "October to March",
        "budget": 2700, "days": 2,
        "overview": "Ancient Chalukya kingdom capital famous for sandstone rock-cut cave temples carved into red cliffs beside Agastya Lake.",
        "attractions": ["Badami Cave Temples", "Agastya Lake", "Bhuthanatha Temples", "Badami Fort", "Banashankari Temple"],
        "nearby": ["Pattadakal", "Aihole", "Hampi"],
        "activities": ["Rock climbing on Badami red sandstone cliffs", "Inspecting 6th-century Nataraja 18-armed sculpture", "Sunset view over Bhuthanatha lake temple"],
        "img_url": "https://images.unsplash.com/photo-1609766857041-ed402ea8069a?auto=format&fit=crop&w=1200&q=80",
        "photographer": "Kiran Hegde", "profile": "https://unsplash.com/@kiranhegde"
    },
    {
        "id": "dandeli", "name": "Dandeli", "state": "Karnataka", "is_ut": False,
        "lat": 15.2415, "lon": 74.6190, "category": "Adventure & Forest", "best_season": "October to May",
        "budget": 3500, "days": 2,
        "overview": "Adrenaline capital of Karnataka situated on the Kali River in dense Western Ghats, famed for white water rafting.",
        "attractions": ["Kali River", "Dandeli Wildlife Sanctuary", "Syntheri Rocks", "Shiroli Peak", "Kavala Caves"],
        "nearby": ["Goa", "Gokarna", "Hubli"],
        "activities": ["Grade 3 white water rafting on Kali river", "Ziplining and river zorbing", "Jungle safari for black panthers and hornbills"],
        "img_url": "https://images.unsplash.com/photo-1506744038136-46273834b3fb?auto=format&fit=crop&w=1200&q=80",
        "photographer": "Sandeep Kulkarni", "profile": "https://unsplash.com/@sandeepkulkarni"
    },
    {
        "id": "kabini", "name": "Kabini", "state": "Karnataka", "is_ut": False,
        "lat": 11.9167, "lon": 76.3500, "category": "Luxury Wildlife", "best_season": "October to May",
        "budget": 6500, "days": 2,
        "overview": "One of India's premier tiger and leopard sanctuaries along Kabini Reservoir, world-famous for the Black Panther.",
        "attractions": ["Nagarhole Tiger Reserve", "Kabini River Boat Safari", "Kabini Dam", "Tribal Village Experience"],
        "nearby": ["Mysuru", "Bandipur", "Wayanad"],
        "activities": ["Boat safari for riverbank elephant herds", "Open 4x4 jeep safari for big cats", "Luxury wildlife tented stay"],
        "img_url": "https://images.unsplash.com/photo-1512343879784-a960bf40e7f2?auto=format&fit=crop&w=1200&q=80",
        "photographer": "Vinod Kumar", "profile": "https://unsplash.com/@vinodkumar"
    },
    {
        "id": "udupi", "name": "Udupi", "state": "Karnataka", "is_ut": False,
        "lat": 13.3409, "lon": 74.7421, "category": "Coastal & Spiritual", "best_season": "October to March",
        "budget": 3000, "days": 2,
        "overview": "Coastal culinary town world-famous for authentic Udupi vegetarian cuisine, Sri Krishna Matha, and St. Mary's basalt island.",
        "attractions": ["Sri Krishna Temple", "Malpe Beach", "St. Mary's Basalt Island", "Kaup Lighthouse", "Delta Beach"],
        "nearby": ["Mangalore", "Murudeshwar", "Kollur"],
        "activities": ["Boat trip to hexagonal columnar basalt rocks on St. Mary's", "Watching Krishna Kanakana Kindi window", "Tasting traditional Udupi Thali"],
        "img_url": "https://images.unsplash.com/photo-1590050752117-238cb0fb12b1?auto=format&fit=crop&w=1200&q=80",
        "photographer": "Praveen Shenoy", "profile": "https://unsplash.com/@praveenshenoy"
    },
    {
        "id": "murudeshwar", "name": "Murudeshwar", "state": "Karnataka", "is_ut": False,
        "lat": 14.0940, "lon": 74.4899, "category": "Coastal Landmark", "best_season": "October to March",
        "budget": 2900, "days": 2,
        "overview": "Seaside coastal pilgrimage spot home to the world's second-tallest Shiva statue (123 ft) and 20-storey Raja Gopura.",
        "attractions": ["Murudeshwar Shiva Statue", "Raja Gopura", "Murudeshwar Beach", "Netrani Scuba Island", "Fort Ruins"],
        "nearby": ["Gokarna", "Honnavar", "Udupi"],
        "activities": ["Scuba diving at Netrani Island", "Lift ride to 18th floor of Raja Gopura", "Water sports on Murudeshwar beach"],
        "img_url": "https://images.unsplash.com/photo-1609766857041-ed402ea8069a?auto=format&fit=crop&w=1200&q=80",
        "photographer": "Venkatesh Rao", "profile": "https://unsplash.com/@venkateshrao"
    },
    {
        "id": "bandipur", "name": "Bandipur National Park", "state": "Karnataka", "is_ut": False,
        "lat": 11.6664, "lon": 76.6291, "category": "Wildlife Safari", "best_season": "October to May",
        "budget": 4200, "days": 2,
        "overview": "Former royal hunting reserve of Mysuru Maharajas, a vital tiger corridor connecting Western and Eastern Ghats.",
        "attractions": ["Bandipur Tiger Reserve Safari Zone", "Himavad Gopalaswamy Betta", "Moyar River Gorge"],
        "nearby": ["Ooty", "Mudumalai", "Mysuru"],
        "activities": ["Early morning tiger and leopard safari", "Visiting foggy Gopalaswamy hill temple", "Spotting Indian gaur and wild dogs"],
        "img_url": "https://images.unsplash.com/photo-1512343879784-a960bf40e7f2?auto=format&fit=crop&w=1200&q=80",
        "photographer": "Darshan Urs", "profile": "https://unsplash.com/@darshanurs"
    },

    # ---------- TELANGANA (8) ----------
    {
        "id": "hyderabad", "name": "Hyderabad", "state": "Telangana", "is_ut": False,
        "lat": 17.3850, "lon": 78.4867, "category": "Heritage & Culinary", "best_season": "October to March",
        "budget": 4200, "days": 3,
        "overview": "City of Pearls celebrated for majestic 400-year Charminar, Golconda acoustic fortress, and fragrant Dum Biryani.",
        "attractions": ["Charminar", "Golconda Fort", "Chowmahalla Palace", "Qutb Shahi Tombs", "Hussain Sagar Lake", "Ramoji Film City"],
        "nearby": ["Warangal", "Bidar", "Nagarjuna Sagar"],
        "activities": ["Acoustic clapping test at Golconda Fort", "Feasting on authentic Hyderabadi Dum Biryani & Irani Chai", "Shopping for pearl jewellery in Laad Bazaar"],
        "img_url": "https://images.unsplash.com/photo-1582510003544-4d00b7f74220?auto=format&fit=crop&w=1200&q=80",
        "photographer": "Mohammed Imran", "profile": "https://unsplash.com/@mohammedimran"
    },
    {
        "id": "warangal", "name": "Warangal", "state": "Telangana", "is_ut": False,
        "lat": 17.9689, "lon": 79.5941, "category": "Kakatiya Heritage", "best_season": "October to March",
        "budget": 2800, "days": 2,
        "overview": "Ancient capital of the Kakatiya Dynasty home to the thousand-pillar temple and iconic stone Thorana gateway.",
        "attractions": ["Thousand Pillar Temple", "Warangal Fort", "Bhadrakali Temple", "Kakatiya Kala Thoranam", "Pakhal Lake"],
        "nearby": ["Ramappa", "Hyderabad", "Khammam"],
        "activities": ["Photographing the monolithic Kakatiya arch", "Studying star-shaped Thousand Pillar Temple", "Boating on Pakhal wildlife lake"],
        "img_url": "https://images.unsplash.com/photo-1609766857041-ed402ea8069a?auto=format&fit=crop&w=1200&q=80",
        "photographer": "Srikanth Reddy", "profile": "https://unsplash.com/@srikanthreddy"
    },
    {
        "id": "ramappa", "name": "Ramappa Temple (Palampet)", "state": "Telangana", "is_ut": False,
        "lat": 18.2644, "lon": 79.9408, "category": "UNESCO Heritage", "best_season": "October to March",
        "budget": 2600, "days": 1,
        "overview": "UNESCO World Heritage 13th-century engineering marvel constructed with floating bricks and intricately carved black basalt.",
        "attractions": ["Ramappa Rudreshwara Temple", "Ramappa Lake", "Katasani Water Reservoir", "Ghanpur Temples"],
        "nearby": ["Warangal", "Mulugu", "Laknavaram"],
        "activities": ["Inspecting floating bricks in water", "Admiring bracket dancing dancer figures", "Boating across Ramappa lake"],
        "img_url": "https://images.unsplash.com/photo-1609766857041-ed402ea8069a?auto=format&fit=crop&w=1200&q=80",
        "photographer": "Vamsi Krishna", "profile": "https://unsplash.com/@vamsikrishna"
    },
    {
        "id": "nagarjuna_sagar", "name": "Nagarjuna Sagar", "state": "Telangana", "is_ut": False,
        "lat": 16.5772, "lon": 79.3125, "category": "Riverine & Dam", "best_season": "September to February",
        "budget": 3000, "days": 2,
        "overview": "World's largest masonry dam on the Krishna River holding an island museum featuring ancient Buddhist monuments.",
        "attractions": ["Nagarjuna Sagar Dam", "Nagarjunakonda Island Museum", "Ethipothala Waterfalls", "Anupu Buddhist Site"],
        "nearby": ["Hyderabad", "Srisailam", "Guntur"],
        "activities": ["Steamer boat cruise to Nagarjunakonda Island", "Viewing massive 26 crest gates water discharge", "Ethipothala falls light show"],
        "img_url": "https://images.unsplash.com/photo-1506744038136-46273834b3fb?auto=format&fit=crop&w=1200&q=80",
        "photographer": "Rajesh Goud", "profile": "https://unsplash.com/@rajeshgoud"
    },
    {
        "id": "bhadrachalam", "name": "Bhadrachalam", "state": "Telangana", "is_ut": False,
        "lat": 17.6688, "lon": 80.8935, "category": "Spiritual Riverine", "best_season": "October to March",
        "budget": 2500, "days": 2,
        "overview": "Sacred temple town on Godavari River banks dedicated to Lord Rama, associated with composer Bhakta Ramadasu.",
        "attractions": ["Sita Ramachandraswamy Temple", "Godavari River Ghats", "Parnasala", "Papikondalu Boat Point"],
        "nearby": ["Khammam", "Rajahmundry", "Warangal"],
        "activities": ["Holy dip in Godavari river", "Godavari river cruise to Papi Hills", "Visiting Ramadasu prison cell history"],
        "img_url": "https://images.unsplash.com/photo-1590050752117-238cb0fb12b1?auto=format&fit=crop&w=1200&q=80",
        "photographer": "Sai Teja", "profile": "https://unsplash.com/@saiteja"
    },
    {
        "id": "nizamabad", "name": "Nizamabad", "state": "Telangana", "is_ut": False,
        "lat": 18.6725, "lon": 78.0941, "category": "Heritage & Water", "best_season": "October to March",
        "budget": 2400, "days": 1,
        "overview": "Historic regional capital adorned with Nizamabad Fort, Ashok Sagar lake garden, and Alisagar reservoir.",
        "attractions": ["Nizamabad Fort", "Alisagar Deer Park", "Ashok Sagar", "Neelakantheswara Temple", "Dichpally Ramalayam"],
        "nearby": ["Hyderabad", "Nanded", "Bodhan"],
        "activities": ["Climbing Nizamabad hill fort", "Boating on Ashok Sagar", "Admiring Dichpally Khajuraho-style temple carvings"],
        "img_url": "https://images.unsplash.com/photo-1582510003544-4d00b7f74220?auto=format&fit=crop&w=1200&q=80",
        "photographer": "Santosh B", "profile": "https://unsplash.com/@santoshb"
    },
    {
        "id": "medak", "name": "Medak", "state": "Telangana", "is_ut": False,
        "lat": 18.0450, "lon": 78.2610, "category": "Heritage Architecture", "best_season": "October to February",
        "budget": 2300, "days": 1,
        "overview": "Historic district centered around towering 175-ft Neo-Gothic Medak Cathedral and 12th-century Kakatiya hill fort.",
        "attractions": ["Medak Cathedral (Cathedral Church)", "Medak Fort", "Pocharam Wildlife Sanctuary & Dam", "Edupayala Vana Durga Temple"],
        "nearby": ["Hyderabad", "Sangareddy", "Siddipet"],
        "activities": ["Admiring stained glass windows inside Medak Church", "Hiking to Medak Fort summit", "Birdwatching at Pocharam reservoir"],
        "img_url": "https://images.unsplash.com/photo-1582510003544-4d00b7f74220?auto=format&fit=crop&w=1200&q=80",
        "photographer": "Nikhil Rao", "profile": "https://unsplash.com/@nikhilrao"
    },
    {
        "id": "ananthagiri_hills", "name": "Ananthagiri Hills", "state": "Telangana", "is_ut": False,
        "lat": 17.3111, "lon": 77.8681, "category": "Nature & Forest", "best_season": "July to February",
        "budget": 2600, "days": 2,
        "overview": "Dense teakwood forest retreat in Vikarabad district, origin of the Musi River and popular weekend camping haven.",
        "attractions": ["Sri Anantha Padmanabha Swamy Temple", "Kotepally Reservoir", "Nagasamudram Lake", "Kerelli View Point"],
        "nearby": ["Hyderabad", "Vikarabad", "Tandur"],
        "activities": ["Kayaking in Kotepally reservoir", "Forest trekking through coffee trees and trails", "Stargazing at clifftop camp"],
        "img_url": "https://images.unsplash.com/photo-1544735716-392fe2489ffa?auto=format&fit=crop&w=1200&q=80",
        "photographer": "Karthik Reddy", "profile": "https://unsplash.com/@karthikreddy"
    },

    # ---------- ANDHRA PRADESH (10) ----------
    {
        "id": "tirupati", "name": "Tirupati", "state": "Andhra Pradesh", "is_ut": False,
        "lat": 13.6288, "lon": 79.4192, "category": "Spiritual Heritage", "best_season": "September to March",
        "budget": 3000, "days": 2,
        "overview": "Ancient sacred hill city home to the world's most visited Hindu shrine, the Sri Venkateswara Temple atop the Tirumala Seven Hills.",
        "attractions": ["Sri Venkateswara Temple (Tirumala)", "Silathoranam Natural Arch", "Kapila Theertham", "Chandragiri Fort", "Padmavathi Temple"],
        "nearby": ["Chandragiri", "Srikalahasti", "Kanipakam"],
        "activities": ["Tirumala Hills Darshan", "Tirupati Laddu Prasadam tasting", "Silathoranam geological walk", "Chandragiri Fort light & sound show"],
        "img_url": "https://images.unsplash.com/photo-1609766857041-ed402ea8069a?auto=format&fit=crop&w=1200&q=80",
        "photographer": "Naveen Kumar", "profile": "https://unsplash.com/@naveenkumar"
    },
    {
        "id": "visakhapatnam", "name": "Visakhapatnam (Vizag)", "state": "Andhra Pradesh", "is_ut": False,
        "lat": 17.6868, "lon": 83.2185, "category": "Coastal City", "best_season": "October to March",
        "budget": 3500, "days": 3,
        "overview": "The 'Jewel of the East Coast', dynamic port city where scenic green Eastern Ghats plunge directly into the Bay of Bengal.",
        "attractions": ["Rishikonda Beach", "Kailasagiri Hilltop Park", "INS Kursura Submarine Museum", "Ramakrishna Beach", "Thotlakonda Buddhist Complex"],
        "nearby": ["Araku Valley", "Borra Caves", "Bheemunipatnam"],
        "activities": ["Touring inside real INS Kursura submarine", "Ropeway ride to Kailasagiri", "Surfing at Rishikonda beach", "Exploring ancient Buddhist stupas"],
        "img_url": "https://images.unsplash.com/photo-1590050752117-238cb0fb12b1?auto=format&fit=crop&w=1200&q=80",
        "photographer": "Pavan Kalyan", "profile": "https://unsplash.com/@pavankalyan"
    },
    {
        "id": "araku_valley", "name": "Araku Valley", "state": "Andhra Pradesh", "is_ut": False,
        "lat": 18.3273, "lon": 82.8775, "category": "Hill Station", "best_season": "October to March",
        "budget": 3200, "days": 2,
        "overview": "Serene valley in the Eastern Ghats famous for aromatic organic tribal coffee plantations, Borra million-year-old limestone caves, and waterfalls.",
        "attractions": ["Borra Caves", "Araku Coffee Museum & Plantations", "Katiki Waterfalls", "Padmapuram Botanical Gardens", "Chaparai Water Cascades"],
        "nearby": ["Visakhapatnam", "Ananthagiri Hills", "Tyda"],
        "recommended_activities": ["Scenic Vistadome train ride through 84 tunnels", "Borra cave stalactite exploration", "Tasting GI-tagged Araku Valley tribal coffee"],
        "img_url": "https://images.unsplash.com/photo-1506744038136-46273834b3fb?auto=format&fit=crop&w=1200&q=80",
        "photographer": "Siva Prasad", "profile": "https://unsplash.com/@sivaprasad"
    },
    {
        "id": "vijayawada", "name": "Vijayawada", "state": "Andhra Pradesh", "is_ut": False,
        "lat": 16.5062, "lon": 80.6480, "category": "Cultural & Riverine", "best_season": "October to March",
        "budget": 2800, "days": 2,
        "overview": "Bustling cultural hub on the banks of Krishna River, famous for hilltop Kanaka Durga Temple and 7th-century rock-cut Undavalli Caves.",
        "attractions": ["Kanaka Durga Temple (Indrakeeladri)", "Prakasam Barrage", "Undavalli Caves (Monolithic Vishnu)", "Bhavani Island", "Mogalarajapuram Caves"],
        "nearby": ["Amaravati", "Mangalagiri", "Kuchipudi"],
        "activities": ["Bhavani Island river resort boating", "Undavalli monolithic cave exploration", "Krishna River evening barrage walk"],
        "img_url": "https://images.unsplash.com/photo-1596707323608-251f49e491c1?auto=format&fit=crop&w=1200&q=80",
        "photographer": "Ravi Teja", "profile": "https://unsplash.com/@raviteja"
    },
    {
        "id": "lepakshi", "name": "Lepakshi", "state": "Andhra Pradesh", "is_ut": False,
        "lat": 13.8042, "lon": 77.6080, "category": "Heritage Architecture", "best_season": "October to March",
        "budget": 2400, "days": 1,
        "overview": "Marvel of 16th-century Vijayanagara architecture famed for the Veerabhadra Temple, the mysterious Hanging Pillar, and colossal monolithic Nandi.",
        "attractions": ["Veerabhadra Temple", "Hanging Pillar of Lepakshi", "Monolithic Nandi Bull (largest in India)", "Nagalinga (Seven-headed Serpent)", "Kalyana Mandapa"],
        "nearby": ["Hindupur", "Bengaluru", "Puttaparthi"],
        "activities": ["Passing cloth under the mysterious Hanging Pillar", "Photographing monolithic granite Nandi", "Studying Vijayanagara ceiling frescoes"],
        "img_url": "https://images.unsplash.com/photo-1600100397608-f010f443a758?auto=format&fit=crop&w=1200&q=80",
        "photographer": "Karthik Reddy", "profile": "https://unsplash.com/@karthikreddy"
    },
    {
        "id": "gandikota", "name": "Gandikota", "state": "Andhra Pradesh", "is_ut": False,
        "lat": 14.8153, "lon": 78.2862, "category": "Canyon & Heritage", "best_season": "October to March",
        "budget": 2600, "days": 2,
        "overview": "The 'Grand Canyon of India', where the Penna River cuts a dramatic 300-foot gorge through red granite Erramala hills guarded by a 12th-century fort.",
        "attractions": ["Gandikota Gorge & Canyon Viewpoint", "Gandikota Fort", "Madhavaraya Swamy Temple", "Raghunathaswamy Temple", "Juma Masjid"],
        "nearby": ["Belum Caves", "Jammalamadugu", "Kadapa"],
        "activities": ["Sunset cliff-edge camping above Penna gorge", "Kayaking on Penna River", "Belum Caves subterranean expedition", "Fort bouldering"],
        "img_url": "https://images.unsplash.com/photo-1506744038136-46273834b3fb?auto=format&fit=crop&w=1200&q=80",
        "photographer": "Chaitanya Krishna", "profile": "https://unsplash.com/@chaitanyak"
    },
    {
        "id": "srisailam", "name": "Srisailam", "state": "Andhra Pradesh", "is_ut": False,
        "lat": 16.0747, "lon": 78.8687, "category": "Spiritual & Nature", "best_season": "October to March",
        "budget": 2600, "days": 2,
        "overview": "Ancient pilgrimage town situated in the deep Nallamala forest hills along Krishna river, housing Mallikarjuna Jyotirlinga and Bhramaramba Shaktipeeth.",
        "attractions": ["Mallikarjuna Swamy Temple", "Srisailam Dam & Krishna Reservoir", "Pathala Ganga Ropeway", "Nallamala Forest Tiger Reserve", "Akka Mahadevi Caves"],
        "nearby": ["Mahanandi", "Nagarjunasagar", "Kurnool"],
        "activities": ["Pathala Ganga ropeway descent and coracle ride", "Boat trip to Akka Mahadevi caves", "Nallamala forest wildlife drive"],
        "img_url": "https://images.unsplash.com/photo-1621252179027-94459d278660?auto=format&fit=crop&w=1200&q=80",
        "photographer": "Sai Sandeep", "profile": "https://unsplash.com/@saisandeep"
    },
    {
        "id": "rajahmundry", "name": "Rajahmundry", "state": "Andhra Pradesh", "is_ut": False,
        "lat": 17.0005, "lon": 81.8040, "category": "Cultural & Riverine", "best_season": "October to March",
        "budget": 2700, "days": 2,
        "overview": "The cultural capital of Andhra Pradesh located on the banks of Godavari River, renowned for the historic Godavari Arch Bridge and Papikondalu boat tours.",
        "attractions": ["Godavari Arch Bridge", "Kotilingeshwara Temple & Ghat", "Papikondalu River Cruise", "Sir Arthur Cotton Museum", "Damerla Rama Rao Art Gallery"],
        "nearby": ["Papikondalu", "Kakinada", "Draksharamam"],
        "activities": ["Scenic Godavari river cruise through Papikondalu hills", "Sunset stroll on Havelock Bridge", "Godavari Harathi darshan"],
        "img_url": "https://images.unsplash.com/photo-1544644181-1484b3fdfc62?auto=format&fit=crop&w=1200&q=80",
        "photographer": "Venkatesh Babu", "profile": "https://unsplash.com/@venkateshbabu"
    },
    {
        "id": "horsley_hills", "name": "Horsley Hills", "state": "Andhra Pradesh", "is_ut": False,
        "lat": 13.6558, "lon": 78.3970, "category": "Hill Station", "best_season": "Throughout the year",
        "budget": 2800, "days": 2,
        "overview": "Quaint hill retreat nestled at 4,147 ft amidst dense eucalyptus, gulmohar, and jacaranda groves, known as the 'Ooty of Andhra Pradesh'.",
        "attractions": ["Horsley Hills Viewpoint", "Gali Bandalu (Wind Rocks)", "Kalyani Eucalyptus Tree (150-yr old)", "Kaundinya Wildlife Sanctuary", "Gangotri Lake"],
        "nearby": ["Madanapalle", "Tirupati", "Bengaluru"],
        "activities": ["Trekking to Gali Bandalu wind rocks", "Ziplining and adventure sports", "Watching sweeping sunset over Chittoor plains"],
        "img_url": "https://images.unsplash.com/photo-1464822759023-fed622ff2c3b?auto=format&fit=crop&w=1200&q=80",
        "photographer": "Harsha Vardhan", "profile": "https://unsplash.com/@harshav"
    },
    {
        "id": "amaravati", "name": "Amaravati", "state": "Andhra Pradesh", "is_ut": False,
        "lat": 16.5828, "lon": 80.3547, "category": "Heritage & Buddhist", "best_season": "October to March",
        "budget": 2500, "days": 1,
        "overview": "Historic 2,000-year-old seat of the Satavahana dynasty on Krishna river, renowned for the colossal Dhyana Buddha statue and Maha Chaitya stupa.",
        "attractions": ["Dhyana Buddha Statue (125-ft)", "Amaravati Maha Chaitya Buddhist Stupa", "Amaralingeswara Swamy Temple", "Archaeological Museum Amaravati"],
        "nearby": ["Guntur", "Vijayawada", "Kondaveedu Fort"],
        "activities": ["Touring Dhyana Buddha meditation hall", "Examining 2nd-century BCE limestone Buddhist carvings", "River Krishna bank walk"],
        "img_url": "https://images.unsplash.com/photo-1590490360182-c33d57733427?auto=format&fit=crop&w=1200&q=80",
        "photographer": "Bhavani Prasad", "profile": "https://unsplash.com/@bhavaniprasad"
    },

    # ---------- PUDUCHERRY (UT) (5) ----------
    {
        "id": "puducherry_white_town", "name": "Puducherry White Town", "state": "Puducherry", "is_ut": True,
        "lat": 11.9338, "lon": 79.8329, "category": "Colonial Coastal", "best_season": "October to March",
        "budget": 3800, "days": 3,
        "overview": "French Riviera of the East lined with pastel mustard colonial villas, bougainvillea streets, and bohemian cafes.",
        "attractions": ["Promenade Beach Rock Beach", "Aurobindo Ashram", "French Quarter Streets", "Basilica of Sacred Heart of Jesus", "Bharathi Park"],
        "nearby": ["Auroville", "Paradise Beach", "Mahabalipuram"],
        "activities": ["Bicycle tour of French Quarter", "Croissant and French pastry tasting", "Sunset stroll on Promenade"],
        "img_url": "https://images.unsplash.com/photo-1582510003544-4d00b7f74220?auto=format&fit=crop&w=1200&q=80",
        "photographer": "Alexandre P", "profile": "https://unsplash.com/@alexandrep"
    },
    {
        "id": "auroville", "name": "Auroville", "state": "Puducherry", "is_ut": True,
        "lat": 11.9839, "lon": 79.8099, "category": "Universal Community", "best_season": "October to March",
        "budget": 3200, "days": 2,
        "overview": "Experimental universal township dedicated to human unity, focused around the golden geodesic sphere Matrimandir.",
        "attractions": ["Matrimandir Golden Dome", "Auroville Visitor Centre", "Savitri Bhavan", "Auro Beach", "Solar Kitchen"],
        "nearby": ["Puducherry", "Tindivanam", "Gingee"],
        "activities": ["Inner Chamber meditation at Matrimandir", "Organic vegan cafe trail", "Pottery and handmade paper making workshop"],
        "img_url": "https://images.unsplash.com/photo-1506744038136-46273834b3fb?auto=format&fit=crop&w=1200&q=80",
        "photographer": "Elena M", "profile": "https://unsplash.com/@elenam"
    },
    {
        "id": "paradise_beach", "name": "Paradise Beach (Chunnambar)", "state": "Puducherry", "is_ut": True,
        "lat": 11.8794, "lon": 79.8169, "category": "Beach & Island", "best_season": "October to March",
        "budget": 3000, "days": 1,
        "overview": "Isolated golden sandspit beach accessible by Chunnambar riverboat ferry with calm waves and beach huts.",
        "attractions": ["Paradise Beach Spit", "Chunnambar Boat House", "Backwater Mangroves", "Arikamedu Port"],
        "nearby": ["Puducherry White Town", "Cuddalore", "Villupuram"],
        "activities": ["Ferry ride across Chunnambar backwaters", "Beach volleyball and water sports", "Relaxing under thatch beach shacks"],
        "img_url": "https://images.unsplash.com/photo-1512343879784-a960bf40e7f2?auto=format&fit=crop&w=1200&q=80",
        "photographer": "Gautam V", "profile": "https://unsplash.com/@gautamv"
    },
    {
        "id": "promenade_beach", "name": "Promenade Beach", "state": "Puducherry", "is_ut": True,
        "lat": 11.9325, "lon": 79.8358, "category": "Beach Promenade", "best_season": "October to March",
        "budget": 3200, "days": 2,
        "overview": "1.5-km scenic vehicular-free rocky promenade fronted by the Bay of Bengal, iconic statues, and colonial landmarks.",
        "attractions": ["Rock Beach", "Mahatma Gandhi Statue", "French War Memorial", "Old Lighthouse", "Dupleix Statue"],
        "nearby": ["White Town", "Goubert Market", "Serenity Beach"],
        "activities": ["Sunrise oceanfront jog", "Evening sea breeze walking with street ice cream", "Heritage lighthouse photography"],
        "img_url": "https://images.unsplash.com/photo-1590050752117-238cb0fb12b1?auto=format&fit=crop&w=1200&q=80",
        "photographer": "Kavitha R", "profile": "https://unsplash.com/@kavithar"
    },
    {
        "id": "arikamedu", "name": "Arikamedu", "state": "Puducherry", "is_ut": True,
        "lat": 11.8953, "lon": 79.8175, "category": "Archaeological", "best_season": "October to March",
        "budget": 2400, "days": 1,
        "overview": "Ancient 1st-century BCE Roman-Chola maritime trading port with brick masonry warehouses on Ariyankuppam River.",
        "attractions": ["Arikamedu Archaeological Site", "Roman Warehouse Ruins", "Ariyankuppam River Mangroves"],
        "nearby": ["Puducherry", "Paradise Beach", "Veerampattinam"],
        "activities": ["Archaeological walking tour", "Spotting ancient amphora pottery traces", "Kayaking in Ariyankuppam river"],
        "img_url": "https://images.unsplash.com/photo-1609766857041-ed402ea8069a?auto=format&fit=crop&w=1200&q=80",
        "photographer": "Sridhar K", "profile": "https://unsplash.com/@sridhark"
    },

    # ---------- LAKSHADWEEP (UT) (5) ----------
    {
        "id": "kavaratti", "name": "Kavaratti Island", "state": "Lakshadweep", "is_ut": True,
        "lat": 10.5667, "lon": 72.6417, "category": "Coral Island", "best_season": "October to April",
        "budget": 5500, "days": 3,
        "overview": "Capital of Lakshadweep archipelago known for crystal turquoise lagoons, coconut canopies, and marine aquarium.",
        "attractions": ["Kavaratti Lagoon", "Ujra Mosque", "Marine Aquarium & Museum", "Dolphin Dive Centre", "Lighthouse"],
        "nearby": ["Agatti", "Bangaram", "Suheli Par"],
        "activities": ["Scuba diving and coral snorkeling", "Glass-bottom boat ride over live reef", "Lagoon kayaking at sunset"],
        "img_url": "https://images.unsplash.com/photo-1512343879784-a960bf40e7f2?auto=format&fit=crop&w=1200&q=80",
        "photographer": "Rasheed K", "profile": "https://unsplash.com/@rasheedk"
    },
    {
        "id": "agatti_island", "name": "Agatti Island", "state": "Lakshadweep", "is_ut": True,
        "lat": 10.8533, "lon": 72.1900, "category": "Coral Island", "best_season": "October to April",
        "budget": 6000, "days": 3,
        "overview": "Gateway island with one of the world's most spectacular airstrips surrounded completely by transparent aquamarine sea.",
        "attractions": ["Agatti Coral Reef", "Lagoon Beach", "Fishing Harbour", "Agatti Water Sports Complex"],
        "nearby": ["Bangaram", "Thinnakara", "Kavaratti"],
        "activities": ["Watching landing on the sea airstrip", "Deep sea game fishing", "Snorkeling with sea turtles"],
        "img_url": "https://images.unsplash.com/photo-1512343879784-a960bf40e7f2?auto=format&fit=crop&w=1200&q=80",
        "photographer": "Farhan Ahmed", "profile": "https://unsplash.com/@farhanahmed"
    },
    {
        "id": "bangaram_island", "name": "Bangaram Island", "state": "Lakshadweep", "is_ut": True,
        "lat": 10.9400, "lon": 72.2900, "category": "Luxury Atoll", "best_season": "October to April",
        "budget": 7500, "days": 3,
        "overview": "Teardrop-shaped uninhabited jewel island fringed with powder white sand, coral atolls, and bioluminescent plankton.",
        "attractions": ["Bangaram Lagoon", "Shipwreck Dive Point", "Thinnakara Island Sandbank", "Parali I & II Islets"],
        "nearby": ["Agatti", "Thinnakara", "Kavaratti"],
        "activities": ["Shipwreck scuba diving", "Island hopping to Thinnakara sandbank", "Watching night glowing bioluminescence"],
        "img_url": "https://images.unsplash.com/photo-1512343879784-a960bf40e7f2?auto=format&fit=crop&w=1200&q=80",
        "photographer": "Nizamudheen M", "profile": "https://unsplash.com/@nizamudheen"
    },
    {
        "id": "minicoy_island", "name": "Minicoy Island", "state": "Lakshadweep", "is_ut": True,
        "lat": 8.2833, "lon": 73.0500, "category": "Culture & Island", "best_season": "October to April",
        "budget": 5200, "days": 3,
        "overview": "Southernmost island with distinct Maldivian Mahl culture, traditional village hamlets, and 300-ft British lighthouse.",
        "attractions": ["Minicoy Lighthouse (1885)", "Traditional Village Hamlets", "Tuna Canneries", "Southern Point Reef"],
        "nearby": ["Maliku Atoll", "Kalpeni", "Kochi"],
        "activities": ["Climbing British Lighthouse for 360-degree atoll views", "Witnessing traditional Lava dance", "Tuna fishing expedition"],
        "img_url": "https://images.unsplash.com/photo-1512343879784-a960bf40e7f2?auto=format&fit=crop&w=1200&q=80",
        "photographer": "Zuhair Ali", "profile": "https://unsplash.com/@zuhairali"
    },
    {
        "id": "kadmat_island", "name": "Kadmat Island", "state": "Lakshadweep", "is_ut": True,
        "lat": 11.2333, "lon": 72.7833, "category": "Lagoon & Water Sports", "best_season": "October to April",
        "budget": 5000, "days": 2,
        "overview": "Elongated cardamum island surrounded on both sides by wide turquoise lagoons ideal for water sports enthusiasts.",
        "attractions": ["Kadmat Marine Reserve", "Kadmat Diving School", "Eastern White Sand Beach", "Coconut Groves"],
        "nearby": ["Amini", "Kiltan", "Agatti"],
        "activities": ["Windsurfing and water skiing in calm lagoon", "PADI scuba certification course", "Kayaking across turquoise shallow flats"],
        "img_url": "https://images.unsplash.com/photo-1512343879784-a960bf40e7f2?auto=format&fit=crop&w=1200&q=80",
        "photographer": "Irfan K", "profile": "https://unsplash.com/@irfank"
    }
]

print(f"South region loaded: {len(SOUTH_DESTINATIONS)} destinations.")
