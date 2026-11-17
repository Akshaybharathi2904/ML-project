"""
TRAVELMATE AI - East India Destinations (42 Verified Destinations)
West Bengal, Odisha, Bihar, Jharkhand, Andaman & Nicobar Islands
"""

EAST_DESTINATIONS = [
    # ---------- WEST BENGAL (12) ----------
    {
        "id": "darjeeling", "name": "Darjeeling", "state": "West Bengal", "is_ut": False,
        "lat": 27.0360, "lon": 88.2627, "category": "Queen of the Hills & Tea", "best_season": "March to May & October to December",
        "budget": 3800, "days": 3,
        "overview": "UNESCO World Heritage Himalayan railway town with panoramic sunrises over Mount Kanchenjunga and champagne tea estates.",
        "attractions": ["Tiger Hill Sunrise", "Darjeeling Himalayan Railway (Toy Train)", "Batasia Loop & War Memorial", "Happy Valley Tea Estate", "Himalayan Mountaineering Institute (HMI)"],
        "nearby": ["Kalimpong", "Kurseong", "Mirik"],
        "activities": ["Dawn sunrise watching over Kanchenjunga at Tiger Hill", "Steam engine joyride on UNESCO Toy Train", "Tasting muscatel champagne Darjeeling First Flush tea"],
        "img_url": "https://images.unsplash.com/photo-1544735716-392fe2489ffa?auto=format&fit=crop&w=1200&q=80",
        "photographer": "Subhankar Ghosh", "profile": "https://unsplash.com/@subhankarghosh"
    },
    {
        "id": "kolkata", "name": "Kolkata", "state": "West Bengal", "is_ut": False,
        "lat": 22.5726, "lon": 88.3639, "category": "City of Joy & Culture", "best_season": "October to March",
        "budget": 4200, "days": 3,
        "overview": "Cultural capital of India along the Hooghly River, adorned with white marble Victoria Memorial, Howrah Bridge, and tramways.",
        "attractions": ["Victoria Memorial Hall", "Howrah Bridge (Rabindra Setu)", "Dakshineswar Kali Temple", "Indian Museum", "Kumartuli (Clay Idol Artisans)", "Park Street"],
        "nearby": ["Sundarbans", "Shantiniketan", "Digha"],
        "activities": ["Riding the vintage heritage Kolkata tramway", "Walking among clay idol sculptors in Kumartuli", "Tasting traditional Kolkata Kathi Rolls, Rosogolla, and Mishti Doi"],
        "img_url": "https://images.unsplash.com/photo-1582510003544-4d00b7f74220?auto=format&fit=crop&w=1200&q=80",
        "photographer": "Avishek Mukherjee", "profile": "https://unsplash.com/@avishekm"
    },
    {
        "id": "sundarbans", "name": "Sundarbans National Park", "state": "West Bengal", "is_ut": False,
        "lat": 21.9497, "lon": 89.1833, "category": "UNESCO Mangrove Wilderness", "best_season": "September to March",
        "budget": 4500, "days": 3,
        "overview": "World's largest tidal halophytic mangrove delta, UNESCO World Heritage sanctuary of the swimming Royal Bengal Tiger.",
        "attractions": ["Sajnekhali Bird Sanctuary & Watchtower", "Dobanki Canopy Walkway", "Sudhanyakhali Tiger Watchtower", "Pakhiralay Village", "Netidhopani Ruins"],
        "nearby": ["Canning", "Kolkata", "Gosaba"],
        "activities": ["Motorboat river safari through mangrove waterways", "Canopy walkway walk at Dobanki", "Spotting estuarine saltwater crocodiles and river terrapins"],
        "img_url": "https://images.unsplash.com/photo-1512343879784-a960bf40e7f2?auto=format&fit=crop&w=1200&q=80",
        "photographer": "Debojyoti Sen", "profile": "https://unsplash.com/@debojyotisen"
    },
    {
        "id": "kalimpong", "name": "Kalimpong", "state": "West Bengal", "is_ut": False,
        "lat": 27.0667, "lon": 88.4667, "category": "Orchids & Monasteries", "best_season": "March to June & September to December",
        "budget": 3200, "days": 2,
        "overview": "Peaceful ridge town overlooking Teesta River valley, world-famous for exotic gladioli and orchid nurseries and colonial mansions.",
        "attractions": ["Deolo Hill (Highest Point)", "Zang Dhok Palri Phodang (Durpin Monastery)", "Morgan House (Colonial Haunted Manor)", "Pine View Nursery (Cactus)", "Lava & Rishyap"],
        "nearby": ["Darjeeling", "Gangtok", "Lava"],
        "activities": ["Paragliding off Deolo Hill summit", "Exploring rare exotic orchid and cactus varieties", "Panoramic views of Teesta River and Sikkim valleys"],
        "img_url": "https://images.unsplash.com/photo-1544735716-392fe2489ffa?auto=format&fit=crop&w=1200&q=80",
        "photographer": "Pranay Chhetri", "profile": "https://unsplash.com/@pranaychhetri"
    },
    {
        "id": "digha", "name": "Digha & Mandarmani", "state": "West Bengal", "is_ut": False,
        "lat": 21.6266, "lon": 87.5074, "category": "Coastal Beach", "best_season": "October to March",
        "budget": 3000, "days": 2,
        "overview": "West Bengal's most popular coastal getaway along the Bay of Bengal, known for flat hard beaches and casuarina plantations.",
        "attractions": ["New Digha Sea Beach", "Marine Aquarium Regional Centre", "Udaipur Beach (Border)", "Mandarmani Drive-in Beach", "Shankarpur Fishing Harbour"],
        "nearby": ["Kolkata", "Contai", "Talsari"],
        "activities": ["Driving along the 13-km flat beach of Mandarmani", "Feasting on freshly caught fried Pomfret and Tiger Prawns", "Watching sunset at Udaipur sea beach"],
        "img_url": "https://images.unsplash.com/photo-1512343879784-a960bf40e7f2?auto=format&fit=crop&w=1200&q=80",
        "photographer": "Sayan Roy", "profile": "https://unsplash.com/@sayanroy"
    },
    {
        "id": "mirik", "name": "Mirik", "state": "West Bengal", "is_ut": False,
        "lat": 26.8920, "lon": 88.1722, "category": "Serene Lake & Tea", "best_season": "October to May",
        "budget": 2900, "days": 2,
        "overview": "Charming Kanchenjunga foothill retreat centered around Sumendu Lake, connected by rainbow footbridge Indreni Pull.",
        "attractions": ["Sumendu (Mirik) Lake", "Indreni Pull Footbridge", "Rameetay Dara Viewpoint", "Bokar Ngedon Chokhor Ling Monastery", "Tingling Tea Estate Viewpoint"],
        "nearby": ["Darjeeling", "Kurseong", "Pashupati (Nepal Border)"],
        "activities": ["Boating on Sumendu Lake with Kanchenjunga reflections", "Horseback riding along lake perimeter pine trails", "Shopping at Pashupati Nagar on Nepal border"],
        "img_url": "https://images.unsplash.com/photo-1506744038136-46273834b3fb?auto=format&fit=crop&w=1200&q=80",
        "photographer": "Bikram Thapa", "profile": "https://unsplash.com/@bikramthapa"
    },
    {
        "id": "shantiniketan", "name": "Shantiniketan (Bolpur)", "state": "West Bengal", "is_ut": False,
        "lat": 23.6800, "lon": 87.6800, "category": "Tagore Cultural Heritage", "best_season": "October to March (Poush Mela in Dec, Basanta Utsav in March)",
        "budget": 3300, "days": 2,
        "overview": "Nobel Laureate Rabindranath Tagore's utopian open-air university Visva-Bharati, cradle of modern Indian art and Baul music.",
        "attractions": ["Visva-Bharati University Open Classrooms", "Uttarayan Complex (Tagore's 5 Houses)", "Rabindra Bhavana Museum", "Khowai Saturday Sanibarer Haat", "Amar Kutir Crafts"],
        "nearby": ["Bolpur", "Burdwan", "Kolkata"],
        "activities": ["Listening to live Baul singers singing under Sonajhuri forest trees", "Shopping Kantha stitch textiles and terracotta jewelry at Saturday Haat", "Visiting Tagore's preserved study at Udayan"],
        "img_url": "https://images.unsplash.com/photo-1582510003544-4d00b7f74220?auto=format&fit=crop&w=1200&q=80",
        "photographer": "Arindam Bhattacharya", "profile": "https://unsplash.com/@arindamb"
    },
    {
        "id": "dooars", "name": "Dooars (Gorumara & Jaldapara)", "state": "West Bengal", "is_ut": False,
        "lat": 26.6800, "lon": 88.8500, "category": "Floodplains & Wildlife", "best_season": "October to April",
        "budget": 3900, "days": 3,
        "overview": "Alluvial floodplains at Bhutan foothills crisscrossed by Murti, Teesta, and Torsa rivers, famous for Rhinos and tea gardens.",
        "attractions": ["Jaldapara National Park (Rhino Safari)", "Gorumara National Park (Jatraprasad Tower)", "Murti River Forest Camp", "Buxa Tiger Reserve & Fort", "Jayanti Riverbed"],
        "nearby": ["Siliguri", "Alipurduar", "Cooch Behar"],
        "activities": ["Elephant safari tracking Indian one-horned rhinos in Jaldapara", "Watchtower birdwatching at Jatraprasad for wild gaur herds", "Pebble walking across scenic white stones of Jayanti river"],
        "img_url": "https://images.unsplash.com/photo-1512343879784-a960bf40e7f2?auto=format&fit=crop&w=1200&q=80",
        "photographer": "Tathagata Das", "profile": "https://unsplash.com/@tathagatadas"
    },
    {
        "id": "siliguri", "name": "Siliguri", "state": "West Bengal", "is_ut": False,
        "lat": 26.7271, "lon": 88.3953, "category": "Gateway Hub", "best_season": "October to April",
        "budget": 3100, "days": 2,
        "overview": "The Chicken's Neck transit hub connecting mainland India to Northeast states, Nepal, and Bhutan, set against tea gardens.",
        "attractions": ["Salugara Monastery (100-ft Stupa)", "Mahananda Wildlife Sanctuary", "Bengal Safari Park", "Sed-Gyued Monastery", "Hong Kong Market"],
        "nearby": ["Darjeeling", "Jalpaiguri", "Mirik"],
        "activities": ["Royal Bengal Tiger safari at North Bengal Safari Park", "Tasting authentic Tibetan Momos and Thukpa in Pradhan Nagar", "Transit launchpad to Sikkim and Bhutan"],
        "img_url": "https://images.unsplash.com/photo-1582510003544-4d00b7f74220?auto=format&fit=crop&w=1200&q=80",
        "photographer": "Dipankar Barman", "profile": "https://unsplash.com/@dipankarbarman"
    },
    {
        "id": "murshidabad", "name": "Murshidabad", "state": "West Bengal", "is_ut": False,
        "lat": 24.1750, "lon": 88.2800, "category": "Nawabi Heritage", "best_season": "October to March",
        "budget": 2900, "days": 2,
        "overview": "Historic capital of the Nawabs of Bengal on the Bhagirathi River, famed for the grand 1,000-door Hazarduari Palace and Kathgola.",
        "attractions": ["Hazarduari Palace (1000 Doors)", "Nizamat Imambara", "Kathgola Palace & Gardens", "Katra Mosque", "Jafarganj Cemetery"],
        "nearby": ["Berhampore", "Plassey (Palashi)", "Malda"],
        "activities": ["Exploring weapons and art gallery in Hazarduari Palace", "Tanga horse carriage ride through historic nawabi avenues", "Shopping pure Murshidabad silk sarees"],
        "img_url": "https://images.unsplash.com/photo-1596176530529-78163a4f7af2?auto=format&fit=crop&w=1200&q=80",
        "photographer": "Tanmoy Sarkar", "profile": "https://unsplash.com/@tanmoysarkar"
    },
    {
        "id": "kurseong", "name": "Kurseong", "state": "West Bengal", "is_ut": False,
        "lat": 26.8810, "lon": 88.2770, "category": "Land of White Orchids", "best_season": "March to June & September to November",
        "budget": 3000, "days": 2,
        "overview": "Peaceful tea town between Siliguri and Darjeeling, renowned for Makaibari organic tea estate, Dow Hill woods, and Eagle's Crag.",
        "attractions": ["Eagle's Crag Viewpoint", "Makaibari Tea Estate", "Dow Hill Forest Trails", "Netaji Subhash Chandra Bose Museum", "Chimney Viewpoint"],
        "nearby": ["Darjeeling", "Mirik", "Siliguri"],
        "activities": ["Organic biodynamic tea tasting at 1859 Makaibari Estate", "Sunset panorama from Eagle's Crag over Balason river", "Walking through mysterious deodar groves of Dow Hill"],
        "img_url": "https://images.unsplash.com/photo-1589308078059-be1415eab4c3?auto=format&fit=crop&w=1200&q=80",
        "photographer": "Pritam Tamang", "profile": "https://unsplash.com/@pritamtamang"
    },
    {
        "id": "bishnupur", "name": "Bishnupur", "state": "West Bengal", "is_ut": False,
        "lat": 23.0750, "lon": 87.3180, "category": "Terracotta Capital", "best_season": "October to March",
        "budget": 2800, "days": 2,
        "overview": "Malla kingdom royal seat famed for 17th-century terracotta temples, Baluchari silk sarees with epic motifs, and Bishnupur Gharana music.",
        "attractions": ["Rasmancha Pyramid Monument", "Jor Bangla Terracotta Temple", "Shyamrai Temple (Five Pinnacles)", "Madan Mohan Temple", "Dalmadal Cannon"],
        "nearby": ["Bankura", "Mukutmanipur", "Kolkata"],
        "activities": ["Admiring intricate terracotta friezes depicting Ramayana episodes", "Watching master weavers craft Baluchari silk sarees", "Buying handcrafted Bankura terracotta horses"],
        "img_url": "https://images.unsplash.com/photo-1609766857041-ed402ea8069a?auto=format&fit=crop&w=1200&q=80",
        "photographer": "Sourav Mondal", "profile": "https://unsplash.com/@souravmondal"
    },

    # ---------- ODISHA (8) ----------
    {
        "id": "puri", "name": "Puri", "state": "Odisha", "is_ut": False,
        "lat": 19.8135, "lon": 85.8312, "category": "Char Dham Pilgrimage", "best_season": "October to March",
        "budget": 3500, "days": 3,
        "overview": "Sacred coastal abode of Lord Jagannath on the Bay of Bengal, world-famous for Ratha Yatra, Golden Beach, and Mahaprasad.",
        "attractions": ["Jagannath Temple Complex", "Puri Golden Beach (Blue Flag)", "Gundicha Temple", "Swargadwar Beach", "Raghurajpur Heritage Craft Village"],
        "nearby": ["Konark", "Bhubaneswar", "Chilika Lake"],
        "activities": ["Partaking in Anandabazar temple Mahaprasad from earthen pots", "Strolling golden sands of Blue Flag certified Golden Beach", "Visiting Pattachitra cloth scroll painting masters in Raghurajpur"],
        "img_url": "https://images.unsplash.com/photo-1590050752117-238cb0fb12b1?auto=format&fit=crop&w=1200&q=80",
        "photographer": "Subham Patnaik", "profile": "https://unsplash.com/@subhampatnaik"
    },
    {
        "id": "konark", "name": "Konark Sun Temple", "state": "Odisha", "is_ut": False,
        "lat": 19.8876, "lon": 86.0945, "category": "UNESCO Architectural Wonder", "best_season": "October to March (Dance Festival in Dec)",
        "budget": 3200, "days": 1,
        "overview": "13th-century Black Pagoda designed as a colossal 24-wheeled chariot of Sun God Surya pulled by seven galloping horses.",
        "attractions": ["Sun Temple (UNESCO World Heritage)", "Chandrabhaga Beach", "Konark Archaeological Museum", "Ramachandi Beach & River Estuary", "Konark Dance Festival Stage"],
        "nearby": ["Puri", "Bhubaneswar", "Pipili"],
        "activities": ["Decoding sundial time calculation from the 24 stone chariot wheels", "Watching sunset at sacred Chandrabhaga beach", "Witnessing classical Odissi performances during Konark Dance Festival"],
        "img_url": "https://images.unsplash.com/photo-1609766857041-ed402ea8069a?auto=format&fit=crop&w=1200&q=80",
        "photographer": "Debashis Mohanty", "profile": "https://unsplash.com/@debashismohanty"
    },
    {
        "id": "bhubaneswar", "name": "Bhubaneswar", "state": "Odisha", "is_ut": False,
        "lat": 20.2961, "lon": 85.8245, "category": "Temple City of India", "best_season": "October to March",
        "budget": 3800, "days": 3,
        "overview": "Ancient temple metropolis boasting over 500 Kalinga sandstone shrines, Lingaraj temple, rock-cut Udayagiri-Khandagiri caves, and Dhauli Shanti Stupa.",
        "attractions": ["Lingaraj Temple (11th Century)", "Mukteswara Temple (Gem of Odishan Architecture)", "Udayagiri & Khandagiri Jain Caves", "Dhauli Peace Pagoda (Ashokan Edicts)", "Nandankanan Zoological Park (White Tigers)"],
        "nearby": ["Puri", "Cuttack", "Konark"],
        "activities": ["Admiring torana archway of Mukteswara Temple", "Reading Emperor Ashoka's rock edicts at Dhauli peace stupa", "Spotting rare white tigers at Nandankanan safari"],
        "img_url": "https://images.unsplash.com/photo-1582510003544-4d00b7f74220?auto=format&fit=crop&w=1200&q=80",
        "photographer": "Pradosh Das", "profile": "https://unsplash.com/@pradoshdas"
    },
    {
        "id": "chilika_lake", "name": "Chilika Lake", "state": "Odisha", "is_ut": False,
        "lat": 19.7167, "lon": 85.3167, "category": "Ramsar Lagoon & Dolphins", "best_season": "November to February",
        "budget": 3600, "days": 2,
        "overview": "Asia's largest brackish water coastal lagoon, world-famous for playful Irrawaddy dolphins and over a million migratory winter birds.",
        "attractions": ["Satapada Dolphin Viewpoint", "Kalijai Island Temple", "Mangalajodi Birding Wetland", "Nalabana Bird Sanctuary", "Honeymoon & Breakfast Islands"],
        "nearby": ["Puri", "Bhubaneswar", "Ganjam"],
        "activities": ["Motorboat cruise to spot rare Irrawaddy dolphins at Satapada", "Silent country boat bird photography in Mangalajodi wetlands", "Visiting sacred island temple of Goddess Kalijai"],
        "img_url": "https://images.unsplash.com/photo-1506744038136-46273834b3fb?auto=format&fit=crop&w=1200&q=80",
        "photographer": "Manoj Tripathy", "profile": "https://unsplash.com/@manojtripathy"
    },
    {
        "id": "simlipal", "name": "Simlipal National Park", "state": "Odisha", "is_ut": False,
        "lat": 21.8500, "lon": 86.3500, "category": "Biosphere & Waterfalls", "best_season": "November to April",
        "budget": 4000, "days": 2,
        "overview": "Dense sal biosphere reserve in Mayurbhanj, sanctuary for Royal Bengal Tigers, wild Asian elephants, and Joranda & Barehipani waterfalls.",
        "attractions": ["Barehipani Falls (Two-tiered 399m)", "Joranda Falls", "Chahala Wildlife Watch Point", "Sitabilas Camp", "Mayurbhanj Chhau Dance Center"],
        "nearby": ["Baripada", "Balasore", "Jamshedpur"],
        "activities": ["Witnessing India's second highest two-tier Barehipani falls", "Open jeep safari through dense sal canopy", "Watching traditional Mayurbhanj Chhau martial dance in Baripada"],
        "img_url": "https://images.unsplash.com/photo-1512343879784-a960bf40e7f2?auto=format&fit=crop&w=1200&q=80",
        "photographer": "Ashok Bhanja", "profile": "https://unsplash.com/@ashokbhanja"
    },
    {
        "id": "gopalpur", "name": "Gopalpur-on-Sea", "state": "Odisha", "is_ut": False,
        "lat": 19.2600, "lon": 84.9100, "category": "Quiet Coastal Port", "best_season": "October to March",
        "budget": 3100, "days": 2,
        "overview": "Historic ancient Kalinga seaport town transformed into a tranquil beach retreat with red crab sand flats and 1871 lighthouse.",
        "attractions": ["Gopalpur Beach & Pier Ruins", "Gopalpur Lighthouse", "Aryapalli Beach", "Tampara Lake Watersports", "Pati Sonapur Beach"],
        "nearby": ["Berhampur", "Chilika", "Taratarini"],
        "activities": ["Climbing Gopalpur lighthouse for coastal vistas", "Speedboating and jet skiing at freshwater Tampara lake", "Watching red ghost crabs scatter on morning beach"],
        "img_url": "https://images.unsplash.com/photo-1590050752117-238cb0fb12b1?auto=format&fit=crop&w=1200&q=80",
        "photographer": "Kailash Mishra", "profile": "https://unsplash.com/@kailashmishra"
    },
    {
        "id": "daringbadi", "name": "Daringbadi", "state": "Odisha", "is_ut": False,
        "lat": 19.9070, "lon": 84.1330, "category": "Kashmir of Odisha", "best_season": "October to March (Sub-zero winter frost)",
        "budget": 2900, "days": 2,
        "overview": "Scenic pine-covered hill station in Kandhamal at 3,000 ft, nicknamed Kashmir of Odisha for winter morning ground frost and coffee plantations.",
        "attractions": ["Daringbadi Coffee Gardens", "Midubanda Waterfalls", "Silent Valley & Pine Forest", "Lovers Point", "Hill View Park (Sunset)"],
        "nearby": ["Phulbani", "Gopalpur", "Bhubaneswar"],
        "activities": ["Walking through organic black pepper and coffee estates", "Witnessing winter frost form on pine forest meadows", "Picnic by rushing Midubanda waterfall stream"],
        "img_url": "https://images.unsplash.com/photo-1544735716-392fe2489ffa?auto=format&fit=crop&w=1200&q=80",
        "photographer": "Sailesh Pradhan", "profile": "https://unsplash.com/@saileshpradhan"
    },
    {
        "id": "cuttack", "name": "Cuttack", "state": "Odisha", "is_ut": False,
        "lat": 20.4625, "lon": 85.8830, "category": "Silver City & Maritime", "best_season": "October to March (Bali Yatra in Nov)",
        "budget": 3000, "days": 2,
        "overview": "Millennium Silver City between Mahanadi and Kathajodi rivers, famous for 10th-century Barabati Fort, silver filigree (Tarakasi), and Dahibara Aloodum.",
        "attractions": ["Barabati Fort & Moat", "Netaji Birthplace Museum", "Mahanadi River Barrage", "Chandi Temple", "Maritime Museum Jobra"],
        "nearby": ["Bhubaneswar", "Choudwar", "Dhenkanal"],
        "activities": ["Watching artisans handcraft delicate silver filigree wire jewelry", "Tasting legendary street-food Dahibara Aloodum at Barabati", "Visiting freedom fighter Netaji Subhash Chandra Bose's ancestral home"],
        "img_url": "https://images.unsplash.com/photo-1582510003544-4d00b7f74220?auto=format&fit=crop&w=1200&q=80",
        "photographer": "Deepak Behera", "profile": "https://unsplash.com/@deepakbehera"
    },

    # ---------- BIHAR (8) ----------
    {
        "id": "bodh_gaya", "name": "Bodh Gaya", "state": "Bihar", "is_ut": False,
        "lat": 24.6961, "lon": 84.9911, "category": "UNESCO Buddhist Epiphany", "best_season": "October to March",
        "budget": 3500, "days": 3,
        "overview": "The supreme epicenter of Buddhism where Siddhartha Gautama attained Supreme Enlightenment beneath the sacred Bodhi Tree in 528 BCE.",
        "attractions": ["Mahabodhi Temple Complex (UNESCO)", "Sacred Bodhi Tree & Vajrasana Diamond Throne", "Great Buddha 80-ft Statue", "Muchalinda Lake", "International Monasteries (Thai, Tibetan, Japanese)"],
        "nearby": ["Gaya", "Rajgir", "Nalanda"],
        "activities": ["Meditating beneath the sacred Bodhi Tree beside Buddhist monks", "Photographing 80-ft giant sandstone Buddha", "Touring ornate Thai golden temple and Japanese Zen gardens"],
        "img_url": "https://images.unsplash.com/photo-1609766857041-ed402ea8069a?auto=format&fit=crop&w=1200&q=80",
        "photographer": "Rahul Anand", "profile": "https://unsplash.com/@rahulanand"
    },
    {
        "id": "nalanda", "name": "Nalanda", "state": "Bihar", "is_ut": False,
        "lat": 25.1357, "lon": 85.4452, "category": "UNESCO Ancient University", "best_season": "October to March",
        "budget": 2900, "days": 1,
        "overview": "UNESCO World Heritage ruins of the ancient 5th-century Buddhist residential university that taught 10,000 students from around the world.",
        "attractions": ["Nalanda Mahavihara Excavated Ruins", "Sariputta Stupa (Temple 3)", "Nalanda Archaeological Museum", "Hiuen Tsang Memorial Hall", "Kundalpur Digambar Jain Temple"],
        "nearby": ["Rajgir", "Bodh Gaya", "Pawapuri"],
        "activities": ["Walking among ancient brick monastery dormitories and lecture halls", "Studying original bronze and stone sculptures in Nalanda Museum", "Visiting Xuanzang Chinese scholar memorial pagoda"],
        "img_url": "https://images.unsplash.com/photo-1609766857041-ed402ea8069a?auto=format&fit=crop&w=1200&q=80",
        "photographer": "Prakash Jha", "profile": "https://unsplash.com/@prakashjha"
    },
    {
        "id": "rajgir", "name": "Rajgir", "state": "Bihar", "is_ut": False,
        "lat": 25.0298, "lon": 85.4206, "category": "Valley of Kings & Peace", "best_season": "October to March",
        "budget": 3100, "days": 2,
        "overview": "Ancient Magadha royal capital nestled in seven hills, revered for Vishwa Shanti Stupa, Vulture's Peak (Gridhrakuta), and glass bridge.",
        "attractions": ["Vishwa Shanti Stupa & Aerial Ropeway", "Griddhakuta (Vulture's Peak)", "Rajgir Glass Bridge & Nature Safari", "Hot Springs (Brahmakund)", "Venu Vana Monastery Garden"],
        "nearby": ["Nalanda", "Bodh Gaya", "Pawapuri"],
        "activities": ["Riding single-chair ropeway up Ratnagiri hill to Peace Pagoda", "Walking the thrill-inducing 85-ft Rajgir Glass Skywalk", "Soaking in holy hot water sulphur springs at Brahmakund"],
        "img_url": "https://images.unsplash.com/photo-1609766857041-ed402ea8069a?auto=format&fit=crop&w=1200&q=80",
        "photographer": "Nishant Kumar", "profile": "https://unsplash.com/@nishantkumar"
    },
    {
        "id": "patna", "name": "Patna (Pataliputra)", "state": "Bihar", "is_ut": False,
        "lat": 25.6127, "lon": 85.1589, "category": "Ancient Capital", "best_season": "October to March",
        "budget": 3500, "days": 2,
        "overview": "Ancient imperial seat of Maurya and Gupta Empires on the Ganga, birth city of Guru Gobind Singh at Takht Sri Patna Sahib.",
        "attractions": ["Takht Sri Patna Sahib Gurudwara", "Golghar Granary Dome", "Bihar Museum (World-Class Architecture)", "Kumhrar Mauryan Ruins", "Patna Planetarium"],
        "nearby": ["Vaishali", "Rajgir", "Bodh Gaya"],
        "activities": ["Visiting magnificent modern galleries of the new Bihar Museum", "Climbing spiral staircase of beehive-shaped Golghar for Ganga views", "Darshan at sacred Takht Sri Patna Sahib birthplace"],
        "img_url": "https://images.unsplash.com/photo-1582510003544-4d00b7f74220?auto=format&fit=crop&w=1200&q=80",
        "photographer": "Ravi Shankar Prasad", "profile": "https://unsplash.com/@ravishankarp"
    },
    {
        "id": "vaishali", "name": "Vaishali", "state": "Bihar", "is_ut": False,
        "lat": 25.9900, "lon": 85.1300, "category": "First Republic", "best_season": "October to March",
        "budget": 2700, "days": 1,
        "overview": "World's earliest recorded democratic republic, birthplace of 24th Jain Tirthankara Lord Mahavira, and Ashoka Lion Pillar site.",
        "attractions": ["Ashoka Pillar & Lion Capital Kolhua", "Buddha Relic Stupa", "Ananda Stupa & Coronation Tank (Abhishek Pushkarini)", "Vishwa Shanti Stupa Vaishali", "Kundalpur Mahavira Birthplace"],
        "nearby": ["Patna", "Muzaffarpur", "Hajipur"],
        "activities": ["Inspecting intact monolithic 3rd-century BCE Ashoka Lion Pillar", "Visiting mud-brick stupa that held one-eighth of Buddha's bodily relics", "Walking around sacred Abhishek Pushkarini coronation tank"],
        "img_url": "https://images.unsplash.com/photo-1609766857041-ed402ea8069a?auto=format&fit=crop&w=1200&q=80",
        "photographer": "Santosh Tiwary", "profile": "https://unsplash.com/@santoshtiwary"
    },
    {
        "id": "valmiki_national_park", "name": "Valmiki National Park", "state": "Bihar", "is_ut": False,
        "lat": 27.4200, "lon": 84.2700, "category": "Terai Tiger Reserve", "best_season": "November to April",
        "budget": 3800, "days": 2,
        "overview": "Bihar's only tiger reserve on the India-Nepal border along the Gandak River, featuring sal forests, tigers, rhinos, and river rapids.",
        "attractions": ["Valmiki Tiger Safari Zone", "Gandak River Barrage & Rapids", "Valmiki Ashram", "Jatashankar Cave", "Kaleshwar Temple"],
        "nearby": ["Bettiah", "Gorakhpur", "Chitwan (Nepal)"],
        "activities": ["4x4 jungle safari tracking Bengal Tigers in sub-Himalayan forest", "Rafting on the wide Gandak river", "Visiting hermitage where Sage Valmiki composed Ramayana"],
        "img_url": "https://images.unsplash.com/photo-1512343879784-a960bf40e7f2?auto=format&fit=crop&w=1200&q=80",
        "photographer": "Arvind Pandey", "profile": "https://unsplash.com/@arvindpandey"
    },
    {
        "id": "sasaram", "name": "Sasaram", "state": "Bihar", "is_ut": False,
        "lat": 24.9500, "lon": 84.0300, "category": "Imperial Mausoleum", "best_season": "October to March",
        "budget": 2600, "days": 1,
        "overview": "Historic city famed for the red sandstone mausoleum of Emperor Sher Shah Suri, set like an island in a square artificial lake.",
        "attractions": ["Sher Shah Suri Tomb (Island Mausoleum)", "Hasan Khan Suri Tomb", "Rohtasgarh Fort", "Ashokan Inscription Cave", "Tomb of Alawal Khan"],
        "nearby": ["Varanasi", "Dehri", "Gaya"],
        "activities": ["Photographing 122-ft high floating dome mausoleum of Sher Shah Suri", "Trekking to massive Rohtasgarh hill plateau fortress", "Inspecting Mauryan Ashokan rock edicts"],
        "img_url": "https://images.unsplash.com/photo-1609766857041-ed402ea8069a?auto=format&fit=crop&w=1200&q=80",
        "photographer": "Sunil Kashyap", "profile": "https://unsplash.com/@sunilkashyap"
    },
    {
        "id": "madhubani", "name": "Madhubani", "state": "Bihar", "is_ut": False,
        "lat": 26.3500, "lon": 86.0800, "category": "Mithila Folk Art", "best_season": "October to March",
        "budget": 2700, "days": 2,
        "overview": "World-famous center of Mithila painting, where village walls and handmade paper are adorned with geometric natural dyes.",
        "attractions": ["Jitwarpur & Ranti Artist Villages", "Nagar Fort (Madhubani Raj Palace)", "Saurath Sabha", "Kapileshwar Temple", "Mithila Heritage Centre"],
        "nearby": ["Darbhanga", "Janakpur (Nepal)", "Muzaffarpur"],
        "activities": ["Hands-on Madhubani painting workshop with national awardee masters in Jitwarpur", "Walking among brightly hand-painted village mud huts", "Tasting traditional Mithila Makhana and fresh fish curry"],
        "img_url": "https://images.unsplash.com/photo-1582510003544-4d00b7f74220?auto=format&fit=crop&w=1200&q=80",
        "photographer": "Pratibha Jha", "profile": "https://unsplash.com/@pratibhajha"
    },

    # ---------- JHARKHAND (8) ----------
    {
        "id": "ranchi", "name": "Ranchi", "state": "Jharkhand", "is_ut": False,
        "lat": 23.3441, "lon": 85.3096, "category": "City of Waterfalls", "best_season": "October to March",
        "budget": 3400, "days": 2,
        "overview": "Capital of Jharkhand on the Chota Nagpur plateau, renowned as the City of Waterfalls (Hundru, Jonha, Dassam) and tribal museums.",
        "attractions": ["Hundru Falls (98m)", "Dassam Falls", "Jonha Falls (Gautamdhara)", "Pahari Mandir & Ranchi Lake", "State Tribal Museum"],
        "nearby": ["Patratu", "Netarhat", "Jamshedpur"],
        "activities": ["Trek down stone steps to Hundru waterfall plunge pool", "Climbing 468 steps of Pahari Mandir for city views", "Scenic winding drive through Patratu Valley ghats"],
        "img_url": "https://images.unsplash.com/photo-1544735716-392fe2489ffa?auto=format&fit=crop&w=1200&q=80",
        "photographer": "Manish Tirkey", "profile": "https://unsplash.com/@manishtirkey"
    },
    {
        "id": "netarhat", "name": "Netarhat", "state": "Jharkhand", "is_ut": False,
        "lat": 23.4833, "lon": 84.2667, "category": "Queen of Chotanagpur", "best_season": "October to April",
        "budget": 2900, "days": 2,
        "overview": "Queen of Chotanagpur plateau at 3,600 ft, famed for breathtaking sunrises and sunsets from Magnolia Point and pine forests.",
        "attractions": ["Magnolia Sunset Point", "Netarhat Sunrise Point", "Upper & Lower Ghaghri Waterfalls", "Netarhat Residential School", "Pine Forest Trails"],
        "nearby": ["Betla National Park", "Lohardaga", "Ranchi"],
        "activities": ["Watching the golden orb sunset from Magnolia Point", "Walking under dense pine needle forest trails", "Trek to Lower Ghaghri forest waterfall"],
        "img_url": "https://images.unsplash.com/photo-1544735716-392fe2489ffa?auto=format&fit=crop&w=1200&q=80",
        "photographer": "Anurag Oraon", "profile": "https://unsplash.com/@anuragoraon"
    },
    {
        "id": "betla_national_park", "name": "Betla National Park", "state": "Jharkhand", "is_ut": False,
        "lat": 23.8667, "lon": 84.1833, "category": "Palamu Tiger Reserve", "best_season": "November to April",
        "budget": 3500, "days": 2,
        "overview": "One of India's earliest tiger sanctuaries in Palamu, featuring elephant herds, ruined 16th-century Chero dynasty forts, and sal canopies.",
        "attractions": ["Betla Safari Zone", "Palamu Twin Forts (Purana & Naya Qila)", "Kechki River Sangam", "Lodha Waterfall (Jharkhand's Highest 143m)"],
        "nearby": ["Daltonganj", "Netarhat", "Latehar"],
        "activities": ["Open jeep safari tracking elephants, leopards, and bison", "Exploring overgrown Mughal-era stone forts in the deep jungle", "Picnic at Kechki confluence of Auranga and Koel rivers"],
        "img_url": "https://images.unsplash.com/photo-1512343879784-a960bf40e7f2?auto=format&fit=crop&w=1200&q=80",
        "photographer": "Prashant Minz", "profile": "https://unsplash.com/@prashantminz"
    },
    {
        "id": "deoghar", "name": "Deoghar (Baidyanath Dham)", "state": "Jharkhand", "is_ut": False,
        "lat": 24.4826, "lon": 86.7000, "category": "Jyotirlinga Pilgrimage", "best_season": "October to March (Shravan Mela in July-Aug)",
        "budget": 2800, "days": 2,
        "overview": "Sacred abode of gods home to Baba Baidyanath Jyotirlinga, where millions of Kanwariyas bring holy Ganga water during Shravan.",
        "attractions": ["Baba Baidyanath Temple Complex", "Trikuta Parvat Ropeway", "Naulakha Mandir", "Tapovan Caves", "Nandan Pahar Amusement Park"],
        "nearby": ["Dumka", "Giridih", "Jasidih"],
        "activities": ["Holy darshan at 12 Jyotirlinga Baidyanath shrine", "Ropeway ride to the three-peaked Trikuta Parvat", "Tasting famous Deoghar Peda sweets"],
        "img_url": "https://images.unsplash.com/photo-1590050752117-238cb0fb12b1?auto=format&fit=crop&w=1200&q=80",
        "photographer": "Gopal Pandey", "profile": "https://unsplash.com/@gopalpandey"
    },
    {
        "id": "jamshedpur", "name": "Jamshedpur (Tatanagar)", "state": "Jharkhand", "is_ut": False,
        "lat": 22.8046, "lon": 86.2029, "category": "Steel City & Lakes", "best_season": "October to March",
        "budget": 3500, "days": 2,
        "overview": "India's first planned industrial city founded by Jamsetji Tata, characterized by tree-lined boulevards, Jubilee Park, and Dalma hills.",
        "attractions": ["Jubilee Park & Musical Fountains", "Dalma Wildlife Sanctuary (Wild Elephants)", "Dimna Lake & Dam", "Tata Steel Zoological Park", "Bhuvaneshwari Temple (Telco)"],
        "nearby": ["Ranchi", "Ghatshila", "Kharagpur"],
        "activities": ["Evening musical laser fountain show at Jubilee Park", "Trekking Dalma Wildlife Sanctuary to spot wild elephants", "Waterside sunset at Dimna Lake reservoir"],
        "img_url": "https://images.unsplash.com/photo-1596176530529-78163a4f7af2?auto=format&fit=crop&w=1200&q=80",
        "photographer": "Avishek Sen", "profile": "https://unsplash.com/@avisheksen"
    },
    {
        "id": "hazaribagh", "name": "Hazaribagh", "state": "Jharkhand", "is_ut": False,
        "lat": 23.9961, "lon": 85.3697, "category": "City of Thousand Gardens", "best_season": "October to March",
        "budget": 2800, "days": 2,
        "overview": "Charming plateau town surrounded by dense forests, Hazaribagh National Park, Canary Hill, and prehistoric rock art caves.",
        "attractions": ["Canary Hill Watchtower", "Hazaribagh Lake", "Hazaribagh Wildlife Sanctuary", "Isko Prehistoric Rock Art Caves", "Surajkund Thermal Spring (88°C)"],
        "nearby": ["Ranchi", "Bokaro", "Koderma"],
        "activities": ["Climbing Canary Hill observation tower for 360-degree forest view", "Viewing 10,000-year-old rock paintings and Sohrai mural art at Isko", "Visiting India's hottest thermal spring at Surajkund"],
        "img_url": "https://images.unsplash.com/photo-1506744038136-46273834b3fb?auto=format&fit=crop&w=1200&q=80",
        "photographer": "Rohit Murmu", "profile": "https://unsplash.com/@rohitmurmu"
    },
    {
        "id": "parasnath", "name": "Parasnath (Shikharji)", "state": "Jharkhand", "is_ut": False,
        "lat": 23.9575, "lon": 86.1360, "category": "Supreme Jain Pilgrimage", "best_season": "October to March",
        "budget": 3000, "days": 2,
        "overview": "Highest mountain peak in Jharkhand (1,365m), the supreme Jain holy mountain where 20 of the 24 Tirthankaras attained Moksha.",
        "attractions": ["Shikharji Holy Peak Temples", "Parasnath Wildlife Sanctuary", "Madhuban Base Camp", "Jal Mandir Madhuban", "Gandharva Nala"],
        "nearby": ["Giridih", "Dhanbad", "Deoghar"],
        "activities": ["27-km sacred barefoot pilgrimage circumambulation across 31 Tonks", "Watching sunrise break over Chota Nagpur from Jharkhand's highest peak", "Exploring marble temples of Madhuban"],
        "img_url": "https://images.unsplash.com/photo-1609766857041-ed402ea8069a?auto=format&fit=crop&w=1200&q=80",
        "photographer": "Naveen Jain", "profile": "https://unsplash.com/@naveenjain"
    },
    {
        "id": "patratu_valley", "name": "Patratu Valley", "state": "Jharkhand", "is_ut": False,
        "lat": 23.6700, "lon": 85.2900, "category": "Scenic Serpentine Ghats", "best_season": "July to March",
        "budget": 2700, "days": 1,
        "overview": "Photographer's paradise featuring a thrilling serpentine hairpin ghat road cutting through emerald hills down to Patratu Dam.",
        "attractions": ["Patratu Valley Hairpin Loop Viewpoint", "Patratu Dam & Boating Resort", "Island Cafe Patratu", "Palani Falls"],
        "nearby": ["Ranchi", "Ramgarh", "Hazaribagh"],
        "activities": ["Motorbike and sports car drive along 14 hairpin loops", "Jet skiing and speedboat cruising in Patratu reservoir", "Sunset photography from valley viewpoint ridge"],
        "img_url": "https://images.unsplash.com/photo-1506744038136-46273834b3fb?auto=format&fit=crop&w=1200&q=80",
        "photographer": "Abhishek Mahto", "profile": "https://unsplash.com/@abhishekm"
    },

    # ---------- ANDAMAN & NICOBAR ISLANDS (UT) (6) ----------
    {
        "id": "port_blair", "name": "Port Blair", "state": "Andaman and Nicobar Islands", "is_ut": True,
        "lat": 11.6234, "lon": 92.7265, "category": "Colonial Freedom Heritage", "best_season": "October to May",
        "budget": 4800, "days": 3,
        "overview": "Capital of the Andaman archipelago steeped in freedom struggle history at Cellular Jail (Kaala Paani) and gateway to tropical coral reefs.",
        "attractions": ["Cellular Jail National Memorial", "Corbyn's Cove Beach", "Samudrika Naval Marine Museum", "Chidiya Tapu Sunset Point", "Anthropological Museum"],
        "nearby": ["Havelock Island", "Ross Island", "Neil Island"],
        "activities": ["Moving Light & Sound Show inside Cellular Jail", "Sunset birdwatching at Chidiya Tapu", "Water scooters and swimming at Corbyn's Cove"],
        "img_url": "https://images.unsplash.com/photo-1512343879784-a960bf40e7f2?auto=format&fit=crop&w=1200&q=80",
        "photographer": "Rohan D'Souza", "profile": "https://unsplash.com/@rohandsouza"
    },
    {
        "id": "havelock_island", "name": "Havelock Island (Swaraj Dweep)", "state": "Andaman and Nicobar Islands", "is_ut": True,
        "lat": 11.9761, "lon": 92.9876, "category": "Asia's Best Beach", "best_season": "October to May",
        "budget": 6000, "days": 3,
        "overview": "Crown jewel island of Andamans home to Radhanagar Beach (voted best in Asia by Time Magazine), world-class scuba diving, and elephant beach.",
        "attractions": ["Radhanagar Beach (Beach No. 7)", "Elephant Beach (Snorkeling Hub)", "Kalapathar Beach", "Govind Nagar Beach", "Vijay Nagar Beach"],
        "nearby": ["Neil Island", "Port Blair", "Barren Island"],
        "activities": ["Scuba diving in coral reef drop-offs", "Sea walking and snorkeling at Elephant Beach", "Mesmerizing sunset on powder-white sands of Radhanagar"],
        "img_url": "https://images.unsplash.com/photo-1512343879784-a960bf40e7f2?auto=format&fit=crop&w=1200&q=80",
        "photographer": "Vikramaditya Roy", "profile": "https://unsplash.com/@vikramaditya"
    },
    {
        "id": "neil_island", "name": "Neil Island (Shaheed Dweep)", "state": "Andaman and Nicobar Islands", "is_ut": True,
        "lat": 11.8333, "lon": 93.0500, "category": "Relaxed Coral Island", "best_season": "October to May",
        "budget": 5200, "days": 2,
        "overview": "Tranquil vegetable bowl island characterized by lush green agricultural patches, turquoise lagoons, and the Natural Coral Bridge.",
        "attractions": ["Natural Rock Bridge (Howrah Bridge)", "Bharatpur Beach (Water Sports)", "Laxmanpur Beach Sunset Point", "Sitapur Sunrise Beach"],
        "nearby": ["Havelock Island", "Port Blair", "Sir Hugh Rose Island"],
        "activities": ["Walking to the living coral natural rock arch at low tide", "Glass-bottom boat ride over live reef at Bharatpur", "Cycling along quiet coconut palm village lanes"],
        "img_url": "https://images.unsplash.com/photo-1512343879784-a960bf40e7f2?auto=format&fit=crop&w=1200&q=80",
        "photographer": "Arunabh Baruah", "profile": "https://unsplash.com/@arunabhb"
    },
    {
        "id": "radhanagar_beach", "name": "Radhanagar Beach", "state": "Andaman and Nicobar Islands", "is_ut": True,
        "lat": 11.9840, "lon": 92.9510, "category": "Blue Flag Paradise", "best_season": "October to May",
        "budget": 5500, "days": 1,
        "overview": "Consistently ranked among the top 10 beaches in the world, with broad crescent pristine white sands framed by tropical rainforest.",
        "attractions": ["Radhanagar Shoreline", "Neil's Cove Lagoon", "Rainforest Nature Trail", "Sunset Watch Point"],
        "nearby": ["Havelock Town", "Elephant Beach", "Kalapathar"],
        "activities": ["Swimming in transparent aquamarine waters", "Strolling 2 km of untouched white sands", "Watching the dramatic purple sunset illuminate the horizon"],
        "img_url": "https://images.unsplash.com/photo-1512343879784-a960bf40e7f2?auto=format&fit=crop&w=1200&q=80",
        "photographer": "Deepak Bhatt", "profile": "https://unsplash.com/@deepakbhatt"
    },
    {
        "id": "baratang", "name": "Baratang Island", "state": "Andaman and Nicobar Islands", "is_ut": True,
        "lat": 12.1167, "lon": 92.7833, "category": "Caves & Mangroves", "best_season": "October to April",
        "budget": 4200, "days": 1,
        "overview": "Adventurous island on the Great Andaman Trunk Road famous for speedboat mangrove safari, limestone caves, and active mud volcanoes.",
        "attractions": ["Limestone Caves (Stalactites & Stalagmites)", "Mangrove Creek Boat Safari", "Active Mud Volcanoes", "Parrot Island Sunset"],
        "nearby": ["Port Blair", "Rangat", "Mayabunder"],
        "activities": ["Speedboat ride speeding through dense mangrove canopy tunnel", "Spelunking through ancient limestone cave formations", "Watching thousands of parrots return to Parrot Island at dusk"],
        "img_url": "https://images.unsplash.com/photo-1506744038136-46273834b3fb?auto=format&fit=crop&w=1200&q=80",
        "photographer": "Debashish Halder", "profile": "https://unsplash.com/@debashishh"
    },
    {
        "id": "ross_island", "name": "Ross Island (Netaji Subhash Chandra Bose Dweep)", "state": "Andaman and Nicobar Islands", "is_ut": True,
        "lat": 11.6739, "lon": 92.7633, "category": "Historic Ghost Town", "best_season": "October to May",
        "budget": 3500, "days": 1,
        "overview": "Former British administrative capital nicknamed 'Paris of the East', now a hauntingly picturesque ghost town overgrown by ancient banyan roots.",
        "attractions": ["British Colonial Ruins (Bakery, Ballroom, Church)", "Subhash Chandra Bose Memorial", "Japanese WWII Bunkers", "Spotted Deer Sanctuary", "Light & Sound Show"],
        "nearby": ["Port Blair", "North Bay Island", "Viper Island"],
        "activities": ["Walking among banyan tree roots swallowing British stone walls", "Hand-feeding gentle spotted deer and peacocks", "Ferry boat ride from Aberdeen Jetty"],
        "img_url": "https://images.unsplash.com/photo-1590050752117-238cb0fb12b1?auto=format&fit=crop&w=1200&q=80",
        "photographer": "Sanjay Acharya", "profile": "https://unsplash.com/@sanjayacharya"
    }
]

print(f"East region loaded: {len(EAST_DESTINATIONS)} destinations.")
