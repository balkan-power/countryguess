#Author: balkanpower
#Version: 1.0

import time
import random
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    print("Guess the country based on the facts!")
    time.sleep(5)
    clear_screen()
    print()
    print("Select the difficulty.")
    print("1. Easy")
    print("2. Medium")
    print("3. Hard")
    difficulty = int(input())

    if difficulty == 1:
        DifficultyList = 6
    elif difficulty == 2:
        DifficultyList = 4
    elif difficulty == 3:
        DifficultyList = 2
    else:
        print("No defined option given, defaulting to Hard.")
        time.sleep(5)
        DifficultyList = 2
    clear_screen()
    
    # country facts to select from
    CountryFacts = {
        "The United States of America": [
            "This country has a large and diverse population.",
            "This country is known for its diverse geography.",
            "This country has a lot of talented musicians and athletes.",
            "This country is well-known for a lot of fast food chains.",
            "This country is a global leader in technology and entertainment.",
            "This country is home to one of the most powerful militaries.",
            "This country has a long history of immigration.",
            "This country has multiple time zones.",
            "This country is famous for its pop culture.",
            "This country has had significant influence on global politics and economics.",
        ],

        "China": [
            "This country has the largest population in the world.",
            "This country is known for its history spanning millenia.",
            "This country has a rapidly growing economy.",
            "This country has significant global manufacturing output.",
            "This country is known for a rich cuisine with regional diversity.",
            "This country has a single-party political system.",
            "This country hosted the 2008 Summer Olympics.",
            "This country has unified and split up multiple times throughout history.",
            "This country invented paper, gunpowder, and the compass.",
            "This country has a strong tradition in martial arts and philosophy.",
        ],

        "Japan": [
            "This country is an island nation in East Asia.",
            "This country is known for its technology and innovation.",
            "This country has a unique traditional and pop culture mix.",
            "This country is famous for its unique food, animation, and warrior history.",
            "This country has a strong economy despite limited natural resources.",
            "This country is prone to earthquakes and tsunamis.",
            "This country has one of the highest life expectancies.",
            "This country uses 3 seperate writing systems for its language.",
            "This country has a long imperial history and a current emperor.",
            "This country has hosted the Olympic Games more than once.",
        ],

        "Germany": [
            "This country is in Central Europe and has a strong economy.",
            "This country is known for its engineering and car manufacturing.",
            "This country has a rich history, including two World Wars.",
            "This country is famous for beer, sausages, and pretzels.",
            "This country is a leader in the European Union.",
            "This country reunified in 1990 after decades of division.",
            "This country has cultural icons in piano history.",
            "This country is home to some famous car manufacturers.",
            "This country has a federal parliamentary republic system.",
            "This country places high value on environmental sustainability.",
        ],

        "Thailand": [
            "This country has never been colonized by a European power.",
            "This country has a deeply rooted tradition involving royalty.",
            "This country is home to a script with loops and curves.",
            "This country's cuisine is famous for its balance of sweet, sour, salty, and spicy.",
            "This country celebrates a major holiday involving water fights.",
            "This country has a city with one of the longest names in the world.",
            "This country has regions famous for lantern festivals.",
            "This country drives on the left side of the road.",
            "This country has many ornate temples and statues of a seated figure.",
            "This country has a rich history in martial arts.",
        ],

        "Bulgaria": [
            "This country uses a script developed by two brothers.",
            "This country is one of the oldest in Europe by name and territory.",
            "This country has a deep tradition of rose oil production.",
            "This country celebrates spring with red and white threads.",
            "This country has mountains, a Black Sea coast, and Roman ruins.",
            "This country was once a powerful medieval empire.",
            "This country has a cultural tradition involving fire-dancing.",
            "This country has a national yogurt strain considered unique.",
            "This country has a nodding custom that may confuse foreigners.",
            "This country once aligned with both East and West in different wars.",
        ],

        "Italy": [
            "This country has more UNESCO World Heritage Sites than any other.",
            "This country is shaped like a piece of footwear.",
            "This country is home to a city with canals instead of streets.",
            "This country was once the heart of a vast ancient empire.",
            "This country has strong regional identities and dialects.",
            "This country borders two independent enclaves.",
            "This country is famous for an event involving painted fast cars.",
            "This country has a long coastline and many islands.",
            "This country has a strong tradition of fashion and design.",
            "This country's cuisine has become globally popular in simplified form.",
        ],

        "France": [
            "This country has a hexagonal shape when seen on a map.",
            "This country has regions known for wine and cheese production.",
            "This country is home to the world’s most visited art museum.",
            "This country has overseas territories on multiple continents.",
            "This country played a key role in the Enlightenment and revolutions.",
            "This country uses one of the most globally spoken languages.",
            "This country has a global cultural influence in cuisine and fashion.",
            "This country has hosted the Olympics multiple times.",
            "This country once built a massive structure of iron as a world fair entrance.",
            "This country is associated with a notorious military leader of the 19th century.",
        ],

        "Brazil": [
            "This country is the largest in its region by area and population.",
            "This country speaks a language different from all its neighbors.",
            "This country has a massive statue overlooking a coastal city.",
            "This country contains the majority of a massive rainforest.",
            "This country has won more international sports titles than most others.",
            "This country celebrates a massive, colorful festival annually.",
            "This country has regions known for Afro-descendant cultural traditions.",
            "This country’s music includes rhythms like samba and bossa nova.",
            "This country has a capital city that was built from scratch.",
            "This country has hosted both the Olympics and the World Cup.",
        ],

        "Spain": [
            "This country has several regional languages besides the main one.",
            "This country is famous for an event involving bulls and running.",
            "This country has islands in both the Atlantic and Mediterranean.",
            "This country had a long civil conflict in the 20th century.",
            "This country has architecture by a man who left a church unfinished.",
            "This country has multiple autonomous communities.",
            "This country influenced much of the Americas culturally and linguistically.",
            "This country eats dinner later than most other countries.",
            "This country had a global empire that started in the 15th century.",
            "This country is associated with flamenco and siestas.",
        ],

        "Romania": [
            "This country has legends involving vampires and castles.",
            "This country is home to a large portion of a mountain range.",
            "This country has a Romance language not typically grouped with others.",
            "This country has a black sea coastline and a large delta.",
            "This country has regions with medieval Saxon villages.",
            "This country changed political systems after 1989 violently.",
            "This country is known for a gymnast who made history.",
            "This country shares borders with five other countries.",
            "This country has a palace that is one of the largest buildings in Europe.",
            "This country has traditional dances like the hora.",
        ],

        "Russia": [
            "This country spans across two continents.",
            "This country has many time zones within its borders.",
            "This country has a long history of revolutions, and reforms.",
            "This country is home to one of the coldest inhabited places on Earth.",
            "This country has a major influence on literature, ballet, and chess.",
            "This country developed its own space program during the Cold War.",
            "This country has both tundra and subtropical regions.",
            "This country’s alphabet differs from the Latin script.",
            "This country has cities that changed names several times in the 20th century.",
            "This country has a famous onion-domed cathedral in its capital.",
        ],

        "The United Kingdom": [
            "This country includes multiple nations under one government.",
            "This country has a globally influential music and cultural scene.",
            "This country has a long-standing monarchy.",
            "This country has hosted the Summer Olympics more than twice.",
            "This country once had the largest empire in history.",
            "This country drives on the left side of the road.",
            "This country has many accents despite its small size.",
            "This country has a legislative body housed in a clock-towered building.",
            "This country has a well-known dish involving fried fish and potatoes.",
            "This country left a political-economic union recently.",
        ],

        "Mexico": [
            "This country has both Pacific and Atlantic coastlines.",
            "This country has ancient ruins from several civilizations.",
            "This country celebrates a holiday involving decorated skulls.",
            "This country has a city that was built on a lake by its ancestors.",
            "This country is the birthplace of chocolate as we know it.",
            "This country’s cuisine includes corn, beans, and spicy peppers.",
            "This country has a vibrant muralist tradition.",
            "This country has had political changes involving revolution and reform.",
            "This country shares its northern border with a global power.",
            "This country’s flag features an eagle with a snake.",
        ],

        "Sweden": [
            "This country is known for its minimalist design and furniture exports.",
            "This country has a tradition of celebrating a holiday with candles worn on the head.",
            "This country has a monarchy but is also a parliamentary democracy.",
            "This country has a reputation for neutrality in international conflicts.",
            "This country is home to a famous ice hotel rebuilt annually.",
            "This country has a high percentage of land covered by forests.",
            "This country is known for a musical group that won Eurovision in the 1970s.",
            "This country has a tradition of taking coffee breaks called 'fika'.",
            "This country has a long coastline along the Baltic Sea.",
            "This country is known for a social welfare system with high taxes.",
        ],

        "Finland": [
            "This country has a high number of saunas per capita.",
            "This country has a tradition of wife-carrying competitions.",
            "This country is known for a strong education system and high literacy rates.",
            "This country has a word for drinking at home in your underwear.",
            "This country has a unique language unrelated to most of its neighbors.",
            "This country has a reputation for being the happiest in the world.",
            "This country has a high number of heavy metal bands per capita.",
            "This country has a tradition of giving new parents a baby box.",
            "This country has a 'day fine' system for traffic violations based on income.",
            "This country has a concept called 'sisu' representing stoic determination.",
        ],

        "Poland": [
            "This country has a city known for a historic salt mine with underground chapels.",
            "This country has a tradition of celebrating a holiday with water fights.",
            "This country has a language with a complex system of consonant clusters.",
            "This country has a history of partitions by neighboring powers.",
            "This country has a famous composer known for piano compositions.",
            "This country has a tradition of decorated Easter eggs called 'pisanki'.",
            "This country has a city with a medieval old town rebuilt after WWII.",
            "This country has a mountain range called the Tatras.",
            "This country has a tradition of serving beet soup called 'barszcz'.",
            "This country has a history of solidarity movements in the 1980s.",
        ],

        "Vietnam": [
            "This country has a cuisine known for a noodle soup with herbs and meat.",
            "This country has a history of resisting colonial powers.",
            "This country has a long coastline along the South China Sea.",
            "This country has a tradition of celebrating a lunar new year called 'Tet'.",
            "This country has a landscape featuring terraced rice fields.",
            "This country has a city formerly known as Saigon.",
            "This country has a famous tunnel system used during wartime.",
            "This country has a traditional dress called 'ao dai'.",
            "This country has a coffee culture with unique egg coffee.",
            "This country has a history of dynastic rule before colonization.",
        ],

        "South Africa": [
            "This country has three capital cities.",
            "This country is known for a significant transition from apartheid.",
            "This country has a diverse population with 11 official languages.",
            "This country has a famous table-shaped mountain.",
            "This country has a history of hosting a major international football tournament.",
            "This country has a significant gold and diamond mining industry.",
            "This country has a tradition of braai, a type of barbecue.",
            "This country has a notable wine-producing region.",
            "This country has a unique floral kingdom with high biodiversity.",
            "This country has a history of Nobel Peace Prize winners.",
        ],

        "Morocco": [
            "This country has a city known for its blue-painted buildings.",
            "This country has a cuisine featuring tagine and couscous.",
            "This country has a mountain range called the Atlas.",
            "This country has a tradition of mint tea served ceremonially.",
            "This country has a historic city with a famous square called Jemaa el-Fnaa.",
            "This country has a coastline along both the Atlantic Ocean and the Mediterranean Sea.",
            "This country has a desert region known for sand dunes.",
            "This country has a history of Berber, Arab, and French influences.",
            "This country has a city known for leather tanneries.",
            "This country has a tradition of intricate tilework called zellige.",
        ],

        "Australia": [
            "This country has a unique animal that carries its young in a pouch.",
            "This country has a natural landmark with a large sandstone monolith.",
            "This country has a famous opera house with a sail-like design.",
            "This country has a reef system visible from space.",
            "This country has a tradition of meat pies and Vegemite.",
            "This country is known for playing rugby.",
            "This country has a desert region known as the Outback.",
            "This country has a history of indigenous cultures dating back thousands of years.",
            "This country has a marsupial known for its hopping locomotion.",
            "This country has a popular beach culture with surfing.",
        ],

        "Cambodia": [
            "This country has a temple complex that appears on its national flag.",
            "This country has a history of a tragic regime in the 1970s.",
            "This country has a river that flows through its capital city.",
            "This country has a traditional dance with intricate hand movements.",
            "This country has a cuisine featuring fish amok and prahok.",
            "This country has a festival involving boat races.",
            "This country has a garment industry significant to its economy.",
            "This country has a tradition of silk weaving.",
            "This country has a city known for its French colonial architecture.",
            "This country has a significant production of cashew nuts.",
        ],

        "Mongolia": [
            "This country has a festival featuring wrestling, archery, and horse racing.",
            "This country has a history of a vast empire in the 13th century.",
            "This country has a traditional dwelling called a ger.",
            "This country has a landscape dominated by steppes and deserts.",
            "This country has a capital city known for its cold winters.",
            "This country has a tradition of throat singing.",
            "This country has a cuisine featuring meat and dairy products.",
            "This country has a history of nomadic herding.",
            "This country has a celebration of the lunar new year called Tsagaan Sar.",
            "This country has a growing interest in modern sports like breakdancing.",
        ],

        "Saudi Arabia": [
            "This country has a city considered the holiest in a major world religion.",
            "This country has a desert known as the Empty Quarter.",
            "This country has a tradition of serving coffee with dates.",
            "This country has a coastline along the Red Sea.",
            "This country has a history of Bedouin nomadic culture.",
            "This country has a monarchy with significant oil wealth.",
            "This country has a dress code influenced by religious practices.",
            "This country has a city known for a large clock tower.",
            "This country has a plan called Vision 2030 for economic diversification.",
            "This country has a tradition of camel racing.",
        ],

        "Syria": [
            "This country has ancient cities with continuous habitation.",
            "This country has a history of Roman and Byzantine ruins.",
            "This country has a cuisine featuring dishes like kibbeh and hummus.",
            "This country has a river that flows through its capital.",
            "This country has a history of diverse religious communities.",
            "This country has a traditional music with the oud instrument.",
            "This country has a history of French colonial influence.",
            "This country has a landscape including mountains and deserts.",
            "This country has a tradition of storytelling in coffeehouses.",
            "This country has been affected by a prolonged civil conflict.",
        ],

        "Israel": [
            "This country has a city sacred to multiple religions.",
            "This country has a desert region called the Negev.",
            "This country has a high-tech industry known as Silicon Wadi.",
            "This country has a holiday commemorating a miracle of oil.",
            "This country has a tradition of communal settlements called kibbutzim.",
            "This country has a cuisine influenced by Middle Eastern and Mediterranean flavors.",
            "This country has a national airline known for its security measures.",
            "This country has a mandatory military service for most citizens.",
            "This country has a parliament called the Knesset.",
            "This country has a significant population of immigrants from diverse backgrounds.",
        ],

        "Egypt": [
            "This country has ancient structures aligned with celestial bodies.",
            "This country has a river considered the lifeblood of its civilization.",
            "This country has a script involving pictorial symbols.",
            "This country has a tradition of preserving bodies for the afterlife.",
            "This country has a city known for a historic library.",
            "This country has a cuisine featuring dishes like koshari and ful medames.",
            "This country has a desert landscape with oases.",
            "This country has a history of pharaohs and dynasties.",
            "This country has a canal connecting two major seas.",
            "This country has a tradition of storytelling through shadow puppetry.",
        ],

        "Turkiye": [
            "This country spans two continents.",
            "This country has a city with two names historically recognized around the world.",
            "This country is known for its layered pastry desserts and strong coffee.",
            "This country has a famous archaeological site older than the pyramids.",
            "This country has a region with unique rock formations and hot air balloons.",
            "This country has a history as the seat of an empire that lasted over 600 years.",
            "This country has a significant production of hazelnuts.",
            "This country has a cuisine that often includes eggplant, yogurt, and lamb.",
            "This country celebrates a secular holiday for its founding leader every year.",
            "This country has a deep tradition in bathhouses called 'hammams'.",
        ],

        "Greece": [
            "This country has thousands of islands, many of which are uninhabited.",
            "This country is often credited as the birthplace of democracy.",
            "This country has a blue and white flag representing the sea and sky.",
            "This country has a cuisine rich in olive oil, feta, and seafood.",
            "This country has a strong tradition of Orthodox Christianity.",
            "This country has a long coastline relative to its land area.",
            "This country has ancient ruins still central to its modern cities.",
            "This country celebrates name days often more than birthdays.",
            "This country has a tradition of smashing plates at celebrations.",
            "This country’s language has a unique alphabet which Latin is indirectly derived from.",
        ],

        "South Korea": [
            "This country is known for global exports in tech and entertainment.",
            "This country has mandatory military service for most men.",
            "This country celebrates a harvest festival called 'Chuseok'.",
            "This country has a writing system created in the 15th century.",
            "This country is known for fermented foods like kimchi.",
            "This country has high-speed internet and competitive gaming culture.",
            "This country has a peninsula with a heavily fortified border.",
            "This country has a booming film and television industry.",
            "This country’s cuisine often includes side dishes called 'banchan'.",
            "This country has rapid urban development with a preserved royal past.",
        ],

        "North Korea": [
            "This country has very limited access to global media and the internet.",
            "This country has a personality-based leadership system.",
            "This country holds massive military parades regularly.",
            "This country is known for mass gymnastics events and displays.",
            "This country has a capital with monuments honoring its leaders.",
            "This country has one of the world’s most closed economies.",
            "This country has tightly controlled tourism policies.",
            "This country is technically still at war with its neighbor due to an armistice.",
            "This country has government-supplied haircuts as a norm.",
            "This country has a large demilitarized zone separating it from another nation.",
        ],

        "Serbia": [
            "This country is landlocked and located in the Balkans.",
            "This country has a strong tradition in Orthodox Christianity.",
            "This country uses both Cyrillic and Latin scripts.",
            "This country is known for its unique brass band music and festivals.",
            "This country has produced several top tennis players.",
            "This country has a capital located at the confluence of two rivers.",
            "This country was once part of a larger federation that dissolved in the 1990s.",
            "This country celebrates a slava, or patron saint day, as a family tradition.",
            "This country has a national dish based on grilled minced meat.",
            "This country has historical ties with both Eastern and Western empires.",
        ],

        "Croatia": [
            "This country has a long coastline along the Adriatic Sea.",
            "This country is known for a popular vacation region with over 1,000 islands.",
            "This country uses the Latin script and speaks a South Slavic language.",
            "This country has a city whose walls inspired a famous fantasy TV series.",
            "This country is known for a necktie-related invention.",
            "This country has both Mediterranean and continental climates.",
            "This country has a popular national football team with a checkerboard jersey.",
            "This country has historic cities such as Split and Zagreb.",
            "This country has traditional dances performed in circular patterns.",
            "This country has a cuisine with strong Italian and Balkan influences.",
        ],

        "Bosnia and Herzegovina": [
            "This country has three main ethnic groups coexisting under a complex political structure.",
            "This country has a historic city with a famous Ottoman-style bridge.",
            "This country was heavily affected during the conflicts of the 1990s.",
            "This country has a mix of Islamic, Orthodox, and Catholic traditions.",
            "This country has mountainous terrain and natural springs.",
            "This country has a cuisine influenced by Turkish and Central European dishes.",
            "This country has a flag featuring yellow, white, and blue colors with stars.",
            "This country has a plural presidency representing different ethnicities.",
            "This country is known for coffee culture and traditional sweets.",
            "This country has a winter sports scene in its mountain towns.",
        ],

        "Austria": [
            "This country is known for its alpine scenery and skiing.",
            "This country was part of a major European empire until the early 20th century.",
            "This country is the birthplace of many classical composers.",
            "This country has a capital famous for its palaces and coffee houses.",
            "This country is landlocked and located in Central Europe.",
            "This country has a strong tradition in opera and orchestras.",
            "This country has a cuisine known for schnitzel and strudel.",
            "This country hosted a major peace treaty after World War I.",
            "This country uses German as its official language.",
            "This country is known for its punctual and efficient rail system.",
        ],

        "Laos": [
            "This country is landlocked and located in Southeast Asia.",
            "This country is known for its Buddhist temples and French colonial history.",
            "This country has a river that plays a central role in daily life.",
            "This country has a capital known for its relaxed atmosphere.",
            "This country has traditional sticky rice as a dietary staple.",
            "This country has a national sport involving kicking a rattan ball.",
            "This country celebrates a New Year festival involving water splashing.",
            "This country shares borders with five other nations.",
            "This country has a mountainous landscape with hidden caves.",
            "This country is one of the most heavily bombed in history due to past conflicts.",
        ],

        "Nigeria": [
            "This country is the most populous in Africa.",
            "This country has over 500 spoken languages.",
            "This country is known for Nollywood, one of the largest film industries in the world.",
            "This country is a major oil producer.",
            "This country has diverse ethnic groups such as Hausa, Yoruba, and Igbo.",
            "This country has a rapidly growing tech sector nicknamed 'Silicon Lagoon.'",
            "This country celebrates festivals like the Durbar and Eyo.",
            "This country has a rich musical scene, known globally for Afrobeats.",
            "This country’s largest city is one of the fastest growing in the world.",
            "This country gained independence from Britain in 1960.",
        ],

        "Kenya": [
            "This country is located on the eastern coast of Africa.",
            "This country is known for its long-distance runners.",
            "This country has famous wildlife safaris and national parks.",
            "This country has diverse geography, including mountains and the Great Rift Valley.",
            "This country has over 40 ethnic groups.",
            "This country’s capital is a major hub for UN organizations in Africa.",
            "This country has coastline along the Indian Ocean.",
            "This country produces significant amounts of tea and coffee.",
            "This country has ancient Swahili coastal settlements.",
            "This country was a British colony until the 1960s.",
        ],

        "Argentina": [
            "This country is the second-largest in South America.",
            "This country is famous for tango music and dance.",
            "This country has a strong beef-eating culture.",
            "This country is known for its football legends.",
            "This country has regions such as Patagonia and the Pampas.",
            "This country is home to parts of the Andes Mountains.",
            "This country has a European-influenced culture and architecture.",
            "This country experienced a major economic crisis in the early 2000s.",
            "This country claims a territory disputed with the UK.",
            "This country has a capital known for its wide avenues and cultural life.",
        ],

        "Canada": [
            "This country is the second-largest by land area in the world.",
            "This country has two official languages.",
            "This country is known for cold winters and vast forests.",
            "This country has a strong tradition in ice hockey.",
            "This country has a high standard of living and universal healthcare.",
            "This country is home to the Rocky Mountains and Niagara Falls.",
            "This country has many national parks and lakes.",
            "This country is part of the Commonwealth.",
            "This country has provinces and territories instead of states.",
            "This country celebrates multiculturalism as part of its identity.",
        ],

        "Slovakia": [
            "This country is landlocked in Central Europe.",
            "This country has many medieval castles and fortresses.",
            "This country was part of a federation that peacefully split in the 1990s.",
            "This country uses the euro as its currency.",
            "This country is known for its mountainous terrain, especially the High Tatras.",
            "This country has a capital on the Danube River.",
            "This country has traditional folk music and dances.",
            "This country has a strong tradition in ice hockey.",
            "This country has thermal springs and wellness resorts.",
            "This country has both Slavic and Central European cultural influences.",
        ],

        "Slovenia": [
            "This country is located at the crossroads of Central and Southeastern Europe.",
            "This country has a short but scenic coastline on the Adriatic Sea.",
            "This country is known for its lakes, caves, and mountains.",
            "This country was part of Yugoslavia until the early 1990s.",
            "This country’s capital is known for its dragon symbol and green spaces.",
            "This country has a strong tradition in winter sports, especially ski jumping.",
            "This country uses the euro and is a member of the Schengen Area.",
            "This country has a high quality of life and ranked education system.",
            "This country has famous natural sites like Lake Bled and Postojna Cave.",
            "This country blends Slavic, Germanic, and Romance cultural influences.",
        ],

        "Czechia": [
            "This country is landlocked in Central Europe.",
            "This country was part of Czechoslovakia until a peaceful split in 1993.",
            "This country’s capital is famous for its historic architecture and bridges.",
            "This country is known for its beer culture.",
            "This country has many medieval castles and old towns.",
            "This country has produced many composers and scientists.",
            "This country has a rich tradition in literature and puppetry.",
            "This country uses the koruna, not the euro.",
            "This country was once part of the Austro-Hungarian Empire.",
            "This country has a strong industrial economy, especially in cars and machinery.",
        ],

        "Montenegro": [
            "This country has a coastline on the Adriatic Sea.",
            "This country became independent from a union in 2006.",
            "This country’s name means 'Black Mountain' in its language.",
            "This country is known for its rugged mountains and beautiful bays.",
            "This country’s Bay of Kotor is a UNESCO World Heritage Site.",
            "This country uses the euro despite not being in the EU.",
            "This country has a small population but a growing tourism sector.",
            "This country was part of Yugoslavia and later Serbia and Montenegro.",
            "This country’s capital is also its largest city.",
            "This country has a mix of Orthodox, Muslim, and Catholic communities.",
        ],

        "North Macedonia": [
            "This country changed its name to resolve a dispute with a neighbor.",
            "This country was once a part of Yugoslavia.",
            "This country’s capital has a large statue often mistaken for Alexander the Great.",
            "This country has both Slavic and ancient Hellenistic historical claims.",
            "This country has rugged mountains and deep lakes.",
            "This country is known for its traditional food like ajvar and tavče gravče.",
            "This country has a growing wine industry.",
            "This country is landlocked in the Balkans.",
            "This country became independent in the early 1990s.",
            "This country uses the denar as its currency.",
        ],

        "Monaco": [
            "This country is one of the smallest in the world by area and population.",
            "This country is located on the French Riviera.",
            "This country is known for its wealth, casinos, and luxury lifestyle.",
            "This country hosts a famous Formula 1 Grand Prix race each year.",
            "This country is a monarchy ruled by the Grimaldi family.",
            "This country has no income tax for residents.",
            "This country is bordered entirely by France and the Mediterranean Sea.",
            "This country is a member of the UN but not the EU.",
            "This country has the highest population density in the world.",
            "This country’s main district is Monte Carlo.",
        ],

        "Singapore": [
            "This country is a city-state located at the tip of the Malay Peninsula.",
            "This country is one of the world's most densely populated countries.",
            "This country has one of the busiest ports in the world.",
            "This country is famous for its strict laws and cleanliness.",
            "This country is a global financial hub with a strong economy.",
            "This country blends Chinese, Malay, Indian, and Western cultures.",
            "This country’s national dish is considered to be Hainanese chicken rice.",
            "This country is known for its efficient public transport system.",
            "This country gained independence from Malaysia in 1965.",
            "This country’s government is known for its meritocracy and long-ruling party.",
        ],

        "Indonesia": [
            "This country is made up of over 17,000 islands.",
            "This country has the fourth-largest population in the world.",
            "This country is home to hundreds of ethnic groups and languages.",
            "This country’s capital is being moved from Jakarta to Nusantara.",
            "This country has active volcanoes and frequent earthquakes.",
            "This country is the largest Muslim-majority country in the world.",
            "This country has a rich tradition of batik, gamelan music, and shadow puppetry.",
            "This country includes the island of Bali, a major tourist destination.",
            "This country was formerly colonized by the Dutch.",
            "This country has tropical rainforests and major biodiversity.",
        ],

        "Malaysia": [
            "This country is split into two main regions, separated by the South China Sea.",
            "This country has a mix of Malay, Chinese, and Indian cultural influences.",
            "This country’s capital is Kuala Lumpur.",
            "This country is known for its cuisine, especially nasi lemak and satay.",
            "This country has a constitutional monarchy with rotating kings.",
            "This country shares the island of Borneo with Indonesia and Brunei.",
            "This country has both modern skyscrapers and ancient rainforests.",
            "This country is a major producer of palm oil and rubber.",
            "This country has a rapidly growing technology and manufacturing sector.",
            "This country is majority Muslim and celebrates many multicultural festivals.",
        ],

        "Botswana": [
            "This country is located in Southern Africa and is landlocked.",
            "This country has a strong record of democracy and political stability.",
            "This country is one of the world's largest producers of diamonds.",
            "This country’s economy has grown significantly since independence in 1966.",
            "This country is home to much of the Kalahari Desert.",
            "This country has a low population density.",
            "This country has large nature reserves like the Okavango Delta.",
            "This country is known for its wildlife and eco-tourism.",
            "This country uses the pula as its currency.",
            "This country has English as an official language along with Setswana.",
        ],

        "Algeria": [
            "This country is the largest in Africa by land area.",
            "This country is located in North Africa and has a Mediterranean coastline.",
            "This country was colonized by France until gaining independence in 1962.",
            "This country has much of the Sahara Desert within its borders.",
            "This country’s official languages include Arabic and Berber.",
            "This country has a strong oil and natural gas industry.",
            "This country is known for its historical cities like Algiers and Oran.",
            "This country has a mix of Arab, Berber, and French cultural influences.",
            "This country fought a long and brutal war for independence.",
            "This country’s food includes couscous and spicy stews.",
        ],

        "Libya": [
            "This country is located in North Africa and has a long Mediterranean coastline.",
            "This country has large reserves of oil and natural gas.",
            "This country was ruled by Muammar Gaddafi for over 40 years.",
            "This country experienced a major civil war after 2011.",
            "This country has vast desert landscapes, including part of the Sahara.",
            "This country’s official language is Arabic.",
            "This country has ancient Roman ruins like Leptis Magna and Sabratha.",
            "This country has a low population density and large uninhabited areas.",
            "This country has struggled with political instability in recent years.",
            "This country borders Egypt, Tunisia, Algeria, and several other African nations.",
        ],

        "Chile": [
            "This country stretches along the southwestern coast of South America.",
            "This country is one of the longest north-south countries in the world.",
            "This country is home to the Atacama Desert, one of the driest places on Earth.",
            "This country has a strong tradition in literature, with Nobel laureates like Pablo Neruda.",
            "This country has one of the most stable economies in South America.",
            "This country has a large wine industry and exports copper.",
            "This country has a varied climate, from desert to glaciers.",
            "This country’s capital is Santiago.",
            "This country was ruled by military dictator Augusto Pinochet in the 20th century.",
            "This country’s coastline is known for frequent earthquakes and tsunamis.",
        ],

        "Bolivia": [
            "This country is landlocked and located in the heart of South America.",
            "This country has two capitals: La Paz and Sucre.",
            "This country has one of the largest indigenous populations in the Americas.",
            "This country is home to Lake Titicaca, one of the highest navigable lakes in the world.",
            "This country is known for its salt flats, especially Salar de Uyuni.",
            "This country has a rich tradition of Andean music and culture.",
            "This country was named after the independence leader Simón Bolívar.",
            "This country has vast highlands, mountains, and tropical rainforests.",
            "This country’s official languages include Spanish and several indigenous languages.",
            "This country has historically been rich in silver and other minerals.",
        ],

        "Colombia": [
            "This country is located in the northwestern corner of South America.",
            "This country is known for coffee, flowers, emeralds, and music like cumbia.",
            "This country is one of the world's most biodiverse nations.",
            "This country has both Caribbean and Pacific coastlines.",
            "This country’s capital is Bogotá.",
            "This country has produced many famous writers, including Gabriel García Márquez.",
            "This country has a history of internal conflict involving guerrilla groups.",
            "This country is known for its vibrant festivals and colorful cities like Medellín.",
            "This country has mountains, jungles, and vast plains called the Llanos.",
            "This country has seen rapid economic growth and improved security in recent decades.",
        ],

        "New Zealand": [
            "This country is made up of two main islands in the southwestern Pacific Ocean.",
            "This country is known for stunning natural scenery and biodiversity.",
            "This country’s indigenous people are the Māori.",
            "This country is a popular filming location for movies like The Lord of the Rings.",
            "This country has a parliamentary democracy and a constitutional monarchy.",
            "This country is famous for extreme sports and outdoor adventures.",
            "This country has a strong agricultural sector, especially in dairy and sheep farming.",
            "This country’s capital is Wellington, but Auckland is its largest city.",
            "This country is known for its rugby team, the All Blacks.",
            "This country has a temperate maritime climate and active geothermal areas.",
        ],

        "Switzerland": [
            "This country is a landlocked country in central Europe.",
            "This country is known for neutrality, banking, and precision engineering.",
            "This country has four official languages: German, French, Italian, and Romansh.",
            "This country is home to the Alps and is famous for skiing and hiking.",
            "This country is known for high-quality chocolate and cheese.",
            "This country has a system of direct democracy and regular referendums.",
            "This country’s capital is Bern, and Zurich is its financial center.",
            "This country is home to many international organizations, including the Red Cross.",
            "This country is not a member of the European Union.",
            "This country has one of the highest standards of living and quality of life in the world.",
        ],

        "Colombia": [
            "This country has coastlines on both the Pacific Ocean and the Caribbean Sea.",
            "This country is known for its high-quality coffee production.",
            "This country is home to parts of the Andes Mountains and the Amazon rainforest.",
            "This country has a history of internal conflict involving guerrilla groups.",
            "This country is famous for its music styles like cumbia and vallenato.",
            "This country’s capital is one of the highest-altitude capitals in the world.",
            "This country celebrates the vibrant Barranquilla Carnival.",
            "This country exports significant amounts of oil and coal.",
            "This country has a major emerald mining industry.",
            "This country has a diverse population including Afro-Colombian and Indigenous communities.",
        ],

        "Cameroon": [
            "This country is often called 'Africa in miniature' for its varied geography and culture.",
            "This country has both English and French as official languages.",
            "This country is a major producer of cocoa, coffee, and cotton.",
            "This country has active volcanoes like Mount Cameroon.",
            "This country’s national football team is known as the Indomitable Lions.",
            "This country has more than 250 ethnic groups and languages.",
            "This country was colonized by Germany, Britain, and France.",
            "This country is known for traditional music styles like makossa.",
            "This country has rainforests rich in biodiversity.",
            "This country faces periodic conflict in its Anglophone regions.",
        ],

        "Sudan": [
            "This country lies along the Nile River and is largely desert.",
            "This country was once the largest in Africa before a secession in 2011.",
            "This country has more pyramids than Egypt.",
            "This country has faced multiple civil wars and political instability.",
            "This country was ruled by military leaders for much of its post-independence history.",
            "This country’s capital sits where the Blue and White Nile meet.",
            "This country has significant gold reserves.",
            "This country has many ancient Nubian archaeological sites.",
            "This country is culturally influenced by both Arab and African traditions.",
            "This country has dealt with economic sanctions and humanitarian crises.",
        ],

        "Republic of the Congo": [
            "This country shares a name with another country.",
            "This country was a former French colony.",
            "This country’s capital lies across the river from another capital.",
            "This country is rich in oil and natural gas.",
            "This country has tropical rainforests and is part of the Congo Basin.",
            "This country gained independence in 1960.",
            "This country has ethnic and linguistic diversity, with over 60 languages spoken.",
            "This country has faced periods of civil conflict and political unrest.",
            "This country is sparsely populated compared to its size.",
            "This country’s economy relies heavily on petroleum exports.",
        ],

        "Somalia": [
            "This country has the longest coastline on the African mainland.",
            "This country is located in the Horn of Africa.",
            "This country uses a flag with a single white star on a light blue background.",
            "This country has experienced prolonged civil war and instability.",
            "This country has a strong tradition of poetry and oral literature.",
            "This country’s economy includes livestock, agriculture, and remittances.",
            "This country has suffered from drought and famine in recent decades.",
            "This country has a largely homogenous ethnic group: the Somali people.",
            "This country has seen piracy off its coast in recent decades.",
            "This country has made attempts at forming a stable federal government since the 2000s.",
        ],

        "Democratic Republic of the Congo": [
            "This country is the second-largest in Africa by area.",
            "This country is extremely rich in natural resources, especially cobalt and copper.",
            "This country was formerly known as Zaire.",
            "This country is home to the Congo River, the deepest in the world.",
            "This country has faced decades of conflict and humanitarian crises.",
            "This country is home to vast tropical rainforests and biodiversity.",
            "This country has a large population, making it one of the most populous in Africa.",
            "This country has cities like Kinshasa, one of the largest francophone cities in the world.",
            "This country has a wide range of ethnic groups and languages, over 200.",
            "This country has a troubled colonial past under Belgian rule.",
        ],

        "Albania": [
            "This country has both Adriatic and Ionian Sea coastlines.",
            "This country was once an isolated communist state under Enver Hoxha.",
            "This country is known for its unique bunkers scattered across the landscape.",
            "This country is part of NATO but not yet in the EU.",
            "This country has a majority Muslim population but is officially secular.",
            "This country has seen strong growth in tourism in recent years.",
            "This country shares cultural similarities with Bulgaria and North Macedonia.",
            "This country’s capital is Tirana.",
            "This country has a traditional code of honor called 'Kanun'.",
            "This country has historical ties to the ancient Illyrians.",
        ],

        "Portugal": [
            "This country is located on the Iberian Peninsula.",
            "This country once had a vast global empire, including Brazil and parts of Africa and Asia.",
            "This country is known for its traditional Fado music.",
            "This country produces cork, wine, and olive oil in large quantities.",
            "This country shares a border with only one other country.",
            "This country’s official language is Portuguese.",
            "This country’s capital city is Lisbon.",
            "This country is known for historic explorers like Vasco da Gama and Magellan.",
            "This country’s cuisine includes dishes like bacalhau (salt cod).",
            "This country includes the autonomous island regions of Madeira and the Azores.",
        ],

        "Belgium": [
            "This country is home to the headquarters of the European Union and NATO.",
            "This country has three official languages: Dutch, French, and German.",
            "This country is known for its beer, chocolate, and waffles.",
            "This country has a complex federal government structure.",
            "This country’s capital is Brussels.",
            "This country has cultural regions known as Flanders and Wallonia.",
            "This country is famous for comic characters like Tintin and the Smurfs.",
            "This country played key roles in both World Wars.",
            "This country has a constitutional monarchy.",
            "This country is known for its medieval towns and Gothic architecture.",
        ],

        "Luxembourg": [
            "This country is one of the smallest sovereign nations in Europe.",
            "This country is a founding member of the EU, NATO, and the UN.",
            "This country has three official languages: Luxembourgish, French, and German.",
            "This country is known for its strong banking and finance sectors.",
            "This country has one of the highest GDPs per capita in the world.",
            "This country has a constitutional monarchy.",
            "This country borders Belgium, France, and Germany.",
            "This country’s capital is also called Luxembourg.",
            "This country is mostly rural with forests and rolling hills.",
            "This country is one of the safest and wealthiest in the world.",
        ],

        "Liechtenstein": [
            "This country is a landlocked microstate in Central Europe.",
            "This country is bordered by Switzerland and Austria.",
            "This country is one of the wealthiest nations in the world per capita.",
            "This country uses the Swiss franc as its currency.",
            "This country is a constitutional monarchy headed by a prince.",
            "This country is known for its strong financial sector and low taxes.",
            "This country has a very low crime rate.",
            "This country is German-speaking.",
            "This country is mostly mountainous and popular for winter sports.",
            "This country is not a member of the European Union but part of the EEA and Schengen Area.",
        ],

        "Andorra": [
            "This country is a small landlocked principality in the Pyrenees Mountains.",
            "This country is bordered by France and Spain.",
            "This country is co-ruled by the President of France and the Bishop of Urgell.",
            "This country has tourism as a major industry, especially for skiing.",
            "This country uses the euro as its currency even though it is not in the EU.",
            "This country is known for its tax haven status.",
            "This country has Catalan as its official language.",
            "This country is one of the smallest countries in Europe.",
            "This country has a high standard of living.",
            "This country has no airports and is only accessible by road.",
        ],

        "Moldova": [
            "This country is located between Romania and Ukraine.",
            "This country was formerly part of the Soviet Union.",
            "This country’s official language is Romanian.",
            "This country has one of the lowest GDPs in Europe.",
            "This country is known for its wine industry and large underground wine cellars.",
            "This country has a breakaway region called Transnistria.",
            "This country’s capital is Chișinău.",
            "This country is landlocked.",
            "This country has seen significant emigration due to economic issues.",
            "This country has cultural influences from both Romania and Russia.",
        ],

        "Ukraine": [
            "This country is the second-largest country in Europe by area after Russia.",
            "This country declared independence from the Soviet Union in 1991.",
            "This country has been involved in a major conflict since 2014, escalating in 2022.",
            "This country is known for its fertile land and agriculture, especially grain production.",
            "This country’s capital is Kyiv.",
            "This country has a strong cultural identity with traditions in music and dance.",
            "This country has major cities like Lviv, Odesa, and Kharkiv.",
            "This country has a population of over 40 million people.",
            "This country is rich in natural resources, including coal and iron ore.",
            "This country has sought closer ties with the European Union.",
        ],

        "Hungary": [
            "This country is landlocked and located in Central Europe.",
            "This country’s capital, Budapest, is divided by the Danube River.",
            "This country has a unique language unrelated to most European languages.",
            "This country was once part of the Austro-Hungarian Empire.",
            "This country is known for thermal baths and spas.",
            "This country has traditional dishes like goulash and paprika-based cuisine.",
            "This country has seen recent political tension within the EU.",
            "This country has many UNESCO World Heritage Sites.",
            "This country has a strong tradition in classical music and folk dancing.",
            "This country was part of the Eastern Bloc during the Cold War.",
        ],

        "Denmark": [
            "This country is a Nordic country located in Northern Europe.",
            "This country is part of the Kingdom of Denmark, which includes Greenland and the Faroe Islands.",
            "This country is known for its welfare state and high standard of living.",
            "This country has a constitutional monarchy.",
            "This country’s capital is Copenhagen.",
            "This country is a founding member of NATO and the EU (though opted out of the euro).",
            "This country is famous for its design, architecture, and cycling culture.",
            "This country is home to the original Legoland and LEGO headquarters.",
            "This country consistently ranks high in happiness and quality of life.",
            "This country has a flat landscape and a strong focus on sustainability.",
        ],

        "Norway": [
            "This country is part of Scandinavia and has a long North Atlantic coastline.",
            "This country is known for its fjords, mountains, and natural beauty.",
            "This country is not in the EU but is part of the Schengen Area and EEA.",
            "This country is one of the richest in the world due to oil and gas exports.",
            "This country has high levels of social welfare and public services.",
            "This country uses the Norwegian krone as its currency.",
            "This country has a strong maritime tradition and fishing industry.",
            "This country’s capital is Oslo.",
            "This country consistently ranks among the happiest and most peaceful countries.",
            "This country has a constitutional monarchy with a royal family.",
        ],

        "Lithuania": [
            "This country is one of the three Baltic states.",
            "This country was the first Soviet republic to declare independence in 1990.",
            "This country’s capital is Vilnius.",
            "This country has a strong Catholic tradition.",
            "This country was once part of a vast commonwealth with Poland.",
            "This country uses the euro as its currency.",
            "This country has a flat landscape and many lakes and forests.",
            "This country has rapidly developed since joining the EU in 2004.",
            "This country has a unique language with ancient Indo-European roots.",
            "This country has a historical region called Samogitia with distinct cultural identity.",
        ],

        "Latvia": [
            "This country is a Baltic state located between Lithuania and Estonia.",
            "This country’s capital is Riga, known for its Art Nouveau architecture.",
            "This country has a significant Russian-speaking minority.",
            "This country is a member of both the EU and NATO.",
            "This country gained independence from the Soviet Union in 1991.",
            "This country has vast forests and a long coastline on the Baltic Sea.",
            "This country uses the euro as its currency.",
            "This country celebrates midsummer with traditional festivals.",
            "This country has a parliamentary republic system of government.",
            "This country is known for its folk music and wooden architecture.",
        ],

        "Estonia": [
            "This country is the northernmost of the three Baltic states.",
            "This country is known for being highly digital and e-government focused.",
            "This country’s capital is Tallinn.",
            "This country has one of the fastest internet speeds in Europe.",
            "This country uses the euro and is a member of the EU and NATO.",
            "This country regained independence from the Soviet Union in 1991.",
            "This country has strong cultural ties to Finland.",
            "This country is mostly flat with over 1,000 lakes and many islands.",
            "This country is one of the most secular countries in the world.",
            "This country offers e-residency to foreign entrepreneurs.",
        ],

        "Ireland": [
            "This country is located on an island to the west of Great Britain.",
            "This country is known for its lush green landscapes and countryside.",
            "This country is a member of the EU but not part of the Schengen Area.",
            "This country uses the euro as its currency.",
            "This country’s capital is Dublin.",
            "This country has a strong literary and musical tradition.",
            "This country has a large diaspora, particularly in the US.",
            "This country has a unique native language, Irish, alongside English.",
            "This country has experienced rapid economic growth in recent decades.",
            "This country is known for companies choosing it for EU headquarters due to favorable tax laws.",
        ],

        "The Netherlands": [
            "This country is known for windmills, tulips, and cycling culture.",
            "This country has a constitutional monarchy with a parliamentary system.",
            "This country’s capital is Amsterdam, though the government is based in The Hague.",
            "This country is famous for its water management and low elevation.",
            "This country is a founding member of the EU and NATO.",
            "This country uses the euro as its currency.",
            "This country has a very high population density.",
            "This country has a strong tradition in arts, especially painting.",
            "This country is home to major international courts and organizations.",
            "This country is among the most progressive on issues like drug policy and euthanasia.",
        ],

        "Peru": [
            "This country was the heart of the ancient Inca Empire.",
            "This country is known for Machu Picchu and Andean culture.",
            "This country has three major geographic regions: coast, mountains, and jungle.",
            "This country’s capital is Lima.",
            "This country has a diverse cuisine known for ceviche.",
            "This country is rich in minerals like copper, gold, and silver.",
            "This country’s official languages include Spanish and Quechua.",
            "This country has Lake Titicaca, the highest navigable lake in the world.",
            "This country has a growing tourism industry tied to archaeology and nature.",
            "This country has one of the largest portions of the Amazon Rainforest.",
        ],

        "Venezuela": [
            "This country has the world’s largest proven oil reserves.",
            "This country’s capital is Caracas.",
            "This country is home to Angel Falls, the world's highest waterfall.",
            "This country has experienced significant economic and political crisis in recent years.",
            "This country’s traditional music includes joropo.",
            "This country has diverse geography, including beaches, plains, and mountains.",
            "This country uses the Venezuelan bolívar as its currency.",
            "This country has a history of migration due to internal instability.",
            "This country was part of Gran Colombia under Simón Bolívar.",
            "This country has a strong baseball culture, with many MLB players.",
        ],

        "Paraguay": [
            "This country is one of two landlocked countries in South America.",
            "This country has two official languages: Spanish and Guaraní.",
            "This country’s capital is Asunción.",
            "This country is known for hydroelectric power from the Itaipú Dam.",
            "This country has a subtropical to tropical climate.",
            "This country has a mix of indigenous and colonial heritage.",
            "This country fought the devastating War of the Triple Alliance in the 19th century.",
            "This country has a relatively small population for its size.",
            "This country’s economy is heavily based on agriculture and electricity exports.",
            "This country has a tradition of harp and polka-style folk music.",
        ],

        "Uruguay": [
            "This country is one of the most politically stable in South America.",
            "This country’s capital is Montevideo.",
            "This country is known for its high literacy rate and social development.",
            "This country has legalized cannabis and same-sex marriage.",
            "This country has strong cultural ties to Argentina.",
            "This country’s economy relies on agriculture, beef, and dairy.",
            "This country has a population of around 3.5 million.",
            "This country is often called the ‘Switzerland of South America.’",
            "This country has a long Atlantic coastline and beach resorts.",
            "This country has a strong football (soccer) tradition.",
        ],

        "Suriname": [
            "This country is the smallest in South America by population.",
            "This country’s capital is Paramaribo.",
            "This country was formerly a Dutch colony.",
            "This country’s official language is Dutch.",
            "This country has a very ethnically diverse population.",
            "This country is heavily forested and part of the Amazon basin.",
            "This country has gold and oil as key resources.",
            "This country has a history of indentured laborers from India and Java.",
            "This country has tropical rainforest climate and biodiversity.",
            "This country borders Brazil, Guyana, and French Guiana.",
        ],

        "Cuba": [
            "This country is the largest island in the Caribbean.",
            "This country’s capital is mentioned in and used as the title of a pop song.",
            "This country has a socialist government and planned economy.",
            "This country is known for its cigars, rum, and classic cars.",
            "This country played a major role during the Cold War with the Cuban Missile Crisis.",
            "This country has a high literacy rate and strong healthcare system.",
            "This country has a rich Afro-Caribbean culture and music scene.",
            "This country’s economy is impacted by long-standing US embargoes.",
            "This country has a one-party political system led by the Communist Party.",
            "This country is famous for its revolutionary history and figures like Fidel Castro and Che Guevara.",
        ],
    }

    CountryAlias = {
    "usa": "The United States of America",
    "united states": "The United States of America",
    "uk": "The United Kingdom",
    "britain": "The United Kingdom",
    "great britain": "United Kingdom",
    "the uk": "The United Kingdom",
    "dprk": "North Korea",
    "prc": "China",
    "rok": "South Korea",
    "america": "United States of America",
    "bosnia": "Bosnia and Herzegovina",
    "czech republic": "Czechia",
    "macedonia": "North Macedonia",
    "congo-brazzavile": "Republic of the Congo",
    "congo": "Republic of the Congo",
    "dpr congo": "Democratic Republic of the Congo",
    "congo-kinshasa": "Democratic Republic of the Congo",
    "netherlands": "The Netherlands",
    "turkey": "Turkiye",
    "republic of korea": "South Korea",
    "democratic people's republic of korea": "North Korea",
    "united states of america": "The United States of America",
    "united kingdom": "The United Kingdom",
}
    
    def GetCountryAlias(answer):
        AliasAnswer = answer.strip().lower()
        return CountryAlias.get(AliasAnswer, AliasAnswer).lower()
    
    def GameRound():
        clear_screen()
        ChosenCountry = random.choice(list(CountryFacts.keys()))
        ShownFacts = random.sample(CountryFacts[ChosenCountry], k=DifficultyList)

        for Factlist in ShownFacts:
            print(Factlist)
        print()
        print("What country is this?")
        answer = input().strip().lower()
        AliasAnswer = GetCountryAlias(answer)
        correct_one = GetCountryAlias(ChosenCountry)

        clear_screen()
        if AliasAnswer == correct_one:
            print(f"Correct guess, it was {ChosenCountry}! you win this round!")
            return True
        else:
            print(f"You are very wrong! It was {ChosenCountry}!")
            return False
    
    win_streak = int(0)

    while True:
        if GameRound():
            win_streak += int(1)
            print(f"You have a win streak of {win_streak}!")
        else:
            win_streak = int(0)
            print("Your streak has been reset!")

        print("Would you like to play again? Yes/No")
        PlayAgain = input()
        if PlayAgain not in ['yes', 'Yes', 'YES', 'y', 'Y', '',]:
            print("Thank you for playing.")
            time.sleep(3)
            break

if __name__ == "__main__":
    main()