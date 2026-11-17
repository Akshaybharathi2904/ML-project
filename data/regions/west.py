"""
TRAVELMATE AI - West India Destinations (46 Verified Destinations)
Rajasthan, Gujarat, Maharashtra, Goa, Dadra and Nagar Haveli and Daman and Diu
"""

WEST_DESTINATIONS = [
    # ---------- RAJASTHAN (12) ----------
    {
        "id": "udaipur", "name": "Udaipur", "state": "Rajasthan", "is_ut": False,
        "lat": 24.5854, "lon": 73.7125, "category": "Lakes & Royal Palaces", "best_season": "October to March",
        "budget": 4500, "days": 3,
        "overview": "City of Lakes and Venice of the East adorned with royal marble palaces, Lake Pichola cruises, and Aravali sunsets.",
        "attractions": ["City Palace Complex", "Lake Pichola Boating", "Jagdish Temple", "Saheliyon Ki Bari", "Bagore Ki Haveli", "Monsoon Palace"],
        "nearby": ["Kumbhalgarh", "Ranakpur", "Chittorgarh"],
        "activities": ["Boat cruise around Taj Lake Palace", "Dharohar folk dance at Bagore Ki Haveli", "Sunset view from Sajjangarh Monsoon Palace"],
        "img_url": "https://images.unsplash.com/photo-1599661046289-e31897846e41?auto=format&fit=crop&w=1200&q=80",
        "photographer": "Gaurav K", "profile": "https://unsplash.com/@gauravk"
    },
    {
        "id": "jaipur", "name": "Jaipur", "state": "Rajasthan", "is_ut": False,
        "lat": 26.9124, "lon": 75.7873, "category": "UNESCO Pink City", "best_season": "October to March",
        "budget": 4200, "days": 3,
        "overview": "The Pink City of India boasting UNESCO World Heritage status, majestic hill forts, astronomical observatories, and bazaars.",
        "attractions": ["Amber Fort & Palace", "Hawa Mahal (Palace of Winds)", "City Palace Jaipur", "Jantar Mantar", "Nahargarh Fort"],
        "nearby": ["Ajmer", "Pushkar", "Abhaneri"],
        "activities": ["Elephant or jeep ride up Amber Fort", "Photographing 953 honeycomb windows of Hawa Mahal", "Tasting traditional Dal Baati Churma at Chokhi Dhani"],
        "img_url": "https://images.unsplash.com/photo-1599661046289-e31897846e41?auto=format&fit=crop&w=1200&q=80",
        "photographer": "Aditya Shiva", "profile": "https://unsplash.com/@adityashiva"
    },
    {
        "id": "jodhpur", "name": "Jodhpur", "state": "Rajasthan", "is_ut": False,
        "lat": 26.2389, "lon": 73.0243, "category": "Blue City & Forts", "best_season": "October to March",
        "budget": 3800, "days": 2,
        "overview": "The Blue City watched over by the colossal 15th-century Mehrangarh Fort rising 400 feet above indigo-washed Brahmin houses.",
        "attractions": ["Mehrangarh Fort", "Jaswant Thada", "Umaid Bhawan Palace", "Clock Tower & Sardar Market", "Mandore Gardens"],
        "nearby": ["Osian", "Khimsar", "Pali"],
        "activities": ["Flying Fox zipline across Mehrangarh moats", "Walking through the blue lanes of Navchokiya", "Tasting Mirchi Vada and Mawa Kachori"],
        "img_url": "https://images.unsplash.com/photo-1582510003544-4d00b7f74220?auto=format&fit=crop&w=1200&q=80",
        "photographer": "Rohan Makhecha", "profile": "https://unsplash.com/@rohanmakhecha"
    },
    {
        "id": "jaisalmer", "name": "Jaisalmer", "state": "Rajasthan", "is_ut": False,
        "lat": 26.9157, "lon": 70.9083, "category": "Golden City & Desert", "best_season": "October to March",
        "budget": 4000, "days": 3,
        "overview": "The Golden City rising from the Thar Desert with its living golden sandstone fort, sculpted havelis, and Sam sand dunes.",
        "attractions": ["Jaisalmer Living Fort (Sonar Qila)", "Sam Sand Dunes", "Patwon Ki Haveli", "Gadisar Lake", "Kuldhara Ghost Village"],
        "nearby": ["Khuri", "Tanot Mata", "Longewala Border"],
        "activities": ["Camel safari and desert camping in Sam dunes", "Exploring living residential fort quarters", "Sunset boating on Gadisar Lake"],
        "img_url": "https://images.unsplash.com/photo-1544735716-392fe2489ffa?auto=format&fit=crop&w=1200&q=80",
        "photographer": "Fakurian Design", "profile": "https://unsplash.com/@fakurian"
    },
    {
        "id": "pushkar", "name": "Pushkar", "state": "Rajasthan", "is_ut": False,
        "lat": 26.4897, "lon": 74.5511, "category": "Sacred Lake & Desert", "best_season": "October to March",
        "budget": 2800, "days": 2,
        "overview": "Sacred desert oasis wrapped around 52 holy ghats, home to the rare Brahma Temple and the colorful annual Pushkar Camel Fair.",
        "attractions": ["Brahma Temple", "Pushkar Holy Lake & 52 Ghats", "Savitri Devi Hilltop Temple", "Varaha Temple", "Pushkar Camel Fair Ground"],
        "nearby": ["Ajmer Sharif", "Kishangarh", "Jaipur"],
        "activities": ["Cable car ride to hilltop Savitri Temple at sunrise", "Witnessing evening maha aarti at Varaha Ghat", "Attending the Pushkar Camel Fair"],
        "img_url": "https://images.unsplash.com/photo-1590050752117-238cb0fb12b1?auto=format&fit=crop&w=1200&q=80",
        "photographer": "Rahul Pandit", "profile": "https://unsplash.com/@rahulpandit"
    },
    {
        "id": "mount_abu", "name": "Mount Abu", "state": "Rajasthan", "is_ut": False,
        "lat": 24.5926, "lon": 72.7156, "category": "Hill Station", "best_season": "Throughout the year",
        "budget": 3500, "days": 2,
        "overview": "The only hill station in Rajasthan, famed for Nakki Lake legends and the world's most intricate marble Dilwara Jain Temples.",
        "attractions": ["Dilwara Jain Temples (11th Century)", "Nakki Lake", "Guru Shikhar Peak (1722m)", "Sunset Point", "Achalgarh Fort"],
        "nearby": ["Ambaji", "Udaipur", "Sirohi"],
        "activities": ["Marveling at translucent marble lace carvings in Dilwara", "Boating on Nakki Lake", "Viewing 360-degree sunset from Guru Shikhar"],
        "img_url": "https://images.unsplash.com/photo-1544735716-392fe2489ffa?auto=format&fit=crop&w=1200&q=80",
        "photographer": "Kishan Rathore", "profile": "https://unsplash.com/@kishanr"
    },
    {
        "id": "ranthambore", "name": "Ranthambore National Park", "state": "Rajasthan", "is_ut": False,
        "lat": 26.0173, "lon": 76.5026, "category": "Tiger Safari", "best_season": "October to June",
        "budget": 4800, "days": 2,
        "overview": "Iconic royal tiger reserve where wild Bengal tigers prowl among ancient fortress ruins, stepwells, and banyan trees.",
        "attractions": ["Ranthambore Tiger Reserve Safari Zones", "Ranthambore Fort (10th Century)", "Padam Talao Lake", "Trinetra Ganesha Temple"],
        "nearby": ["Sawai Madhopur", "Jaipur", "Tonk"],
        "activities": ["Open Canter or Gypsy tiger safari in Zone 1-5", "Climbing to 10th-century UNESCO Ranthambore Fort", "Visiting ancient Trinetra Ganesha Temple"],
        "img_url": "https://images.unsplash.com/photo-1512343879784-a960bf40e7f2?auto=format&fit=crop&w=1200&q=80",
        "photographer": "Dinesh Pareek", "profile": "https://unsplash.com/@dineshpareek"
    },
    {
        "id": "bikaner", "name": "Bikaner", "state": "Rajasthan", "is_ut": False,
        "lat": 28.0229, "lon": 73.3119, "category": "Desert Fort & Culture", "best_season": "October to March",
        "budget": 3200, "days": 2,
        "overview": "Thar desert trading stronghold celebrated for unconquered red sandstone Junagarh Fort, Karni Mata rat temple, and Bikaneri Bhujia.",
        "attractions": ["Junagarh Fort", "Karni Mata Temple (Deshnoke)", "Lalgarh Palace", "National Research Centre on Camel", "Rampuria Havelis"],
        "nearby": ["Deshnoke", "Gajner", "Jaisalmer"],
        "activities": ["Visiting Karni Mata temple with 25,000 holy black rats", "Sampling fresh camel milk ice cream at Camel Research Centre", "Photographing red sandstone Rampuria Havelis"],
        "img_url": "https://images.unsplash.com/photo-1609766857041-ed402ea8069a?auto=format&fit=crop&w=1200&q=80",
        "photographer": "Sanjay Bika", "profile": "https://unsplash.com/@sanjaybika"
    },
    {
        "id": "chittorgarh", "name": "Chittorgarh", "state": "Rajasthan", "is_ut": False,
        "lat": 24.8887, "lon": 74.6269, "category": "Fortress of Valor", "best_season": "October to March",
        "budget": 2800, "days": 1,
        "overview": "India's largest fort complex perched atop a 180m hill, immortalized by Rajput valor, Rani Padmini's jauhar, and Vijay Stambha.",
        "attractions": ["Chittorgarh Fort Complex", "Vijay Stambha (Tower of Victory)", "Kirti Stambha", "Rani Padmini's Palace", "Meera Temple"],
        "nearby": ["Udaipur", "Bhilwara", "Kumbhalgarh"],
        "activities": ["Climbing the 9-storey carved Tower of Victory", "Visiting water pavilions of Rani Padmini palace", "Learning legends of Mirabai"],
        "img_url": "https://images.unsplash.com/photo-1609766857041-ed402ea8069a?auto=format&fit=crop&w=1200&q=80",
        "photographer": "Manish Shekhawat", "profile": "https://unsplash.com/@manishs"
    },
    {
        "id": "kumbhalgarh", "name": "Kumbhalgarh", "state": "Rajasthan", "is_ut": False,
        "lat": 25.1528, "lon": 73.5872, "category": "Mighty Fortress", "best_season": "October to March",
        "budget": 3500, "days": 2,
        "overview": "Mewar mountain fortress featuring the Great Wall of India—the second-longest continuous wall in the world (36 km).",
        "attractions": ["Kumbhalgarh Fort & 36km Wall", "Badal Mahal (Cloud Palace)", "Kumbhalgarh Wildlife Sanctuary", "Neelkanth Mahadev Temple"],
        "nearby": ["Ranakpur", "Udaipur", "Nathdwara"],
        "activities": ["Walking the Great Wall of India ramparts", "Evening sound and light show illuminating fort battlements", "Visiting nearby marble Jain temples of Ranakpur"],
        "img_url": "https://images.unsplash.com/photo-1599661046289-e31897846e41?auto=format&fit=crop&w=1200&q=80",
        "photographer": "Devendra Sisodia", "profile": "https://unsplash.com/@devendras"
    },
    {
        "id": "bundi", "name": "Bundi", "state": "Rajasthan", "is_ut": False,
        "lat": 25.4415, "lon": 75.6440, "category": "Stepwells & Murals", "best_season": "October to March",
        "budget": 2700, "days": 2,
        "overview": "Picturesque Rajput blue town renowned for dramatic Taragarh Fort, exquisite Bundi school palace murals, and 50+ ornate stepwells.",
        "attractions": ["Taragarh Fort", "Bundi Garh Palace & Chitrashala", "Raniji Ki Baori Stepwell", "Nawal Sagar Lake", "Sukh Mahal"],
        "nearby": ["Kota", "Ranthambore", "Chittorgarh"],
        "activities": ["Studying vibrant turquoise murals in Chitrashala", "Descending 46m deep steps of Raniji Ki Baori", "Exploring atmospheric ruins of Taragarh Fort"],
        "img_url": "https://images.unsplash.com/photo-1582510003544-4d00b7f74220?auto=format&fit=crop&w=1200&q=80",
        "photographer": "Arvind Hada", "profile": "https://unsplash.com/@arvindhada"
    },
    {
        "id": "alwar", "name": "Alwar & Sariska", "state": "Rajasthan", "is_ut": False,
        "lat": 27.5530, "lon": 76.6346, "category": "Heritage & Tiger Reserve", "best_season": "October to March",
        "budget": 3400, "days": 2,
        "overview": "Aravalli kingdom gateway home to Bala Quila fort, Siliserh Palace lake, Sariska Tiger Reserve, and mysterious Bhangarh.",
        "attractions": ["Sariska Tiger Reserve", "Bala Quila (Alwar Fort)", "Siliserh Lake Palace", "City Palace Alwar & Moosi Maharani Chhatri", "Bhangarh Fort Ruins"],
        "nearby": ["Jaipur", "Delhi", "Bhangarh"],
        "activities": ["Tiger safari in Sariska valleys", "Boating on historic Siliserh Lake", "Visiting haunted ruins of Bhangarh Fort"],
        "img_url": "https://images.unsplash.com/photo-1512343879784-a960bf40e7f2?auto=format&fit=crop&w=1200&q=80",
        "photographer": "Narender Yadav", "profile": "https://unsplash.com/@narenderyadav"
    },

    # ---------- GUJARAT (10) ----------
    {
        "id": "ahmedabad", "name": "Ahmedabad", "state": "Gujarat", "is_ut": False,
        "lat": 23.0225, "lon": 72.5714, "category": "UNESCO World Heritage City", "best_season": "October to March",
        "budget": 3800, "days": 3,
        "overview": "India's first UNESCO World Heritage City, cradle of the Independence movement at Sabarmati Ashram, and stepwell architecture.",
        "attractions": ["Sabarmati Gandhi Ashram", "Adalaj Stepwell", "Sabarmati Riverfront", "Sidi Saiyyed Mosque (Tree of Life)", "Hutheesing Jain Temple"],
        "nearby": ["Gandhinagar", "Modhera", "Patan"],
        "activities": ["Heritage Pol walking tour in Old City", "Visiting Gandhi's Hriday Kunj spinning charkha", "Street food hopping at Manek Chowk night bazaar"],
        "img_url": "https://images.unsplash.com/photo-1582510003544-4d00b7f74220?auto=format&fit=crop&w=1200&q=80",
        "photographer": "Hardik Patel", "profile": "https://unsplash.com/@hardikpatel"
    },
    {
        "id": "rann_of_kutch", "name": "Rann of Kutch (Dhordo)", "state": "Gujarat", "is_ut": False,
        "lat": 23.7337, "lon": 69.8597, "category": "White Salt Desert", "best_season": "November to February (Rann Utsav)",
        "budget": 5200, "days": 3,
        "overview": "World's largest salt desert transforming under the full moon into an endless surreal white canvas during the vibrant Rann Utsav.",
        "attractions": ["White Desert (Dhordo)", "Kalo Dungar (Black Hill - Highest Point)", "Rann Utsav Tent City", "Hodka Craft Village", "India Bridge"],
        "nearby": ["Bhuj", "Mandvi", "Dholavira"],
        "activities": ["Full moon night walk on gleaming white salt", "Visiting Kutchi Rogan art and mirror embroidery artisans", "Sunset panoramic view over Great Rann from Kalo Dungar"],
        "img_url": "https://images.unsplash.com/photo-1506744038136-46273834b3fb?auto=format&fit=crop&w=1200&q=80",
        "photographer": "Nirav Dave", "profile": "https://unsplash.com/@niravdave"
    },
    {
        "id": "gir_national_park", "name": "Gir National Park (Sasan Gir)", "state": "Gujarat", "is_ut": False,
        "lat": 21.1243, "lon": 70.8242, "category": "Asiatic Lion Sanctuary", "best_season": "December to April",
        "budget": 4500, "days": 2,
        "overview": "The last and only natural refuge on Earth for the majestic Asiatic Lion (Panthera leo persica) in dry deciduous scrub forest.",
        "attractions": ["Gir Jungle Safari Core Zone", "Devalia Safari Park (Gir Interpretation Zone)", "Kamleshwar Dam", "Crocodile Breeding Farm"],
        "nearby": ["Junagadh", "Somnath", "Diu"],
        "activities": ["Open Gypsy safari to spot Asiatic Lion prides", "Crocodile watching at Kamleshwar reservoir", "Interacting with pastoral Maldhari tribes"],
        "img_url": "https://images.unsplash.com/photo-1512343879784-a960bf40e7f2?auto=format&fit=crop&w=1200&q=80",
        "photographer": "Bhavin Shah", "profile": "https://unsplash.com/@bhavinshah"
    },
    {
        "id": "somnath", "name": "Somnath", "state": "Gujarat", "is_ut": False,
        "lat": 20.8880, "lon": 70.4012, "category": "Sacred Jyotirlinga", "best_season": "October to March",
        "budget": 2900, "days": 2,
        "overview": "First among the 12 holy Shiva Jyotirlingas, standing on the rugged Arabian Sea coast as an eternal symbol of resurrection.",
        "attractions": ["Somnath Temple & Sea Promenade", "Triveni Sangam", "Bhalka Tirth", "Prabhas Patan Museum", "Sound & Light Show"],
        "nearby": ["Veraval", "Gir", "Diu"],
        "activities": ["Evening sound and light show narrated by Amitabh Bachchan", "Walking along the Arabian sea promenade barrier", "Darshan at gold-domed Jyotirlinga"],
        "img_url": "https://images.unsplash.com/photo-1609766857041-ed402ea8069a?auto=format&fit=crop&w=1200&q=80",
        "photographer": "Chirag Joshi", "profile": "https://unsplash.com/@chiragjoshi"
    },
    {
        "id": "dwarka", "name": "Dwarka", "state": "Gujarat", "is_ut": False,
        "lat": 22.2442, "lon": 68.9685, "category": "Chardham Sacred", "best_season": "October to March",
        "budget": 3100, "days": 2,
        "overview": "Ancient Kingdom of Lord Krishna on the western tip of Saurashtra, one of the four cardinal Chardham pilgrimage sites.",
        "attractions": ["Dwarkadhish Temple (Jagat Mandir)", "Bet Dwarka Island", "Nageshwar Jyotirlinga", "Rukmini Devi Temple", "Shivrajpur Blue Flag Beach"],
        "nearby": ["Porbandar", "Jamnagar", "Somnath"],
        "activities": ["Boat ferry to holy Bet Dwarka island", "Watching 52-yard flag unfurling atop Dwarkadhish temple", "Swimming at pristine Shivrajpur Blue Flag Beach"],
        "img_url": "https://images.unsplash.com/photo-1609766857041-ed402ea8069a?auto=format&fit=crop&w=1200&q=80",
        "photographer": "Miten Trivedi", "profile": "https://unsplash.com/@mitentrivedi"
    },
    {
        "id": "statue_of_unity", "name": "Statue of Unity (Kevadia)", "state": "Gujarat", "is_ut": False,
        "lat": 21.8380, "lon": 73.7191, "category": "Monument & Eco-Tourism", "best_season": "October to March",
        "budget": 4200, "days": 2,
        "overview": "World's tallest statue (182 meters) honoring Sardar Vallabhbhai Patel on the Narmada River against the Vindhya-Satpura hills.",
        "attractions": ["Statue of Unity 153m Viewing Gallery", "Sardar Sarovar Dam", "Valley of Flowers Kevadia", "Jungle Safari & Aviary", "Glow Garden"],
        "nearby": ["Vadodara", "Bharuch", "Rajpipla"],
        "activities": ["Elevator ride to the chest viewing gallery inside the 182m statue", "Laser projection sound and light show on statue facade", "Dinner cruise on Narmada River"],
        "img_url": "https://images.unsplash.com/photo-1596176530529-78163a4f7af2?auto=format&fit=crop&w=1200&q=80",
        "photographer": "Parthiv Vyas", "profile": "https://unsplash.com/@parthivvyas"
    },
    {
        "id": "saputara", "name": "Saputara", "state": "Gujarat", "is_ut": False,
        "lat": 20.5794, "lon": 73.7495, "category": "Hill Station", "best_season": "July to March",
        "budget": 3300, "days": 2,
        "overview": "Abode of Serpents, the sole hill station in Gujarat nestled in the Sahyadri ranges of the Dang tribal forest belt.",
        "attractions": ["Saputara Lake", "Sunset Point & Cable Car", "Gira Waterfalls", "Step Garden", "Artist Village"],
        "nearby": ["Waghai", "Surat", "Nashik"],
        "activities": ["Boating on picturesque Saputara Lake", "Ropeway ride across valley to Sunset Point", "Tribal bamboo craft and Warli painting workshop"],
        "img_url": "https://images.unsplash.com/photo-1544735716-392fe2489ffa?auto=format&fit=crop&w=1200&q=80",
        "photographer": "Snehal Patel", "profile": "https://unsplash.com/@snehalpatel"
    },
    {
        "id": "champaner", "name": "Champaner-Pavagadh", "state": "Gujarat", "is_ut": False,
        "lat": 22.4842, "lon": 73.5358, "category": "UNESCO Archaeological", "best_season": "October to March",
        "budget": 2800, "days": 2,
        "overview": "UNESCO World Heritage site blending 8th-century Hindu-Jain Pavagadh hill temples with 16th-century Sultanate mosques.",
        "attractions": ["Jami Masjid Champaner", "Kalika Mata Temple Pavagadh", "Pavagadh Ropeway", "Kevada Masjid & Stepwell", "Citadel Walls"],
        "nearby": ["Vadodara", "Halol", "Ahmedabad"],
        "activities": ["Ropeway cable car ride up Pavagadh volcanic hill", "Admiring delicate stone jali carving at Jami Masjid", "Heritage walk through fort gateway ruins"],
        "img_url": "https://images.unsplash.com/photo-1609766857041-ed402ea8069a?auto=format&fit=crop&w=1200&q=80",
        "photographer": "Jayesh Parmar", "profile": "https://unsplash.com/@jayeshparmar"
    },
    {
        "id": "bhuj", "name": "Bhuj", "state": "Gujarat", "is_ut": False,
        "lat": 23.2420, "lon": 69.6669, "category": "Kutch Heritage & Craft", "best_season": "October to March",
        "budget": 3400, "days": 3,
        "overview": "Historic walled capital of Kutch celebrated for Prag Mahal Venetian palace, Aina Mahal Hall of Mirrors, and artisan craft villages.",
        "attractions": ["Aina Mahal (Hall of Mirrors)", "Prag Mahal & Clock Tower", "Kutch Museum", "Hamirsar Lake", "Shree Swaminarayan Temple Bhuj"],
        "nearby": ["Dhordo", "Mandvi", "Anjar"],
        "activities": ["Climbing Prag Mahal 45m Gothic clock tower", "Visiting Bhujodi artisan village for Ajrakh block prints", "Evening walk around Hamirsar Lake"],
        "img_url": "https://images.unsplash.com/photo-1582510003544-4d00b7f74220?auto=format&fit=crop&w=1200&q=80",
        "photographer": "Tarun Kutchhi", "profile": "https://unsplash.com/@tarunkutchhi"
    },
    {
        "id": "modhera", "name": "Modhera & Patan", "state": "Gujarat", "is_ut": False,
        "lat": 23.5833, "lon": 72.1333, "category": "UNESCO Sun Temple & Stepwell", "best_season": "October to March",
        "budget": 3000, "days": 1,
        "overview": "Architectural showcase featuring the 11th-century Modhera Sun Temple and UNESCO Rani Ki Vav inverted subterranean stepwell in Patan.",
        "attractions": ["Modhera Sun Temple & Surya Kund", "Rani Ki Vav (Queen's Stepwell)", "Patan Patola Silk Weaving House", "Sahastralinga Talav"],
        "nearby": ["Mehsana", "Ahmedabad", "Patan"],
        "activities": ["Inspecting 500+ principal sculptures inside Rani Ki Vav", "Photographing geometric steps of Surya Kund tank", "Watching double-ikat Patola silk saree weaving"],
        "img_url": "https://images.unsplash.com/photo-1609766857041-ed402ea8069a?auto=format&fit=crop&w=1200&q=80",
        "photographer": "Nirali Solanki", "profile": "https://unsplash.com/@niralisolanki"
    },

    # ---------- MAHARASHTRA (12) ----------
    {
        "id": "mumbai", "name": "Mumbai", "state": "Maharashtra", "is_ut": False,
        "lat": 18.9220, "lon": 72.8347, "category": "Metropolitan Capital", "best_season": "October to March",
        "budget": 5500, "days": 3,
        "overview": "Financial and Bollywood capital of India, famous for Gateway of India, UNESCO Victorian Gothic ensemble, and Marine Drive Queen's Necklace.",
        "attractions": ["Gateway of India", "Marine Drive (Queen's Necklace)", "Chhatrapati Shivaji Maharaj Terminus (CSMT)", "Elephanta Caves", "Colaba Causeway"],
        "nearby": ["Alibaug", "Lonavala", "Elephanta Island"],
        "activities": ["Ferry ride to 6th-century Elephanta Shiva rock caves", "Evening sunset walk on Marine Drive promenade", "Tasting Mumbai street food at Chowpatty Beach"],
        "img_url": "https://images.unsplash.com/photo-1570168007204-dfb528c6958f?auto=format&fit=crop&w=1200&q=80",
        "photographer": "Hardik Joshi", "profile": "https://unsplash.com/@hardikjoshi"
    },
    {
        "id": "pune", "name": "Pune", "state": "Maharashtra", "is_ut": False,
        "lat": 18.5204, "lon": 73.8567, "category": "Oxford of the East", "best_season": "July to March",
        "budget": 3800, "days": 3,
        "overview": "Cultural capital of the Marathas blending historic Shaniwar Wada, Aga Khan Palace, Osho ashram, and Sahyadri trek gateways.",
        "attractions": ["Shaniwar Wada", "Aga Khan Palace (Gandhi Memorial)", "Sinhagad Fort", "Dagdusheth Halwai Ganpati Temple", "Osho International Teerth"],
        "nearby": ["Lavasa", "Lonavala", "Mahabaleshwar"],
        "activities": ["Early morning trek to Sinhagad Fort with fresh pitla-bhakri", "Visiting Gandhi memorial at Aga Khan Palace", "Exploring Peshwa history at Shaniwar Wada"],
        "img_url": "https://images.unsplash.com/photo-1582510003544-4d00b7f74220?auto=format&fit=crop&w=1200&q=80",
        "photographer": "Saurabh Deshmukh", "profile": "https://unsplash.com/@saurabhd"
    },
    {
        "id": "lonavala", "name": "Lonavala & Khandala", "state": "Maharashtra", "is_ut": False,
        "lat": 18.7557, "lon": 73.4091, "category": "Sahyadri Hill Station", "best_season": "June to February",
        "budget": 3600, "days": 2,
        "overview": "Dual Sahyadri hill gateways famed for cascading monsoon waterfalls, Karla and Bhaja Buddhist caves, and chikki confectioneries.",
        "attractions": ["Tiger's Leap (Tiger Point)", "Bhushi Dam", "Karla & Bhaja Caves (2nd Century BCE)", "Rajmachi Fort Viewpoint", "Lonavala Lake"],
        "nearby": ["Khandala", "Pawna Lake", "Kamshet"],
        "activities": ["Camping and stargazing by Pawna Lake", "Exploring 2200-year-old rock-cut chaitya hall at Karla", "Tasting traditional Maganlal Lonavala chikki"],
        "img_url": "https://images.unsplash.com/photo-1544735716-392fe2489ffa?auto=format&fit=crop&w=1200&q=80",
        "photographer": "Prashant Shinde", "profile": "https://unsplash.com/@prashantshinde"
    },
    {
        "id": "mahabaleshwar", "name": "Mahabaleshwar", "state": "Maharashtra", "is_ut": False,
        "lat": 17.9237, "lon": 73.6586, "category": "Strawberry Hill Station", "best_season": "October to June",
        "budget": 4200, "days": 3,
        "overview": "Strawberry Capital of India nestled on the Western Ghats plateau, source of the sacred Krishna River, and Pratapgad Fort.",
        "attractions": ["Venna Lake", "Arthur's Seat (Queen of Points)", "Mapro Garden Strawberry Farm", "Pratapgad Fort", "Elephant's Head Point"],
        "nearby": ["Panchgani", "Pratapgad", "Wai"],
        "activities": ["Fresh strawberry with whipped cream tasting at Mapro", "Boating on Venna Lake", "Climbing Chhatrapati Shivaji's Pratapgad Fort"],
        "img_url": "https://images.unsplash.com/photo-1544735716-392fe2489ffa?auto=format&fit=crop&w=1200&q=80",
        "photographer": "Mandar Patil", "profile": "https://unsplash.com/@mandarpatil"
    },
    {
        "id": "alibaug", "name": "Alibaug", "state": "Maharashtra", "is_ut": False,
        "lat": 18.6414, "lon": 72.8722, "category": "Coastal Getaway", "best_season": "October to May",
        "budget": 3900, "days": 2,
        "overview": "Coastal coastal getaway easily reached by ferry from Mumbai, famous for Kolaba sea fort, coconut groves, and fresh seafood.",
        "attractions": ["Kolaba Sea Fort", "Varsoli Beach", "Nagaon Beach Water Sports", "Kashid White Sand Beach", "Murud-Janjira Sea Fort"],
        "nearby": ["Kashid", "Murud", "Mumbai"],
        "activities": ["Walking through seawater at low tide to Kolaba Fort", "Water sports on Nagaon Beach", "Authentic Konkani fish thali dining"],
        "img_url": "https://images.unsplash.com/photo-1512343879784-a960bf40e7f2?auto=format&fit=crop&w=1200&q=80",
        "photographer": "Swapnil Kulkarni", "profile": "https://unsplash.com/@swapnilk"
    },
    {
        "id": "aurangabad", "name": "Chhatrapati Sambhajinagar (Ajanta & Ellora)", "state": "Maharashtra", "is_ut": False,
        "lat": 19.8762, "lon": 75.3433, "category": "UNESCO World Heritage Caves", "best_season": "October to March",
        "budget": 3800, "days": 3,
        "overview": "Gateway to the breathtaking rock-cut UNESCO masterpieces of Ajanta Buddhist murals and the monolithic Kailash Temple at Ellora.",
        "attractions": ["Ellora Caves & Kailash Temple (Cave 16)", "Ajanta Caves (Frescoes & Murals)", "Bibi Ka Maqbara (Taj of Deccan)", "Daulatabad Fort", "Panchakki"],
        "nearby": ["Daulatabad", "Khuldabad", "Shirdi"],
        "activities": ["Marveling at Kailash Temple carved top-down from single rock", "Studying 2000-year-old Buddhist murals at Ajanta", "Climbing subterranean maze in Daulatabad Fort"],
        "img_url": "https://images.unsplash.com/photo-1609766857041-ed402ea8069a?auto=format&fit=crop&w=1200&q=80",
        "photographer": "Ajay Kadam", "profile": "https://unsplash.com/@ajaykadam"
    },
    {
        "id": "nashik", "name": "Nashik", "state": "Maharashtra", "is_ut": False,
        "lat": 19.9975, "lon": 73.7898, "category": "Wine Capital & Kumbh", "best_season": "October to March",
        "budget": 3600, "days": 2,
        "overview": "Wine Capital of India on the holy Godavari River, renowned for Sula Vineyard tasting cellars and Trimbakeshwar Jyotirlinga.",
        "attractions": ["Sula Vineyards & Winery", "Trimbakeshwar Shiva Jyotirlinga", "Panchavati & Sita Gufaa", "Pandavleni Caves (1st Century BCE)", "Dugarwadi Waterfall"],
        "nearby": ["Trimbak", "Igatpuri", "Shirdi"],
        "activities": ["Wine tasting and grape stomping at Sula Vineyards", "Darshan at sacred Trimbakeshwar Jyotirlinga", "Exploring rock-cut Buddhist Pandavleni caves"],
        "img_url": "https://images.unsplash.com/photo-1506744038136-46273834b3fb?auto=format&fit=crop&w=1200&q=80",
        "photographer": "Nilesh Gaikwad", "profile": "https://unsplash.com/@nileshgaikwad"
    },
    {
        "id": "tadoba", "name": "Tadoba Andhari Tiger Reserve", "state": "Maharashtra", "is_ut": False,
        "lat": 20.2450, "lon": 79.3025, "category": "Jewel of Vidarbha Wildlife", "best_season": "October to June",
        "budget": 4800, "days": 3,
        "overview": "Maharashtra's oldest and largest tiger sanctuary, famed as the Land of Tigers with one of the highest big-cat densities in India.",
        "attractions": ["Tadoba National Park Core Safari", "Moharli Safari Zone", "Tadoba Lake", "Erai Dam Reservoir", "Kolsa Range"],
        "nearby": ["Chandrapur", "Nagpur", "Wardha"],
        "activities": ["Open Gypsy tiger safari through bamboo thickets", "Spotting tigers swimming in Erai waters during summer", "Birdwatching on Tadoba Lake"],
        "img_url": "https://images.unsplash.com/photo-1512343879784-a960bf40e7f2?auto=format&fit=crop&w=1200&q=80",
        "photographer": "Hemant Jadhav", "profile": "https://unsplash.com/@hemantjadhav"
    },
    {
        "id": "matheran", "name": "Matheran", "state": "Maharashtra", "is_ut": False,
        "lat": 18.9865, "lon": 73.2676, "category": "Automobile-Free Hill", "best_season": "October to May",
        "budget": 3200, "days": 2,
        "overview": "Asia's only automobile-free hill station perched at 2,600 feet on red laterite soil, reached by Neral Toy Train and horse trails.",
        "attractions": ["Charlotte Lake", "Panorama Point (360-degree)", "Echo Point & Louisa Point", "Neral-Matheran Toy Train", "King George Point"],
        "nearby": ["Neral", "Karjat", "Mumbai"],
        "activities": ["Riding the heritage narrow-gauge toy train", "Horse riding along red laterite forest paths", "Watching sunrise from Panorama Point"],
        "img_url": "https://images.unsplash.com/photo-1544735716-392fe2489ffa?auto=format&fit=crop&w=1200&q=80",
        "photographer": "Deepak Sawant", "profile": "https://unsplash.com/@deepaksawant"
    },
    {
        "id": "shirdi", "name": "Shirdi", "state": "Maharashtra", "is_ut": False,
        "lat": 19.7667, "lon": 74.4764, "category": "Spiritual Pilgrimage", "best_season": "Throughout the year",
        "budget": 2900, "days": 2,
        "overview": "Sacred abode of 19th-century saint Sai Baba, attracting millions to the Samadhi Mandir, Dwarkamai mosque, and Chavadi.",
        "attractions": ["Sai Baba Samadhi Temple", "Dwarkamai Mosque", "Chavadi", "Lendi Baug Garden", "Shani Shingnapur (Lockless Village)"],
        "nearby": ["Nashik", "Shani Shingnapur", "Aurangabad"],
        "activities": ["Kakad Aarti at Sai Baba Samadhi Mandir", "Visiting the lockless village of Shani Shingnapur", "Community dining at massive Prasadalaya"],
        "img_url": "https://images.unsplash.com/photo-1582510003544-4d00b7f74220?auto=format&fit=crop&w=1200&q=80",
        "photographer": "Mahesh Shinde", "profile": "https://unsplash.com/@maheshshinde"
    },
    {
        "id": "kolhapur", "name": "Kolhapur", "state": "Maharashtra", "is_ut": False,
        "lat": 16.7050, "lon": 74.2433, "category": "Historic & Culinary", "best_season": "October to March",
        "budget": 3000, "days": 2,
        "overview": "Princely Maratha capital on the Panchganga River famous for Mahalaxmi Temple, leather Kolhapuri chappals, and spicy cuisine.",
        "attractions": ["Mahalaxmi (Amba Bai) Temple", "New Palace & Chhatrapati Shahu Museum", "Rankala Lake", "Panhala Fort", "Khasbag Wrestling Arena"],
        "nearby": ["Panhala", "Goa", "Belgaum"],
        "activities": ["Feasting on fiery Kolhapuri Tambda and Pandhra Rassa", "Watching traditional Kushti wrestling at Talim arena", "Shopping handcrafted Kolhapuri leather chappals"],
        "img_url": "https://images.unsplash.com/photo-1582510003544-4d00b7f74220?auto=format&fit=crop&w=1200&q=80",
        "photographer": "Vishal Bhosale", "profile": "https://unsplash.com/@vishalbhosale"
    },
    {
        "id": "panchgani", "name": "Panchgani", "state": "Maharashtra", "is_ut": False,
        "lat": 17.9237, "lon": 73.8016, "category": "Sahyadri Tableland", "best_season": "September to May",
        "budget": 3500, "days": 2,
        "overview": "Scenic hill station cradled between five hills, celebrated for Asia's second-longest Table Land volcanic plateau and boarding schools.",
        "attractions": ["Table Land Plateau (95 Acres)", "Sydney Point", "Parsi Point Overlooking Dhom Dam", "Mapro Garden", "Devil's Kitchen Caves"],
        "nearby": ["Mahabaleshwar", "Wai", "Satara"],
        "activities": ["Horse riding across vast volcanic Table Land", "Viewing emerald Dhom Dam waters from Parsi Point", "Paragliding over Krishna River valley"],
        "img_url": "https://images.unsplash.com/photo-1544735716-392fe2489ffa?auto=format&fit=crop&w=1200&q=80",
        "photographer": "Rohan Chitnis", "profile": "https://unsplash.com/@rohanchitnis"
    },

    # ---------- GOA (8) ----------
    {
        "id": "goa_north", "name": "North Goa (Calangute & Baga)", "state": "Goa", "is_ut": False,
        "lat": 15.5439, "lon": 73.7553, "category": "Beaches & Nightlife", "best_season": "November to February",
        "budget": 4500, "days": 4,
        "overview": "Vibrant beach hub famous for bustling golden sand shores, watersports, beach shacks, and legendary flea markets.",
        "attractions": ["Baga Beach", "Calangute Beach", "Aguada Fort & Lighthouse", "Anjuna Flea Market", "Chapora Fort (Dil Chahta Hai)"],
        "nearby": ["Panaji", "Anjuna", "Morjim"],
        "activities": ["Water sports parasailing and jet skiing at Baga", "Sunset view from 17th-century Aguada Fort", "Enjoying fresh seafood curry at beach shacks"],
        "img_url": "https://images.unsplash.com/photo-1512343879784-a960bf40e7f2?auto=format&fit=crop&w=1200&q=80",
        "photographer": "Alexey Turenkov", "profile": "https://unsplash.com/@alexeyt"
    },
    {
        "id": "goa_south", "name": "South Goa (Palolem & Agonda)", "state": "Goa", "is_ut": False,
        "lat": 15.0100, "lon": 74.0232, "category": "Serene Beaches", "best_season": "November to March",
        "budget": 4200, "days": 3,
        "overview": "Peaceful tropical paradise of crescent-shaped white sand beaches, coconut groves, silent noise parties, and dolphin cruises.",
        "attractions": ["Palolem Beach", "Agonda Beach", "Cabo de Rama Fort", "Cola Beach Lagoon", "Butterfly Beach"],
        "nearby": ["Cavelossim", "Margao", "Colva"],
        "activities": ["Kayaking in sea and freshwater Cola lagoon", "Dolphin spotting boat cruise", "Attending headphone silent noise party in Palolem"],
        "img_url": "https://images.unsplash.com/photo-1512343879784-a960bf40e7f2?auto=format&fit=crop&w=1200&q=80",
        "photographer": "Eshwar Naik", "profile": "https://unsplash.com/@eshwarnaik"
    },
    {
        "id": "panaji", "name": "Panaji (Panjim)", "state": "Goa", "is_ut": False,
        "lat": 15.4909, "lon": 73.8278, "category": "Colonial Heritage", "best_season": "November to March",
        "budget": 4000, "days": 2,
        "overview": "Charming state capital along Mandovi River celebrated for Fontainhas Latin Quarter, Portuguese villas, and river cruises.",
        "attractions": ["Fontainhas Latin Quarter", "Our Lady of the Immaculate Conception Church", "Mandovi River Cruise", "Miramar Beach", "Goa State Museum"],
        "nearby": ["Old Goa", "Dona Paula", "Reis Magos"],
        "activities": ["Walking tour of pastel-hued Fontainhas Latin Quarter", "Sunset casino or cultural cruise on Mandovi River", "Visiting Baroque Immaculate Conception church"],
        "img_url": "https://images.unsplash.com/photo-1582510003544-4d00b7f74220?auto=format&fit=crop&w=1200&q=80",
        "photographer": "Savio Fernandes", "profile": "https://unsplash.com/@saviof"
    },
    {
        "id": "old_goa", "name": "Old Goa (Velha Goa)", "state": "Goa", "is_ut": False,
        "lat": 15.5031, "lon": 73.9118, "category": "UNESCO World Heritage", "best_season": "October to March",
        "budget": 3200, "days": 1,
        "overview": "Former capital of Portuguese India, housing Asia's largest churches including Basilica of Bom Jesus with St. Francis Xavier relics.",
        "attractions": ["Basilica of Bom Jesus", "Se Cathedral (Largest in Asia)", "Church of St. Francis of Assisi", "St. Augustine Tower", "Archaeological Museum"],
        "nearby": ["Panaji", "Divar Island", "Ponda"],
        "activities": ["Viewing the sacred relics of St. Francis Xavier", "Listening to the Golden Bell inside Se Cathedral", "Visiting ruins of 46m St. Augustine tower"],
        "img_url": "https://images.unsplash.com/photo-1609766857041-ed402ea8069a?auto=format&fit=crop&w=1200&q=80",
        "photographer": "Melroy D'Souza", "profile": "https://unsplash.com/@melroydsouza"
    },
    {
        "id": "dudhsagar", "name": "Dudhsagar Waterfalls", "state": "Goa", "is_ut": False,
        "lat": 15.3144, "lon": 74.3144, "category": "Majestic Waterfalls", "best_season": "July to December",
        "budget": 3500, "days": 1,
        "overview": "Sea of Milk, a magnificent 310m four-tiered cascade on Mandovi River in Bhagwan Mahavir Wildlife Sanctuary with a railway bridge across it.",
        "attractions": ["Dudhsagar Falls", "Bhagwan Mahavir Wildlife Sanctuary", "Railway Viaduct View Point", "Tambdi Surla Mahadev Temple"],
        "nearby": ["Mollem", "Kulem", "Ponda"],
        "activities": ["Jeep safari through jungle streams in Mollem", "Swimming in the natural freshwater pool at waterfall base", "Visiting 12th-century basalt Tambdi Surla temple"],
        "img_url": "https://images.unsplash.com/photo-1544735716-392fe2489ffa?auto=format&fit=crop&w=1200&q=80",
        "photographer": "Nikhil Patil", "profile": "https://unsplash.com/@nikhilpatil"
    },
    {
        "id": "anjuna", "name": "Anjuna & Vagator", "state": "Goa", "is_ut": False,
        "lat": 15.5800, "lon": 73.7430, "category": "Bohemian & Cliffs", "best_season": "November to March",
        "budget": 4200, "days": 2,
        "overview": "Hippie cradle of Goa featuring rocky red clifftops, Wednesday flea markets, Chapora fort ruins, and sunset beach lounges.",
        "attractions": ["Anjuna Flea Market", "Vagator Red Cliffs Beach", "Chapora Fort", "Curling's & Shiva Valley", "Little Vagator (Ozran)"],
        "nearby": ["Baga", "Siolim", "Morjim"],
        "activities": ["Wednesday shopping at open-air Anjuna Flea Market", "Sunset viewing from Chapora Fort ramparts", "Psychedelic trance music experiences on beach"],
        "img_url": "https://images.unsplash.com/photo-1512343879784-a960bf40e7f2?auto=format&fit=crop&w=1200&q=80",
        "photographer": "Rohan Sequeira", "profile": "https://unsplash.com/@rohansequeira"
    },
    {
        "id": "morjim", "name": "Morjim & Ashwem", "state": "Goa", "is_ut": False,
        "lat": 15.6174, "lon": 73.7381, "category": "Turtle Beach & Serenity", "best_season": "November to March",
        "budget": 4600, "days": 2,
        "overview": "Tranquil nesting beach for endangered Olive Ridley sea turtles on the Chapora River mouth, famed for upscale seaside boutiques.",
        "attractions": ["Morjim Olive Ridley Nesting Beach", "Ashwem Beach", "Chapora River Estuary", "Mandrem Beach"],
        "nearby": ["Arambol", "Siolim", "Vagator"],
        "activities": ["Spotting Olive Ridley turtle hatchlings in season", "Paddleboarding and kitesurfing in shallow sea", "Fine coastal dining at chic beach clubs"],
        "img_url": "https://images.unsplash.com/photo-1512343879784-a960bf40e7f2?auto=format&fit=crop&w=1200&q=80",
        "photographer": "Dmitry V", "profile": "https://unsplash.com/@dmitryv"
    },
    {
        "id": "canacona", "name": "Canacona (Cabo de Rama)", "state": "Goa", "is_ut": False,
        "lat": 15.0889, "lon": 73.9217, "category": "Clifftop & Solitude", "best_season": "November to March",
        "budget": 3800, "days": 2,
        "overview": "Southern tip district of Goa featuring ancient Portuguese clifftop Cabo de Rama Fort overlooking vast turquoise waters.",
        "attractions": ["Cabo de Rama Fort & Beach", "Cotigao Wildlife Sanctuary", "Galgibaga Turtle Beach", "Talpona River Mouth"],
        "nearby": ["Palolem", "Agonda", "Karwar"],
        "activities": ["Panoramic ocean viewing from Cabo de Rama ramparts", "Walking the treetop canopy bridge in Cotigao sanctuary", "Peaceful sunset at undeveloped Galgibaga beach"],
        "img_url": "https://images.unsplash.com/photo-1590050752117-238cb0fb12b1?auto=format&fit=crop&w=1200&q=80",
        "photographer": "Joaquim Pinto", "profile": "https://unsplash.com/@joaquimpinto"
    },

    # ---------- DADRA & NAGAR HAVELI AND DAMAN & DIU (UT) (4) ----------
    {
        "id": "daman", "name": "Daman", "state": "Dadra and Nagar Haveli and Daman and Diu", "is_ut": True,
        "lat": 20.3974, "lon": 72.8328, "category": "Portuguese Coastal", "best_season": "October to March",
        "budget": 3200, "days": 2,
        "overview": "Former Portuguese coastal enclave on the Daman Ganga River, featuring monumental Moti Daman and Nani Daman forts.",
        "attractions": ["Moti Daman Fort", "Nani Daman Fort & Lighthouse", "Jampore Beach", "Devka Beach & Amusement Park", "Church of Bom Jesus"],
        "nearby": ["Vapi", "Silvassa", "Surat"],
        "activities": ["Walking the sea-facing ramparts of Moti Daman Fort", "Water sports and horse rides on Jampore beach", "Tax-free shopping and seafood dining"],
        "img_url": "https://images.unsplash.com/photo-1590050752117-238cb0fb12b1?auto=format&fit=crop&w=1200&q=80",
        "photographer": "Ketan Solanki", "profile": "https://unsplash.com/@ketansolanki"
    },
    {
        "id": "diu", "name": "Diu Island", "state": "Dadra and Nagar Haveli and Daman and Diu", "is_ut": True,
        "lat": 20.7144, "lon": 70.9874, "category": "Island Fortress", "best_season": "October to March",
        "budget": 3400, "days": 2,
        "overview": "Peaceful coastal island featuring the formidable 16th-century sea-surrounded Diu Fort, Naida Caves, and Nagoa beach.",
        "attractions": ["Diu Fort (Sea Fortress)", "Naida Caves (Sunlit Rock Formations)", "Nagoa Beach (Hoka Trees)", "St. Paul's Church", "Gangeshwar Mahadev"],
        "nearby": ["Somnath", "Gir", "Una"],
        "activities": ["Exploring sun-dappled Naida Caves labyrinths", "Walking cannon ramparts of sea-girt Diu Fort", "Water sports on crescent Nagoa Beach with Hoka palms"],
        "img_url": "https://images.unsplash.com/photo-1590050752117-238cb0fb12b1?auto=format&fit=crop&w=1200&q=80",
        "photographer": "Ankit Rathod", "profile": "https://unsplash.com/@ankitrathod"
    },
    {
        "id": "silvassa", "name": "Silvassa", "state": "Dadra and Nagar Haveli and Daman and Diu", "is_ut": True,
        "lat": 20.2763, "lon": 73.0083, "category": "Tribal Heritage & Greenery", "best_season": "October to March",
        "budget": 2900, "days": 2,
        "overview": "Capital of Dadra and Nagar Haveli surrounded by Warli tribal villages, Portuguese church heritage, and wildlife gardens.",
        "attractions": ["Tribal Cultural Museum", "Vasona Lion Safari Park", "Our Lady of Piety Church", "Nakshatra Garden", "Madhuban Dam"],
        "nearby": ["Daman", "Vapi", "Dudhni"],
        "activities": ["Warli tribal painting workshop", "Mini lion safari at Vasona", "Boating on Madhuban reservoir waters"],
        "img_url": "https://images.unsplash.com/photo-1506744038136-46273834b3fb?auto=format&fit=crop&w=1200&q=80",
        "photographer": "Girish Patel", "profile": "https://unsplash.com/@girishpatel"
    },
    {
        "id": "dudhni_lake", "name": "Dudhni Lake", "state": "Dadra and Nagar Haveli and Daman and Diu", "is_ut": True,
        "lat": 20.1265, "lon": 73.1367, "category": "Water Sports & Camping", "best_season": "October to March",
        "budget": 2800, "days": 1,
        "overview": "Scenic water sports haven formed by the vast backwaters of Madhuban Dam on the Damanganga River.",
        "attractions": ["Dudhni Water Sports Complex", "Madhuban Dam Backwaters", "Tribal Homestays", "Forest Walking Trails"],
        "nearby": ["Silvassa", "Khanvel", "Jawhar"],
        "activities": ["Speedboating, water scooters, and kayaking", "Campfire and tent camping by the lake", "Visiting nearby Khanvel tribal gardens"],
        "img_url": "https://images.unsplash.com/photo-1506744038136-46273834b3fb?auto=format&fit=crop&w=1200&q=80",
        "photographer": "Paresh Vartak", "profile": "https://unsplash.com/@pareshvartak"
    }
]

print(f"West region loaded: {len(WEST_DESTINATIONS)} destinations.")
