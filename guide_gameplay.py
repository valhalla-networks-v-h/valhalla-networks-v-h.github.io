"""Content of gameplay.html: the complete player guide (English). Facts come from the gamemode code (checked
2026-10-03); keep numbers in step with the server when systems change. Used by build.py (GAMEPLAY)."""

GAMEPLAY = [
    ("berlin", "Berlin, 1942", [
        ("p", "Valhalla Networks is a serious roleplay server on Garry's Mod. Every player is a person of the city - with papers, "
              "a job, a bank account, a service record and a reputation. The factions run Berlin, the civilians keep it alive, "
              "and some of them fight the state in secret."),
        ("p", "Everything is connected. A tip on the telephone leads to a warrant, the warrant to an arrest, the arrest to an "
              "interrogation, and the interrogation to a raid. Events, wages and the war between state and resistance run on "
              "their own - you do not need a staff member to have something to do."),
        ("p", "This guide explains every system. The short versions are in the in-game handbook (F1), every command is on the "
              "Commands page, and the resistance has its own guide."),
    ]),
    ("first-hour", "Your first hour", [
        ("ol", [
            "**Create your character.** Pick a name and a look, then your origin: year of birth (1880-1924), birthplace and "
            "occupation. All three are printed on your identity card.",
            "**You start as a citizen of Berlin** with empty pockets. Your first daily reward (250 RM) arrives a few seconds "
            "after you load in, and the first-steps hints follow - /guide shows them again.",
            "**Find work at the Labour Office** next to the station: delivery driver, postman or street repairs. Each task pays "
            "at once.",
            "**Eat.** Buy bread or a sandwich at the General Store or the Coffee House - your hunger bar empties over two hours.",
            "**Your paycheck** arrives every 10 minutes and goes straight into your bank account (a pay account is opened for "
            "you). Withdraw it at a counter in the Reichsbank.",
            "**Get a driving licence** at the Licence Office in the police station (5,000 RM, service level 3), then buy a car "
            "at the dealer.",
            "**Join a faction.** Apply on our Discord or ask staff in game with @ - they put you on the roster.",
        ]),
    ]),
    ("controls", "Controls and menus", [
        ("table", ["Key", "What it does"], [
            ["F1", "Main menu: character, inventory, the handbook, the rules and your settings."],
            ["F2", "Door menu: buy a door, or give tenants and guests access to yours."],
            ["F3", "Recognise menu: let the people around you learn your name."],
            ["E", "Use: people, doors, telephones, lockers, shops, platforms. On a person with restraints: tie them up."],
            ["C", "Third-person view on and off."],
            ["X", "Voice chat (about 11 metres)."],
            ["Hold T", "Gesture wheel: salute, oath, wave, bow and more."],
            ["I", "Inspect your weapon and its attachments."],
            ["E + R / Shift + E + R", "Weapon safety on and off / change the fire mode."],
            ["@ text", "Ticket to the staff team."],
        ]),
    ]),
    ("work", "Work and money", [
        ("h3", "The Labour Office"),
        ("p", "Press E on the clerk at the Labour Office and pick a job. A marker shows your next stop and its distance; the "
              "next task follows two seconds after you finish one. During a **supply shortage** every job pays double."),
        ("table", ["Job", "Pay per task", "How it works"], [
            ["Delivery driver", "120 RM + 0.9 RM per metre, 6 XP", "You get a company truck (Opel Blitz) at the truck depot. "
             "Drive the cargo to the marked building."],
            ["Postman", "70 RM + 0.6 RM per metre, 4 XP", "On foot: walk the letter to the marked door."],
            ["Street repairs", "90 RM, 4 XP", "Find the sparking spot in the street and repair it (E, 6 seconds)."],
        ]),
        ("h3", "Paychecks"),
        ("p", "Everyone who is not away from the keyboard is paid every 10 minutes, straight into the bank. The first paycheck "
              "opens a free **pay account** for you; at the Pay Office in the Reichsbank you choose which account receives it."),
        ("table", ["Who", "Pay every 10 minutes"], [
            ["Civilians", "80 RM"],
            ["Faction members by rank", "Enlisted 120, NCO 200, Officer 320, General 500 RM"],
            ["Bonuses", "VIP +25 %, seeding +50 % while fewer than 10 players are online, police +15 % / +30 % during unrest "
                        "and uprisings, party tier up to +20 %"],
        ]),
        ("h3", "Daily reward"),
        ("p", "Load your character once a day: 250 RM on the first day, then 400, 550, 700, 850, 1,000 and 1,150 RM from the "
              "seventh day on. Miss a day and the streak starts again."),
        ("h3", "Service level"),
        ("ul", [
            "10 XP for every 5 minutes of active play, plus XP for jobs (4-6), ore (3), harvests (2), medals (25) and the "
            "wheel of fortune (40). /level shows your progress, /top the roll of honour.",
            "Level ups pay **level x 150 RM** and unlock things: the driving licence needs level 3, bigger cars levels 2-8.",
            "Titles: Newcomer, Resident (3), Regular (6), Veteran (10), Old Guard (15), Pillar of Berlin (20), Legend (30).",
        ]),
        ("h3", "The Reichsbank"),
        ("ul", [
            "**Bank Manager:** open accounts - the first is your free pay account, a second costs 50,000 RM, a third 100,000.",
            "**Counters:** deposit, withdraw, transfer to any account number, rename the account, read the logs.",
            "**Safe-deposit box:** every account has an item bank (6 x 5 slots) - items must come out before you use them.",
            "**Shared accounts:** add other characters by their ID and choose what they may do (deposit, withdraw, transfer ...).",
            "**Interest** is paid every hour you are in town - but only with a party tier (see below).",
            "Carrying more than **100,000 RM in cash** stops you from sprinting. Keep big money at the bank.",
        ]),
        ("h3", "Money between players"),
        ("ul", [
            "/givemoney <amount> to the person you look at (\"20k\" works), /dropmoney <amount> (at least 100 RM).",
            "/advertisement <text> puts an advert in the global chat for 500 RM (once every 2 minutes).",
        ]),
    ]),
    ("party", "The Party Office", [
        ("p", "Party tiers are bought one after another at the Party Office. Each gives bank interest every hour, a pay bonus, "
              "cheaper telephone numbers and a title on your name tag."),
        ("table", ["Tier", "Price", "Pay", "Phone numbers", "Interest per hour"], [
            ["I Party Candidate", "5,000 RM", "-", "-", "0.25 % (max 250)"],
            ["II Party Member", "8,000 RM", "+5 %", "-", "0.5 % (max 500)"],
            ["III Block Warden", "10,000 RM", "+10 %", "-10 %", "0.75 % (max 900)"],
            ["IV Gruppenleiter", "15,000 RM", "+15 %", "-20 %", "1 % (max 1,500)"],
            ["V Local Group Leader", "20,000 RM", "+20 %", "-30 %", "1.5 % (max 2,500)"],
        ]),
        ("ul", [
            "**Tier IV:** 15 % off luxury cars, your tips on the 8000 line count as trusted and pay double, and you carry a "
            "party card (/showpapers p).",
            "**Tier V:** everything of Tier IV, the state limousine from the Government tab, /broadcast once an hour, "
            "1,000 RM into the bank when the state wins the week, and /sponsor - a civilian you vouch for pays 3,000 instead "
            "of 5,000 RM for Tier I.",
        ]),
    ]),
    ("shops", "Shops, food and health", [
        ("p", "Shops sell at the listed price and buy back at half of it."),
        ("table", ["Shop", "What you find there"], [
            ["General Store, Village Store", "Bread, cheese, beans, canned meat, sardines, pretzels; flashlight, cigarettes, "
             "documents; seeds and a watering can; luggage for a bigger inventory (valise 750, suitcase 2,000, steamer trunk "
             "5,000 RM); carrier pigeons and a wireless set."],
            ["Coffee House, Restaurant, Casino Bar", "Cake, coffee and sandwiches; steak and lobster; drinks and cigars."],
            ["Tailor", "Suits from 200 to 800 RM."],
            ["Pharmacy", "Bandages and gauze (+15/+20 HP), splint (fixes a broken leg), first aid kit (+100 HP over 10 seconds), "
             "suture kit, IV bag (+50 HP)."],
            ["Gun Shop", "Pistols and the Kar98k, from 1,800 to 4,500 RM."],
            ["Tool Shop", "Pickaxe (120), fishing pole (250), bait, seeds. Buys fish, ore and wood."],
            ["Ore Trader, Fishmonger, Greengrocer", "Buy what you mined, caught or grew."],
            ["The Man in the Coat", "The black market: lockpicks, restraints, illegal guns, a radio and other things the "
             "law forbids. The Fence buys what he cannot sell."],
        ]),
        ("h3", "Hunger"),
        ("p", "Your hunger bar empties in about two hours. Every food and drink fills it - a 20 HP meal is worth about 30 "
              "minutes. An empty stomach only reminds you to eat; it no longer hurts you."),
        ("h3", "Health"),
        ("ul", [
            "Health comes back slowly on its own; the Pharmacy is faster.",
            "A shot in the leg breaks it: you walk at 40 % speed until you use a splint.",
            "After you die you respawn at your faction base (or in the city) and must stay away from the place of your death "
            "for 5 minutes (new life rule). Your equipped weapons are lost.",
        ]),
    ]),
    ("side-jobs", "Mining, farming and fishing", [
        ("h3", "Mining"),
        ("ul", [
            "Buy a pickaxe at the Tool Shop, equip it and hit an ore vein at the mine: four hits make one ore. A vein holds "
            "eight ore and grows one back every 45 seconds.",
            "Your mining level decides what you can dig: coal from the start, iron at level 2, copper at level 3, gold at level 4. "
            "/mining shows your progress.",
            "The Ore Trader at the mine pays half the list price: coal about 10, iron 17, copper 27, gold 60 RM per ore.",
        ]),
        ("h3", "Farming"),
        ("ul", [
            "Buy seeds (corn, wheat, tomato, lettuce, pepper) and plant them on open ground.",
            "A plant is ripe after 5 minutes - 3 minutes if you water it once. Press E to harvest 2-4 crops (+2 XP).",
            "Anyone can harvest a ripe plant, so guard your field. The Greengrocer buys the crops.",
        ]),
        ("h3", "Fishing"),
        ("ul", [
            "You need a fishing pole and bait in your inventory. Use \"Fishing\" and cast into water.",
            "After 15 seconds you get a bite - stay close. The bait is often lost (60 %).",
            "The Fishmonger by the forest bridge buys the catch; fish also fill your hunger.",
        ]),
    ]),
    ("papers", "Papers", [
        ("p", "Police and soldiers check papers. Keep yours in order - a missing paper can end in a cell."),
        ("table", ["Paper", "Who has it", "How to get it"], [
            ["Identity card", "Everyone", "Automatic, valid for 5 years. It shows a WANTED stamp while you have a warrant."],
            ["Driving licence", "Car drivers", "Licence Office at the police station (5,000 RM, level 3), or from the police."],
            ["Military pass", "Armed forces", "With your enlistment."],
            ["Service ID", "Police, state and party offices", "With your post."],
            ["Party card", "Party tier IV and V", "With the tier."],
        ]),
        ("p", "/papers shows your own papers. /showpapers id (or f, w, s, p) holds one up to the person you look at."),
    ]),
    ("phone", "Telephone", [
        ("ol", [
            "Buy a number at the Telephone Office: a random one for 150 RM, or choose one - 7 digits 400, 6 digits 800, "
            "5 digits 2,500, 4 digits 8,000, 3 digits 25,000 RM.",
            "/phone puts your telephone where you look (a table or the floor). Using it again moves it; /removephone takes it down.",
            "Press E on any telephone to dial. Pick a name from the phonebook or type the number and press CALL.",
            "The other phone rings; the owner answers with E and you talk privately.",
        ]),
        ("ul", [
            "/phonebook lists everyone online first, with their faction, then the official numbers. /mynumber shows yours.",
            "**8000** is the anonymous tip line of the police (see Law and order).",
        ]),
    ]),
    ("homes", "Homes and doors", [
        ("ul", [
            "Look at a free door and type /doorbuy or press F2. Most doors cost 250 RM, apartments 600 RM.",
            "F2 on your own door opens the access menu: add tenants and guests. Your keys lock (left click) and unlock (right click).",
            "/doorsell gives you half back. Doors you own are released when you leave the server.",
            "Faction doors open for members with E and lock behind them. The Reichsbank, the church, the cafe, the bar and the "
            "doors next to shops are not for sale.",
        ]),
    ]),
    ("vehicles", "Vehicles", [
        ("p", "Press E on a garage platform (the car dealer at the station square or a motor pool), stand at its edge and pick "
              "a car - or open the dealership to buy and sell."),
        ("table", ["Tab", "Price", "Notes"], [
            ["Private cars", "1,500-5,500 RM", "Some need service level 2 or 3."],
            ["Commercial", "3,000-12,000 RM", "Vans and trucks; the bus needs level 8."],
            ["Luxury", "7,500-30,000 RM", "Mercedes 770, Mercedes 290, Audi 920, Horch and the fastest sports cars; levels 5-8."],
            ["Premium", "10,000-18,000 RM", "The 1950s collection for supporters."],
            ["Government", "free", "Police, army and officials: Kubelwagen, Horch Kfz. 15, BMW R75 motorcycles, troop "
                                   "bicycles, Sd.Kfz. halftracks (the larger ones from NCO)."],
        ]),
        ("ul", [
            "You need a driving licence for your own cars. One vehicle can be out at a time; it is put away when you leave.",
            "Only you and holders of a spare key (/carkeys <name>) can drive. /carinfo shows who owns a car.",
            "A wrecked car spends 3 minutes in the workshop. Selling it back returns 60 %.",
        ]),
    ]),
    ("factions", "Factions and service", [
        ("p", "Four faction groups run the city - Government, Party, Armed Forces and Security - next to civilian organisations "
              "such as the Red Cross, Siemens & Halske, the Hotel Adlon and the organised crime of the Ringverein. Apply on "
              "Discord or with @ in game; staff put you on the roster through the personnel office."),
        ("h3", "Ranks"),
        ("p", "Enlisted, NCO, Officer and General. Your rank decides your pay, your uniform, your weapons, the vehicles you may "
              "take and some doors. Officers can promote members of their own faction up to the rank below their own."),
        ("h3", "Uniform and equipment"),
        ("ul", [
            "**Lockers** (E) give you the uniform of your faction and rank, your civilian clothes and any personal outfits.",
            "**Quartermaster:** buy your own weapons (melee 20, sidearm 80, rifle 100, heavy 150, grenade 25 RM, a few special "
            "prices), sign out up to three service weapons for free, buy magazines (6-10 RM, rockets 60) and refill your kit "
            "for free once a minute. A field radio and restraints are issued free.",
            "Service weapons cannot be dropped, traded or sold. When you die, your equipped weapons are lost.",
        ]),
        ("h3", "Medals and flags"),
        ("ul", [
            "122 medals in 10 groups. Staff and officers of your faction award them with a reason; they appear above your name "
            "and in /medals and give 25 XP.",
            "Faction members raise and lower flags with E.",
        ]),
    ]),
    ("law", "Law and order", [
        ("h3", "For everyone"),
        ("ul", [
            "Police, soldiers and the state offices can stop you, check your papers and search you.",
            "Contraband: weapons (tools such as pickaxes and fishing poles are fine), ammunition, drugs and resistance material.",
            "A restrained person can be freed by anyone who holds E on them for 3 seconds.",
            "Jail lasts 1-30 minutes in real time - also while you are offline. You are released in front of the police station; "
            "the arrest clears your warrant and your heat.",
            "/wanted shows the wanted list. WANTED boards hang in the police garage, the security headquarters, the Ministry "
            "of the Interior and the state police office.",
        ]),
        ("h3", "For the police"),
        ("ul", [
            "Restraints: E on a person (2 seconds). Drag a restrained person with left click.",
            "/checkid asks for papers - a restrained person has to show all of them. /search lists the inventory and pays a "
            "bounty for confiscated goods: weapons 150, drugs 80, ammunition 10, resistance material 120 RM (up to 1,500 RM an hour).",
            "/jail <minutes> [reason] puts a restrained person into a cell. /unjail lets them out.",
            "Officers issue warrants at a WANTED board (up to 40 entries, \"armed and dangerous\" optional).",
        ]),
        ("h3", "The tip line 8000"),
        ("ul", [
            "Dial 8000 at any telephone: pick a person and what they did - resistance activity, black market, weapons, curfew "
            "breach or something else.",
            "If the person is jailed within 30 minutes you get 250 RM - 500 RM for a real resistance member, double for party "
            "tier IV and higher. One tip every 5 minutes, at most four paid tips an hour.",
            "Each tip makes the suspect more suspicious (heat). The line is dead while the resistance has cut a junction box.",
        ]),
    ]),
    ("casino", "Spielbank Berlin", [
        ("table", ["Game", "How it works"], [
            ["Slot machines", "E spins, ALT + E changes the bet (10-500 RM). Three of a kind pay 8x to 150x; three Reichsmark "
             "symbols win the progressive jackpot (starts at 2,500 RM and grows with every bet)."],
            ["Wheel of fortune", "One free spin a day, otherwise 175 RM. Prizes from 25 to 2,500 RM, XP, a free spin or a "
             "tenth of the jackpot."],
            ["Roulette", "Bets close 25 seconds after the first chip. A number pays 35:1, dozens 2:1, red/black, even/odd and "
             "halves 1:1. Up to 8 bets per round."],
        ]),
        ("p", "The more you wager in total, the higher your casino level - Bronze (5,000 RM) to Diamond (1.5 million) adds up "
              "to +10 % to every win. /casinotop shows the biggest wins."),
    ]),
    ("city", "The living city", [
        ("table", ["City event", "Duration", "What happens"], [
            ["Supply shortage", "15 min", "Every Labour Office job pays double."],
            ["Air raid", "3 min", "Sirens - get off the streets."],
            ["Bounty", "20 min", "The police get 500 RM for every wanted person they arrest."],
            ["Dark night", "15 min", "Resistance points count double."],
            ["Uprising", "15 min", "At 85 % unrest: double resistance points, 150 RM for every resistance fighter jailed."],
        ]),
        ("ul", [
            "Events start on their own every 30-45 minutes when at least three people are in town.",
            "**Unrest** (/city): Calm, Restless (30 %), Unrest (60 %), Uprising (85 %). It rises with every resistance success, "
            "falls with arrests and slowly drifts back to normal.",
            "**The weekly war:** every arrest, leaflet and broadcast counts for the state or the resistance. On Monday everyone "
            "who fought for the winning side is paid - 500 RM plus 25 RM per point, up to 5,000 RM.",
            "The resistance has its own guide - see the Resistance page.",
        ]),
    ]),
    ("roleplay", "Roleplay tools", [
        ("table", ["Command", "What it does"], [
            ["Normal chat", "Spoken words, heard within about 5 metres."],
            ["/w, /y", "Whisper, shout."],
            ["/me, /it", "Describe what your character does / what happens around you."],
            ["// or /ooc, /looc", "Out of character: everyone (10 seconds between messages) / only people nearby."],
            ["/roll [max]", "Roll a die (up to 100)."],
            ["/anim 0-10", "Parade rest, arms crossed, hands up, salute, wave, nod, halt, point, beckon, fist on chest; 0 stops."],
            ["/chardesc, /fallover", "Your description; fall down for 1-60 seconds."],
            ["/r, /radio", "Talk on your radio's frequency (switch it on and set the frequency in the item menu)."],
        ]),
        ("ul", [
            "**F3** lets people around you learn your name; a mask hides who you are.",
            "**Carrier pigeon:** a note of up to 140 characters to anyone in town - from outdoors, every 2 minutes, and it can "
            "be shot down.",
            "Notes and documents can be written and handed over as items.",
        ]),
    ]),
    ("supporters", "Supporters", [
        ("ul", [
            "VIP and store packages pay for the server. VIP gives +25 % pay, two more character slots, the premium cars and PAC3.",
            "/pac opens the PAC3 outfit editor (VIP, the PAC3 package and admins).",
            "/perks shows what you have and how long it lasts. Packages arrive in game within a minute.",
        ]),
    ]),
    ("rules", "The rules in short", [
        ("ol", [
            "**Community:** respect everyone; no cheats, exploits, spam or advertising.",
            "**Setting:** this is history, not ideology. Hard limits apply and sensitive topics stay brief.",
            "**Roleplay:** stay in character, no metagaming, no powergaming, fear for your life, 5-minute new life rule.",
            "**Combat:** no random killing or running people over; heavy weapons, raids and vehicle theft need approval.",
            "**Staff:** follow staff instructions; report problems with @ or on Discord.",
        ]),
        ("p", "The full rules are on the Rules page and in F1."),
    ]),
    ("help", "Help", [
        ("ul", [
            "Type **@** and your question in the chat - it opens a ticket, even when no staff member is online.",
            "/guide repeats the first-steps hints; F1 has the handbook and the rules.",
            "Our Discord answers everything else.",
        ]),
    ]),
]
