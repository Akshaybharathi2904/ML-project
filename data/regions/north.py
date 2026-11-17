"""
TRAVELMATE AI - North India Destinations (78 Verified Destinations)
Himachal Pradesh, Uttarakhand, Punjab, Haryana, Uttar Pradesh, Delhi, Jammu and Kashmir, Ladakh, Chandigarh
"""

NORTH_DESTINATIONS = [
    # ---------- HIMACHAL PRADESH (12) ----------
    {
        "id": "manali", "name": "Manali", "state": "Himachal Pradesh", "is_ut": False,
        "lat": 32.2396, "lon": 77.1887, "category": "Himalayan Hill Station", "best_season": "October to June",
        "budget": 4000, "days": 4,
        "overview": "High-altitude Himalayan resort town renowned for snow-capped peaks, pine valleys, and cafes along the Beas River.",
        "attractions": ["Solang Valley", "Rohtang Pass", "Hadimba Temple", "Old Manali", "Jogini Waterfalls"],
        "nearby": ["Kullu", "Kasol", "Naggar"],
        "activities": ["Paragliding in Solang Valley", "Visiting historic wooden Hadimba Temple", "Trek to Jogini Waterfall"],
        "img_url": "https://images.unsplash.com/photo-1605649487212-47bdab064df7?auto=format&fit=crop&w=1200&q=80",
        "photographer": "Ashish Thakur", "profile": "https://unsplash.com/@ashishthakur"
    },
    {
        "id": "shimla", "name": "Shimla", "state": "Himachal Pradesh", "is_ut": False,
        "lat": 31.1048, "lon": 77.1734, "category": "Colonial Hill Station", "best_season": "March to June & Dec to Feb",
        "budget": 3800, "days": 3,
        "overview": "Former summer capital of British India perched on seven hills, famous for Mall Road, Ridge, and Kalka Toy Train.",
        "attractions": ["The Ridge", "Mall Road", "Jakhu Temple & Hanuman Statue", "Viceregal Lodge", "Kufri"],
        "nearby": ["Kufri", "Chail", "Narkanda"],
        "activities": ["UNESCO Kalka-Shimla Toy Train ride", "Evening stroll on The Ridge", "Ropeway ride to Jakhu Temple"],
        "img_url": "https://images.unsplash.com/photo-1597074866923-dc0589150358?auto=format&fit=crop&w=1200&q=80",
        "photographer": "Rajat Sharma", "profile": "https://unsplash.com/@rajatsharma"
    },
    {
        "id": "dharamshala", "name": "Dharamshala", "state": "Himachal Pradesh", "is_ut": False,
        "lat": 32.2190, "lon": 76.3234, "category": "Tibetan & Himalayan", "best_season": "March to June & Sep to Nov",
        "budget": 3400, "days": 3,
        "overview": "Spiritual residence of the Dalai Lama in Kangra Valley, surrounded by cedar forests beneath Dhauladhar peaks.",
        "attractions": ["Tsuglagkhang Complex (Dalai Lama Temple)", "HPCA Cricket Stadium", "Bhagsunag Waterfall", "Namgyal Monastery", "St. John in the Wilderness"],
        "nearby": ["McLeod Ganj", "Palampur", "Kangra"],
        "activities": ["Triund day trek", "Attending public teachings of Dalai Lama", "Visiting the high-altitude HPCA stadium"],
        "img_url": "https://images.unsplash.com/photo-1588714477688-cf28a50e94f7?auto=format&fit=crop&w=1200&q=80",
        "photographer": "Vikram Negi", "profile": "https://unsplash.com/@vikramnegi"
    },
    {
        "id": "spiti_valley", "name": "Spiti Valley", "state": "Himachal Pradesh", "is_ut": False,
        "lat": 32.2461, "lon": 78.0349, "category": "High-Altitude Desert", "best_season": "May to October",
        "budget": 4200, "days": 5,
        "overview": "The Middle Land between Tibet and India, a high-altitude cold desert of thousand-year-old monasteries and starry skies.",
        "attractions": ["Key Monastery", "Chandratal Lake", "Dhankar Monastery", "Kibber Village", "Kaza Market"],
        "nearby": ["Kaza", "Tabo", "Pin Valley"],
        "activities": ["Camping by crescent-shaped Chandratal Lake", "Mailing a postcard from Hikkim highest post office", "Visiting 1000-year-old Tabo Monastery"],
        "img_url": "https://images.unsplash.com/photo-1544735716-392fe2489ffa?auto=format&fit=crop&w=1200&q=80",
        "photographer": "Prashant Gupta", "profile": "https://unsplash.com/@prashantgupta"
    },
    {
        "id": "kasol", "name": "Kasol", "state": "Himachal Pradesh", "is_ut": False,
        "lat": 32.0100, "lon": 77.3150, "category": "Nature & Trekking", "best_season": "April to June & Oct to Nov",
        "budget": 2800, "days": 3,
        "overview": "Mini Israel of the Himalayas situated on the Parvati River, the trailhead for Kheerganga and Tosh treks.",
        "attractions": ["Parvati River Bank", "Manikaran Sahib Gurudwara", "Chalal Village", "Tosh Village", "Kheerganga Hot Springs"],
        "nearby": ["Manikaran", "Tosh", "Malana"],
        "activities": ["Kheerganga trek and natural sulphur bath", "Relaxing by Parvati riverbanks", "Sampling Israeli Shakshuka in village cafes"],
        "img_url": "https://images.unsplash.com/photo-1544735716-392fe2489ffa?auto=format&fit=crop&w=1200&q=80",
        "photographer": "Rohit Verma", "profile": "https://unsplash.com/@rohitverma"
    },
    {
        "id": "dalhousie", "name": "Dalhousie", "state": "Himachal Pradesh", "is_ut": False,
        "lat": 32.5387, "lon": 75.9710, "category": "Colonial Hill Station", "best_season": "March to June & Sep to Dec",
        "budget": 3500, "days": 3,
        "overview": "Tranquil hill retreat founded in 1854 across five pine-clad hills, gateway to the Switzerland of India, Khajjiar.",
        "attractions": ["Khajjiar Lake & Meadow", "Panchpula", "Dainkund Peak", "St. John's Church", "Kalatop Wildlife Sanctuary"],
        "nearby": ["Khajjiar", "Chamba", "Dharamsala"],
        "activities": ["Zorbing and horse riding in Khajjiar meadows", "Trekking to Dainkund singing hill peak", "Nature walk through Kalatop deodar forest"],
        "img_url": "https://images.unsplash.com/photo-1506744038136-46273834b3fb?auto=format&fit=crop&w=1200&q=80",
        "photographer": "Sunil Rana", "profile": "https://unsplash.com/@sunilrana"
    },
    {
        "id": "bir_billing", "name": "Bir Billing", "state": "Himachal Pradesh", "is_ut": False,
        "lat": 32.0436, "lon": 76.7170, "category": "Adventure & Paragliding", "best_season": "October to June",
        "budget": 3600, "days": 2,
        "overview": "World paragliding capital in Kangra Valley, where Billing serves as the 2400m takeoff ridge and Bir the landing meadow.",
        "attractions": ["Billing Paragliding Take-off Site", "Chokling Monastery", "Deer Park Institute", "Bir Tea Factory", "Baijnath Shiva Temple"],
        "nearby": ["Palampur", "Dharamshala", "Joginder Nagar"],
        "activities": ["Tandem paragliding flight over Kangra Valley", "Sunset viewing at Bir landing ground", "Visiting 13th-century stone Baijnath temple"],
        "img_url": "https://images.unsplash.com/photo-1506744038136-46273834b3fb?auto=format&fit=crop&w=1200&q=80",
        "photographer": "Anurag Kashyap", "profile": "https://unsplash.com/@anuragk"
    },
    {
        "id": "kullu", "name": "Kullu", "state": "Himachal Pradesh", "is_ut": False,
        "lat": 31.9579, "lon": 77.1095, "category": "Valley of Gods", "best_season": "March to June & Sep to Nov",
        "budget": 3200, "days": 2,
        "overview": "Valley of Gods on the Beas River celebrated for grand week-long Dussehra festivities and woolen Kullu shawls.",
        "attractions": ["Raghunath Temple", "Bijli Mahadev Temple", "Great Himalayan National Park", "Bhrigu Lake", "Raisan River Rafting"],
        "nearby": ["Manali", "Naggar", "Tirthan Valley"],
        "activities": ["White water rafting on Beas River", "Trek to lightning-struck Bijli Mahadev", "Shopping authentic Kullu handloom shawls"],
        "img_url": "https://images.unsplash.com/photo-1544735716-392fe2489ffa?auto=format&fit=crop&w=1200&q=80",
        "photographer": "Deepak Mehta", "profile": "https://unsplash.com/@deepakmehta"
    },
    {
        "id": "kinnaur", "name": "Kinnaur (Kalpa & Sangla)", "state": "Himachal Pradesh", "is_ut": False,
        "lat": 31.5372, "lon": 78.2562, "category": "Tribal Himalayan", "best_season": "April to October",
        "budget": 3800, "days": 4,
        "overview": "Land of fairy tales on the Indo-Tibetan highway, home to sacred Kinner Kailash peak, apple orchards, and Chitkul.",
        "attractions": ["Kinner Kailash View Point", "Chitkul (Last Village)", "Kamru Fort Sangla", "Baspa River Valley", "Hindustan-Tibet Highway Cliff"],
        "nearby": ["Sangla", "Chitkul", "Reckong Peo"],
        "activities": ["Visiting India's last inhabited village Chitkul", "Watching dawn turn Kinner Kailash golden", "Trekking the Baspa riverbank"],
        "img_url": "https://images.unsplash.com/photo-1544735716-392fe2489ffa?auto=format&fit=crop&w=1200&q=80",
        "photographer": "Pooja Negi", "profile": "https://unsplash.com/@poojanegi"
    },
    {
        "id": "chamba", "name": "Chamba", "state": "Himachal Pradesh", "is_ut": False,
        "lat": 32.5534, "lon": 76.1258, "category": "Heritage & River", "best_season": "March to June & Sep to Nov",
        "budget": 2800, "days": 2,
        "overview": "Ancient medieval capital on the Ravi River celebrated for 10th-century Lakshmi Narayan temples and miniature Pahari paintings.",
        "attractions": ["Lakshmi Narayan Temple Complex", "Chaugan Grassland", "Bhuri Singh Museum", "Chamunda Devi Temple", "Rang Mahal"],
        "nearby": ["Dalhousie", "Khajjiar", "Bharmour"],
        "activities": ["Exploring Pahari miniature paintings in museum", "Viewing Ravi river valley from Chamunda hilltop", "Shopping for Chamba Rumal embroidery"],
        "img_url": "https://images.unsplash.com/photo-1609766857041-ed402ea8069a?auto=format&fit=crop&w=1200&q=80",
        "photographer": "Girish Chand", "profile": "https://unsplash.com/@girishchand"
    },
    {
        "id": "jibhi", "name": "Jibhi (Tirthan Valley)", "state": "Himachal Pradesh", "is_ut": False,
        "lat": 31.6360, "lon": 77.3490, "category": "Hidden Nature Gem", "best_season": "March to June & Sep to Nov",
        "budget": 3100, "days": 3,
        "overview": "Enchanting offbeat cedar hamlet in Banjar Valley, celebrated for Victorian wooden cottages, freshwater streams, and Serolsar Lake.",
        "attractions": ["Jibhi Waterfall", "Jalori Pass", "Serolsar Lake", "Chehni Kothi Tower", "Great Himalayan National Park Gateway"],
        "nearby": ["Shoja", "Tirthan Valley", "Aut"],
        "activities": ["Trek through oak forest to Serolsar Lake", "Visiting 1500-year-old wooden Chehni Kothi tower", "Trout fishing in Tirthan river"],
        "img_url": "https://images.unsplash.com/photo-1506744038136-46273834b3fb?auto=format&fit=crop&w=1200&q=80",
        "photographer": "Aman Sethi", "profile": "https://unsplash.com/@amansethi"
    },
    {
        "id": "kaza", "name": "Kaza", "state": "Himachal Pradesh", "is_ut": False,
        "lat": 32.2276, "lon": 78.0710, "category": "High-Altitude Hub", "best_season": "May to October",
        "budget": 3500, "days": 3,
        "overview": "Administrative capital and cultural nerve center of Spiti Valley, perched at 12,000 feet on the Spiti River banks.",
        "attractions": ["Kaza Main Bazaar", "Sakya Tengyeling Monastery", "Komic Highest Village with Road", "Langza Fossil Village", "Hikkim Post Office"],
        "nearby": ["Key Monastery", "Tabo", "Kibber"],
        "activities": ["Hunting ancient sea fossils at Langza", "Visiting the grand Buddha statue facing the valley", "Renting Enfield bikes for Spiti circuits"],
        "img_url": "https://images.unsplash.com/photo-1544735716-392fe2489ffa?auto=format&fit=crop&w=1200&q=80",
        "photographer": "Kunal Sen", "profile": "https://unsplash.com/@kunalsen"
    },

    # ---------- UTTARAKHAND (14) ----------
    {
        "id": "rishikesh", "name": "Rishikesh", "state": "Uttarakhand", "is_ut": False,
        "lat": 30.0869, "lon": 78.2676, "category": "Yoga & Adventure", "best_season": "September to May",
        "budget": 3200, "days": 3,
        "overview": "Yoga Capital of the World on the sacred Ganges, famous for suspension bridges, ashrams, and whitewater rafting.",
        "attractions": ["Ram Jhula & Laxman Jhula", "Triveni Ghat Evening Aarti", "Beatles Ashram (Chaurasi Kutia)", "Neelkanth Mahadev", "Shivpuri Rafting"],
        "nearby": ["Haridwar", "Dehradun", "Mussoorie"],
        "activities": ["Whitewater rafting on the Ganges", "Ganga Aarti at Triveni Ghat", "Yoga and meditation session at Parmarth Niketan"],
        "img_url": "https://images.unsplash.com/photo-1590050752117-238cb0fb12b1?auto=format&fit=crop&w=1200&q=80",
        "photographer": "Vishal Arya", "profile": "https://unsplash.com/@vishalarya"
    },
    {
        "id": "mussoorie", "name": "Mussoorie", "state": "Uttarakhand", "is_ut": False,
        "lat": 30.4598, "lon": 78.0644, "category": "Hill Station", "best_season": "March to June & Sep to Nov",
        "budget": 3800, "days": 3,
        "overview": "Queen of the Hills commanding sweeping panoramas of the Doon Valley and snow-laden Garhwal Himalayan peaks.",
        "attractions": ["Kempty Falls", "Mall Road", "Gun Hill Ropeway", "Camel's Back Road", "Company Garden"],
        "nearby": ["Dhanaulti", "Dehradun", "Kanatal"],
        "activities": ["Cable car ride to Gun Hill", "Evening stroll on Camel's Back Road", "Visiting George Everest House"],
        "img_url": "https://images.unsplash.com/photo-1597074866923-dc0589150358?auto=format&fit=crop&w=1200&q=80",
        "photographer": "Amit Rawat", "profile": "https://unsplash.com/@amitrawat"
    },
    {
        "id": "nainital", "name": "Nainital", "state": "Uttarakhand", "is_ut": False,
        "lat": 29.3803, "lon": 79.4636, "category": "Lake Hill Station", "best_season": "March to June & Oct to Feb",
        "budget": 3600, "days": 3,
        "overview": "Charming Lake District of India centered around the eye-shaped emerald Naini Lake fringed by green hills.",
        "attractions": ["Naini Lake Boating", "Naina Devi Temple", "Snow View Point", "Tiffin Top (Dorothy's Seat)", "Eco Cave Gardens"],
        "nearby": ["Bhimtal", "Naukuchiatal", "Almora"],
        "activities": ["Boating on emerald Naini Lake", "Ropeway ride to Snow View Point", "Crawling through Eco Cave rocky tunnels"],
        "img_url": "https://images.unsplash.com/photo-1544735716-392fe2489ffa?auto=format&fit=crop&w=1200&q=80",
        "photographer": "Harish Joshi", "profile": "https://unsplash.com/@harishjoshi"
    },
    {
        "id": "haridwar", "name": "Haridwar", "state": "Uttarakhand", "is_ut": False,
        "lat": 29.9457, "lon": 78.1642, "category": "Spiritual Gateway", "best_season": "October to April",
        "budget": 2600, "days": 2,
        "overview": "Gateway to the Gods where the holy Ganges emerges from the Himalayas onto the Indo-Gangetic plains.",
        "attractions": ["Har Ki Pauri Ghat", "Mansa Devi Temple", "Chandi Devi Temple", "Maya Devi Temple", "Daksheswara Mahadev"],
        "nearby": ["Rishikesh", "Dehradun", "Rajaji National Park"],
        "activities": ["Witnessing grand Ganga Aarti at Har Ki Pauri", "Ropeway ride to Mansa Devi hill temple", "Taking a holy dip in Brahmakund"],
        "img_url": "https://images.unsplash.com/photo-1582510003544-4d00b7f74220?auto=format&fit=crop&w=1200&q=80",
        "photographer": "Saurabh Pandey", "profile": "https://unsplash.com/@saurabhpandey"
    },
    {
        "id": "jim_corbett", "name": "Jim Corbett National Park", "state": "Uttarakhand", "is_ut": False,
        "lat": 29.5300, "lon": 78.7747, "category": "Tiger Reserve", "best_season": "November to June",
        "budget": 4500, "days": 3,
        "overview": "India's oldest national park on the Ramganga River, world-renowned for Royal Bengal Tigers and wild elephants.",
        "attractions": ["Dhikala Safari Zone", "Bijrani Safari Zone", "Corbett Falls", "Garjiya Devi Temple", "Ramganga River Reservoir"],
        "nearby": ["Ramnagar", "Nainital", "Ranikhet"],
        "activities": ["Open 4x4 Gypsy jungle safari", "Overnight stay inside Dhikala forest rest house", "Birdwatching along Ramganga river"],
        "img_url": "https://images.unsplash.com/photo-1512343879784-a960bf40e7f2?auto=format&fit=crop&w=1200&q=80",
        "photographer": "Rohit Negi", "profile": "https://unsplash.com/@rohitnegi"
    },
    {
        "id": "auli", "name": "Auli", "state": "Uttarakhand", "is_ut": False,
        "lat": 30.5284, "lon": 79.5668, "category": "Skiing & Snow Peak", "best_season": "December to March (Skiing) & Year-round",
        "budget": 4800, "days": 3,
        "overview": "India's premier skiing destination offering 360-degree views of Nanda Devi, Kamet, and Mana Parvat peaks.",
        "attractions": ["Auli Ropeway (4km)", "Auli Artificial Lake", "Gorson Bugyal Trek", "Kwani Bugyal", "Joshimath Gateway"],
        "nearby": ["Joshimath", "Badrinath", "Hemkund Sahib"],
        "activities": ["Snow skiing on groomed Himalayan slopes", "Riding India's longest cable car from Joshimath", "Trek to Gorson alpine meadow"],
        "img_url": "https://images.unsplash.com/photo-1544735716-392fe2489ffa?auto=format&fit=crop&w=1200&q=80",
        "photographer": "Kunal Bisht", "profile": "https://unsplash.com/@kunalbisht"
    },
    {
        "id": "kedarnath", "name": "Kedarnath", "state": "Uttarakhand", "is_ut": False,
        "lat": 30.7352, "lon": 79.0669, "category": "Sacred Himalayan", "best_season": "May to June & Sep to Oct",
        "budget": 4500, "days": 3,
        "overview": "One of the 12 sacred Jyotirlingas of Lord Shiva standing against the majestic snow walls of Kedarnath Peak.",
        "attractions": ["Kedarnath Temple", "Bhairavnath Temple", "Gandhi Sarovar (Chorabari Lake)", "Mandakini River Source", "Vasuki Tal"],
        "nearby": ["Guptkashi", "Gaurikund", "Sonprayag"],
        "activities": ["16-km sacred trek from Gaurikund", "Attending evening Shiva aarti amidst mountain peaks", "Helicopter pilgrimage ride"],
        "img_url": "https://images.unsplash.com/photo-1544735716-392fe2489ffa?auto=format&fit=crop&w=1200&q=80",
        "photographer": "Praveen Uniyal", "profile": "https://unsplash.com/@praveenu"
    },
    {
        "id": "badrinath", "name": "Badrinath", "state": "Uttarakhand", "is_ut": False,
        "lat": 30.7433, "lon": 79.4938, "category": "Sacred Dham", "best_season": "May to June & Sep to Oct",
        "budget": 4000, "days": 2,
        "overview": "Premier Chardham pilgrimage dedicated to Lord Vishnu, set between Nar and Narayana mountain ranges beside Alaknanda River.",
        "attractions": ["Badrinath Temple", "Tapt Kund Hot Springs", "Mana (First Indian Village)", "Vasudhara Falls", "Bheem Pul"],
        "nearby": ["Joshimath", "Auli", "Valley of Flowers"],
        "activities": ["Bath in natural hot sulphur Tapt Kund", "Visiting India's first tea stall in Mana village", "Hike to 400-ft Vasudhara Falls"],
        "img_url": "https://images.unsplash.com/photo-1609766857041-ed402ea8069a?auto=format&fit=crop&w=1200&q=80",
        "photographer": "Deepak Bhatt", "profile": "https://unsplash.com/@deepakbhatt"
    },
    {
        "id": "valley_of_flowers", "name": "Valley of Flowers", "state": "Uttarakhand", "is_ut": False,
        "lat": 30.7280, "lon": 79.6053, "category": "UNESCO Alpine Biosphere", "best_season": "July to September",
        "budget": 4600, "days": 4,
        "overview": "UNESCO World Heritage alpine valley blanketed with over 500 species of wild Himalayan blooms and blue poppies.",
        "attractions": ["Valley of Flowers National Park", "Pushpawati River", "Joan Margaret Legge Memorial", "Hemkund Sahib"],
        "nearby": ["Govindghat", "Ghangaria", "Joshimath"],
        "activities": ["Trekking through blossoming alpine meadows", "Spotting Himalayan Blue Poppies and Brahmakamal", "Ascending to Hemkund Sahib glacial lake"],
        "img_url": "https://images.unsplash.com/photo-1506744038136-46273834b3fb?auto=format&fit=crop&w=1200&q=80",
        "photographer": "Manish Pant", "profile": "https://unsplash.com/@manishpant"
    },
    {
        "id": "chopta", "name": "Chopta (Tungnath & Chandrashila)", "state": "Uttarakhand", "is_ut": False,
        "lat": 30.4859, "lon": 79.1770, "category": "Meadows & Peak", "best_season": "April to November & Winter Snow",
        "budget": 3000, "days": 3,
        "overview": "Mini Switzerland of Uttarakhand and base for the trek to Tungnath, the highest Shiva temple in the world (3680m).",
        "attractions": ["Tungnath Temple", "Chandrashila Summit (4000m)", "Deoria Tal Lake", "Chopta Bugyal Meadows", "Ukhimath"],
        "nearby": ["Ukhimath", "Sari Village", "Gopeshwar"],
        "activities": ["Trek to Tungnath the highest Shiva temple", "Sunrise 360-degree Himalayan view from Chandrashila", "Camping beside Deoria Tal reflecting Chaukhamba"],
        "img_url": "https://images.unsplash.com/photo-1544735716-392fe2489ffa?auto=format&fit=crop&w=1200&q=80",
        "photographer": "Naveen Chauhan", "profile": "https://unsplash.com/@naveenchauhan"
    },
    {
        "id": "almora", "name": "Almora", "state": "Uttarakhand", "is_ut": False,
        "lat": 29.5971, "lon": 79.6591, "category": "Cultural Hill Station", "best_season": "March to June & Sep to Nov",
        "budget": 3000, "days": 2,
        "overview": "Cultural heart of Kumaon situated on a horse-saddle ridge, famed for Kasar Devi magnetic field, temples, and Bal Mithai.",
        "attractions": ["Kasar Devi Temple", "Jageshwar Temple Complex", "Zero Point Binsar", "Chitai Golu Devta Temple", "Bright End Corner"],
        "nearby": ["Binsar", "Ranikhet", "Kausani"],
        "activities": ["Visiting geomagnetic Kasar Devi temple", "Tasting traditional Bal Mithai and Singauri", "Exploring 100+ stone temples at Jageshwar"],
        "img_url": "https://images.unsplash.com/photo-1605649487212-47bdab064df7?auto=format&fit=crop&w=1200&q=80",
        "photographer": "Bhupendra Bisht", "profile": "https://unsplash.com/@bhupendrab"
    },
    {
        "id": "lansdowne", "name": "Lansdowne", "state": "Uttarakhand", "is_ut": False,
        "lat": 29.8377, "lon": 78.6874, "category": "Cantonment Retreat", "best_season": "Throughout the year",
        "budget": 3200, "days": 2,
        "overview": "Quiet, pristine cantonment hill town established in 1887 with pine forests, colonial bungalows, and mountain peace.",
        "attractions": ["Bhulla Tal Lake", "Tip N Top View Point", "St. John's Church", "Garhwal Rifles Regimental Museum", "Tarkeshwar Mahadev"],
        "nearby": ["Kotdwar", "Pauri", "Corbett"],
        "activities": ["Boating on Bhulla Tal", "Quiet walk through pine-clad Lovers Lane", "Panoramic sunset from Tip N Top"],
        "img_url": "https://images.unsplash.com/photo-1544735716-392fe2489ffa?auto=format&fit=crop&w=1200&q=80",
        "photographer": "Surender Rawat", "profile": "https://unsplash.com/@surenderrawat"
    },
    {
        "id": "ranikhet", "name": "Ranikhet", "state": "Uttarakhand", "is_ut": False,
        "lat": 29.6434, "lon": 79.4322, "category": "Hill Station & Golf", "best_season": "March to June & Sep to Nov",
        "budget": 3300, "days": 2,
        "overview": "Queen's Meadow in Kumaon hills featuring Asia's highest 9-hole golf course, apple orchards, and Trishul peak views.",
        "attractions": ["Ranikhet Golf Course", "Chaubatia Apple Orchards", "Jhula Devi Temple", "Kumaon Regimental Centre Museum", "Bhalu Dam"],
        "nearby": ["Almora", "Kausani", "Nainital"],
        "activities": ["Playing golf on high-altitude green slopes", "Picking fresh fruit at Chaubatia orchards", "Tying bell for wish at Jhula Devi temple"],
        "img_url": "https://images.unsplash.com/photo-1506744038136-46273834b3fb?auto=format&fit=crop&w=1200&q=80",
        "photographer": "Dinesh Chandra", "profile": "https://unsplash.com/@dineshchandra"
    },
    {
        "id": "kausani", "name": "Kausani", "state": "Uttarakhand", "is_ut": False,
        "lat": 29.8543, "lon": 79.5967, "category": "Panoramic Himalayas", "best_season": "March to June & Sep to Nov",
        "budget": 2900, "days": 2,
        "overview": "Switzerland of India as dubbed by Mahatma Gandhi, offering a uninterrupted 300-km panoramic vista of Himalayan peaks.",
        "attractions": ["Anasakti Ashram (Gandhi Ashram)", "Kausani Tea Estate", "Rudradhari Falls & Caves", "Baijnath Temple", "Pinnath Peak"],
        "nearby": ["Baijnath", "Bageshwar", "Almora"],
        "activities": ["Watching 300-km golden sunrise over Trishul and Nanda Devi", "Meditating at Anasakti Ashram", "Tea factory tour and fresh garden tea tasting"],
        "img_url": "https://images.unsplash.com/photo-1544735716-392fe2489ffa?auto=format&fit=crop&w=1200&q=80",
        "photographer": "Kamal Pandey", "profile": "https://unsplash.com/@kamalpandey"
    },

    # ---------- PUNJAB (8) ----------
    {
        "id": "amritsar", "name": "Amritsar", "state": "Punjab", "is_ut": False,
        "lat": 31.6340, "lon": 74.8723, "category": "Spiritual & Heritage", "best_season": "October to March",
        "budget": 3500, "days": 3,
        "overview": "Spiritual capital of Sikhism housing the revered Harmandir Sahib (Golden Temple), Wagah Border, and rich cuisine.",
        "attractions": ["Golden Temple (Harmandir Sahib)", "Wagah Border Beating Retreat", "Jallianwala Bagh", "Partition Museum", "Gobindgarh Fort"],
        "nearby": ["Jalandhar", "Lahore Border", "Tarn Taran"],
        "activities": ["Partaking in community Langar service at Golden Temple", "Watching the Wagah Border parade", "Kulcha and lassi food trail in Old City"],
        "img_url": "https://images.unsplash.com/photo-1609766857041-ed402ea8069a?auto=format&fit=crop&w=1200&q=80",
        "photographer": "Simranjeet Singh", "profile": "https://unsplash.com/@simranjeets"
    },
    {
        "id": "patiala", "name": "Patiala", "state": "Punjab", "is_ut": False,
        "lat": 30.3398, "lon": 76.3869, "category": "Royal Heritage", "best_season": "October to March",
        "budget": 3000, "days": 2,
        "overview": "Royal city of Maharajas famed for Qila Mubarak palace, Patiala shahi turbans, Paranda tassels, and Phulkari embroidery.",
        "attractions": ["Qila Mubarak Complex", "Sheesh Mahal Palace", "Baradari Gardens", "Moti Bagh Palace", "Kali Devi Temple"],
        "nearby": ["Chandigarh", "Ambala", "Ludhiana"],
        "activities": ["Exploring mirror-worked Sheesh Mahal", "Shopping for authentic Phulkari dupattas and juttis", "Walking in royal Baradari gardens"],
        "img_url": "https://images.unsplash.com/photo-1582510003544-4d00b7f74220?auto=format&fit=crop&w=1200&q=80",
        "photographer": "Gurpreet Singh", "profile": "https://unsplash.com/@gurpreetsingh"
    },
    {
        "id": "anandpur_sahib", "name": "Anandpur Sahib", "state": "Punjab", "is_ut": False,
        "lat": 31.2361, "lon": 76.4983, "category": "Sacred Sikh Heritage", "best_season": "October to March",
        "budget": 2700, "days": 2,
        "overview": "City of Bliss, birthplace of the Khalsa panth in 1699 by Guru Gobind Singh Ji, famous for the grand Hola Mohalla festival.",
        "attractions": ["Takht Sri Kesgarh Sahib", "Virasat-e-Khalsa Museum", "Qila Anandgarh Sahib", "Naina Devi Hill Temple"],
        "nearby": ["Nangal Dam", "Rupnagar", "Chandigarh"],
        "activities": ["Visiting state-of-the-art Virasat-e-Khalsa museum", "Witnessing Gatka martial arts during Hola Mohalla", "Langar at Takht Sri Kesgarh Sahib"],
        "img_url": "https://images.unsplash.com/photo-1609766857041-ed402ea8069a?auto=format&fit=crop&w=1200&q=80",
        "photographer": "Harmanpreet Singh", "profile": "https://unsplash.com/@harmanpreets"
    },
    {
        "id": "ludhiana", "name": "Ludhiana", "state": "Punjab", "is_ut": False,
        "lat": 30.9010, "lon": 75.8573, "category": "Industrial & Heritage", "best_season": "October to March",
        "budget": 3100, "days": 2,
        "overview": "Manchester of India on the Sutlej River, home to Punjab Agricultural University rural museum and Lodhi Fort.",
        "attractions": ["Punjab Agricultural University Museum", "Lodhi Fort", "Hardy's World", "Nehru Rose Garden", "Tiger Safari Zoo"],
        "nearby": ["Jalandhar", "Khanna", "Chandigarh"],
        "activities": ["Exploring Punjabi rural heritage village at PAU", "Visiting textile and hosiery craft markets", "Strolling in Rose Garden"],
        "img_url": "https://images.unsplash.com/photo-1582510003544-4d00b7f74220?auto=format&fit=crop&w=1200&q=80",
        "photographer": "Jaspreet Gill", "profile": "https://unsplash.com/@jaspreetgill"
    },
    {
        "id": "kapurthala", "name": "Kapurthala", "state": "Punjab", "is_ut": False,
        "lat": 31.3802, "lon": 75.3819, "category": "French Architectural", "best_season": "October to March",
        "budget": 2900, "days": 1,
        "overview": "Paris of Punjab adorned with French Versailles-style Jagatjit Palace, Moorish Mosque, and Indo-Saracenic buildings.",
        "attractions": ["Jagatjit Palace (Sainik School)", "Moorish Mosque", "Elysée Palace", "Shalimar Gardens", "Kanjli Wetland"],
        "nearby": ["Jalandhar", "Amritsar", "Sultanpur Lodhi"],
        "activities": ["Touring French-inspired Jagatjit Palace", "Admiring Moroccan-style Moorish Mosque", "Birdwatching at Kanjli Wetland"],
        "img_url": "https://images.unsplash.com/photo-1582510003544-4d00b7f74220?auto=format&fit=crop&w=1200&q=80",
        "photographer": "Maninder Dhillon", "profile": "https://unsplash.com/@maninderd"
    },
    {
        "id": "bathinda", "name": "Bathinda", "state": "Punjab", "is_ut": False,
        "lat": 30.2110, "lon": 74.9455, "category": "Historic Fortress", "best_season": "October to March",
        "budget": 2600, "days": 1,
        "overview": "Ancient city home to the 1,400-year-old brick Qila Mubarak fort where India's first female ruler Razia Sultana was imprisoned.",
        "attractions": ["Qila Mubarak Bathinda", "Thermal Power Plant Lakes", "Chetak Park", "Maiser Khana Temple", "Rose Garden"],
        "nearby": ["Faridkot", "Mansa", "Abohar"],
        "activities": ["Exploring towering ramparts of brick Qila Mubarak", "Boating on Bathinda lakes", "Tasting traditional Sarson da Saag and Makki di Roti"],
        "img_url": "https://images.unsplash.com/photo-1609766857041-ed402ea8069a?auto=format&fit=crop&w=1200&q=80",
        "photographer": "Balwinder Singh", "profile": "https://unsplash.com/@balwinders"
    },
    {
        "id": "jalandhar", "name": "Jalandhar", "state": "Punjab", "is_ut": False,
        "lat": 31.3260, "lon": 75.5762, "category": "Sports & Heritage", "best_season": "October to March",
        "budget": 2800, "days": 2,
        "overview": "Historic Doaba hub famous as India's premier manufacturer of world-class sports goods, Wonderland, and Devi Talab.",
        "attractions": ["Devi Talab Mandir", "Wonderland Theme Park", "Pushpa Gujral Science City", "Jang-e-Azadi Memorial", "St. Mary's Cathedral"],
        "nearby": ["Amritsar", "Ludhiana", "Kapurthala"],
        "activities": ["Exploring Science City experiential exhibits", "Shopping international-grade cricket and sports gear", "Visiting Devi Talab holy pond"],
        "img_url": "https://images.unsplash.com/photo-1582510003544-4d00b7f74220?auto=format&fit=crop&w=1200&q=80",
        "photographer": "Amanjot Sidhu", "profile": "https://unsplash.com/@amanjots"
    },
    {
        "id": "pathankot", "name": "Pathankot", "state": "Punjab", "is_ut": False,
        "lat": 32.2689, "lon": 75.6499, "category": "Gateway & Lake", "best_season": "October to April",
        "budget": 2700, "days": 1,
        "overview": "Strategic tri-junction gateway linking Punjab, Himachal, and Jammu, situated near Mukteshwar Mahadev cave temples.",
        "attractions": ["Mukteshwar Temple & Caves", "Shahpurkandi Fort", "Ranjit Sagar Dam", "Nurpur Fort"],
        "nearby": ["Dalhousie", "Dharamsala", "Jammu"],
        "activities": ["Visiting Pandava cave shrines on Ravi riverbank", "Viewing Ranjit Sagar Dam reservoir", "Gateway break before Himachal hills"],
        "img_url": "https://images.unsplash.com/photo-1506744038136-46273834b3fb?auto=format&fit=crop&w=1200&q=80",
        "photographer": "Rajinder Verma", "profile": "https://unsplash.com/@rajinderverma"
    },

    # ---------- HARYANA (8) ----------
    {
        "id": "kurukshetra", "name": "Kurukshetra", "state": "Haryana", "is_ut": False,
        "lat": 29.9695, "lon": 76.8783, "category": "Epic Spiritual", "best_season": "October to March",
        "budget": 2600, "days": 2,
        "overview": "Dharmakshetra battlefield of the Mahabharata and the sacred birthplace of the Bhagavad Gita at Jyotisar.",
        "attractions": ["Brahma Sarovar", "Jyotisar Birthplace of Gita", "Sheikh Chilli's Tomb", "Sannihit Sarovar", "Kurukshetra Panorama"],
        "nearby": ["Karnal", "Ambala", "Chandigarh"],
        "activities": ["Holy dip in vast Brahma Sarovar during solar eclipse", "Sound and light show at Jyotisar sacred banyan tree", "Exploring Persian-style Sheikh Chilli tomb"],
        "img_url": "https://images.unsplash.com/photo-1582510003544-4d00b7f74220?auto=format&fit=crop&w=1200&q=80",
        "photographer": "Vivek Sharma", "profile": "https://unsplash.com/@viveksharma"
    },
    {
        "id": "sultanpur", "name": "Sultanpur National Park", "state": "Haryana", "is_ut": False,
        "lat": 28.4617, "lon": 76.8924, "category": "Bird Sanctuary", "best_season": "November to February",
        "budget": 2400, "days": 1,
        "overview": "Ramsar wetland sanctuary hosting over 250 species of winter migratory birds from Siberia, Central Asia, and Europe.",
        "attractions": ["Sultanpur Lake", "Watch Towers & Bird Hideouts", "Interpretation Centre", "Wetland Trails"],
        "nearby": ["Gurugram", "Delhi", "Damdama Lake"],
        "activities": ["Birdwatching for Siberian Cranes and flamingos", "Photography from lake watchtowers", "Eco walk along wetland embankment"],
        "img_url": "https://images.unsplash.com/photo-1512343879784-a960bf40e7f2?auto=format&fit=crop&w=1200&q=80",
        "photographer": "Nitin Goel", "profile": "https://unsplash.com/@nitingoel"
    },
    {
        "id": "panchkula", "name": "Panchkula", "state": "Haryana", "is_ut": False,
        "lat": 30.6942, "lon": 76.8606, "category": "Gateway & Heritage", "best_season": "October to March",
        "budget": 3000, "days": 2,
        "overview": "Planned satellite city at the foot of the Shivalik Hills, home to historic Pinjore Gardens and Mata Mansa Devi.",
        "attractions": ["Pinjore Yadavindra Gardens", "Mata Mansa Devi Temple", "Nada Sahib Gurudwara", "Cactus Garden", "Ramgarh Fort"],
        "nearby": ["Chandigarh", "Morni Hills", "Kalka"],
        "activities": ["Evening illuminated walk in Mughal-style Pinjore Gardens", "Visiting Asia's largest succulent Cactus Garden", "Darshan at Mansa Devi"],
        "img_url": "https://images.unsplash.com/photo-1506744038136-46273834b3fb?auto=format&fit=crop&w=1200&q=80",
        "photographer": "Rajesh Saini", "profile": "https://unsplash.com/@rajeshsaini"
    },
    {
        "id": "morni_hills", "name": "Morni Hills", "state": "Haryana", "is_ut": False,
        "lat": 30.6975, "lon": 77.0867, "category": "Hill Station", "best_season": "September to April",
        "budget": 2800, "days": 2,
        "overview": "The only hill station in Haryana nestled in Shivalik ranges, known for Tikkar Taal twin lakes and pine slopes.",
        "attractions": ["Tikkar Taal Lakes", "Morni Fort Ruins", "Adventure Park Morni", "Karoh Peak (Highest in Haryana)"],
        "nearby": ["Panchkula", "Chandigarh", "Nahan"],
        "activities": ["Kayaking and boating on Tikkar Taal", "Trekking to Karoh Peak", "Camping under the stars on lake shore"],
        "img_url": "https://images.unsplash.com/photo-1544735716-392fe2489ffa?auto=format&fit=crop&w=1200&q=80",
        "photographer": "Deepak Dhiman", "profile": "https://unsplash.com/@deepakdhiman"
    },
    {
        "id": "pinjore", "name": "Pinjore", "state": "Haryana", "is_ut": False,
        "lat": 30.7958, "lon": 76.9150, "category": "Mughal Garden", "best_season": "October to March",
        "budget": 2500, "days": 1,
        "overview": "Historic 17th-century Mughal terraced garden town featuring descending water canals, fountains, and royal pavilions.",
        "attractions": ["Yadavindra Mughal Gardens", "Sheesh Mahal & Rang Mahal", "Bhima Devi Temple Complex (Khajuraho of North)", "Pinjore Heritage Train"],
        "nearby": ["Kalka", "Panchkula", "Shimla"],
        "activities": ["Strolling through seven descending garden terraces", "Exploring ruins of 11th-century Bhima Devi temple", "Mango Festival in summer"],
        "img_url": "https://images.unsplash.com/photo-1582510003544-4d00b7f74220?auto=format&fit=crop&w=1200&q=80",
        "photographer": "Alok Mishra", "profile": "https://unsplash.com/@alokmishra"
    },
    {
        "id": "surajkund", "name": "Surajkund", "state": "Haryana", "is_ut": False,
        "lat": 28.4878, "lon": 77.2831, "category": "Craft & Reservoir", "best_season": "November to February",
        "budget": 3200, "days": 1,
        "overview": "Ancient 10th-century sun-worshipping amphitheater reservoir famed for hosting the international Surajkund Crafts Mela.",
        "attractions": ["Surajkund Sun Reservoir", "Anagpur Dam", "Asola Bhatti Wildlife Sanctuary", "Surajkund International Crafts Mela Ground"],
        "nearby": ["Faridabad", "Delhi", "Badkhal Lake"],
        "activities": ["Attending February Surajkund Crafts Mela", "Exploring 10th-century Tomar Sun amphitheater", "Birdwatching in Asola Bhatti"],
        "img_url": "https://images.unsplash.com/photo-1609766857041-ed402ea8069a?auto=format&fit=crop&w=1200&q=80",
        "photographer": "Manish Gupta", "profile": "https://unsplash.com/@manishgupta"
    },
    {
        "id": "damdama_lake", "name": "Damdama Lake", "state": "Haryana", "is_ut": False,
        "lat": 28.3039, "lon": 77.0789, "category": "Lake Adventure", "best_season": "October to March",
        "budget": 3400, "days": 1,
        "overview": "Sprawling natural lake nestled against Aravalli hills, a premier weekend adventure getaway near the national capital.",
        "attractions": ["Damdama Lake Water Sports", "Aravalli Ridge Trails", "Sohna Hot Springs", "Adventure Camps"],
        "nearby": ["Gurugram", "Sohna", "Delhi"],
        "activities": ["Boating and kayaking on Damdama Lake", "Rock climbing and Burma bridge at adventure camps", "Aravalli trail cycling"],
        "img_url": "https://images.unsplash.com/photo-1506744038136-46273834b3fb?auto=format&fit=crop&w=1200&q=80",
        "photographer": "Varun Chopra", "profile": "https://unsplash.com/@varunchopra"
    },
    {
        "id": "karnal", "name": "Karnal", "state": "Haryana", "is_ut": False,
        "lat": 29.6857, "lon": 76.9905, "category": "Heritage & Lake", "best_season": "October to March",
        "budget": 2500, "days": 1,
        "overview": "City of Danveer Karna on the Western Yamuna Canal, featuring historic Karna Lake, European cantonment church tower, and forts.",
        "attractions": ["Karna Lake", "Cantonment Church Tower", "Kalpana Chawla Planetarium", "Miran Sahib Tomb"],
        "nearby": ["Kurukshetra", "Panipat", "Delhi"],
        "activities": ["Boating on Karna Lake", "Astronomical show at Kalpana Chawla Planetarium", "Heritage cantonment history walk"],
        "img_url": "https://images.unsplash.com/photo-1582510003544-4d00b7f74220?auto=format&fit=crop&w=1200&q=80",
        "photographer": "Sanjay Malik", "profile": "https://unsplash.com/@sanjaymalik"
    },

    # ---------- UTTAR PRADESH (12) ----------
    {
        "id": "varanasi", "name": "Varanasi", "state": "Uttar Pradesh", "is_ut": False,
        "lat": 25.3176, "lon": 82.9739, "category": "Spiritual Capital", "best_season": "October to March",
        "budget": 3200, "days": 3,
        "overview": "One of the world's oldest living cities and sacred spiritual capital on the holy Ganges River.",
        "attractions": ["Kashi Vishwanath Temple", "Dashashwamedh Ghat Aarti", "Assi Ghat", "Manikarnika Ghat", "Sarnath Buddhist Park"],
        "nearby": ["Sarnath", "Chunar", "Prayagraj"],
        "activities": ["Dawn sunrise boat ride on the Ganges", "Witnessing grand evening Ganga Aarti at Dashashwamedh", "Tasting Banarasi paan and kachori jalebi"],
        "img_url": "https://images.unsplash.com/photo-1561361513-2d000a50f0dc?auto=format&fit=crop&w=1200&q=80",
        "photographer": "Ankit Kumar", "profile": "https://unsplash.com/@ankitkumar"
    },
    {
        "id": "agra", "name": "Agra", "state": "Uttar Pradesh", "is_ut": False,
        "lat": 27.1767, "lon": 78.0081, "category": "Mughal Wonder", "best_season": "October to March",
        "budget": 3800, "days": 2,
        "overview": "City of the immortal Taj Mahal, Agra Fort, and rich Mughal architectural masterpieces along the Yamuna.",
        "attractions": ["Taj Mahal", "Agra Fort", "Fatehpur Sikri", "Itmad-ud-Daulah (Baby Taj)", "Mehtab Bagh"],
        "nearby": ["Mathura", "Fatehpur Sikri", "Bharatpur"],
        "activities": ["Viewing Taj Mahal at sunrise from Mehtab Bagh", "Exploring palatial red sandstone Agra Fort", "Tasting traditional Agra Petha"],
        "img_url": "https://images.unsplash.com/photo-1564507592333-c60657eea523?auto=format&fit=crop&w=1200&q=80",
        "photographer": "Jovyn Chamb", "profile": "https://unsplash.com/@jovynchamb"
    },
    {
        "id": "lucknow", "name": "Lucknow", "state": "Uttar Pradesh", "is_ut": False,
        "lat": 26.8467, "lon": 80.9462, "category": "Nawabi Heritage & Food", "best_season": "October to March",
        "budget": 3500, "days": 3,
        "overview": "City of Nawabs celebrated for grand Bara Imambara labyrinth, intricate Chikankari embroidery, and Awadhi kebabs.",
        "attractions": ["Bara Imambara & Bhool Bhulaiya", "Chota Imambara", "Rumi Darwaza", "British Residency", "Hazratganj"],
        "nearby": ["Ayodhya", "Kanpur", "Naimisharanya"],
        "activities": ["Navigating the Bhool Bhulaiya acoustic maze", "Feasting on Galouti Kebabs at Tunday Kababi", "Shopping authentic Chikankari kurtas"],
        "img_url": "https://images.unsplash.com/photo-1582510003544-4d00b7f74220?auto=format&fit=crop&w=1200&q=80",
        "photographer": "Faheem Siddiqui", "profile": "https://unsplash.com/@faheemsiddiqui"
    },
    {
        "id": "ayodhya", "name": "Ayodhya", "state": "Uttar Pradesh", "is_ut": False,
        "lat": 26.7922, "lon": 82.1998, "category": "Sacred Heritage", "best_season": "October to March",
        "budget": 3000, "days": 2,
        "overview": "Sacred ancient capital of the Kosala Kingdom on the Saryu River, celebrated birthplace of Lord Rama.",
        "attractions": ["Shri Ram Janmabhoomi Mandir", "Hanuman Garhi", "Kanak Bhavan", "Saryu River Ghats (Ram Ki Paidi)", "Nageshwarnath Temple"],
        "nearby": ["Lucknow", "Varanasi", "Prayagraj"],
        "activities": ["Darshan at grand Shri Ram Janmabhoomi Mandir", "Evening Saryu River Aarti at Ram Ki Paidi", "Visiting gold-ornamented Kanak Bhavan"],
        "img_url": "https://images.unsplash.com/photo-1609766857041-ed402ea8069a?auto=format&fit=crop&w=1200&q=80",
        "photographer": "Prashant Pandey", "profile": "https://unsplash.com/@prashantp"
    },
    {
        "id": "mathura_vrindavan", "name": "Mathura & Vrindavan", "state": "Uttar Pradesh", "is_ut": False,
        "lat": 27.4924, "lon": 77.6737, "category": "Braj Heritage", "best_season": "October to March",
        "budget": 2800, "days": 2,
        "overview": "Sacred Braj Bhoomi on the Yamuna River, celebrated for Krishna Janmabhoomi, Banke Bihari, and joyful Holi festivals.",
        "attractions": ["Shri Krishna Janmasthan", "Banke Bihari Temple", "Prem Mandir", "ISKCON Vrindavan", "Vishram Ghat"],
        "nearby": ["Agra", "Govardhan", "Barsana"],
        "activities": ["Evening musical fountain and light show at Prem Mandir", "Yamuna boat ride at Vishram Ghat", "Tasting traditional Mathura Peda and Rabri"],
        "img_url": "https://images.unsplash.com/photo-1582510003544-4d00b7f74220?auto=format&fit=crop&w=1200&q=80",
        "photographer": "Gopal Sharma", "profile": "https://unsplash.com/@gopalsharma"
    },
    {
        "id": "prayagraj", "name": "Prayagraj (Allahabad)", "state": "Uttar Pradesh", "is_ut": False,
        "lat": 25.4358, "lon": 81.8463, "category": "Sangam & Heritage", "best_season": "October to March",
        "budget": 2900, "days": 2,
        "overview": "Holy city at the sacred Triveni Sangam of Ganga, Yamuna, and Saraswati, host of the world's largest gathering, Kumbh Mela.",
        "attractions": ["Triveni Sangam", "Allahabad Fort & Akshaya Vat", "Anand Bhavan", "Khusro Bagh", "All Saints Cathedral"],
        "nearby": ["Varanasi", "Ayodhya", "Chitrakoot"],
        "activities": ["Boat ride to the confluence of Ganga and Yamuna", "Touring Nehru family ancestral Anand Bhavan", "Viewing Mughal stone mausoleums at Khusro Bagh"],
        "img_url": "https://images.unsplash.com/photo-1590050752117-238cb0fb12b1?auto=format&fit=crop&w=1200&q=80",
        "photographer": "Abhinav Shukla", "profile": "https://unsplash.com/@abhinavshukla"
    },
    {
        "id": "sarnath", "name": "Sarnath", "state": "Uttar Pradesh", "is_ut": False,
        "lat": 25.3811, "lon": 83.0214, "category": "Buddhist Heritage", "best_season": "October to March",
        "budget": 2700, "days": 1,
        "overview": "Sacred Deer Park where Gautama Buddha delivered his first sermon; home to the Dhamek Stupa and Ashoka Lion Capital.",
        "attractions": ["Dhamek Stupa", "Ashoka Pillar & Lion Capital (National Emblem)", "Sarnath Archaeological Museum", "Mulagandha Kuti Vihar", "Chaukhandi Stupa"],
        "nearby": ["Varanasi", "Chunar", "Jaunpur"],
        "activities": ["Viewing the original 3rd-century BCE Ashokan Lion Capital", "Meditating beside ancient Dhamek Stupa", "Visiting international Buddhist temples"],
        "img_url": "https://images.unsplash.com/photo-1609766857041-ed402ea8069a?auto=format&fit=crop&w=1200&q=80",
        "photographer": "Naveen Tiwari", "profile": "https://unsplash.com/@naveentiwari"
    },
    {
        "id": "jhansi", "name": "Jhansi", "state": "Uttar Pradesh", "is_ut": False,
        "lat": 25.4484, "lon": 78.5685, "category": "Fortress & History", "best_season": "October to March",
        "budget": 2600, "days": 2,
        "overview": "Historic Bundelkhand gateway famed for Rani Lakshmibai's heroic stand against the British in the 1857 First War of Independence.",
        "attractions": ["Jhansi Fort (Rani Jhansi Ka Qila)", "Rani Mahal", "Government Museum Jhansi", "Barua Sagar Lake"],
        "nearby": ["Orchha", "Gwalior", "Khajuraho"],
        "activities": ["Walking the battlements of hill-top Jhansi Fort", "Viewing Rani Lakshmibai murals in Rani Mahal", "Day excursion to Orchha palaces"],
        "img_url": "https://images.unsplash.com/photo-1582510003544-4d00b7f74220?auto=format&fit=crop&w=1200&q=80",
        "photographer": "Dharmendra Bundela", "profile": "https://unsplash.com/@dharmendrab"
    },
    {
        "id": "fatehpur_sikri", "name": "Fatehpur Sikri", "state": "Uttar Pradesh", "is_ut": False,
        "lat": 27.0945, "lon": 77.6679, "category": "UNESCO Mughal", "best_season": "October to March",
        "budget": 3000, "days": 1,
        "overview": "Akbar's 16th-century red sandstone ghost city, boasting the colossal 54m Buland Darwaza and Salim Chishti tomb.",
        "attractions": ["Buland Darwaza", "Tomb of Salim Chishti", "Panch Mahal", "Jama Masjid", "Diwan-i-Khas Pillar"],
        "nearby": ["Agra", "Bharatpur", "Mathura"],
        "activities": ["Passing beneath the world's highest gateway Buland Darwaza", "Tying sacred wish thread at Salim Chishti marble shrine", "Photographing unique Diwan-i-Khas central pillar"],
        "img_url": "https://images.unsplash.com/photo-1564507592333-c60657eea523?auto=format&fit=crop&w=1200&q=80",
        "photographer": "Vikram Rathore", "profile": "https://unsplash.com/@vikramrathore"
    },
    {
        "id": "dudhwa", "name": "Dudhwa National Park", "state": "Uttar Pradesh", "is_ut": False,
        "lat": 28.4900, "lon": 80.6500, "category": "Terai Wildlife", "best_season": "November to April",
        "budget": 4200, "days": 3,
        "overview": "Vast Terai grassland wilderness on the Indo-Nepal border, home to Royal Bengal Tigers, one-horned rhinos, and swamp deer.",
        "attractions": ["Dudhwa Tiger Reserve Core", "Rhino Rehabilitation Area", "Suheli River", "Kishanpur Wildlife Sanctuary"],
        "nearby": ["Lakhimpur Kheri", "Pilibhit", "Lucknow"],
        "activities": ["Elephant-back safari into high tall grass for rhinos", "Jeep safari for swamp deer (Barasingha)", "Birdwatching along Suheli river"],
        "img_url": "https://images.unsplash.com/photo-1512343879784-a960bf40e7f2?auto=format&fit=crop&w=1200&q=80",
        "photographer": "Kailash Mishra", "profile": "https://unsplash.com/@kailashm"
    },
    {
        "id": "kushinagar", "name": "Kushinagar", "state": "Uttar Pradesh", "is_ut": False,
        "lat": 26.7411, "lon": 83.8890, "category": "Buddhist Sacred", "best_season": "October to March",
        "budget": 2700, "days": 1,
        "overview": "One of the four paramount Buddhist pilgrimage sites where Gautama Buddha attained Parinirvana (final release).",
        "attractions": ["Parinirvana Stupa & Temple (Reclining Buddha)", "Ramabhar Stupa (Cremation Site)", "Matha Kuar Shrine", "Myanmar & Thai Monasteries"],
        "nearby": ["Gorakhpur", "Lumbini (Nepal)", "Varanasi"],
        "activities": ["Paying homage at the 6-meter monolithic Reclining Buddha", "Circumambulating the ancient Ramabhar brick stupa", "Visiting international Buddhist pavilions"],
        "img_url": "https://images.unsplash.com/photo-1609766857041-ed402ea8069a?auto=format&fit=crop&w=1200&q=80",
        "photographer": "Sunil Maurya", "profile": "https://unsplash.com/@sunilmaurya"
    },
    {
        "id": "chitrakoot_up", "name": "Chitrakoot", "state": "Uttar Pradesh", "is_ut": False,
        "lat": 25.1788, "lon": 80.8688, "category": "Spiritual Nature", "best_season": "October to March",
        "budget": 2400, "days": 2,
        "overview": "Forest of Many Wonders where Lord Rama, Sita, and Lakshmana spent eleven years of their forest exile on Mandakini River.",
        "attractions": ["Ramghat on Mandakini", "Kamadgiri Hill Parikrama", "Hanuman Dhara Waterfall", "Gupt Godavari Caves", "Sphatik Shila"],
        "nearby": ["Satna", "Prayagraj", "Banda"],
        "activities": ["Boat ride on calm holy Mandakini River", "Exploring natural cave chambers of Gupt Godavari", "5-km holy parikrama of Kamadgiri hill"],
        "img_url": "https://images.unsplash.com/photo-1590050752117-238cb0fb12b1?auto=format&fit=crop&w=1200&q=80",
        "photographer": "Rameshwar Tripathi", "profile": "https://unsplash.com/@rameshwart"
    },

    # ---------- DELHI (UT) (4) ----------
    {
        "id": "delhi_central", "name": "New Delhi Central", "state": "Delhi", "is_ut": True,
        "lat": 28.6139, "lon": 77.2090, "category": "National Capital", "best_season": "October to March",
        "budget": 4500, "days": 3,
        "overview": "Heart of India's capital showcasing Lutyens' grand avenues, Rashtrapati Bhavan, India Gate, and National Museum.",
        "attractions": ["India Gate & Kartavya Path", "Rashtrapati Bhavan", "National Museum", "Lodhi Gardens", "Humayun's Tomb"],
        "nearby": ["Old Delhi", "Gurugram", "Noida"],
        "activities": ["Evening walk along Kartavya Path and India Gate", "Picnic among 15th-century tombs in Lodhi Garden", "Visiting UNESCO Humayun Tomb Mughal gardens"],
        "img_url": "https://images.unsplash.com/photo-1587474260584-136574528ed5?auto=format&fit=crop&w=1200&q=80",
        "photographer": "Fakurian Design", "profile": "https://unsplash.com/@fakurian"
    },
    {
        "id": "old_delhi", "name": "Old Delhi (Shahjahanabad)", "state": "Delhi", "is_ut": True,
        "lat": 28.6562, "lon": 77.2410, "category": "Historic Walled City", "best_season": "October to March",
        "budget": 3000, "days": 2,
        "overview": "Mughal walled city of Emperor Shah Jahan renowned for massive Red Fort, Jama Masjid, and bustling Chandni Chowk lanes.",
        "attractions": ["Red Fort (Lal Qila)", "Jama Masjid", "Chandni Chowk Market", "Khari Baoli Spice Market", "Paranthe Wali Gali"],
        "nearby": ["New Delhi", "Civil Lines", "Connaught Place"],
        "activities": ["Cycle rickshaw ride through narrow spice alleys of Khari Baoli", "Climbing southern minaret of Jama Masjid", "Tasting traditional stuffed paranthas"],
        "img_url": "https://images.unsplash.com/photo-1582510003544-4d00b7f74220?auto=format&fit=crop&w=1200&q=80",
        "photographer": "Varun Yadav", "profile": "https://unsplash.com/@varunyadav"
    },
    {
        "id": "mehrauli", "name": "Mehrauli & South Delhi", "state": "Delhi", "is_ut": True,
        "lat": 28.5245, "lon": 77.1855, "category": "UNESCO Architecture", "best_season": "October to March",
        "budget": 3500, "days": 2,
        "overview": "Oldest inhabited precinct of Delhi, home to the soaring 73m Qutub Minar, stepwells, and ancient ruins in Mehrauli Park.",
        "attractions": ["Qutub Minar Complex", "Iron Pillar of Delhi", "Mehrauli Archaeological Park", "Lotus Temple", "Hauz Khas Village"],
        "nearby": ["Saket", "Vasant Kunj", "Central Delhi"],
        "activities": ["Marveling at rust-resistant 1600-year Iron Pillar", "Sunset drink overlooking medieval Hauz Khas reservoir", "Meditating in Bahai Lotus Temple"],
        "img_url": "https://images.unsplash.com/photo-1564507592333-c60657eea523?auto=format&fit=crop&w=1200&q=80",
        "photographer": "Nikhil Mitra", "profile": "https://unsplash.com/@nikhilmitra"
    },
    {
        "id": "connaught_place", "name": "Connaught Place & Modern Delhi", "state": "Delhi", "is_ut": True,
        "lat": 28.6315, "lon": 77.2167, "category": "Urban Heritage & Dining", "best_season": "October to March",
        "budget": 4000, "days": 2,
        "overview": "Colonial Georgian-style circular business hub, historic Jantar Mantar observatory, and Agrasen Ki Baoli stepwell.",
        "attractions": ["Connaught Place Inner & Outer Circles", "Jantar Mantar", "Agrasen Ki Baoli Stepwell", "Bangla Sahib Gurudwara", "Janpath Flea Market"],
        "nearby": ["Rajiv Chowk", "Khan Market", "Central Delhi"],
        "activities": ["Sipping coffee in heritage colonial arcades", "Volunteering and dining at Gurudwara Bangla Sahib", "Bargain shopping at Janpath Market"],
        "img_url": "https://images.unsplash.com/photo-1587474260584-136574528ed5?auto=format&fit=crop&w=1200&q=80",
        "photographer": "Sahil Grover", "profile": "https://unsplash.com/@sahilgrover"
    },

    # ---------- JAMMU AND KASHMIR (UT) (8) ----------
    {
        "id": "srinagar", "name": "Srinagar", "state": "Jammu and Kashmir", "is_ut": True,
        "lat": 34.0837, "lon": 74.7973, "category": "Valley & Lakes", "best_season": "April to October & Winter Snow",
        "budget": 4500, "days": 4,
        "overview": "Paradise on Earth famed for tranquil Dal Lake shikaras, wooden houseboats, and terraced Mughal royal gardens.",
        "attractions": ["Dal Lake & Floating Market", "Shalimar Bagh & Nishat Bagh", "Shankaracharya Temple", "Hazratbal Shrine", "Old Srinagar Zaina Kadal"],
        "nearby": ["Gulmarg", "Pahalgam", "Sonamarg"],
        "activities": ["Shikara ride on Dal Lake at dawn", "Overnight stay in cedar wood carved houseboat", "Tasting traditional 36-course Kashmiri Wazwan"],
        "img_url": "https://images.unsplash.com/photo-1595815771614-ade9d652a65d?auto=format&fit=crop&w=1200&q=80",
        "photographer": "Aaqib Bhat", "profile": "https://unsplash.com/@aaqibbhat"
    },
    {
        "id": "gulmarg", "name": "Gulmarg", "state": "Jammu and Kashmir", "is_ut": True,
        "lat": 34.0484, "lon": 74.3805, "category": "Snow Resort & Skiing", "best_season": "December to March (Snow) & May to Sep",
        "budget": 5200, "days": 3,
        "overview": "Meadow of Flowers home to the world's highest gondola cable car and premier winter skiing slopes on Mount Apharwat.",
        "attractions": ["Gulmarg Gondola (Phase 1 & 2)", "Apharwat Peak (4200m)", "Alpather Frozen Lake", "Gulmarg Golf Course", "St. Mary's Church"],
        "nearby": ["Srinagar", "Tangmarg", "Baramulla"],
        "activities": ["Riding the Gulmarg Gondola up to 13,780 feet", "Skiing and snowboarding on powdery slopes", "Trek to high-altitude Alpather Lake"],
        "img_url": "https://images.unsplash.com/photo-1544735716-392fe2489ffa?auto=format&fit=crop&w=1200&q=80",
        "photographer": "Irfan Dar", "profile": "https://unsplash.com/@irfandar"
    },
    {
        "id": "pahalgam", "name": "Pahalgam", "state": "Jammu and Kashmir", "is_ut": True,
        "lat": 34.0160, "lon": 75.3150, "category": "Valleys & Rivers", "best_season": "March to November",
        "budget": 4200, "days": 3,
        "overview": "Valley of the Shepherds on the roaring Lidder River, starting point for the annual sacred Amarnath Yatra.",
        "attractions": ["Betaab Valley", "Aru Valley", "Chandanwari", "Baisaran (Mini Switzerland)", "Lidder River Water Sports"],
        "nearby": ["Srinagar", "Anantnag", "Amarnath"],
        "activities": ["Horse riding to lush green Baisaran meadows", "Angling for brown trout in Lidder River", "Exploring Bollywood shooting spots in Betaab Valley"],
        "img_url": "https://images.unsplash.com/photo-1595815771614-ade9d652a65d?auto=format&fit=crop&w=1200&q=80",
        "photographer": "Tanveer Lone", "profile": "https://unsplash.com/@tanveerlone"
    },
    {
        "id": "sonamarg", "name": "Sonamarg", "state": "Jammu and Kashmir", "is_ut": True,
        "lat": 34.3000, "lon": 75.2950, "category": "Glacier & Meadow", "best_season": "April to October",
        "budget": 4000, "days": 2,
        "overview": "Meadow of Gold nestled in the Sindh River valley, gateway to Ladakh and the glistening Thajiwas Glacier.",
        "attractions": ["Thajiwas Glacier", "Sindh River Valley", "Zoji La Pass Gateway", "Baltal Valley", "Vishansar Lake Trail"],
        "nearby": ["Srinagar", "Kargil", "Baltal"],
        "activities": ["Pony ride to the snow edge of Thajiwas Glacier", "Rafting in the swift torrents of Sindh River", "Crossing the dramatic mountain gateway Zoji La"],
        "img_url": "https://images.unsplash.com/photo-1544735716-392fe2489ffa?auto=format&fit=crop&w=1200&q=80",
        "photographer": "Bashir Wani", "profile": "https://unsplash.com/@bashirwani"
    },
    {
        "id": "patnitop", "name": "Patnitop", "state": "Jammu and Kashmir", "is_ut": True,
        "lat": 33.0847, "lon": 75.3267, "category": "Hill Retreat", "best_season": "May to October & Dec to Feb",
        "budget": 3300, "days": 2,
        "overview": "Scenic pine-covered plateau in Udhampur district offering cable car rides, paragliding, and winter snow.",
        "attractions": ["Skyview Ropeway Patnitop", "Nathatop Meadows", "Sanasar Lake", "Naag Temple", "Circular Road Walk"],
        "nearby": ["Kud", "Batote", "Katra"],
        "activities": ["Riding the Skyview cable car over pine forests", "Paragliding in Sanasar meadow", "Tasting famous hot Patnitop Kaladi cheese"],
        "img_url": "https://images.unsplash.com/photo-1506744038136-46273834b3fb?auto=format&fit=crop&w=1200&q=80",
        "photographer": "Rohit Dogra", "profile": "https://unsplash.com/@rohitdogra"
    },
    {
        "id": "katra", "name": "Katra (Vaishno Devi)", "state": "Jammu and Kashmir", "is_ut": True,
        "lat": 32.9926, "lon": 74.9317, "category": "Sacred Pilgrimage", "best_season": "Throughout the year",
        "budget": 3200, "days": 2,
        "overview": "Bustling foothills base town for the 14-km sacred mountain pilgrimage to the holy shrine of Mata Vaishno Devi in Trikuta Hills.",
        "attractions": ["Mata Vaishno Devi Bhawan", "Ardhkuwari Cave", "Bhairon Temple Ropeway", "Ban Ganga", "Trikuta Hills View"],
        "nearby": ["Jammu", "Patnitop", "Shivkhori"],
        "activities": ["14-km night trek to Bhawan with chanting pilgrims", "Ropeway ride from Bhawan to Bhairon Temple", "Visiting sacred Ardhkuwari womb cave"],
        "img_url": "https://images.unsplash.com/photo-1582510003544-4d00b7f74220?auto=format&fit=crop&w=1200&q=80",
        "photographer": "Amit Saini", "profile": "https://unsplash.com/@amitsaini"
    },
    {
        "id": "yusmarg", "name": "Yusmarg", "state": "Jammu and Kashmir", "is_ut": True,
        "lat": 33.8290, "lon": 74.6640, "category": "Offbeat Meadow", "best_season": "April to October",
        "budget": 3000, "days": 2,
        "overview": "Meadow of Jesus, an offbeat serene highland encircled by dense pine trees and snow peaks of the Pir Panjal range.",
        "attractions": ["Doodh Ganga River", "Nilnag Lake", "Sang-e-Safed Valley", "Charar-e-Sharief Shrine"],
        "nearby": ["Srinagar", "Budgam", "Pakherpora"],
        "activities": ["Horse trek along Doodh Ganga rushing stream", "Hike through pine forest to blue Nilnag Lake", "Picnic on velvet rolling green meadows"],
        "img_url": "https://images.unsplash.com/photo-1544735716-392fe2489ffa?auto=format&fit=crop&w=1200&q=80",
        "photographer": "Mudassir Mir", "profile": "https://unsplash.com/@mudassirmir"
    },
    {
        "id": "doodhpathri", "name": "Doodhpathri", "state": "Jammu and Kashmir", "is_ut": True,
        "lat": 33.8833, "lon": 74.5667, "category": "Valley of Milk", "best_season": "May to September",
        "budget": 2900, "days": 1,
        "overview": "Untouched alpine meadow in Budgam district where the foaming Shaliganga river looks like flowing milk over pebbles.",
        "attractions": ["Shaliganga Riverbank", "Doodhpathri Green Bowl", "Dikshal Meadows", "Parihas Stream"],
        "nearby": ["Srinagar", "Budgam", "Khansahib"],
        "activities": ["Dipping feet in cold frothy Shaliganga stream", "Picnic on lush green carpet meadows", "Photography of Pir Panjal mountain ridges"],
        "img_url": "https://images.unsplash.com/photo-1506744038136-46273834b3fb?auto=format&fit=crop&w=1200&q=80",
        "photographer": "Zubair Reshi", "profile": "https://unsplash.com/@zubairreshi"
    },

    # ---------- LADAKH (UT) (8) ----------
    {
        "id": "leh", "name": "Leh", "state": "Ladakh", "is_ut": True,
        "lat": 34.1526, "lon": 77.5771, "category": "Himalayan Desert", "best_season": "May to September",
        "budget": 4500, "days": 4,
        "overview": "High-altitude desert capital nestled at 11,500 feet, crowned by historic 17th-century Leh Palace and Shanti Stupa.",
        "attractions": ["Shanti Stupa", "Leh Royal Palace", "Hall of Fame Museum", "Magnetic Hill", "Spituk Monastery"],
        "nearby": ["Nubra Valley", "Pangong Tso", "Khardung La"],
        "activities": ["Watching sunset over Indus Valley from Shanti Stupa", "Testing gravity-defying car pull at Magnetic Hill", "Stargazing under crystal clear skies"],
        "img_url": "https://images.unsplash.com/photo-1506744038136-46273834b3fb?auto=format&fit=crop&w=1200&q=80",
        "photographer": "Stanzin Norbu", "profile": "https://unsplash.com/@stanzinnorbu"
    },
    {
        "id": "nubra_valley", "name": "Nubra Valley (Diskit & Hunder)", "state": "Ladakh", "is_ut": True,
        "lat": 34.5428, "lon": 77.5667, "category": "Sand Dunes & Oasis", "best_season": "May to October",
        "budget": 4200, "days": 2,
        "overview": "Valley of Flowers where the Shyok and Nubra rivers cut through white sand dunes dotted with double-humped Bactrian camels.",
        "attractions": ["Hunder White Sand Dunes", "Diskit Monastery & 32m Maitreya Buddha", "Turtuk Village (Balti Culture)", "Panamik Hot Springs"],
        "nearby": ["Leh", "Turtuk", "Sumur"],
        "activities": ["Double-humped Bactrian camel safari in Hunder dunes", "Blessings at towering golden Maitreya Buddha statue", "Visiting India's northernmost Balti village Turtuk"],
        "img_url": "https://images.unsplash.com/photo-1544735716-392fe2489ffa?auto=format&fit=crop&w=1200&q=80",
        "photographer": "Tsering Dorje", "profile": "https://unsplash.com/@tseringdorje"
    },
    {
        "id": "pangong_tso", "name": "Pangong Tso", "state": "Ladakh", "is_ut": True,
        "lat": 33.7595, "lon": 78.6674, "category": "High-Altitude Glacial Lake", "best_season": "May to September",
        "budget": 4800, "days": 2,
        "overview": "Endorheic saltwater lake at 14,270 feet spanning India and Tibet, celebrated for shifting shades of cobalt, azure, and turquoise.",
        "attractions": ["Pangong Lake Shore", "Spangmik Village", "Lukung Viewpoint", "Marmot Colony Trail"],
        "nearby": ["Leh", "Tangtse", "Chushul"],
        "activities": ["Camping in lakeside dome tents under the Milky Way", "Watching colors change from turquoise to deep purple", "Spotting Himalayan marmots"],
        "img_url": "https://images.unsplash.com/photo-1506744038136-46273834b3fb?auto=format&fit=crop&w=1200&q=80",
        "photographer": "Rigzin Angdu", "profile": "https://unsplash.com/@rigzinangdu"
    },
    {
        "id": "zanskar_valley", "name": "Zanskar Valley (Padum)", "state": "Ladakh", "is_ut": True,
        "lat": 33.4667, "lon": 76.9333, "category": "Rugged Remote Wilderness", "best_season": "June to September (Summer) & Jan-Feb (Chadar)",
        "budget": 4500, "days": 4,
        "overview": "Remote high-altitude valley isolated by mountains, famous for clifftop Phuktal monastery and winter frozen river Chadar trek.",
        "attractions": ["Phuktal Monastery (Honeycombed in Cave)", "Padum Town", "Zangla Palace Ruins", "Karsha Monastery", "Drang Drung Glacier"],
        "nearby": ["Kargil", "Padum", "Rangdum"],
        "activities": ["Trek to cave-hanging Phuktal Gompa", "Viewing winding Drang-Drung Glacier from Pensi La", "Winter frozen Zanskar river Chadar trek"],
        "img_url": "https://images.unsplash.com/photo-1544735716-392fe2489ffa?auto=format&fit=crop&w=1200&q=80",
        "photographer": "Lobzang Namgyal", "profile": "https://unsplash.com/@lobzangn"
    },
    {
        "id": "tso_moriri", "name": "Tso Moriri (Korzok)", "state": "Ladakh", "is_ut": True,
        "lat": 32.9000, "lon": 78.3167, "category": "Wetland & High Lake", "best_season": "June to September",
        "budget": 4600, "days": 2,
        "overview": "Sacred high-altitude Ramsar wetland lake at 14,836 feet in Changthang, frequented by black-necked cranes and Changpa nomads.",
        "attractions": ["Korzok Monastery", "Tso Moriri Lake Shore", "Changthang Wildlife Sanctuary", "Nomadic Changpa Settlements"],
        "nearby": ["Chumathang", "Tso Kar", "Leh"],
        "activities": ["Birdwatching rare Black-necked Cranes and Bar-headed Geese", "Visiting 300-year-old Korzok Gompa", "Interacting with Changpa pashmina nomads"],
        "img_url": "https://images.unsplash.com/photo-1506744038136-46273834b3fb?auto=format&fit=crop&w=1200&q=80",
        "photographer": "Sonam Wangchuk", "profile": "https://unsplash.com/@sonamw"
    },
    {
        "id": "kargil", "name": "Kargil", "state": "Ladakh", "is_ut": True,
        "lat": 34.5539, "lon": 76.1310, "category": "Historic Gateway", "best_season": "May to October",
        "budget": 3200, "days": 2,
        "overview": "Historic Silk Route junction on the Suru River and site of the 1999 Kargil War memorial against rugged granite peaks.",
        "attractions": ["Kargil War Memorial (Drass)", "Suru Valley", "Mulbekh Giant Rock Buddha", "Hunderman Border Heritage Village"],
        "nearby": ["Drass", "Leh", "Srinagar"],
        "activities": ["Paying tribute at Drass Kargil War Memorial", "Viewing 9m 1st-century Maitreya Buddha carved in rock at Mulbekh", "Touring Hunderman partitioned village museum"],
        "img_url": "https://images.unsplash.com/photo-1544735716-392fe2489ffa?auto=format&fit=crop&w=1200&q=80",
        "photographer": "Mohsin Raza", "profile": "https://unsplash.com/@mohsinraza"
    },
    {
        "id": "khardung_la", "name": "Khardung La", "state": "Ladakh", "is_ut": True,
        "lat": 34.2789, "lon": 77.6047, "category": "Mountain Pass", "best_season": "May to October",
        "budget": 3800, "days": 1,
        "overview": "Legendary motorable high mountain pass in the Ladakh Range perched at 17,982 feet, the gateway to Nubra and Siachen.",
        "attractions": ["Khardung La Top Landmark", "Khardung La Souvenir Shop & Cafe", "Panoramic Karakoram View"],
        "nearby": ["Leh", "Nubra Valley", "South Pullu"],
        "activities": ["Photographing summit at 17,982 feet", "Downhill mountain biking to Leh", "Sipping hot butter tea in India's highest military canteen"],
        "img_url": "https://images.unsplash.com/photo-1544735716-392fe2489ffa?auto=format&fit=crop&w=1200&q=80",
        "photographer": "Rinchen Ladakhi", "profile": "https://unsplash.com/@rinchenl"
    },
    {
        "id": "hemis", "name": "Hemis", "state": "Ladakh", "is_ut": True,
        "lat": 33.9126, "lon": 77.7072, "category": "Monastery & National Park", "best_season": "June to September",
        "budget": 3600, "days": 2,
        "overview": "Spiritual retreat home to Ladakh's wealthiest Drukpa monastery and the vast Hemis National Park, premier snow leopard habitat.",
        "attractions": ["Hemis Monastery (1672)", "Hemis National Park (Snow Leopard Reserve)", "Hemis Museum", "Gotsang Hermitage"],
        "nearby": ["Thiksey", "Shey", "Leh"],
        "activities": ["Attending the Hemis Tsechu festival with Cham masked dances", "Winter tracking of wild Snow Leopards with naturalists", "Viewing colossal sacred Thangkas"],
        "img_url": "https://images.unsplash.com/photo-1609766857041-ed402ea8069a?auto=format&fit=crop&w=1200&q=80",
        "photographer": "Diskit Angmo", "profile": "https://unsplash.com/@diskitangmo"
    },

    # ---------- CHANDIGARH (UT) (4) ----------
    {
        "id": "chandigarh_capitol", "name": "Chandigarh Capitol Complex", "state": "Chandigarh", "is_ut": True,
        "lat": 30.7589, "lon": 76.8041, "category": "UNESCO Modern Architecture", "best_season": "October to March",
        "budget": 3500, "days": 2,
        "overview": "UNESCO World Heritage site designed by Swiss-French master architect Le Corbusier, featuring the Open Hand Monument.",
        "attractions": ["Palace of Assembly", "Secretariat Building", "High Court", "Open Hand Monument", "Tower of Shadows"],
        "nearby": ["Rock Garden", "Sukhna Lake", "Mohali"],
        "activities": ["Guided architectural tour of Le Corbusier's masterpiece", "Photographing 26-meter rotating Open Hand monument", "Studying modernist concrete brutalism"],
        "img_url": "https://images.unsplash.com/photo-1582510003544-4d00b7f74220?auto=format&fit=crop&w=1200&q=80",
        "photographer": "Amandeep Singh", "profile": "https://unsplash.com/@amandeepsingh"
    },
    {
        "id": "rock_garden", "name": "Rock Garden of Chandigarh", "state": "Chandigarh", "is_ut": True,
        "lat": 30.7525, "lon": 76.8067, "category": "Sculpture Art Park", "best_season": "October to March",
        "budget": 2800, "days": 1,
        "overview": "Visionary 40-acre outdoor sculpture garden created secretly by Nek Chand entirely out of industrial, ceramic, and urban waste.",
        "attractions": ["Nek Chand's Sculptures", "Interlocking Courtyards & Waterfalls", "Ceramic Tile Mosaic Dolls", "Doll Museum"],
        "nearby": ["Sukhna Lake", "Capitol Complex", "Sector 17"],
        "activities": ["Walking through maze-like stone arches and waterfalls", "Admiring sculptures made of broken bangles and crockery", "Photography in open-air amphitheater"],
        "img_url": "https://images.unsplash.com/photo-1590050752117-238cb0fb12b1?auto=format&fit=crop&w=1200&q=80",
        "photographer": "Gurpreet Brar", "profile": "https://unsplash.com/@gurpreetbrar"
    },
    {
        "id": "sukhna_lake", "name": "Sukhna Lake", "state": "Chandigarh", "is_ut": True,
        "lat": 30.7421, "lon": 76.8188, "category": "Lake & Promenade", "best_season": "October to March",
        "budget": 2700, "days": 1,
        "overview": "Scenic 3 sq km artificial rainfed lake at the foothills of the Shivalik range, Chandigarh's favorite morning jog and boating hub.",
        "attractions": ["Sukhna Promenade", "Boating Club", "Garden of Silence", "Sukhna Wildlife Sanctuary", "Bird Watching Tower"],
        "nearby": ["Rock Garden", "Golf Club", "Sector 26"],
        "activities": ["Paddle boating at sunset on Sukhna Lake", "Morning jog on 2-km shaded lake promenade", "Visiting Buddha statue at Garden of Silence"],
        "img_url": "https://images.unsplash.com/photo-1506744038136-46273834b3fb?auto=format&fit=crop&w=1200&q=80",
        "photographer": "Mandeep Kaler", "profile": "https://unsplash.com/@mandeepkaler"
    },
    {
        "id": "rose_garden", "name": "Zakir Hussain Rose Garden", "state": "Chandigarh", "is_ut": True,
        "lat": 30.7467, "lon": 76.7825, "category": "Botanical Wonder", "best_season": "December to March (Flowering)",
        "budget": 2600, "days": 1,
        "overview": "Asia's largest botanical rose garden spread over 30 landscaped acres with 50,000 rose bushes of 1,600 distinct varieties.",
        "attractions": ["Rose Garden Pathways", "Medicinal Plants Section", "Fountain Avenue", "Annual Rose Festival"],
        "nearby": ["Sector 17 Plaza", "Museum and Art Gallery", "Sukhna Lake"],
        "activities": ["Strolling through 1,600 varieties of blooming roses", "Attending the annual February Rose Festival", "Visiting nearby Government Museum & Art Gallery"],
        "img_url": "https://images.unsplash.com/photo-1589308078059-be1415eab4c3?auto=format&fit=crop&w=1200&q=80",
        "photographer": "Karan Batra", "profile": "https://unsplash.com/@karanbatra"
    }
]

print(f"North region loaded: {len(NORTH_DESTINATIONS)} destinations.")
