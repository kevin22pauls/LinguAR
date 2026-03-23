"""
Hand-crafted dialogues for 20 COCO objects (Part 3).

Objects: wine glass, cup, fork, knife, spoon, bowl, banana, apple,
         sandwich, orange, broccoli, carrot, hot dog, pizza, donut,
         cake, chair, couch, potted plant, bed

Each object has 5 levels x 3 dialogues = 15 dialogues.
Each dialogue has exactly 4 turns: learner, system, learner, system.
Total: 300 dialogues.
"""

DIALOGUES_PART3 = {
    # ──────────────────────────────────────────────
    # WINE GLASS
    # ──────────────────────────────────────────────
    "wine glass": {
        "beginner": [
            [
                ("learner", "This glass is very tall."),
                ("system", "Yes, it has a long stem. We call it a wine glass."),
                ("learner", "I want juice in this glass."),
                ("system", "Sure, let me pour some mango juice for you."),
            ],
            [
                ("learner", "The wine glass looks pretty."),
                ("system", "It does! The glass is thin and shiny."),
                ("learner", "Can I drink water from it?"),
                ("system", "Of course, you can use it for any drink."),
            ],
            [
                ("learner", "I see a wine glass on the table."),
                ("system", "That glass is for the special dinner tonight."),
                ("learner", "My mother uses these for guests."),
                ("system", "That is a nice tradition in many Indian homes."),
            ],
        ],
        "elementary": [
            [
                ("learner", "We are using wine glasses for the party today."),
                ("system", "That is wonderful. Are you celebrating something?"),
                ("learner", "Yes, my sister passed her board exams last week."),
                ("system", "Congratulations to her! She must be very happy."),
            ],
            [
                ("learner", "I accidentally dropped a wine glass yesterday."),
                ("system", "Oh no, did it break? Those glasses are fragile."),
                ("learner", "It broke into many small pieces on the floor."),
                ("system", "Be careful cleaning up. Use a broom, not your hands."),
            ],
            [
                ("learner", "My grandmother is pouring rose milk into wine glasses."),
                ("system", "That sounds lovely. Rose milk looks beautiful in tall glasses."),
                ("learner", "She always serves drinks this way during festivals."),
                ("system", "It makes ordinary drinks feel special and festive."),
            ],
        ],
        "intermediate": [
            [
                ("learner", "I have never understood why wine glasses have such long stems."),
                ("system", "The stem keeps your hand away from the bowl so the drink stays cool."),
                ("learner", "That makes sense, because warm hands would heat the liquid quickly."),
                ("system", "Exactly. It is a clever design that serves a practical purpose."),
            ],
            [
                ("learner", "If we had more wine glasses, we could set the table properly for the reception."),
                ("system", "How many guests are you expecting for the function?"),
                ("learner", "About forty people are coming, but we only have twenty glasses."),
                ("system", "You could rent extra glassware from a catering service nearby."),
            ],
            [
                ("learner", "My aunt has collected crystal wine glasses from different countries."),
                ("system", "That is an interesting hobby. Does she display them somewhere?"),
                ("learner", "She keeps them in a wooden cabinet with glass doors in her living room."),
                ("system", "Crystal glassware can be quite valuable, so that is a wise choice."),
            ],
        ],
        "upper_intermediate": [
            [
                ("learner", "It is said that the shape of a wine glass can change how a drink tastes."),
                ("system", "That is true. The width of the rim affects how the liquid reaches your tongue."),
                ("learner", "I was told that wider glasses are preferred for drinks with strong aromas."),
                ("system", "Yes, a wider bowl allows the aroma to develop before you take a sip."),
            ],
            [
                ("learner", "The wine glasses that were ordered for the wedding have not arrived yet."),
                ("system", "When were they supposed to be delivered?"),
                ("learner", "They were expected three days ago, and the wedding is this Saturday."),
                ("system", "I would suggest calling the supplier immediately and arranging a backup plan."),
            ],
            [
                ("learner", "My friend mentioned that handblown wine glasses are considered more elegant."),
                ("system", "They are, because each piece is slightly unique due to the crafting process."),
                ("learner", "However, she also admitted that they are much more expensive than machine-made ones."),
                ("system", "That is the trade-off between artisan craftsmanship and mass production."),
            ],
        ],
        "advanced": [
            [
                ("learner", "Were it not for the fragility of fine crystal, wine glasses would be far more practical for everyday use."),
                ("system", "That is an interesting point. Do you think durability should take priority over aesthetics?"),
                ("learner", "I believe there is a balance to be struck, as tempered glass now offers both resilience and elegance."),
                ("system", "Indeed, material science has advanced to the point where compromise is no longer necessary."),
            ],
            [
                ("learner", "The cultural significance of glassware in hospitality rituals warrants more scholarly attention than it currently receives."),
                ("system", "That is a thought-provoking observation. Are you referring to any particular tradition?"),
                ("learner", "In South Indian households, the choice of vessel communicates respect toward the guest, whether it be brass, silver, or glass."),
                ("system", "You raise a valid point about how material culture encodes social hierarchies and values."),
            ],
            [
                ("learner", "I would argue that the wine glass has become a symbol of sophistication that transcends its functional purpose."),
                ("system", "That is a perspective shared by many design historians. What led you to this conclusion?"),
                ("learner", "Observing how restaurants use stemware to signal quality, even when serving simple beverages, convinced me."),
                ("system", "You have identified a fascinating example of how form influences perception independent of content."),
            ],
        ],
    },

    # ──────────────────────────────────────────────
    # CUP
    # ──────────────────────────────────────────────
    "cup": {
        "beginner": [
            [
                ("learner", "I need a cup of tea."),
                ("system", "Sure, I will make some tea for you."),
                ("learner", "Please add milk and sugar."),
                ("system", "Of course, that is how most people like it."),
            ],
            [
                ("learner", "This cup has a nice colour."),
                ("system", "Thank you, I bought it from a shop near my house."),
                ("learner", "I like the flower design on it."),
                ("system", "My grandmother painted those flowers herself."),
            ],
            [
                ("learner", "The cup is very hot right now."),
                ("system", "Be careful. Hold it by the handle."),
                ("learner", "I will wait for it to cool down."),
                ("system", "That is a good idea. You do not want to burn yourself."),
            ],
        ],
        "elementary": [
            [
                ("learner", "I was drinking coffee when my cup slipped from my hands."),
                ("system", "Did it spill everywhere? Coffee stains are hard to remove."),
                ("learner", "Yes, it spilled all over my white school uniform."),
                ("system", "Try soaking the stain in warm water with some lemon juice."),
            ],
            [
                ("learner", "My father is making filter coffee in a steel cup."),
                ("system", "South Indian filter coffee is famous all over the country."),
                ("learner", "He learned to make it from my grandfather many years ago."),
                ("system", "Family recipes are always the best. The taste is never the same elsewhere."),
            ],
            [
                ("learner", "We are buying new cups for our school canteen."),
                ("system", "What kind of cups are you looking for?"),
                ("learner", "We need steel cups because plastic ones are not allowed anymore."),
                ("system", "That is a good decision for both health and the environment."),
            ],
        ],
        "intermediate": [
            [
                ("learner", "I have always preferred drinking tea from a clay cup rather than a ceramic one."),
                ("system", "Clay cups do add a unique earthy flavour to the tea."),
                ("learner", "Whenever I visit the railway station, I make sure to buy tea in a kulhad."),
                ("system", "Those small clay cups are a beloved part of Indian tea culture."),
            ],
            [
                ("learner", "If I had brought my reusable cup, I would not have needed a disposable one."),
                ("system", "Carrying a reusable cup is a simple way to reduce waste."),
                ("learner", "I think every college student should keep one in their bag."),
                ("system", "Many cafes even offer a discount when you bring your own cup."),
            ],
            [
                ("learner", "The measuring cup I ordered online turned out to be much smaller than expected."),
                ("system", "Did you check the capacity before placing the order?"),
                ("learner", "I thought it was in millilitres, but it was actually listed in ounces."),
                ("system", "Unit conversions can be confusing when shopping from international sellers."),
            ],
        ],
        "upper_intermediate": [
            [
                ("learner", "It has been reported that disposable paper cups are lined with a thin layer of plastic."),
                ("system", "That is correct, which is why they cannot be recycled easily."),
                ("learner", "Many people are unaware that these cups end up in landfills rather than recycling centres."),
                ("system", "Raising awareness about this issue could encourage more people to switch to reusable alternatives."),
            ],
            [
                ("learner", "The tea that was served in the meeting room had already gone cold by the time I arrived."),
                ("system", "That tends to happen when meetings run longer than expected."),
                ("learner", "I was told that the chai had been prepared almost an hour before I got there."),
                ("system", "Perhaps an insulated flask would be a better option for serving tea during long meetings."),
            ],
            [
                ("learner", "A cup that my grandmother used for over thirty years finally cracked last month."),
                ("system", "That must have been difficult for her. Old belongings carry sentimental value."),
                ("learner", "She was quite upset because it was given to her as a wedding gift by her mother."),
                ("system", "Objects like that become part of our identity, and losing them feels like losing a memory."),
            ],
        ],
        "advanced": [
            [
                ("learner", "The humble teacup has served as a vehicle for diplomacy, commerce, and cultural exchange across centuries."),
                ("system", "That is a sweeping claim. Could you elaborate on a specific historical example?"),
                ("learner", "Consider how British tea culture, mediated through the teacup, was itself shaped by Chinese porcelain traditions."),
                ("system", "An excellent point that illustrates how material objects carry the traces of global interconnection."),
            ],
            [
                ("learner", "I contend that the ritual of sharing a cup of tea holds greater social significance in India than almost any other daily practice."),
                ("system", "That is a bold assertion. What evidence would you offer in support?"),
                ("learner", "From roadside chai stalls to corporate boardrooms, the act of offering tea signals hospitality and trust universally."),
                ("system", "You make a compelling case that this practice transcends class, region, and language in Indian society."),
            ],
            [
                ("learner", "Had the artisan not experimented with the glaze, this cup would never have acquired its distinctive crackle pattern."),
                ("system", "Accidental discoveries in ceramics have produced some of the most celebrated techniques."),
                ("learner", "It reminds me of how Japanese kintsugi embraces imperfection by repairing broken pottery with gold."),
                ("system", "Both traditions suggest that beauty can emerge from what might otherwise be considered a flaw or failure."),
            ],
        ],
    },

    # ──────────────────────────────────────────────
    # FORK
    # ──────────────────────────────────────────────
    "fork": {
        "beginner": [
            [
                ("learner", "I need a fork to eat noodles."),
                ("system", "Here is a fork. Be careful, the noodles are hot."),
                ("learner", "Thank you, this fork is very shiny."),
                ("system", "I cleaned all the cutlery this morning."),
            ],
            [
                ("learner", "Where is the fork on the table?"),
                ("system", "The fork goes on the left side of the plate."),
                ("learner", "I always forget which side it goes on."),
                ("system", "Just remember: fork and left both have four letters."),
            ],
            [
                ("learner", "This fork has four sharp points."),
                ("system", "Yes, those points are called prongs or tines."),
                ("learner", "I use a fork to eat my pasta."),
                ("system", "Forks are very useful for picking up slippery food."),
            ],
        ],
        "elementary": [
            [
                ("learner", "I was looking for a fork but I could only find spoons."),
                ("system", "Check the second drawer on the right. The forks are there."),
                ("learner", "I found them, but some of these forks are very old and bent."),
                ("system", "We should replace those. Bent forks are difficult to eat with."),
            ],
            [
                ("learner", "My little brother is learning to eat with a fork for the first time."),
                ("system", "How old is he? It can take some time to learn."),
                ("learner", "He is three years old and he keeps dropping the food."),
                ("system", "That is completely normal. Give him soft foods like banana pieces to practise with."),
            ],
            [
                ("learner", "We were setting the table and I placed the forks on the wrong side."),
                ("system", "Which side did you put them on?"),
                ("learner", "I put them on the right side, next to the knives."),
                ("system", "In Western table settings, forks go on the left. But honestly, it does not matter much at home."),
            ],
        ],
        "intermediate": [
            [
                ("learner", "I find it interesting that forks were not commonly used in Europe until the seventeenth century."),
                ("system", "That is true. Before that, most people ate with their hands or a knife."),
                ("learner", "In India, eating with hands is still considered perfectly normal and even preferable."),
                ("system", "Every culture has its own dining customs, and none is superior to another."),
            ],
            [
                ("learner", "If you twist the fork against the spoon, it becomes much easier to eat spaghetti."),
                ("system", "That is a technique many Italians use. Have you tried it?"),
                ("learner", "Yes, my cousin showed me when we went to an Italian restaurant in Chennai."),
                ("system", "It takes a little practice, but it keeps the noodles from falling off."),
            ],
            [
                ("learner", "The school canteen has started providing steel forks instead of plastic ones."),
                ("system", "That is a positive change. Was there a particular reason for the switch?"),
                ("learner", "Our eco club presented data on plastic waste to the principal, and she agreed immediately."),
                ("system", "Student initiatives like that can make a real difference in reducing environmental harm."),
            ],
        ],
        "upper_intermediate": [
            [
                ("learner", "It is often assumed that using a fork is the standard way to eat around the world."),
                ("system", "That is a common misconception. A large portion of the world eats with hands or chopsticks."),
                ("learner", "A study I read suggested that only about a third of the global population uses forks regularly."),
                ("system", "That statistic challenges the Eurocentric view that fork use represents civilised dining."),
            ],
            [
                ("learner", "The silver forks that were inherited from my great-grandmother are kept in a velvet-lined box."),
                ("system", "Silver cutlery requires special care to prevent tarnishing."),
                ("learner", "My mother was told by a jeweller that they should be polished with baking soda paste."),
                ("system", "That is an effective and inexpensive method that has been used for generations."),
            ],
            [
                ("learner", "A fork designed for eating salad is typically larger than one meant for desserts."),
                ("system", "Yes, cutlery sizes are matched to the type of course being served."),
                ("learner", "I find it bewildering that a formal Western dinner can require up to five different forks."),
                ("system", "The complexity of formal table settings can be intimidating, even for those who grew up with them."),
            ],
        ],
        "advanced": [
            [
                ("learner", "The fork's journey from a Byzantine curiosity to an indispensable Western utensil reveals much about cultural diffusion."),
                ("system", "Indeed. Its initial rejection in medieval Europe is a fascinating case of resistance to foreign customs."),
                ("learner", "One might argue that the fork's acceptance was less about practicality and more about evolving notions of refinement."),
                ("system", "That analysis aligns with Norbert Elias's theory of the civilising process and its emphasis on bodily restraint."),
            ],
            [
                ("learner", "Were designers to prioritise ergonomics over tradition, the standard fork might look quite different today."),
                ("system", "Adaptive cutlery for people with limited mobility already explores alternative fork designs."),
                ("learner", "It strikes me that mainstream design rarely incorporates insights from accessibility research until market forces demand it."),
                ("system", "You have identified a persistent tension between inclusive design principles and commercial conservatism."),
            ],
            [
                ("learner", "I would submit that the fork, as a dining instrument, has subtly shaped the way Western cuisines prepare and present food."),
                ("system", "Could you provide a specific example of how the fork influenced food preparation?"),
                ("learner", "The prevalence of bite-sized portions in European cuisine arguably developed because food needed to be manageable with fork tines."),
                ("system", "That is a persuasive argument, especially when contrasted with cultures where bread or hands serve as the primary eating tool."),
            ],
        ],
    },

    # ──────────────────────────────────────────────
    # KNIFE
    # ──────────────────────────────────────────────
    "knife": {
        "beginner": [
            [
                ("learner", "Please give me a knife to cut this."),
                ("system", "Here you go. Be careful with the sharp edge."),
                ("learner", "I will cut the bread into pieces."),
                ("system", "Good idea. Small pieces are easier to eat."),
            ],
            [
                ("learner", "This knife is not very sharp."),
                ("system", "You are right. It needs to be sharpened."),
                ("learner", "My father sharpens knives at home."),
                ("system", "That is a useful skill to have."),
            ],
            [
                ("learner", "The knife goes on the right side."),
                ("system", "Yes, next to the plate with the blade facing in."),
                ("learner", "I am learning to set the table."),
                ("system", "You are doing a very good job so far."),
            ],
        ],
        "elementary": [
            [
                ("learner", "My mother was chopping vegetables with a big knife yesterday."),
                ("system", "Was she making something special for dinner?"),
                ("learner", "She made sambar with lots of fresh vegetables from the market."),
                ("system", "Fresh vegetables make sambar taste so much better than frozen ones."),
            ],
            [
                ("learner", "I am using a butter knife to spread jam on my toast."),
                ("system", "Butter knives are safer because they are not very sharp."),
                ("learner", "I think children should always use butter knives instead of sharp ones."),
                ("system", "I agree. Safety in the kitchen is very important, especially for young people."),
            ],
            [
                ("learner", "We bought a new set of kitchen knives last weekend."),
                ("system", "Where did you buy them from?"),
                ("learner", "We found them at a stainless steel shop on Ranganathan Street."),
                ("system", "That area has some of the best kitchenware shops in the city."),
            ],
        ],
        "intermediate": [
            [
                ("learner", "If you hold the knife at the correct angle, cutting onions becomes much easier."),
                ("system", "That is true. A proper grip also prevents accidents."),
                ("learner", "My cooking teacher showed us the claw technique to protect our fingers."),
                ("system", "The claw grip is essential for safe knife work. It keeps fingertips tucked away."),
            ],
            [
                ("learner", "I have noticed that Japanese kitchen knives are sharpened on only one side."),
                ("system", "Yes, single-bevel knives are common in Japanese cuisine for precision cuts."),
                ("learner", "That must make a difference when cutting sashimi or thin vegetable slices."),
                ("system", "It does. The single bevel allows for incredibly thin, clean cuts that a double-bevel knife cannot achieve."),
            ],
            [
                ("learner", "The fruit vendor near our school cuts mangoes so quickly with his knife."),
                ("system", "Street vendors develop impressive knife skills through years of practice."),
                ("learner", "I asked him once, and he told me he has been cutting fruit for over twenty years."),
                ("system", "That level of experience turns a simple task into something that looks almost effortless."),
            ],
        ],
        "upper_intermediate": [
            [
                ("learner", "It is widely believed that a sharp knife is actually safer than a dull one."),
                ("system", "That sounds counterintuitive. Could you explain the reasoning?"),
                ("learner", "A dull knife requires more force, which makes it more likely to slip and cause injury."),
                ("system", "That makes perfect sense. Controlled, precise cuts are only possible with a well-maintained blade."),
            ],
            [
                ("learner", "The Swiss Army knife that my uncle brought from abroad was confiscated at the airport."),
                ("system", "Sharp objects are prohibited in carry-on luggage for security reasons."),
                ("learner", "He was told that it should have been packed in his checked baggage instead."),
                ("system", "It is an easy mistake to make, but airport security rules are strictly enforced everywhere."),
            ],
            [
                ("learner", "A traditional South Indian kitchen would have relied on an aruvamanai rather than a Western-style knife."),
                ("system", "The aruvamanai is a fascinating tool. It is essentially a blade mounted on a wooden base."),
                ("learner", "My grandmother still prefers it because she says it gives her more control over the cut."),
                ("system", "Many traditional tools are remarkably well-designed for their specific purpose and context."),
            ],
        ],
        "advanced": [
            [
                ("learner", "The knife occupies a peculiar position in human culture as both an essential tool and a symbol of danger."),
                ("system", "That duality is reflected in many cultural practices, from ceremonial daggers to kitchen rituals."),
                ("learner", "It is telling that the gesture of offering a knife handle-first is universally understood as a sign of peaceful intent."),
                ("system", "Such gestures demonstrate how deeply embedded our awareness of potential threat is in everyday etiquette."),
            ],
            [
                ("learner", "Had metallurgy not advanced beyond bronze, the evolution of cuisine would have been fundamentally constrained."),
                ("system", "The relationship between tool technology and culinary development is indeed underexplored."),
                ("learner", "Steel blades enabled the fine knife work that underpins French, Japanese, and Chinese culinary traditions alike."),
                ("system", "You have drawn a compelling connection between material science and the art of gastronomy."),
            ],
            [
                ("learner", "I would contend that the declining prevalence of knife skills in home cooking reflects a broader disconnection from food preparation."),
                ("system", "Do you attribute this to the rise of processed foods and kitchen gadgets?"),
                ("learner", "Partly, but I also think that urbanisation and shrinking kitchens have discouraged the kind of elaborate cooking that demands skilled knife work."),
                ("system", "Your analysis touches on how physical spaces and economic pressures shape culinary practices in profound ways."),
            ],
        ],
    },

    # ──────────────────────────────────────────────
    # SPOON
    # ──────────────────────────────────────────────
    "spoon": {
        "beginner": [
            [
                ("learner", "I eat rice with a spoon."),
                ("system", "A spoon is good for eating rice and dal."),
                ("learner", "This spoon is made of steel."),
                ("system", "Steel spoons are very common in Indian homes."),
            ],
            [
                ("learner", "Can I have a big spoon please?"),
                ("system", "Here is a serving spoon for you."),
                ("learner", "I want to serve myself some rasam."),
                ("system", "Be careful, the rasam is still very hot."),
            ],
            [
                ("learner", "My baby sister uses a small spoon."),
                ("system", "Baby spoons are small and soft for safety."),
                ("learner", "She likes to hold the spoon herself."),
                ("system", "That is wonderful. She is learning to eat on her own."),
            ],
        ],
        "elementary": [
            [
                ("learner", "I was stirring my coffee with a spoon when it fell into the cup."),
                ("system", "Was the spoon too small for the cup?"),
                ("learner", "Yes, I was using a teaspoon and the mug was very deep."),
                ("system", "A longer spoon would work better for tall mugs."),
            ],
            [
                ("learner", "My grandmother is feeding my cousin with a silver spoon."),
                ("system", "Is it his annaprasana ceremony today?"),
                ("learner", "Yes, it is his first rice-eating ceremony and the whole family came."),
                ("system", "The silver spoon is traditional for this occasion. What a lovely celebration."),
            ],
            [
                ("learner", "We did not have enough spoons for everyone at the picnic."),
                ("system", "How many people were there?"),
                ("learner", "There were twelve of us but we only brought eight spoons."),
                ("system", "Next time, it helps to count the spoons before packing the picnic basket."),
            ],
        ],
        "intermediate": [
            [
                ("learner", "I have been looking for a good set of measuring spoons for my baking projects."),
                ("system", "Accurate measurements are crucial in baking. Have you checked any kitchen supply stores?"),
                ("learner", "Most stores here sell cups and spoons in millilitres, which is what Indian recipes use."),
                ("system", "That is convenient. American recipes use cups and tablespoons, which can be confusing."),
            ],
            [
                ("learner", "If you heat a metal spoon in hot water, it conducts heat very quickly to your hand."),
                ("system", "That is basic thermodynamics. Metal is an excellent conductor of heat."),
                ("learner", "That explains why wooden spoons are preferred for stirring dishes on the stove."),
                ("system", "Exactly. Wood is a poor conductor, so the handle stays cool even when the food is boiling."),
            ],
            [
                ("learner", "The custom of tasting food with a separate spoon is more hygienic than tasting from the cooking spoon."),
                ("system", "Absolutely. Sharing utensils can spread germs easily."),
                ("learner", "My mother always keeps a small tasting spoon next to the stove for this reason."),
                ("system", "That is a simple habit that makes a big difference in kitchen hygiene."),
            ],
        ],
        "upper_intermediate": [
            [
                ("learner", "It is often said that someone born into privilege was born with a silver spoon in their mouth."),
                ("system", "That idiom dates back to at least the sixteenth century in English."),
                ("learner", "I find it fascinating how a simple kitchen utensil became a metaphor for wealth and social class."),
                ("system", "Everyday objects frequently acquire symbolic meaning through centuries of cultural usage."),
            ],
            [
                ("learner", "The spoons that were displayed at the folk art museum had been carved entirely by hand from coconut shell."),
                ("system", "Coconut shell crafts are a traditional art form in Kerala and Tamil Nadu."),
                ("learner", "The artisan was reported to have spent an entire day carving just one decorative spoon."),
                ("system", "That level of dedication highlights the patience and skill involved in preserving traditional craftsmanship."),
            ],
            [
                ("learner", "A spoon designed for left-handed users is angled differently from a standard right-handed one."),
                ("system", "That is an example of ergonomic design that most people never consider."),
                ("learner", "My left-handed friend mentioned that she had never encountered such a spoon until she visited a specialty store abroad."),
                ("system", "The needs of left-handed individuals are frequently overlooked in product design, which affects about ten percent of the population."),
            ],
        ],
        "advanced": [
            [
                ("learner", "The spoon is arguably the oldest and most universal eating utensil, predating both the fork and the chopstick."),
                ("system", "Archaeological evidence supports that claim, with shell and bone spoons found in Neolithic sites."),
                ("learner", "Its persistence across every known culture suggests that the spoon addresses a fundamental human need that no other tool satisfies."),
                ("system", "The ability to consume liquids and semi-solids efficiently is indeed a requirement that the spoon uniquely fulfils."),
            ],
            [
                ("learner", "I would argue that the transition from communal serving spoons to individual ones marked a pivotal shift in dining etiquette."),
                ("system", "That shift is closely linked to evolving ideas about personal hygiene and bodily boundaries."),
                ("learner", "It parallels the broader individualisation of eating practices that accompanied urbanisation and the nuclear family structure."),
                ("system", "Your observation connects material culture to social transformation in a way that is both insightful and well-supported."),
            ],
            [
                ("learner", "Were one to examine spoon design across cultures, one would discover that form is invariably dictated by the staple food of the region."),
                ("system", "Could you provide a specific comparison to illustrate that claim?"),
                ("learner", "The deep, rounded South Asian spoon for dal contrasts sharply with the flat, shallow Chinese soup spoon designed for broth with solids."),
                ("system", "That comparison elegantly demonstrates how culinary traditions and utensil design co-evolve in response to dietary patterns."),
            ],
        ],
    },

    # ──────────────────────────────────────────────
    # BOWL
    # ──────────────────────────────────────────────
    "bowl": {
        "beginner": [
            [
                ("learner", "I eat my cereal in a bowl."),
                ("system", "A bowl is perfect for cereal and milk."),
                ("learner", "This bowl is blue and round."),
                ("system", "It is a nice bowl. Do you use it every day?"),
            ],
            [
                ("learner", "Please pass me the soup bowl."),
                ("system", "Here it is. The tomato soup is ready."),
                ("learner", "The bowl feels warm in my hands."),
                ("system", "That is because the soup inside is very hot."),
            ],
            [
                ("learner", "My dog eats from a metal bowl."),
                ("system", "Metal bowls are strong and easy to clean."),
                ("learner", "I wash his bowl every evening."),
                ("system", "That is very responsible of you. Clean bowls keep pets healthy."),
            ],
        ],
        "elementary": [
            [
                ("learner", "I was carrying a bowl of sambar when I tripped on the step."),
                ("system", "Oh no! Did the sambar spill?"),
                ("learner", "Most of it spilled on the kitchen floor and it was very messy."),
                ("system", "Hot sambar can be dangerous. I hope you did not burn yourself."),
            ],
            [
                ("learner", "My mother is mixing the batter in a large steel bowl."),
                ("system", "Is she making dosa batter or something else?"),
                ("learner", "She is making idli batter because we have guests coming tomorrow morning."),
                ("system", "Homemade idlis are always softer and tastier than shop-bought ones."),
            ],
            [
                ("learner", "We bought a set of ceramic bowls at the Diwali sale."),
                ("system", "Ceramic bowls look beautiful on the dining table."),
                ("learner", "They came in different colours and each family member chose one."),
                ("system", "Having your own special bowl makes mealtimes more personal and fun."),
            ],
        ],
        "intermediate": [
            [
                ("learner", "I have started eating my meals from a smaller bowl to control portion sizes."),
                ("system", "Research shows that smaller plates and bowls can help people eat less."),
                ("learner", "It tricks the brain into thinking the portion is larger than it actually is."),
                ("system", "That is called the Delboeuf illusion, and it has been well documented in food psychology studies."),
            ],
            [
                ("learner", "If the singing bowl is struck gently, it produces a deep resonating tone."),
                ("system", "Singing bowls are used in meditation and sound therapy."),
                ("learner", "My yoga teacher uses one at the beginning and end of each session."),
                ("system", "The sustained vibration is said to promote relaxation and mental clarity."),
            ],
            [
                ("learner", "The traditional brass bowl used in Tamil temples has a very specific shape and purpose."),
                ("system", "Are you referring to the bowl used for offering prasadam?"),
                ("learner", "Yes, and also the ones used for abhishekam, which have a small spout for pouring."),
                ("system", "Temple vessels follow designs that have remained unchanged for hundreds of years."),
            ],
        ],
        "upper_intermediate": [
            [
                ("learner", "It has been suggested that bowl-based meals are inherently more balanced than plate-based ones."),
                ("system", "That is an interesting nutritional claim. What is the reasoning behind it?"),
                ("learner", "A bowl naturally layers grains, vegetables, and protein together, encouraging variety in a single serving."),
                ("system", "The popularity of poke bowls and Buddha bowls in modern cuisine seems to support that observation."),
            ],
            [
                ("learner", "The ancient pottery bowls that were excavated from the Indus Valley site are remarkably well preserved."),
                ("system", "The craftsmanship of Harappan pottery continues to impress archaeologists."),
                ("learner", "What struck me was that the shapes were so similar to bowls we still use in South Indian kitchens today."),
                ("system", "That continuity suggests that some functional designs are so effective that they persist across millennia."),
            ],
            [
                ("learner", "My neighbour was advised by her doctor to avoid eating from plastic bowls that are heated in the microwave."),
                ("system", "Certain plastics can release harmful chemicals when exposed to high temperatures."),
                ("learner", "She was told that glass or ceramic bowls are considered much safer for microwave use."),
                ("system", "That is sound advice, especially since many households use the microwave for reheating food daily."),
            ],
        ],
        "advanced": [
            [
                ("learner", "The bowl, as a vessel, embodies a paradox: it is defined as much by its emptiness as by what it contains."),
                ("system", "That observation resonates with Zen Buddhist philosophy, where the empty bowl symbolises openness and receptivity."),
                ("learner", "One might extend the metaphor to argue that a good student, like an empty bowl, must first be willing to receive before they can be filled."),
                ("system", "That is a profound pedagogical insight, and it appears across contemplative traditions from Taoism to Sufism."),
            ],
            [
                ("learner", "I would maintain that the communal serving bowl fosters a sense of shared sustenance that individual plating cannot replicate."),
                ("system", "That is a view strongly held in many collectivist cultures. Do you see it changing?"),
                ("learner", "Unfortunately, hygiene concerns accelerated by the pandemic have pushed even traditional households toward individual servings."),
                ("system", "The tension between communal warmth and individual safety is one that many societies are still navigating."),
            ],
            [
                ("learner", "Had the potter not understood the precise relationship between clay composition and firing temperature, these bowls would have cracked."),
                ("system", "Ceramic science involves a remarkable amount of empirical knowledge accumulated over generations."),
                ("learner", "It humbles me to consider that ancient potters mastered through intuition what modern engineers model with computational simulations."),
                ("system", "Your reflection highlights the sophistication of traditional knowledge systems that are too often dismissed as primitive."),
            ],
        ],
    },

    # ──────────────────────────────────────────────
    # BANANA
    # ──────────────────────────────────────────────
    "banana": {
        "beginner": [
            [
                ("learner", "I like to eat bananas every day."),
                ("system", "Bananas are a healthy and tasty fruit."),
                ("learner", "This banana is yellow and sweet."),
                ("system", "Yellow bananas are ripe and ready to eat."),
            ],
            [
                ("learner", "My mother packs a banana in my lunch box."),
                ("system", "That is a great snack for school."),
                ("learner", "I eat it during the break time."),
                ("system", "Bananas give you energy to study in the afternoon."),
            ],
            [
                ("learner", "There are many bananas on the table."),
                ("system", "We call a group of bananas a bunch."),
                ("learner", "Can I take one banana please?"),
                ("system", "Of course, help yourself to as many as you want."),
            ],
        ],
        "elementary": [
            [
                ("learner", "I was making a banana milkshake when the mixer stopped working."),
                ("system", "That is frustrating. Did you manage to fix it?"),
                ("learner", "My father checked it and found that the blade was stuck."),
                ("system", "Sometimes frozen banana pieces can jam the blades. Try cutting them smaller next time."),
            ],
            [
                ("learner", "We are buying bananas from the vendor outside the temple."),
                ("system", "Temple vendors usually sell pooja bananas. Are they for an offering?"),
                ("learner", "Yes, we need them for the navagraha pooja this evening."),
                ("system", "Small yellow bananas are traditionally used for temple offerings in Tamil Nadu."),
            ],
            [
                ("learner", "My grandmother made delicious banana chips during the last Onam festival."),
                ("system", "Kerala-style banana chips are famous throughout India."),
                ("learner", "She used raw bananas and fried them in coconut oil with a little salt."),
                ("system", "That combination of raw banana and coconut oil gives the chips their unique flavour."),
            ],
        ],
        "intermediate": [
            [
                ("learner", "I have read that India is the largest producer of bananas in the world."),
                ("system", "That is correct. Tamil Nadu alone produces a significant share of the national output."),
                ("learner", "It surprises me that such a common fruit has such enormous economic importance."),
                ("system", "Bananas are a staple food for millions and a major source of livelihood for farming communities."),
            ],
            [
                ("learner", "If you wrap banana stems around your garden plants, they retain moisture much better."),
                ("system", "That is an old agricultural technique. Does your family use it?"),
                ("learner", "My grandfather taught me this method when we were planting jasmine in our backyard."),
                ("system", "Traditional farming wisdom like that is based on generations of practical observation."),
            ],
            [
                ("learner", "The banana leaf meal I had at the wedding was the most satisfying lunch I have eaten this year."),
                ("system", "Banana leaf meals are a highlight of South Indian celebrations."),
                ("learner", "There were at least fifteen different items served, from avial to payasam."),
                ("system", "A well-laid banana leaf meal is a feast that engages all five senses."),
            ],
        ],
        "upper_intermediate": [
            [
                ("learner", "It is estimated that the Cavendish banana, which dominates global trade, is threatened by a fungal disease."),
                ("system", "You are referring to Panama disease Tropical Race 4. It is indeed a serious threat."),
                ("learner", "Scientists have warned that if a resistant variety is not developed soon, banana exports could collapse."),
                ("system", "The lack of genetic diversity in commercial banana cultivation makes the crop extremely vulnerable."),
            ],
            [
                ("learner", "The banana fibre sarees that are woven in some parts of Tamil Nadu were showcased at a recent craft exhibition."),
                ("system", "Banana fibre textiles are gaining attention as a sustainable alternative to synthetic fabrics."),
                ("learner", "The weaver I spoke with explained that extracting fibre from banana stems is an entirely manual process."),
                ("system", "That labour-intensive process is part of what makes these textiles valuable and difficult to scale commercially."),
            ],
            [
                ("learner", "My nutritionist recommended eating a banana before exercise because it provides sustained energy."),
                ("system", "Bananas are rich in potassium and natural sugars that fuel physical activity."),
                ("learner", "She mentioned that the combination of carbohydrates and potassium also helps prevent muscle cramps."),
                ("system", "That is why bananas are commonly seen at marathon aid stations around the world."),
            ],
        ],
        "advanced": [
            [
                ("learner", "The banana plant holds a singular position in South Indian culture, serving simultaneously as food, fibre, vessel, and sacred offering."),
                ("system", "Few plants are as comprehensively utilised. Can you think of a parallel in any other culture?"),
                ("learner", "The coconut palm comes close, but I would argue that the banana's role in ritual practice gives it an additional layer of cultural significance."),
                ("system", "Your comparison is apt, and it underscores how certain plants become embedded in the total fabric of a civilisation."),
            ],
            [
                ("learner", "I find it deeply ironic that the most widely consumed banana variety lacks the genetic diversity needed to survive a single determined pathogen."),
                ("system", "The Gros Michel banana's near-extinction in the 1950s should have served as a warning."),
                ("learner", "Yet commercial agriculture persisted with monoculture because uniformity was more profitable than resilience."),
                ("system", "Your critique touches on a fundamental flaw in industrial agriculture: the prioritisation of short-term efficiency over long-term sustainability."),
            ],
            [
                ("learner", "Were it not for the banana leaf's natural water-resistant properties, the tradition of serving festival meals on leaves might never have developed."),
                ("system", "Material properties often shape cultural practices in ways we take for granted."),
                ("learner", "Moreover, the leaf's mild aroma and the way it interacts with hot food subtly enhance the dining experience in ways that plates cannot."),
                ("system", "That multisensory dimension is precisely what makes banana leaf dining a practice that resists replacement by modern tableware."),
            ],
        ],
    },

    # ──────────────────────────────────────────────
    # APPLE
    # ──────────────────────────────────────────────
    "apple": {
        "beginner": [
            [
                ("learner", "I have a red apple in my bag."),
                ("system", "Red apples are sweet and crunchy."),
                ("learner", "I eat an apple after lunch every day."),
                ("system", "That is a very healthy habit to have."),
            ],
            [
                ("learner", "Can I have an apple please?"),
                ("system", "Sure, do you want a red one or a green one?"),
                ("learner", "I want the red apple. It looks fresh."),
                ("system", "Here you go. Wash it before you eat it."),
            ],
            [
                ("learner", "My teacher has an apple on her desk."),
                ("system", "Did someone give it to her as a gift?"),
                ("learner", "Yes, my friend brought it for her today."),
                ("system", "That is a sweet gesture. Teachers appreciate small kindnesses."),
            ],
        ],
        "elementary": [
            [
                ("learner", "I was eating an apple when I found a worm inside it."),
                ("system", "That must have been a shock. Did you throw it away?"),
                ("learner", "Yes, I felt so disgusted that I could not eat anything else."),
                ("system", "Organic apples sometimes have insects because they are grown without pesticides."),
            ],
            [
                ("learner", "My mother is making apple halwa for the festival tomorrow."),
                ("system", "Apple halwa sounds unusual. How is it made?"),
                ("learner", "She grates the apples and cooks them with ghee, sugar, and cardamom."),
                ("system", "That sounds delicious. I would love to try the recipe sometime."),
            ],
            [
                ("learner", "Apples from Kashmir are arriving in our local market this week."),
                ("system", "Kashmiri apples are known for their sweetness and firm texture."),
                ("learner", "My father always waits for the season because they taste much better than imported ones."),
                ("system", "Seasonal and local fruits are usually fresher and more affordable too."),
            ],
        ],
        "intermediate": [
            [
                ("learner", "I have been wondering why apples turn brown so quickly after you cut them."),
                ("system", "It is caused by oxidation. The flesh reacts with oxygen in the air."),
                ("learner", "My science teacher suggested squeezing lemon juice on the slices to slow the browning."),
                ("system", "The citric acid in lemon juice inhibits the enzyme responsible for oxidation."),
            ],
            [
                ("learner", "If Newton had not been sitting under that apple tree, would someone else have discovered gravity?"),
                ("system", "The story is likely apocryphal, but it raises an interesting question about scientific discovery."),
                ("learner", "I think someone else would have eventually reached the same conclusion through different observations."),
                ("system", "Most historians of science agree that major discoveries tend to emerge when the conditions are right, regardless of the individual."),
            ],
            [
                ("learner", "The phrase an apple a day keeps the doctor away has been around for over a hundred years."),
                ("system", "It originated in Wales in the 1860s, though the exact wording has changed over time."),
                ("learner", "While apples are certainly nutritious, I doubt any single food can guarantee good health."),
                ("system", "You are right. A balanced diet with variety is far more important than relying on any one food."),
            ],
        ],
        "upper_intermediate": [
            [
                ("learner", "It is often overlooked that apple cultivation in India is concentrated in just a few northern states."),
                ("system", "Himachal Pradesh and Jammu and Kashmir account for the vast majority of production."),
                ("learner", "Climate change has been reported to be shifting the viable growing zones higher into the mountains."),
                ("system", "Farmers in traditional apple-growing regions have already noticed reduced yields due to warmer winters."),
            ],
            [
                ("learner", "The apples that were sold to us as organic turned out to have been treated with a wax coating."),
                ("system", "Wax coatings are used to extend shelf life and improve appearance."),
                ("learner", "A consumer advocacy group revealed that the labelling standards for organic produce are poorly enforced in India."),
                ("system", "Stricter regulation and transparent certification would help consumers make informed choices."),
            ],
            [
                ("learner", "My friend was told by her dentist that eating apples is beneficial for oral health."),
                ("system", "The fibrous texture of apples helps clean teeth and stimulate the gums."),
                ("learner", "However, she was also cautioned that the natural sugars in apples can contribute to decay if teeth are not brushed."),
                ("system", "That nuance is important and illustrates why nutrition advice should always be considered in context."),
            ],
        ],
        "advanced": [
            [
                ("learner", "The apple's journey from the wild forests of Kazakhstan to supermarket shelves worldwide is a remarkable story of co-evolution with humans."),
                ("system", "The genetic origins of the domestic apple in Central Asia have only recently been confirmed through DNA analysis."),
                ("learner", "What fascinates me is that every named apple variety is essentially a clone, propagated through grafting rather than seed."),
                ("system", "That dependence on clonal propagation creates the same vulnerability to disease that afflicts other monoculture crops."),
            ],
            [
                ("learner", "I would submit that the symbolic weight of the apple in Western mythology has no equivalent in Indian cultural narratives."),
                ("system", "That is an intriguing cross-cultural observation. The apple features in Greek, Norse, and Judeo-Christian mythology prominently."),
                ("learner", "In Indian tradition, the mango arguably occupies the analogous symbolic space as a fruit associated with desire, fertility, and abundance."),
                ("system", "Your parallel is illuminating and suggests that cultures assign mythological significance to whichever fruit is central to their agrarian life."),
            ],
            [
                ("learner", "Had colonial administrators not introduced apple orchards in Himachal Pradesh, the economic landscape of the region would be unrecognisable today."),
                ("system", "The Stokes family's role in establishing apple cultivation in Kotgarh is well documented."),
                ("learner", "It is a complex legacy, as the prosperity brought by apple farming is inseparable from the colonial enterprise that initiated it."),
                ("system", "You have articulated a nuance that is often absent from celebratory accounts of agricultural development in India."),
            ],
        ],
    },

    # ──────────────────────────────────────────────
    # SANDWICH
    # ──────────────────────────────────────────────
    "sandwich": {
        "beginner": [
            [
                ("learner", "I want a cheese sandwich please."),
                ("system", "Sure, would you like it toasted or plain?"),
                ("learner", "I want it toasted with butter."),
                ("system", "Coming right up. Toasted sandwiches taste the best."),
            ],
            [
                ("learner", "My sandwich has tomato and cucumber."),
                ("system", "That sounds fresh and healthy."),
                ("learner", "I made it by myself this morning."),
                ("system", "Well done! Making your own food is a great skill."),
            ],
            [
                ("learner", "There is a sandwich shop near my school."),
                ("system", "Do you buy sandwiches from there often?"),
                ("learner", "I go there with my friends on Fridays."),
                ("system", "Friday treats with friends make the week feel complete."),
            ],
        ],
        "elementary": [
            [
                ("learner", "I was eating my sandwich on the bus when it fell apart."),
                ("system", "Eating on a moving bus can be tricky. What happened?"),
                ("learner", "The filling came out and landed on my school trousers."),
                ("system", "That sounds embarrassing. Maybe wrap sandwiches tightly in foil next time."),
            ],
            [
                ("learner", "My mother is making a chutney sandwich for my trip tomorrow."),
                ("system", "Green chutney sandwiches are a Mumbai specialty. Does she make them often?"),
                ("learner", "She makes them whenever we travel because they are easy to carry."),
                ("system", "Sandwiches are ideal travel food because they do not need reheating."),
            ],
            [
                ("learner", "We tried a new sandwich at the bakery last weekend."),
                ("system", "What was in it?"),
                ("learner", "It had grilled paneer with mint sauce and lots of vegetables."),
                ("system", "That sounds like a filling and delicious combination."),
            ],
        ],
        "intermediate": [
            [
                ("learner", "I have always thought that the best sandwiches are the simplest ones."),
                ("system", "Many people share that view. What is your favourite simple sandwich?"),
                ("learner", "Bread, butter, and jam is all I need, especially with fresh white bread."),
                ("system", "Sometimes the classics are classics for a reason. Simplicity allows each ingredient to shine."),
            ],
            [
                ("learner", "If you toast the bread before adding the filling, the sandwich stays crisp much longer."),
                ("system", "That is a useful tip. Soggy sandwiches are not very appetising."),
                ("learner", "My hostel roommate taught me this trick because our lunch break was four hours after packing."),
                ("system", "Practical solutions like that come from real experience with everyday problems."),
            ],
            [
                ("learner", "The Bombay sandwich is quite different from anything you would find in a Western country."),
                ("system", "What makes it distinctly Indian?"),
                ("learner", "The layers of beetroot, potato, and green chutney with masala give it a uniquely spicy character."),
                ("system", "It is a perfect example of how a global food concept gets adapted to local tastes and ingredients."),
            ],
        ],
        "upper_intermediate": [
            [
                ("learner", "It is believed that the sandwich was named after the Earl of Sandwich, who wanted to eat without leaving his card table."),
                ("system", "That origin story is widely cited, though some historians question its accuracy."),
                ("learner", "Regardless of the true origin, the concept of placing food between bread existed long before the eighteenth century."),
                ("system", "Middle Eastern flatbreads with fillings predate the European sandwich by centuries, if not millennia."),
            ],
            [
                ("learner", "The sandwiches that were prepared for the school sports day were finished within the first hour."),
                ("system", "How many sandwiches had been made?"),
                ("learner", "Three hundred were prepared, but the organisers were told that at least five hundred were needed."),
                ("system", "Underestimating food requirements for large events is a common planning mistake."),
            ],
            [
                ("learner", "A nutritionist I consulted recommended replacing white bread with whole wheat for my daily sandwiches."),
                ("system", "Whole wheat bread has more fibre and a lower glycaemic index."),
                ("learner", "She explained that the refined flour in white bread causes a rapid spike in blood sugar levels."),
                ("system", "Small dietary changes like that can have a significant impact on long-term health."),
            ],
        ],
        "advanced": [
            [
                ("learner", "The sandwich epitomises the modern imperative to eat quickly, efficiently, and with minimal disruption to productivity."),
                ("system", "That is a sharp cultural critique. Do you see the sandwich as symptomatic of a broader problem?"),
                ("learner", "I do. The fact that we celebrate a food designed to avoid pausing work reveals how deeply we have internalised the values of constant productivity."),
                ("system", "Your analysis echoes concerns raised by the slow food movement, which advocates for mindful eating as an act of resistance."),
            ],
            [
                ("learner", "Were one to trace the globalisation of the sandwich, one would find that its spread closely mirrors the expansion of British colonial influence."),
                ("system", "That is an astute observation. The sandwich arrived in India through the British Raj."),
                ("learner", "Yet Indian adaptations like the Bombay sandwich and the bread pakora have so thoroughly localised the concept that its colonial origins are largely forgotten."),
                ("system", "That process of cultural absorption and transformation is characteristic of how colonised societies reclaim imported practices on their own terms."),
            ],
            [
                ("learner", "I contend that the sandwich's greatest virtue is its democratic accessibility, requiring neither special equipment nor culinary expertise."),
                ("system", "That accessibility has made it a staple across socioeconomic classes worldwide."),
                ("learner", "From a street vendor's egg sandwich in Chennai to an elaborate club sandwich in a five-star hotel, the underlying structure remains identical."),
                ("system", "You have elegantly captured how a single culinary form can span the entire spectrum of class and context without losing its essential identity."),
            ],
        ],
    },

    # ──────────────────────────────────────────────
    # ORANGE
    # ──────────────────────────────────────────────
    "orange": {
        "beginner": [
            [
                ("learner", "I have an orange in my lunch box."),
                ("system", "Oranges are full of vitamin C."),
                ("learner", "It is round and bright orange."),
                ("system", "Can you peel it by yourself?"),
            ],
            [
                ("learner", "I like to drink orange juice."),
                ("system", "Fresh orange juice is better than packaged juice."),
                ("learner", "My mother squeezes oranges every morning."),
                ("system", "You are lucky to have fresh juice every day."),
            ],
            [
                ("learner", "The orange tastes sweet and sour."),
                ("system", "That mix of flavours is what makes oranges special."),
                ("learner", "I share my orange with my friend."),
                ("system", "Sharing food with friends is a lovely thing to do."),
            ],
        ],
        "elementary": [
            [
                ("learner", "I was peeling an orange and the juice squirted into my eye."),
                ("system", "That must have stung! Did you rinse your eye with water?"),
                ("learner", "Yes, my teacher helped me wash it and I felt better after a few minutes."),
                ("system", "Orange peel oil can be quite irritating. It happens to everyone sometimes."),
            ],
            [
                ("learner", "We are buying Nagpur oranges because they are in season right now."),
                ("system", "Nagpur is called the Orange City of India for good reason."),
                ("learner", "My uncle lives in Nagpur and he sends us a box every December."),
                ("system", "Getting a box of fresh oranges from Nagpur must be a wonderful treat."),
            ],
            [
                ("learner", "My little sister painted an orange in her art class today."),
                ("system", "That is a common subject for still life paintings."),
                ("learner", "She used three different shades to show the light and shadow."),
                ("system", "That shows good observation skills. Your sister has a talent for art."),
            ],
        ],
        "intermediate": [
            [
                ("learner", "I have often wondered whether the fruit was named after the colour or the colour after the fruit."),
                ("system", "Historically, the fruit came first. The English word for the colour came from the fruit's name."),
                ("learner", "That is surprising because it seems so natural to assume that colours are named independently."),
                ("system", "Before the word orange entered English, the colour was simply described as a shade of red."),
            ],
            [
                ("learner", "If you add orange peel to your compost, it takes longer to decompose than other fruit scraps."),
                ("system", "Citrus peels contain oils that slow down decomposition. Did you learn this in your gardening class?"),
                ("learner", "Yes, our teacher told us to chop the peels into small pieces to speed up the process."),
                ("system", "Composting is a valuable skill. Reducing kitchen waste benefits both your garden and the environment."),
            ],
            [
                ("learner", "Cough syrups with orange flavour are easier for children to take than bitter medicines."),
                ("system", "Flavouring is important for paediatric medicines to ensure compliance."),
                ("learner", "My pharmacy professor mentioned that orange is the most popular masking flavour in liquid medications."),
                ("system", "Its strong, sweet taste effectively covers the bitterness of many active pharmaceutical ingredients."),
            ],
        ],
        "upper_intermediate": [
            [
                ("learner", "It is widely reported that the nutritional value of commercially grown oranges has declined over the past fifty years."),
                ("system", "Some studies attribute this to soil depletion caused by intensive farming practices."),
                ("learner", "A food scientist I read about argued that modern varieties are bred for size and shelf life rather than nutrient content."),
                ("system", "That trade-off between commercial viability and nutritional quality is a recurring issue in industrial agriculture."),
            ],
            [
                ("learner", "The orange groves that once surrounded the town have been converted into residential developments."),
                ("system", "Urban expansion frequently comes at the cost of agricultural land."),
                ("learner", "Residents were told that the land had been rezoned for housing, and very few opposed the decision."),
                ("system", "The economic pressures driving land conversion are difficult to resist, especially when housing demand is high."),
            ],
            [
                ("learner", "My grandmother insists that oranges eaten cold from the refrigerator have less flavour than those kept at room temperature."),
                ("system", "There is scientific support for that claim. Cold temperatures suppress volatile aroma compounds."),
                ("learner", "She was always considered old-fashioned, but it turns out her instinct was based on genuine sensory perception."),
                ("system", "Traditional knowledge frequently anticipates what science later confirms through controlled experiments."),
            ],
        ],
        "advanced": [
            [
                ("learner", "The global orange juice industry exemplifies how a perishable local product was transformed into a commodified global staple through technological innovation."),
                ("system", "Frozen concentrate technology in the 1940s was the pivotal development. What aspect interests you most?"),
                ("learner", "The disconnect between the marketed image of fresh-squeezed naturalness and the industrial reality of flavour packs and year-long storage."),
                ("system", "You have identified a tension that applies broadly to processed foods marketed under the guise of freshness."),
            ],
            [
                ("learner", "Were it not for the Silk Road and subsequent maritime trade routes, citrus fruits might never have reached the Mediterranean basin."),
                ("system", "The diffusion of citrus from Southeast Asia is indeed a remarkable chapter in agricultural history."),
                ("learner", "What I find most compelling is how each culture that adopted the orange transformed it into something distinctly its own, from Seville marmalade to Indian mosambi juice."),
                ("system", "That pattern of adoption and adaptation is one of the most consistent themes in the history of food globalisation."),
            ],
            [
                ("learner", "I would argue that the orange has been unfairly reduced to a mere vehicle for vitamin C in popular nutrition discourse."),
                ("system", "That reductive view does overlook its rich phytochemical profile."),
                ("learner", "Beyond ascorbic acid, oranges contain flavonoids, carotenoids, and fibre that collectively contribute to health in ways that a vitamin supplement cannot replicate."),
                ("system", "Your point underscores a fundamental principle of nutrition: whole foods offer synergistic benefits that isolated nutrients cannot match."),
            ],
        ],
    },

    # ──────────────────────────────────────────────
    # BROCCOLI
    # ──────────────────────────────────────────────
    "broccoli": {
        "beginner": [
            [
                ("learner", "This broccoli looks like a small tree."),
                ("system", "Many children think broccoli looks like tiny trees."),
                ("learner", "I eat broccoli with my dinner."),
                ("system", "That is great. Broccoli is very good for you."),
            ],
            [
                ("learner", "The broccoli is green and fresh."),
                ("system", "Fresh broccoli should be firm and dark green."),
                ("learner", "My mother cooks it with garlic."),
                ("system", "Garlic and broccoli taste wonderful together."),
            ],
            [
                ("learner", "I do not like broccoli very much."),
                ("system", "Have you tried it with cheese sauce?"),
                ("learner", "No, but that sounds really good."),
                ("system", "Cheese makes broccoli tastier for many people."),
            ],
        ],
        "elementary": [
            [
                ("learner", "I was helping my mother wash broccoli when I found a caterpillar in it."),
                ("system", "That happens sometimes with fresh vegetables from the market."),
                ("learner", "I screamed and dropped the broccoli into the sink."),
                ("system", "Soaking vegetables in salt water for ten minutes helps remove hidden insects."),
            ],
            [
                ("learner", "Our school lunch included broccoli soup for the first time today."),
                ("system", "How did the students react to it?"),
                ("learner", "Most of my classmates did not want to try it, but I thought it was delicious."),
                ("system", "Being open to trying new foods is a wonderful quality."),
            ],
            [
                ("learner", "My father started adding broccoli to our meals after the doctor told him to eat more greens."),
                ("system", "Broccoli is one of the most nutritious green vegetables available."),
                ("learner", "He stir-fries it with soy sauce and it tastes better than I expected."),
                ("system", "A good sauce or seasoning can make any vegetable enjoyable."),
            ],
        ],
        "intermediate": [
            [
                ("learner", "I have noticed that broccoli was not common in Indian markets even ten years ago."),
                ("system", "You are right. It became widely available only after supermarket chains expanded."),
                ("learner", "Now even street vendors in our neighbourhood sell broccoli alongside traditional Indian vegetables."),
                ("system", "Globalisation of food supply chains has dramatically changed what is available in local markets."),
            ],
            [
                ("learner", "If you overcook broccoli, it turns mushy and loses most of its nutrients."),
                ("system", "Steaming for just three to four minutes preserves both texture and vitamins."),
                ("learner", "My cooking class teacher told us that blanching and shocking in ice water keeps the colour bright."),
                ("system", "That technique is used in restaurant kitchens to maintain the vibrant green appearance."),
            ],
            [
                ("learner", "Some researchers believe that broccoli contains compounds that may help prevent certain types of cancer."),
                ("system", "Sulforaphane, found in broccoli, has shown promise in laboratory studies."),
                ("learner", "However, my biology teacher cautioned us that laboratory results do not always translate to real-world benefits."),
                ("system", "That is an important distinction. Nutrition science requires careful interpretation of evidence."),
            ],
        ],
        "upper_intermediate": [
            [
                ("learner", "It has been observed that children who are exposed to a variety of vegetables early tend to be less fussy eaters later."),
                ("system", "Early exposure does seem to shape food preferences. Is that relevant to your experience?"),
                ("learner", "My parents introduced broccoli to me when I was very young, and I have enjoyed it ever since."),
                ("system", "Your experience aligns with research on the critical period for developing dietary habits in childhood."),
            ],
            [
                ("learner", "A report published last month revealed that pesticide residues were found on a significant percentage of broccoli samples tested in Indian markets."),
                ("system", "That is concerning. Were the levels above the permitted safety limits?"),
                ("learner", "Some samples exceeded the maximum residue limits, and consumers were advised to wash produce thoroughly."),
                ("system", "Regulatory oversight of pesticide use needs to be strengthened to protect public health."),
            ],
            [
                ("learner", "The broccoli that was grown in our school garden turned out smaller than the ones sold in shops."),
                ("system", "Home-grown vegetables are often smaller because they lack the intensive fertilisation used in commercial farming."),
                ("learner", "Our teacher explained that the flavour is often more concentrated in smaller, naturally grown specimens."),
                ("system", "That is frequently the case, as commercial varieties are optimised for size and uniformity rather than taste."),
            ],
        ],
        "advanced": [
            [
                ("learner", "Broccoli's relatively recent arrival in the Indian culinary landscape offers an interesting case study in dietary globalisation."),
                ("system", "What specific aspect of its adoption do you find most noteworthy?"),
                ("learner", "The speed with which it has been assimilated into Indian cooking, appearing in everything from gobi-style preparations to fusion stir-fries."),
                ("system", "That adaptability reflects the remarkable flexibility of Indian cuisine, which has historically absorbed ingredients from diverse sources."),
            ],
            [
                ("learner", "I would contend that the cultural resistance to broccoli among some populations is less about taste and more about unfamiliarity."),
                ("system", "The neophobia hypothesis suggests that humans are predisposed to distrust unfamiliar foods."),
                ("learner", "Repeated exposure and positive social modelling have been shown to overcome that initial aversion more effectively than nutritional education alone."),
                ("system", "Your point has significant implications for public health campaigns that rely heavily on information rather than behavioural strategies."),
            ],
            [
                ("learner", "Had plant breeders not developed broccoli from the wild cabbage ancestor through centuries of selective cultivation, we would lack one of our most nutrient-dense vegetables."),
                ("system", "The entire Brassica oleracea family, including cauliflower, kale, and Brussels sprouts, originated from the same wild plant."),
                ("learner", "It is a testament to the power of artificial selection that such dramatically different vegetables share a single progenitor species."),
                ("system", "Darwin himself used Brassica as a compelling example of variation under domestication in his foundational work."),
            ],
        ],
    },

    # ──────────────────────────────────────────────
    # CARROT
    # ──────────────────────────────────────────────
    "carrot": {
        "beginner": [
            [
                ("learner", "This carrot is long and orange."),
                ("system", "Carrots come in orange, red, and even purple."),
                ("learner", "I like to eat raw carrots."),
                ("system", "Raw carrots are crunchy and sweet."),
            ],
            [
                ("learner", "My rabbit likes to eat carrots."),
                ("system", "Rabbits love carrots, but they should not eat too many."),
                ("learner", "I give him one carrot every day."),
                ("system", "That is a good amount. Too many can upset their tummy."),
            ],
            [
                ("learner", "We use carrots to make halwa."),
                ("system", "Carrot halwa is a very popular Indian sweet."),
                ("learner", "My grandmother makes the best halwa."),
                ("system", "Grandmothers always have the best recipes."),
            ],
        ],
        "elementary": [
            [
                ("learner", "I was grating carrots for halwa and I scraped my knuckle on the grater."),
                ("system", "Ouch! Graters can be dangerous if you are not careful."),
                ("learner", "My mother put a bandage on it and told me to stop grating near the end of the carrot."),
                ("system", "Good advice. Always leave a small piece rather than grating it down to your fingers."),
            ],
            [
                ("learner", "Our science teacher brought a carrot to class to show us how plants store food."),
                ("system", "The carrot root stores energy in the form of sugars and starches."),
                ("learner", "She cut it in half and showed us the different layers inside."),
                ("system", "The outer layer and the inner core have different textures and colours, which shows the internal structure."),
            ],
            [
                ("learner", "We planted carrot seeds in our terrace garden two months ago."),
                ("system", "Have the carrots started growing yet?"),
                ("learner", "The green tops are visible but we have not pulled them out to check the roots."),
                ("system", "Carrots usually take about three months to fully develop underground."),
            ],
        ],
        "intermediate": [
            [
                ("learner", "I have read that carrots were originally purple before the orange variety became dominant."),
                ("system", "That is correct. Dutch farmers in the seventeenth century popularised the orange carrot."),
                ("learner", "Some people say it was to honour the Dutch royal family, the House of Orange."),
                ("system", "That story is popular but debated. The orange variety may have simply been sweeter and more appealing."),
            ],
            [
                ("learner", "If you cook carrots, your body absorbs more beta-carotene than from raw ones."),
                ("system", "Cooking breaks down the cell walls and makes the nutrients more accessible."),
                ("learner", "But my nutritionist said that raw carrots have more vitamin C because heat destroys it."),
                ("system", "Both raw and cooked carrots have benefits, which is why including both in your diet is ideal."),
            ],
            [
                ("learner", "The gajar ka halwa at our neighbourhood sweet shop sells out every evening during winter."),
                ("system", "Winter is peak carrot season, and fresh red carrots make the best halwa."),
                ("learner", "The owner told me his recipe uses only khoya, sugar, and cardamom, with no artificial colour."),
                ("system", "The natural deep red colour of Indian carrots makes artificial colouring completely unnecessary."),
            ],
        ],
        "upper_intermediate": [
            [
                ("learner", "It was once believed that eating large quantities of carrots could significantly improve night vision."),
                ("system", "That myth was actually promoted by British propaganda during World War Two."),
                ("learner", "The real purpose was to conceal the development of radar technology by attributing pilot accuracy to carrot consumption."),
                ("system", "It is a remarkable example of how wartime misinformation can become embedded in popular culture for decades."),
            ],
            [
                ("learner", "The organic carrots that were tested in a recent study showed higher levels of certain antioxidants than conventionally grown ones."),
                ("system", "Some studies do find nutritional differences, though the evidence is not conclusive across all nutrients."),
                ("learner", "Critics of the study pointed out that the sample size was too small to draw definitive conclusions."),
                ("system", "Methodological limitations like that are common in nutrition research and should always be acknowledged."),
            ],
            [
                ("learner", "A farmer I interviewed for my school project explained that carrots grow best in loose, sandy soil."),
                ("system", "Compacted soil causes carrots to grow stunted or misshapen."),
                ("learner", "He mentioned that adding river sand to clay-heavy soil in Tamil Nadu improved his yield dramatically."),
                ("system", "Adapting farming techniques to local soil conditions is essential for successful vegetable cultivation."),
            ],
        ],
        "advanced": [
            [
                ("learner", "The carrot's transformation from a tough, bitter root to the sweet, tender vegetable we know today is a testament to the cumulative power of selective breeding."),
                ("system", "Centuries of deliberate selection have altered nearly every characteristic of the original wild carrot."),
                ("learner", "What strikes me is that this process occurred without any understanding of genetics, relying entirely on empirical observation and patient iteration."),
                ("system", "Pre-scientific plant breeding achieved outcomes that rival modern biotechnology in their transformative scope."),
            ],
            [
                ("learner", "I would argue that the carrot halwa tradition in North India represents a sophisticated example of culinary alchemy, transforming a humble root into an indulgent dessert."),
                ("system", "The slow reduction process concentrates flavours and sugars in a way that is technically demanding."),
                ("learner", "The patience required, often hours of continuous stirring, imbues the dish with a cultural significance that transcends its ingredients."),
                ("system", "You have articulated how labour-intensive preparation elevates a dish from mere sustenance to an expression of care and celebration."),
            ],
            [
                ("learner", "Were the global food system to prioritise nutrient density over caloric yield, root vegetables like the carrot would assume far greater agricultural importance."),
                ("system", "Current agricultural incentives do favour high-calorie staples like wheat and rice over nutrient-dense vegetables."),
                ("learner", "Reforming subsidy structures to reward nutritional quality could simultaneously address malnutrition and encourage crop diversity."),
                ("system", "That policy recommendation aligns with proposals from several international food security organisations, though implementation remains politically challenging."),
            ],
        ],
    },

    # ──────────────────────────────────────────────
    # HOT DOG
    # ──────────────────────────────────────────────
    "hot dog": {
        "beginner": [
            [
                ("learner", "I see a hot dog on the plate."),
                ("system", "A hot dog has a sausage inside a long bun."),
                ("learner", "I want ketchup on my hot dog."),
                ("system", "Here is the ketchup bottle. Squeeze it gently."),
            ],
            [
                ("learner", "This is my first time eating a hot dog."),
                ("system", "How do you like it? Is it tasty?"),
                ("learner", "It is good but a little spicy."),
                ("system", "The mustard makes it spicy. Try it with just ketchup."),
            ],
            [
                ("learner", "My friend brought hot dogs to the picnic."),
                ("system", "Hot dogs are easy to eat outdoors."),
                ("learner", "We ate them in the park after playing."),
                ("system", "That sounds like a fun day with friends."),
            ],
        ],
        "elementary": [
            [
                ("learner", "I was eating a hot dog at the fair when the sausage slipped out of the bun."),
                ("system", "That always happens when you take too big a bite."),
                ("learner", "It fell right onto my new shoes and left a mustard stain."),
                ("system", "Mustard stains are tough to remove. Try rubbing the spot with vinegar and water."),
            ],
            [
                ("learner", "My father is grilling chicken hot dogs for the birthday party."),
                ("system", "Chicken hot dogs are a popular choice in India since many families do not eat pork or beef."),
                ("learner", "He added some Indian spices to the marinade to give them extra flavour."),
                ("system", "That is a creative twist. Fusion food often tastes better than the original."),
            ],
            [
                ("learner", "We saw a hot dog cart outside the cinema last Saturday."),
                ("system", "Street food carts near cinemas are always popular."),
                ("learner", "The vendor was putting lots of onions and green chutney on each hot dog."),
                ("system", "That is a very Indian take on a Western snack. I bet it tasted amazing."),
            ],
        ],
        "intermediate": [
            [
                ("learner", "I have heard that hot dogs are one of the most popular street foods in America."),
                ("system", "They are, especially at baseball games and city street corners."),
                ("learner", "It is interesting how such a simple food has become deeply embedded in American culture."),
                ("system", "Food identity is often shaped by what is cheap, portable, and widely available."),
            ],
            [
                ("learner", "If you read the ingredient list on a packaged hot dog, you might be surprised by what it contains."),
                ("system", "Processed meats often contain preservatives, fillers, and high levels of sodium."),
                ("learner", "My health science teacher used hot dogs as an example to teach us about reading food labels."),
                ("system", "Understanding food labels is an essential life skill that helps people make informed dietary choices."),
            ],
            [
                ("learner", "The vegetarian hot dog I tried at the new cafe was surprisingly close in taste to the real thing."),
                ("system", "Plant-based meat alternatives have improved dramatically in recent years."),
                ("learner", "My friend, who is a strict vegetarian, said it was the first time she could enjoy something like a hot dog."),
                ("system", "Inclusive food options allow everyone to participate in shared dining experiences regardless of dietary restrictions."),
            ],
        ],
        "upper_intermediate": [
            [
                ("learner", "It is frequently argued that processed meats like hot dogs are linked to increased health risks."),
                ("system", "The World Health Organisation has classified processed meat as a Group 1 carcinogen."),
                ("learner", "That classification caused widespread alarm, but many people misunderstood what Group 1 actually means."),
                ("system", "Group 1 refers to the strength of evidence, not the degree of risk, which is a crucial distinction often lost in media coverage."),
            ],
            [
                ("learner", "The hot dog eating contest held annually in New York has been described as both entertaining and disturbing."),
                ("system", "Competitive eating events attract large audiences but also face criticism."),
                ("learner", "Some commentators have argued that glorifying excessive consumption is irresponsible in a world where millions go hungry."),
                ("system", "That ethical tension between entertainment and social responsibility is a valid concern that deserves thoughtful debate."),
            ],
            [
                ("learner", "A food historian I listened to on a podcast traced the hot dog's origins to German immigrants in nineteenth-century America."),
                ("system", "The frankfurter and the wiener both have German and Austrian roots."),
                ("learner", "She explained that the bread bun was added by American vendors to make the sausage easier to eat while walking."),
                ("system", "That practical innovation is what transformed a European sausage into a distinctly American street food."),
            ],
        ],
        "advanced": [
            [
                ("learner", "The hot dog serves as an unexpectedly rich lens through which to examine the intersections of immigration, industrialisation, and American identity."),
                ("system", "Its history does encapsulate many of the defining forces of modern American society."),
                ("learner", "German immigrants brought the sausage, industrial meatpacking made it affordable, and baseball stadiums turned it into a national symbol."),
                ("system", "Your synthesis demonstrates how a seemingly trivial food item can illuminate broad historical and sociological patterns."),
            ],
            [
                ("learner", "Were consumers fully aware of the industrial processes behind mass-produced hot dogs, demand might shift significantly toward artisanal alternatives."),
                ("system", "Transparency in food production is a growing consumer concern, particularly among younger demographics."),
                ("learner", "Yet the price differential between artisanal and mass-produced options ensures that affordability will continue to outweigh transparency for most consumers."),
                ("system", "You have identified the central paradox of ethical consumption: awareness alone does not overcome economic constraints."),
            ],
            [
                ("learner", "I find it telling that the hot dog has resisted the gourmet elevation that the hamburger has undergone in recent decades."),
                ("system", "The burger has indeed been transformed by the premium dining segment. Why do you think the hot dog has not?"),
                ("learner", "Perhaps the hot dog's association with cheapness and mass production is so deeply ingrained that reimagining it as a luxury item feels inherently absurd."),
                ("system", "That observation touches on how certain foods become locked into cultural categories that are remarkably resistant to repositioning."),
            ],
        ],
    },

    # ──────────────────────────────────────────────
    # PIZZA
    # ──────────────────────────────────────────────
    "pizza": {
        "beginner": [
            [
                ("learner", "I love eating pizza for dinner."),
                ("system", "Pizza is enjoyed by people all around the world."),
                ("learner", "My favourite pizza has lots of cheese."),
                ("system", "Cheese pizza is a classic choice."),
            ],
            [
                ("learner", "Can we order a pizza tonight?"),
                ("system", "Sure, what toppings would you like?"),
                ("learner", "I want mushroom and corn please."),
                ("system", "Good choice. I will place the order now."),
            ],
            [
                ("learner", "The pizza box is very large."),
                ("system", "Pizza boxes are big to keep the pizza flat."),
                ("learner", "There are eight slices in this pizza."),
                ("system", "That is enough for the whole family to share."),
            ],
        ],
        "elementary": [
            [
                ("learner", "I was waiting for the pizza delivery when the rain started."),
                ("system", "Did the delivery person arrive on time despite the rain?"),
                ("learner", "He was thirty minutes late and the pizza was a little cold."),
                ("system", "That is disappointing. You could reheat it in the oven for a few minutes."),
            ],
            [
                ("learner", "My friends and I are making pizza at home for the first time."),
                ("system", "That sounds like fun! Are you making the dough from scratch?"),
                ("learner", "Yes, we used a recipe from the internet and it turned out surprisingly well."),
                ("system", "Homemade pizza is always more satisfying because you put effort into making it."),
            ],
            [
                ("learner", "The new pizza shop near our school has a paneer tikka pizza on the menu."),
                ("system", "Indian-style pizzas have become very popular in recent years."),
                ("learner", "I tried it yesterday and the spicy paneer with melted cheese was an amazing combination."),
                ("system", "Fusion foods like that show how global dishes can be adapted to local tastes."),
            ],
        ],
        "intermediate": [
            [
                ("learner", "I have noticed that every country seems to have its own version of pizza."),
                ("system", "That is true. Even within Italy, pizza styles vary greatly by region."),
                ("learner", "In India, tandoori chicken pizza is something you would never find in Naples."),
                ("system", "Localisation of global foods is a natural process driven by available ingredients and taste preferences."),
            ],
            [
                ("learner", "If you let the dough rise for a longer time, the crust becomes lighter and more flavourful."),
                ("system", "Slow fermentation develops more complex flavours through natural yeast activity."),
                ("learner", "A chef I watched online said he lets his dough rest for at least twenty-four hours."),
                ("system", "Professional pizzaiolos often use long fermentation times, sometimes up to seventy-two hours."),
            ],
            [
                ("learner", "The debate over whether pineapple belongs on pizza seems to divide people more than any other food question."),
                ("system", "It is one of those topics where opinions are surprisingly strong."),
                ("learner", "Personally, I think people should eat whatever they enjoy without being judged for it."),
                ("system", "That is a sensible and respectful perspective on what is ultimately a matter of personal preference."),
            ],
        ],
        "upper_intermediate": [
            [
                ("learner", "It is estimated that the global pizza industry is worth over a hundred and fifty billion dollars annually."),
                ("system", "That figure makes pizza one of the most commercially significant foods on the planet."),
                ("learner", "What surprised me was that India is one of the fastest-growing pizza markets in the world."),
                ("system", "Rising incomes, urbanisation, and exposure to global cuisine have all fuelled that growth."),
            ],
            [
                ("learner", "Neapolitan pizza was granted UNESCO intangible cultural heritage status in recognition of its traditional preparation method."),
                ("system", "That acknowledgement highlights the cultural significance of food traditions beyond mere nutrition."),
                ("learner", "Some Italian purists were reportedly offended by the idea that variations like American deep-dish could also be called pizza."),
                ("system", "Cultural ownership of food is a sensitive topic, and globalisation inevitably creates tensions around authenticity."),
            ],
            [
                ("learner", "The pizzas that were served at our school's annual day event had been ordered from three different restaurants."),
                ("system", "Managing food for a large event requires careful coordination."),
                ("learner", "The organisers were criticised because several students with lactose intolerance had no dairy-free option available."),
                ("system", "Dietary inclusivity should always be considered when planning food for events attended by diverse groups."),
            ],
        ],
        "advanced": [
            [
                ("learner", "Pizza's global dominance is less a triumph of Italian cuisine than a demonstration of how capitalism transforms local foods into universally marketable commodities."),
                ("system", "That is a provocative framing. Do you see the spread of pizza as fundamentally a commercial phenomenon?"),
                ("learner", "The Neapolitan original and a fast-food chain pizza share little beyond shape, which suggests that the brand of pizza has become detached from its culinary substance."),
                ("system", "Your analysis parallels arguments made about other globalised products where the name endures while the essence is hollowed out."),
            ],
            [
                ("learner", "Were one to examine the environmental footprint of the pizza supply chain, the results would be sobering."),
                ("system", "Dairy farming for mozzarella alone has a substantial carbon footprint."),
                ("learner", "When you add wheat cultivation, tomato processing, logistics, and packaging, a single pizza represents an extraordinary concentration of resources."),
                ("system", "That systems-level analysis is essential for understanding the true cost of foods that appear simple and affordable."),
            ],
            [
                ("learner", "I contend that the adoption of pizza in India reveals as much about aspirational class identity as it does about changing taste preferences."),
                ("system", "Could you elaborate on the class dimension of pizza consumption in India?"),
                ("learner", "Dining at a pizza chain signalled modernity and cosmopolitan taste during the liberalisation era, a symbolic departure from traditional foodways."),
                ("system", "You have perceptively linked food choice to the broader cultural shifts triggered by economic liberalisation in the 1990s."),
            ],
        ],
    },

    # ──────────────────────────────────────────────
    # DONUT
    # ──────────────────────────────────────────────
    "donut": {
        "beginner": [
            [
                ("learner", "I want a chocolate donut please."),
                ("system", "Here you go. This one has chocolate sprinkles too."),
                ("learner", "The donut is round with a hole."),
                ("system", "Yes, that hole is what makes a donut special."),
            ],
            [
                ("learner", "I ate a donut for breakfast today."),
                ("system", "Donuts are a treat, but not every day."),
                ("learner", "I know, I usually eat idli for breakfast."),
                ("system", "Idli is much healthier. Save donuts for special days."),
            ],
            [
                ("learner", "There are many donuts in the box."),
                ("system", "How many donuts are there? Can you count them?"),
                ("learner", "I count six donuts in the box."),
                ("system", "Six donuts is enough for the whole family."),
            ],
        ],
        "elementary": [
            [
                ("learner", "I was choosing a donut at the bakery when I could not decide between strawberry and vanilla."),
                ("system", "That is a tough choice. Which one did you pick in the end?"),
                ("learner", "I asked the shopkeeper for one of each because they both looked so good."),
                ("system", "Sometimes the best decision is not to choose at all."),
            ],
            [
                ("learner", "My class is planning to sell donuts at the school fair next month."),
                ("system", "That is a great fundraising idea. Will you make them or buy them?"),
                ("learner", "We are going to order them from a bakery and sell them at a small profit."),
                ("system", "That teaches you about business while raising money for a good cause."),
            ],
            [
                ("learner", "I watched a video of donuts being made in a factory and it was fascinating."),
                ("system", "Factory production of donuts involves some interesting machinery."),
                ("learner", "The dough was cut into rings by a machine and dropped into hot oil automatically."),
                ("system", "Modern food manufacturing is highly automated, which is how they produce thousands per hour."),
            ],
        ],
        "intermediate": [
            [
                ("learner", "I have been trying to bake donuts at home, but they never turn out as fluffy as the ones from shops."),
                ("system", "Achieving the right texture depends on several factors. What recipe are you using?"),
                ("learner", "I followed an online recipe, but I think my oil temperature was too low during frying."),
                ("system", "Oil temperature is critical. Too low and the donuts absorb excess oil; too high and they brown before cooking inside."),
            ],
            [
                ("learner", "If donuts did not have so much sugar, they could be a reasonable breakfast option."),
                ("system", "Some bakeries now offer reduced-sugar or baked versions as healthier alternatives."),
                ("learner", "My mother tried making baked donuts with whole wheat flour and jaggery instead of sugar."),
                ("system", "That sounds like a nutritious adaptation that keeps the shape and fun while improving the ingredients."),
            ],
            [
                ("learner", "The donut chain that opened in our mall last year has already become one of the busiest shops there."),
                ("system", "International food chains tend to attract large crowds when they first open in India."),
                ("learner", "I remember standing in a queue for forty minutes just to buy a box of six."),
                ("system", "The novelty factor drives initial demand, though it usually settles down after a few months."),
            ],
        ],
        "upper_intermediate": [
            [
                ("learner", "It is often pointed out that the donut's hole was originally a practical solution to ensure even cooking."),
                ("system", "Without the hole, the centre of the dough would remain raw while the outside overcooked."),
                ("learner", "A sea captain named Hanson Gregory is credited with inventing the hole in the nineteenth century."),
                ("system", "Whether that story is entirely accurate is debated, but the hole certainly solved a real culinary problem."),
            ],
            [
                ("learner", "The donuts that were donated to the orphanage by the local bakery were received with tremendous excitement by the children."),
                ("system", "Small gestures like that can bring immense joy."),
                ("learner", "The bakery owner told me that he was inspired to start the initiative after reading about food waste in the baking industry."),
                ("system", "Redirecting surplus food to those in need is one of the most effective ways to address both waste and hunger simultaneously."),
            ],
            [
                ("learner", "A food critic I follow argued that the Indian vada is essentially a savoury donut that predates its Western counterpart by centuries."),
                ("system", "The structural similarity between a medu vada and a donut is hard to deny."),
                ("learner", "Both involve dough shaped into a ring and deep-fried, yet they are rarely compared in food writing."),
                ("system", "That oversight may reflect a broader tendency in food journalism to centre Western culinary traditions as the default reference point."),
            ],
        ],
        "advanced": [
            [
                ("learner", "The donut occupies an unusual cultural niche as a food that is simultaneously celebratory and self-indulgent, associated with both joy and guilt."),
                ("system", "That duality is amplified by modern health consciousness. How do you think it affects consumption patterns?"),
                ("learner", "People often frame eating a donut as a guilty pleasure, which paradoxically increases its appeal as a form of minor transgression."),
                ("system", "The psychology of forbidden foods is well documented, and your observation aligns with research on the rebound effect of dietary restriction."),
            ],
            [
                ("learner", "Were the donut not so deeply embedded in American popular culture through police dramas and office stereotypes, its global perception might be quite different."),
                ("system", "Media representation has certainly shaped the donut's international image."),
                ("learner", "It is a case where cultural exports carry their symbolic associations along with them, so consuming the food becomes a way of participating in the culture."),
                ("system", "You have described a mechanism of soft power that operates through everyday consumption rather than through formal cultural diplomacy."),
            ],
            [
                ("learner", "I would maintain that the artisanal donut movement represents a broader societal desire to reclaim craftsmanship in an era of industrial homogeneity."),
                ("system", "The premium donut shops that have proliferated in urban centres certainly cater to that desire."),
                ("learner", "Yet I wonder whether the movement is genuinely about quality or merely about repackaging indulgence at a higher price point."),
                ("system", "That critical distinction between authentic craft and commodified authenticity is one of the defining tensions of contemporary consumer culture."),
            ],
        ],
    },

    # ──────────────────────────────────────────────
    # CAKE
    # ──────────────────────────────────────────────
    "cake": {
        "beginner": [
            [
                ("learner", "I love chocolate cake the most."),
                ("system", "Chocolate cake is everyone's favourite."),
                ("learner", "My birthday cake had five candles."),
                ("system", "Happy birthday! Did you make a wish?"),
            ],
            [
                ("learner", "This cake is very soft and sweet."),
                ("system", "A good cake should be moist and fluffy."),
                ("learner", "My mother baked it at home."),
                ("system", "Homemade cakes always taste the best."),
            ],
            [
                ("learner", "Can I have one more piece of cake?"),
                ("system", "Of course, there is plenty left for everyone."),
                ("learner", "Thank you, the cake is really delicious."),
                ("system", "I will tell the baker that you liked it."),
            ],
        ],
        "elementary": [
            [
                ("learner", "I was decorating a cake when I accidentally knocked it off the table."),
                ("system", "Oh no! Was it completely ruined?"),
                ("learner", "One side was smashed but we fixed it by adding extra icing on that side."),
                ("system", "That is a clever solution. Sometimes mistakes lead to creative fixes."),
            ],
            [
                ("learner", "My sister is learning to bake cakes by watching online tutorials."),
                ("system", "There are so many baking channels on the internet now."),
                ("learner", "Her first attempt was a disaster but her second cake turned out quite well."),
                ("system", "Baking improves with practice. The important thing is that she kept trying."),
            ],
            [
                ("learner", "We ordered a pineapple cake for my parents' wedding anniversary yesterday."),
                ("system", "Pineapple cake is a very popular choice for celebrations in India."),
                ("learner", "The bakery wrote their names in icing on the top of the cake."),
                ("system", "Personal touches like that make a celebration cake feel more special."),
            ],
        ],
        "intermediate": [
            [
                ("learner", "I have been thinking about starting a small cake business from home after I finish school."),
                ("system", "Home baking businesses have become quite successful in India. What inspired you?"),
                ("learner", "I noticed that custom cakes for birthdays and weddings are always in demand in my neighbourhood."),
                ("system", "Starting small with orders from friends and family is a practical way to build skills and reputation."),
            ],
            [
                ("learner", "If you substitute butter with oil in a cake recipe, the texture becomes denser but moister."),
                ("system", "Each fat behaves differently in baking because of its molecular structure."),
                ("learner", "My aunt uses coconut oil in her cakes, which gives them a subtle tropical flavour."),
                ("system", "Regional ingredients often give baked goods a distinctive character that sets them apart from standard recipes."),
            ],
            [
                ("learner", "The cake-cutting ceremony at Indian birthday parties has become so central that the party feels incomplete without it."),
                ("system", "It is interesting how cake cutting has been adopted into Indian celebration culture."),
                ("learner", "Even at midnight birthday celebrations, cutting the cake is the moment everyone gathers for."),
                ("system", "The ritual of gathering around a cake creates a shared moment of joy that transcends cultural boundaries."),
            ],
        ],
        "upper_intermediate": [
            [
                ("learner", "It is reported that the global cake decorating industry has grown significantly due to social media."),
                ("system", "Platforms like Instagram have turned cake decoration into a visual art form."),
                ("learner", "Bakers are now expected to create cakes that are not only delicious but also photogenic and shareable."),
                ("system", "The pressure to produce visually stunning cakes has raised the bar for both professional and home bakers."),
            ],
            [
                ("learner", "The wedding cake that was ordered for my cousin's reception was a five-tier structure decorated with fresh flowers."),
                ("system", "Multi-tier wedding cakes require significant structural engineering."),
                ("learner", "The baker explained that each tier was supported by internal dowels to prevent the layers from collapsing."),
                ("system", "The technical skill involved in large-scale cake construction is often underappreciated by those who simply enjoy eating them."),
            ],
            [
                ("learner", "A documentary I watched revealed that commercial cake mixes were deliberately made less convenient in the 1950s to make bakers feel more involved."),
                ("system", "You are referring to the addition of a fresh egg to the mix. That is a famous marketing case study."),
                ("learner", "The theory was that consumers felt guilty using a mix that was too easy, so adding an egg gave them a sense of accomplishment."),
                ("system", "It illustrates how consumer psychology can be more important than product design in determining commercial success."),
            ],
        ],
        "advanced": [
            [
                ("learner", "The cake occupies a paradoxical position in contemporary culture as both a symbol of celebration and an object of dietary anxiety."),
                ("system", "That tension is evident in the proliferation of sugar-free and vegan cake options."),
                ("learner", "I find it revealing that people apologise for eating cake, as if joy and health were fundamentally incompatible."),
                ("system", "Your observation points to a broader cultural pathology where pleasure is perpetually shadowed by guilt, particularly around food."),
            ],
            [
                ("learner", "Were the economic contribution of home bakers properly accounted for, it would constitute a significant segment of the informal food economy in India."),
                ("system", "The home baking sector is largely invisible in official economic statistics."),
                ("learner", "Many women, in particular, operate successful businesses from their kitchens without formal recognition or institutional support."),
                ("system", "Formalising and supporting this sector could provide economic empowerment while preserving the artisanal character of the products."),
            ],
            [
                ("learner", "I would argue that the birthday cake ritual has been so thoroughly commercialised that its original symbolic meaning has been obscured."),
                ("system", "What do you understand that original meaning to be?"),
                ("learner", "Historically, the cake and candles represented an offering and a prayer, but today they serve primarily as a photo opportunity and a commercial transaction."),
                ("system", "Your critique resonates with broader concerns about the commodification of ritual, where the form persists but the substance is emptied."),
            ],
        ],
    },

    # ──────────────────────────────────────────────
    # CHAIR
    # ──────────────────────────────────────────────
    "chair": {
        "beginner": [
            [
                ("learner", "I sit on a chair in my classroom."),
                ("system", "Every student has their own chair and desk."),
                ("learner", "My chair is made of wood."),
                ("system", "Wooden chairs are strong and last a long time."),
            ],
            [
                ("learner", "Please bring me a chair to sit on."),
                ("system", "Here is a chair. It is right next to the window."),
                ("learner", "Thank you, I like sitting near the window."),
                ("system", "You can see the garden from there."),
            ],
            [
                ("learner", "There are not enough chairs for everyone."),
                ("system", "We need two more chairs for the last row."),
                ("learner", "I will bring chairs from the next room."),
                ("system", "That is very helpful of you. Thank you."),
            ],
        ],
        "elementary": [
            [
                ("learner", "I was leaning back on my chair when it almost tipped over."),
                ("system", "Tilting your chair is dangerous. Did your teacher notice?"),
                ("learner", "Yes, she told me to keep all four legs on the ground at all times."),
                ("system", "That is important. Many students have been hurt by falling backwards in their chairs."),
            ],
            [
                ("learner", "My father is fixing a broken chair leg with glue and nails."),
                ("system", "Is it one of the dining chairs?"),
                ("learner", "Yes, the leg cracked last week when my uncle sat on it too quickly."),
                ("system", "Wooden furniture can be repaired many times if you know how to work with it."),
            ],
            [
                ("learner", "We are rearranging the chairs in the hall for the school assembly."),
                ("system", "How many chairs do you need to set up?"),
                ("learner", "We need about two hundred chairs in neat rows for the entire school."),
                ("system", "That is a big job. Make sure to leave aisles so people can walk through."),
            ],
        ],
        "intermediate": [
            [
                ("learner", "I have been sitting in the same chair for five hours studying, and my back is aching badly."),
                ("system", "Sitting for long periods without a break is harmful for your posture and spine."),
                ("learner", "My physiotherapist recommended getting up and stretching every thirty minutes."),
                ("system", "Regular breaks and an ergonomic chair can prevent chronic back problems."),
            ],
            [
                ("learner", "If the classroom chairs had cushions, students would be much more comfortable during long lectures."),
                ("system", "Hard wooden chairs can be quite uncomfortable for extended periods."),
                ("learner", "Some international schools have ergonomic chairs that support the lower back."),
                ("system", "While cost is a factor, student comfort directly affects concentration and learning outcomes."),
            ],
            [
                ("learner", "The old teak rocking chair on my grandmother's veranda has been in our family for three generations."),
                ("system", "Teak furniture is known for its exceptional durability and beauty."),
                ("learner", "My grandfather bought it when he moved to this house in 1960, and it still feels sturdy."),
                ("system", "Well-made teak furniture can last over a century if properly maintained."),
            ],
        ],
        "upper_intermediate": [
            [
                ("learner", "It is well established that poorly designed chairs contribute to musculoskeletal disorders among office workers."),
                ("system", "Ergonomics research has consistently demonstrated the link between seating and spinal health."),
                ("learner", "Despite this evidence, many workplaces in India continue to provide chairs that offer no lumbar support whatsoever."),
                ("system", "The gap between ergonomic research and workplace implementation remains significant, particularly in cost-sensitive environments."),
            ],
            [
                ("learner", "The chairs that were donated to our village school by an NGO were assembled by the students themselves."),
                ("system", "Involving students in building their own furniture has educational value beyond the practical outcome."),
                ("learner", "The children were reported to treat the chairs with much greater care because they had a personal stake in their creation."),
                ("system", "That sense of ownership is a powerful motivator for responsible behaviour."),
            ],
            [
                ("learner", "A furniture designer I met at an exhibition explained that the chair is considered one of the most challenging objects to design."),
                ("system", "That may surprise people who take chairs for granted. What makes it so difficult?"),
                ("learner", "She said that a chair must simultaneously support weight, accommodate diverse body types, and remain aesthetically pleasing."),
                ("system", "Balancing structural, functional, and visual requirements in a single object is indeed a formidable design challenge."),
            ],
        ],
        "advanced": [
            [
                ("learner", "The chair, more than any other piece of furniture, encodes assumptions about the body, social hierarchy, and cultural norms."),
                ("system", "That is a sweeping claim. Can you ground it in a specific example?"),
                ("learner", "Consider the throne, which is simply a chair elevated and ornamented to signify power, demonstrating how seating and authority are inseparable."),
                ("system", "Your example illustrates how a functional object can accumulate layers of symbolic meaning through deliberate design choices."),
            ],
            [
                ("learner", "Had the concept of the chair not existed, architectural design would have evolved along fundamentally different lines to accommodate floor-level living."),
                ("system", "Japanese traditional architecture is an instructive example of design oriented around sitting on the floor."),
                ("learner", "The absence of chairs in traditional Japanese interiors required lower furniture, wider rooms, and different proportions entirely."),
                ("system", "Your counterfactual reasoning reveals how a single piece of furniture can shape an entire built environment."),
            ],
            [
                ("learner", "I would argue that the proliferation of the standardised plastic chair represents both a democratisation of comfort and an aesthetic impoverishment of public spaces."),
                ("system", "The monobloc chair is the most produced piece of furniture in history. Your critique is widely shared."),
                ("learner", "Its ubiquity in every context from roadside tea stalls to government offices speaks to its affordability, but its uniformity erases all sense of place."),
                ("system", "You have articulated a tension that applies broadly to mass production: universal access often comes at the cost of cultural particularity."),
            ],
        ],
    },

    # ──────────────────────────────────────────────
    # COUCH
    # ──────────────────────────────────────────────
    "couch": {
        "beginner": [
            [
                ("learner", "I like to sit on the couch and read."),
                ("system", "The couch is a comfortable place for reading."),
                ("learner", "Our couch is brown and very soft."),
                ("system", "That sounds like a cosy couch."),
            ],
            [
                ("learner", "My cat sleeps on the couch every day."),
                ("system", "Cats love soft and warm places to nap."),
                ("learner", "She leaves fur all over the couch."),
                ("system", "A lint roller can help remove the cat fur easily."),
            ],
            [
                ("learner", "We watch television on the couch."),
                ("system", "That is what most families do in the evening."),
                ("learner", "My whole family sits together on it."),
                ("system", "Family time on the couch is always special."),
            ],
        ],
        "elementary": [
            [
                ("learner", "I was jumping on the couch when my mother told me to stop immediately."),
                ("system", "Jumping on furniture can break it and also hurt you."),
                ("learner", "She said the springs inside the couch were already damaged from too much jumping."),
                ("system", "Replacing couch springs is expensive. It is better to play on the floor."),
            ],
            [
                ("learner", "We are moving to a new flat and the couch will not fit through the door."),
                ("system", "That is a common problem when moving large furniture."),
                ("learner", "The movers said they might need to remove the door frame to get it inside."),
                ("system", "Sometimes tilting the couch at an angle can help. Measure the doorway and the couch first."),
            ],
            [
                ("learner", "My grandmother fell asleep on the couch last night and woke up with a stiff neck."),
                ("system", "Sleeping on a couch is not ideal for the body."),
                ("learner", "We put a blanket over her because she looked so peaceful sleeping there."),
                ("system", "That was thoughtful of you. A pillow under her head would have helped too."),
            ],
        ],
        "intermediate": [
            [
                ("learner", "I have been trying to convince my parents to replace our old couch, but they are quite attached to it."),
                ("system", "Sentimental attachment to furniture is very common. How old is the couch?"),
                ("learner", "It is almost fifteen years old, and the fabric is worn thin in several places."),
                ("system", "Reupholstering might be a good compromise. It preserves the frame while giving it a fresh appearance."),
            ],
            [
                ("learner", "If we rearranged the living room with the couch against the opposite wall, the space would feel much larger."),
                ("system", "Furniture placement has a significant impact on how spacious a room feels."),
                ("learner", "I saw a home design video that suggested keeping the couch away from the walls entirely."),
                ("system", "Floating furniture in the centre of a room works well in larger spaces but may feel cramped in smaller Indian flats."),
            ],
            [
                ("learner", "The leather couch in my uncle's office looks impressive, but it becomes unbearably hot in Chennai's summer."),
                ("system", "Leather absorbs and retains heat, which is a disadvantage in tropical climates."),
                ("learner", "Fabric upholstery would be far more practical, but he insists that leather looks more professional."),
                ("system", "Appearance and comfort often conflict, and the best choice depends on what you prioritise."),
            ],
        ],
        "upper_intermediate": [
            [
                ("learner", "It has been observed that people who work from home frequently use the couch as their primary workstation."),
                ("system", "That habit increased dramatically during the pandemic lockdowns."),
                ("learner", "Physiotherapists have warned that prolonged couch-sitting while working can lead to serious postural problems."),
                ("system", "The couch is designed for relaxation, not for the sustained upright posture that productive work requires."),
            ],
            [
                ("learner", "The couch that was delivered to our house last week did not match the colour shown on the website."),
                ("system", "Colour discrepancies between online images and actual products are a frequent complaint."),
                ("learner", "My mother was told by the customer service team that screen colours may vary, and no exchange would be offered."),
                ("system", "That response is frustrating but highlights the risks of purchasing large items online without seeing them in person."),
            ],
            [
                ("learner", "My interior designer friend mentioned that the couch is typically the anchor piece around which the rest of a living room is designed."),
                ("system", "Its size and placement determine traffic flow, focal points, and overall layout."),
                ("learner", "She advised choosing the couch first and then selecting the rug, curtains, and side tables to complement it."),
                ("system", "That approach ensures visual coherence and prevents the common mistake of assembling mismatched pieces."),
            ],
        ],
        "advanced": [
            [
                ("learner", "The couch has become the centrepiece of modern domestic life, mediating our relationship with entertainment, rest, and increasingly, work."),
                ("system", "Its multifunctionality reflects the collapsing boundaries between leisure and labour in contemporary life."),
                ("learner", "I find it concerning that a single piece of furniture now serves as a site for binge-watching, remote work, and social interaction, all while promoting physical inactivity."),
                ("system", "Your concern aligns with public health research linking sedentary living room habits to chronic disease."),
            ],
            [
                ("learner", "Were furniture designers to take environmental sustainability seriously, the disposable couch would be replaced by modular, repairable designs."),
                ("system", "The fast furniture industry generates enormous waste, much like fast fashion."),
                ("learner", "A couch designed for disassembly and component replacement could last decades, but the industry profits from planned obsolescence."),
                ("system", "You have identified a systemic incentive structure that prioritises short-term sales over long-term environmental responsibility."),
            ],
            [
                ("learner", "I contend that the couch, more than the dining table, has become the true gathering place of the Indian household."),
                ("system", "That is an interesting shift from the traditional centrality of the kitchen or dining area."),
                ("learner", "Television and smartphones have reoriented domestic life around the living room, making the couch the default site for family interaction."),
                ("system", "Your observation captures a fundamental transformation in how technology reshapes domestic spatial practices and family dynamics."),
            ],
        ],
    },

    # ──────────────────────────────────────────────
    # POTTED PLANT
    # ──────────────────────────────────────────────
    "potted plant": {
        "beginner": [
            [
                ("learner", "I have a potted plant on my desk."),
                ("system", "Plants make any room look beautiful."),
                ("learner", "I water it every morning before school."),
                ("system", "That is very responsible of you."),
            ],
            [
                ("learner", "The potted plant has green leaves."),
                ("system", "Green leaves mean the plant is healthy."),
                ("learner", "I put it near the window for sunlight."),
                ("system", "Good thinking. Plants need sunlight to grow."),
            ],
            [
                ("learner", "My mother has many potted plants at home."),
                ("system", "Does she keep them inside or outside?"),
                ("learner", "She keeps some inside and some on the balcony."),
                ("system", "Different plants need different amounts of sunlight."),
            ],
        ],
        "elementary": [
            [
                ("learner", "I was watering my potted plant when I noticed tiny white insects on the leaves."),
                ("system", "Those might be mealybugs. They are common on indoor plants."),
                ("learner", "My mother sprayed neem oil on the leaves and the bugs disappeared in a few days."),
                ("system", "Neem oil is a natural and effective way to deal with plant pests."),
            ],
            [
                ("learner", "Our teacher asked each student to bring a potted plant to school for Environment Day."),
                ("system", "What kind of plant did you bring?"),
                ("learner", "I brought a small tulsi plant because my grandmother said it purifies the air."),
                ("system", "Tulsi is considered sacred in many Indian homes and it does have medicinal properties."),
            ],
            [
                ("learner", "My potted money plant was growing so fast that it started climbing the wall."),
                ("system", "Money plants are vigorous climbers. Did you give it a support to grow on?"),
                ("learner", "I tied a string along the wall and now it follows the string upward."),
                ("system", "That is a clever solution. Money plants look lovely when they trail along a wall."),
            ],
        ],
        "intermediate": [
            [
                ("learner", "I have discovered that talking to my potted plants seems to help them grow better."),
                ("system", "Some studies suggest that the carbon dioxide from your breath may benefit plants."),
                ("learner", "Whether or not that is true, caring for plants has become a calming routine for me."),
                ("system", "The mental health benefits of gardening are well documented, even with just a few potted plants."),
            ],
            [
                ("learner", "If you choose the right plants, a small balcony garden can provide fresh herbs for everyday cooking."),
                ("system", "Which herbs grow well in pots in your experience?"),
                ("learner", "Curry leaves, mint, and coriander all thrive in pots on our south-facing balcony in Chennai."),
                ("system", "Those three herbs are essential to South Indian cooking and having them fresh makes a noticeable difference in flavour."),
            ],
            [
                ("learner", "The trend of gifting potted plants instead of cut flowers has been growing steadily."),
                ("system", "Potted plants last much longer and are more environmentally friendly."),
                ("learner", "My friend gifted me a small succulent for my birthday, and it is still alive after two years."),
                ("system", "Succulents are perfect gifts because they require minimal care and survive even occasional neglect."),
            ],
        ],
        "upper_intermediate": [
            [
                ("learner", "It has been shown that indoor potted plants can improve air quality by absorbing certain pollutants."),
                ("system", "The NASA Clean Air Study identified several houseplants that effectively filter toxins."),
                ("learner", "However, more recent research has questioned whether the number of plants needed for a noticeable effect is practical for a typical room."),
                ("system", "That is an important qualification. The original study was conducted in sealed chambers, not real-world living spaces."),
            ],
            [
                ("learner", "The potted plants that were placed in the hospital waiting area were removed after concerns about soil-borne pathogens were raised."),
                ("system", "Infection control in hospitals must take precedence over aesthetic considerations."),
                ("learner", "A compromise was suggested: using hydroponic plants that grow in water instead of soil."),
                ("system", "That solution addresses the hygiene concern while preserving the calming effect that plants provide in healthcare settings."),
            ],
            [
                ("learner", "My neighbour was told by a Vastu consultant that certain potted plants should not be kept inside the house."),
                ("system", "Vastu Shastra has specific recommendations about plants and their placement."),
                ("learner", "She rearranged her entire collection based on those guidelines, moving thorny plants outdoors and keeping broad-leafed ones inside."),
                ("system", "Whether one follows Vastu or not, the principle of thoughtful placement does affect both the aesthetics and the health of indoor plants."),
            ],
        ],
        "advanced": [
            [
                ("learner", "The potted plant is a curious object: a fragment of nature domesticated and contained, serving human aesthetic needs while being entirely dependent on human care."),
                ("system", "That framing raises questions about the relationship between cultivation and control."),
                ("learner", "One might argue that the potted plant symbolises our desire to incorporate nature into our lives on our own terms, without accepting its wildness."),
                ("system", "Your observation echoes critiques of the pastoral tradition, where nature is valued only insofar as it conforms to human preferences."),
            ],
            [
                ("learner", "Were urban planners to mandate greenery in every residential unit, potted plants could collectively mitigate the urban heat island effect in dense cities."),
                ("system", "Rooftop and balcony gardens have shown measurable cooling effects in pilot studies."),
                ("learner", "The challenge lies in sustaining such initiatives, as mandatory green spaces require ongoing maintenance that many residents may lack the time or resources to provide."),
                ("system", "You have identified the critical gap between well-intentioned green policy and the practical realities of implementation in resource-constrained contexts."),
            ],
            [
                ("learner", "I contend that the contemporary obsession with houseplants among urban millennials reflects a deeper yearning for connection with the natural world that city life systematically denies."),
                ("system", "The timing of the houseplant boom, coinciding with increased urbanisation and remote work, supports your thesis."),
                ("learner", "The irony is that these plants are consumed as commodities, shipped across continents in plastic pots, in a process that further degrades the ecosystems they are meant to evoke."),
                ("system", "You have exposed a contradiction at the heart of consumer-driven environmentalism that deserves far more critical scrutiny."),
            ],
        ],
    },

    # ──────────────────────────────────────────────
    # BED
    # ──────────────────────────────────────────────
    "bed": {
        "beginner": [
            [
                ("learner", "I sleep in my bed every night."),
                ("system", "A good bed helps you sleep well."),
                ("learner", "My bed has a blue blanket on it."),
                ("system", "Blue is a calm colour, perfect for sleeping."),
            ],
            [
                ("learner", "I make my bed every morning."),
                ("system", "That is a very good daily habit."),
                ("learner", "My mother taught me how to do it."),
                ("system", "A tidy bed makes the whole room look neat."),
            ],
            [
                ("learner", "My bed is next to the window."),
                ("system", "Do you like the fresh air while you sleep?"),
                ("learner", "Yes, I can hear the birds in the morning."),
                ("system", "Waking up to birdsong is a lovely way to start the day."),
            ],
        ],
        "elementary": [
            [
                ("learner", "I was reading a book in bed when I fell asleep and dropped the book on my face."),
                ("system", "That happens to me too. Were you reading something boring?"),
                ("learner", "No, it was actually very interesting but I was too tired to keep my eyes open."),
                ("system", "Next time, set a time limit for reading in bed so you fall asleep before you drop the book."),
            ],
            [
                ("learner", "My younger brother and I are sharing a bed because we only have two bedrooms."),
                ("system", "Sharing a room or a bed is very common in Indian households."),
                ("learner", "He moves around a lot in his sleep and sometimes kicks me."),
                ("system", "Placing a pillow between you might help create a boundary."),
            ],
            [
                ("learner", "We bought a new bed for my grandmother because her old one was too hard."),
                ("system", "Older people often need softer mattresses for comfort."),
                ("learner", "She tested several beds at the furniture shop before choosing one with a cotton mattress."),
                ("system", "Cotton mattresses breathe well in hot weather, which is important for comfort in India."),
            ],
        ],
        "intermediate": [
            [
                ("learner", "I have noticed that I sleep much better when my bed sheets are freshly washed."),
                ("system", "Clean bedding contributes to both comfort and hygiene."),
                ("learner", "My mother changes the sheets every Sunday without fail, and she says it was her mother's rule."),
                ("system", "Weekly sheet changes prevent the buildup of dust mites and bacteria that can affect sleep quality."),
            ],
            [
                ("learner", "If I could design my own bed, I would include built-in storage underneath for books and clothes."),
                ("system", "Storage beds are very popular in India because homes tend to have limited space."),
                ("learner", "Our current bed already has drawers, but they are not deep enough for thicker items like blankets."),
                ("system", "Hydraulic lift beds offer much more storage space because the entire mattress base lifts up."),
            ],
            [
                ("learner", "The traditional Indian practice of sleeping on the floor on a mat has health advocates who claim it benefits the spine."),
                ("system", "There is ongoing debate about whether firm or soft sleeping surfaces are better for back health."),
                ("learner", "My yoga instructor sleeps on a thin mat and says his back pain disappeared within months of switching."),
                ("system", "Individual experiences vary, and what works for one person may not suit another."),
            ],
        ],
        "upper_intermediate": [
            [
                ("learner", "It is widely acknowledged that sleep quality has a direct impact on academic performance in students."),
                ("system", "Research consistently shows that well-rested students perform better in memory, attention, and problem-solving tasks."),
                ("learner", "Despite this evidence, many Indian students sacrifice sleep during exam periods, believing that more study hours compensate for less rest."),
                ("system", "That is a counterproductive strategy, as sleep deprivation impairs the very cognitive functions needed for exam success."),
            ],
            [
                ("learner", "The beds in the hostel I stayed at during my summer programme were uncomfortably narrow and had thin mattresses."),
                ("system", "Institutional bedding is often prioritised by cost rather than comfort."),
                ("learner", "Several students complained, and the warden was told that better mattresses would be provided by the next academic year."),
                ("system", "Improving sleep conditions in student hostels should be a priority, given its direct link to health and performance."),
            ],
            [
                ("learner", "A sleep researcher I heard speak at a conference explained that the bed should be associated exclusively with sleep and rest."),
                ("system", "That principle is central to cognitive behavioural therapy for insomnia."),
                ("learner", "She advised against studying, eating, or using phones in bed because these activities weaken the brain's association between the bed and sleep."),
                ("system", "Building that strong mental association is one of the most effective non-pharmacological approaches to improving sleep."),
            ],
        ],
        "advanced": [
            [
                ("learner", "The bed is perhaps the most intimate object in human experience, yet it receives remarkably little philosophical attention compared to other domestic furnishings."),
                ("system", "That oversight is curious, given that we spend approximately a third of our lives in bed."),
                ("learner", "I suspect the association of the bed with vulnerability, dreams, and the unconscious mind makes it uncomfortable territory for rational inquiry."),
                ("system", "Your hypothesis is intriguing and suggests that the bed occupies a liminal space between the rational and the irrational that resists easy analysis."),
            ],
            [
                ("learner", "Were the mattress industry to be held to stricter transparency standards, consumers would discover that many premium products offer no measurable advantage over mid-range alternatives."),
                ("system", "The mattress market is notorious for opaque pricing and exaggerated health claims."),
                ("learner", "The difficulty of objectively comparing sleep quality across mattresses makes this industry particularly susceptible to marketing manipulation."),
                ("system", "You have identified a market failure where information asymmetry empowers sellers at the expense of consumers who lack the means to evaluate competing claims."),
            ],
            [
                ("learner", "I would argue that the joint family sleeping arrangement, where multiple generations shared sleeping spaces, fostered a sense of belonging that the modern private bedroom has inadvertently dissolved."),
                ("system", "That is a perspective not often heard in discussions about housing modernisation."),
                ("learner", "The shift toward individual bedrooms, while undeniably offering privacy, has also created physical separation within families that may contribute to feelings of isolation."),
                ("system", "Your argument invites us to consider what is lost when architectural progress prioritises individual autonomy over communal intimacy."),
            ],
        ],
    },
}
