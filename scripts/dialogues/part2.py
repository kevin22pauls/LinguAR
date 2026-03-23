"""
Hand-crafted dialogues for 20 COCO objects (Part 2).

Objects: elephant, bear, zebra, giraffe, backpack, umbrella, handbag, tie,
         suitcase, frisbee, skis, snowboard, sports ball, kite, baseball bat,
         baseball glove, skateboard, surfboard, tennis racket, bottle

Each object has 5 levels x 3 dialogues = 15 dialogues.
Each dialogue has exactly 4 turns: learner, system, learner, system.
Total: 20 objects x 15 dialogues = 300 dialogues.
"""

DIALOGUES_PART2 = {
    # =========================================================================
    # ELEPHANT
    # =========================================================================
    "elephant": {
        "beginner": [
            [
                ("learner", "The elephant is very big."),
                ("system", "Yes! Elephants are the largest land animals."),
                ("learner", "It has a long trunk."),
                ("system", "That's right. They use their trunk to drink water and grab food."),
            ],
            [
                ("learner", "I see an elephant at the zoo."),
                ("system", "How exciting! What is the elephant doing?"),
                ("learner", "It eats leaves from a tree."),
                ("system", "Elephants eat a lot. They can eat over 100 kilograms of food a day."),
            ],
            [
                ("learner", "Elephants live in groups."),
                ("system", "Yes, a group of elephants is called a herd."),
                ("learner", "The baby elephant stays near its mother."),
                ("system", "That's correct. Mother elephants protect their babies carefully."),
            ],
        ],
        "elementary": [
            [
                ("learner", "We are watching a documentary about elephants tonight."),
                ("system", "That sounds interesting. Which channel is it on?"),
                ("learner", "It was on National Geographic last week too."),
                ("system", "National Geographic makes excellent wildlife documentaries."),
            ],
            [
                ("learner", "The elephant is spraying water on its back."),
                ("system", "Elephants do that to cool themselves down."),
                ("learner", "Yesterday the zookeeper gave it a bath."),
                ("system", "Zookeepers take great care of their elephants every day."),
            ],
            [
                ("learner", "I drew an elephant for my art project."),
                ("system", "How wonderful! Did you draw it from memory?"),
                ("learner", "I looked at photos from our zoo visit last month."),
                ("system", "Using real photos as reference is a great idea for drawing."),
            ],
        ],
        "intermediate": [
            [
                ("learner", "I have always wanted to visit an elephant sanctuary."),
                ("system", "There are several good ones in Kerala and Thailand."),
                ("learner", "If I saved enough money, I would go to Kerala first."),
                ("system", "Kerala's sanctuaries are well known for ethical elephant care."),
            ],
            [
                ("learner", "The elephant population has declined over the past century."),
                ("system", "Yes, habitat loss and poaching are the main threats."),
                ("learner", "If governments enforced stricter laws, poaching would decrease."),
                ("system", "Absolutely. Strong enforcement has already helped in some regions."),
            ],
            [
                ("learner", "Have you ever seen an elephant use tools in the wild?"),
                ("system", "I have read that they use branches to swat flies."),
                ("learner", "Scientists have found that elephants can solve simple puzzles."),
                ("system", "Their intelligence is truly remarkable among land animals."),
            ],
        ],
        "upper_intermediate": [
            [
                ("learner", "It is believed that elephants can remember locations for decades."),
                ("system", "Yes, their spatial memory is considered extraordinary by researchers."),
                ("learner", "The matriarch was reported to have led her herd to water during a drought."),
                ("system", "Matriarchs pass down knowledge that is essential for the herd's survival."),
            ],
            [
                ("learner", "The documentary explained that elephant communication is more complex than previously thought."),
                ("system", "Indeed, they use infrasound that travels several kilometres underground."),
                ("learner", "Researchers said that these low-frequency calls were detected by other herds far away."),
                ("system", "This discovery has changed how scientists study elephant social behaviour."),
            ],
            [
                ("learner", "Elephants are often regarded as one of the most emotionally intelligent species."),
                ("system", "They have been observed mourning their dead, which is quite rare."),
                ("learner", "A wildlife expert mentioned that elephants were seen returning to the bones of their relatives."),
                ("system", "Such behaviour suggests a depth of social bonding that few animals display."),
            ],
        ],
        "advanced": [
            [
                ("learner", "Were it not for international ivory trade bans, African elephant populations might have collapsed entirely."),
                ("system", "The 1989 CITES ban was indeed pivotal, though enforcement remains inconsistent across nations."),
                ("learner", "One could argue that community-based conservation programmes yield more sustainable outcomes than top-down regulations."),
                ("system", "That is a nuanced perspective, and evidence from several African countries supports both approaches working in tandem."),
            ],
            [
                ("learner", "The ethical implications of keeping elephants in captivity warrant serious philosophical scrutiny."),
                ("system", "Many bioethicists contend that their cognitive complexity makes confinement inherently problematic."),
                ("learner", "I would suggest that sanctuaries, provided they replicate natural social structures, represent a defensible compromise."),
                ("system", "That position aligns with current best practices, though critics argue even sanctuaries impose artificial constraints."),
            ],
            [
                ("learner", "It is essential that we reconsider the anthropocentric framework through which elephant intelligence is typically evaluated."),
                ("system", "Cognitive ethologists have been advocating precisely that shift for over a decade now."),
                ("learner", "Should we not develop assessment criteria that account for the unique ecological niches elephants inhabit?"),
                ("system", "Absolutely. Species-appropriate metrics would provide a far more accurate picture of their cognitive landscape."),
            ],
        ],
    },
    # =========================================================================
    # BEAR
    # =========================================================================
    "bear": {
        "beginner": [
            [
                ("learner", "The bear is brown and big."),
                ("system", "Yes! Bears come in many colours like brown, black, and white."),
                ("learner", "It likes to eat fish."),
                ("system", "That's right. Bears catch fish from rivers with their paws."),
            ],
            [
                ("learner", "I saw a bear in the zoo."),
                ("system", "What kind of bear was it?"),
                ("learner", "It was a black bear."),
                ("system", "Black bears are common in North America and parts of Asia."),
            ],
            [
                ("learner", "Bears sleep in winter."),
                ("system", "Yes, that is called hibernation."),
                ("learner", "They eat a lot before winter."),
                ("system", "They need to store energy to survive the cold months."),
            ],
        ],
        "elementary": [
            [
                ("learner", "The bear is climbing a tree to find honey."),
                ("system", "Bears have strong claws that help them climb."),
                ("learner", "Last week I watched a video of a bear catching salmon."),
                ("system", "Those videos from Alaska are amazing to watch."),
            ],
            [
                ("learner", "We are studying bears in our science class."),
                ("system", "What have you learned about them so far?"),
                ("learner", "Our teacher told us that polar bears live near the Arctic."),
                ("system", "Polar bears are specially adapted to survive in freezing temperatures."),
            ],
            [
                ("learner", "The bear in the wildlife park was playing with a ball."),
                ("system", "Bears are quite playful, especially young ones."),
                ("learner", "The guide said it weighed over two hundred kilograms."),
                ("system", "That is about average for an adult bear of that species."),
            ],
        ],
        "intermediate": [
            [
                ("learner", "I have read that bears can run faster than most people."),
                ("system", "Yes, some bears can reach speeds of fifty kilometres per hour."),
                ("learner", "If someone encountered a bear in the forest, what would you advise them to do?"),
                ("system", "Experts recommend staying calm, avoiding eye contact, and slowly backing away."),
            ],
            [
                ("learner", "The sloth bear is native to the Indian subcontinent."),
                ("system", "Have you ever seen one at a wildlife reserve here?"),
                ("learner", "I have visited the Daroji Sloth Bear Sanctuary in Karnataka once."),
                ("system", "That sanctuary is one of the best places to observe them in their natural habitat."),
            ],
            [
                ("learner", "If bear habitats were better protected, human-bear conflicts would decrease."),
                ("system", "Forest encroachment is a major reason bears wander into villages."),
                ("learner", "Conservation groups have already started planting buffer zones around bear territories."),
                ("system", "Buffer zones can significantly reduce encounters between bears and local communities."),
            ],
        ],
        "upper_intermediate": [
            [
                ("learner", "It is widely known that bear populations are threatened by deforestation and climate change."),
                ("system", "The IUCN has listed several bear species as vulnerable or endangered."),
                ("learner", "Researchers have suggested that corridor forests could be established to connect fragmented habitats."),
                ("system", "Wildlife corridors have been shown to improve genetic diversity in isolated bear populations."),
            ],
            [
                ("learner", "The documentary claimed that bears were being relocated to safer reserves across the country."),
                ("system", "Relocation programmes are controversial because bears sometimes return to their original territory."),
                ("learner", "It was argued by some conservationists that community education is more effective than relocation."),
                ("system", "Both strategies are needed, as neither alone has proved sufficient in high-conflict areas."),
            ],
            [
                ("learner", "The bear that had been rescued from a street performer was eventually released into the wild."),
                ("system", "Rehabilitation of captive bears is a long and complex process."),
                ("learner", "The organisation reported that the bear had adapted well to its new environment."),
                ("system", "Successful rewilding stories like that give hope to conservation efforts."),
            ],
        ],
        "advanced": [
            [
                ("learner", "Were policymakers to allocate greater funding for bear conservation, the long-term ecological benefits would far outweigh the costs."),
                ("system", "Economic analyses of ecosystem services provided by apex predators support that assertion."),
                ("learner", "It is incumbent upon governments to recognise that biodiversity preservation constitutes an investment rather than an expenditure."),
                ("system", "Framing conservation in economic terms has proven effective in securing legislative support in several countries."),
            ],
            [
                ("learner", "The notion that bears are inherently dangerous to humans is a misconception perpetuated by sensationalist media."),
                ("system", "Statistical data show that bear attacks are exceedingly rare relative to other wildlife encounters."),
                ("learner", "I would contend that fostering coexistence requires dismantling such narratives through evidence-based public education."),
                ("system", "Well-designed outreach programmes in Scandinavia have demonstrably shifted public attitudes toward large carnivores."),
            ],
            [
                ("learner", "Should current warming trends persist, polar bear populations may decline to unsustainable levels within decades."),
                ("system", "The loss of Arctic sea ice has already reduced hunting grounds for polar bears considerably."),
                ("learner", "One must question whether ex-situ conservation alone can preserve a species whose survival is inextricably linked to its habitat."),
                ("system", "That raises a fundamental dilemma in conservation biology: captive breeding without habitat restoration is ultimately futile."),
            ],
        ],
    },
    # =========================================================================
    # ZEBRA
    # =========================================================================
    "zebra": {
        "beginner": [
            [
                ("learner", "The zebra has black and white stripes."),
                ("system", "Yes! Every zebra has a unique stripe pattern."),
                ("learner", "It looks like a horse."),
                ("system", "Zebras and horses are related, but zebras are wild animals."),
            ],
            [
                ("learner", "I see three zebras at the zoo."),
                ("system", "Do they all look the same to you?"),
                ("learner", "No, they have different stripes."),
                ("system", "Good observation! Their stripes are like fingerprints."),
            ],
            [
                ("learner", "Zebras live in Africa."),
                ("system", "That's correct. They live on grasslands called savannas."),
                ("learner", "They eat grass all day long."),
                ("system", "Yes, zebras are herbivores that graze for many hours."),
            ],
        ],
        "elementary": [
            [
                ("learner", "The zebras are running together across the field."),
                ("system", "They stay in groups to protect each other from predators."),
                ("learner", "We learned about zebra migration in geography class."),
                ("system", "The great migration in East Africa is one of nature's most spectacular events."),
            ],
            [
                ("learner", "I am drawing a zebra for my school project."),
                ("system", "Are you going to colour it with stripes?"),
                ("learner", "I already finished the stripes and added some grass around it."),
                ("system", "That sounds like a wonderful drawing. Your teacher will love it."),
            ],
            [
                ("learner", "The documentary showed a baby zebra standing up for the first time."),
                ("system", "Baby zebras can stand within minutes of being born."),
                ("learner", "It was walking beside its mother by the end of the show."),
                ("system", "They need to move quickly to stay safe from lions and hyenas."),
            ],
        ],
        "intermediate": [
            [
                ("learner", "Scientists have debated whether zebras are white with black stripes or black with white stripes."),
                ("system", "Recent research suggests they are actually black with white stripes."),
                ("learner", "If I remember correctly, the stripes may help confuse biting flies."),
                ("system", "Yes, studies have shown that flies find it harder to land on striped surfaces."),
            ],
            [
                ("learner", "I have watched several documentaries about zebras and their survival strategies."),
                ("system", "What aspect of their behaviour impressed you the most?"),
                ("learner", "The way they form a circle around young ones when a predator approaches is remarkable."),
                ("system", "That defensive formation demonstrates sophisticated group coordination."),
            ],
            [
                ("learner", "If zebras could be domesticated like horses, would people ride them?"),
                ("system", "Many have tried throughout history, but zebras are far more unpredictable."),
                ("learner", "Their temperament has made domestication nearly impossible."),
                ("system", "Exactly. They tend to panic under stress and can deliver a powerful kick."),
            ],
        ],
        "upper_intermediate": [
            [
                ("learner", "It has been hypothesised that zebra stripes serve a thermoregulatory function."),
                ("system", "The theory suggests that black and white stripes create air currents that cool the animal."),
                ("learner", "However, a recent study was published that challenged this hypothesis with thermal imaging data."),
                ("system", "Scientific understanding of stripe function continues to evolve as new evidence emerges."),
            ],
            [
                ("learner", "The Grevy's zebra, which is the largest species, is classified as endangered."),
                ("system", "Fewer than three thousand remain in the wild, primarily in Kenya and Ethiopia."),
                ("learner", "It was reported that community conservancies had helped stabilise their numbers in recent years."),
                ("system", "Local involvement in conservation has proven far more effective than external interventions alone."),
            ],
            [
                ("learner", "Zebras are known to form strong social bonds that persist throughout their lifetime."),
                ("system", "Studies have shown they can recognise individual herd members by their stripe patterns."),
                ("learner", "A researcher explained that separated zebras were observed calling out to each other for days."),
                ("system", "Such findings reveal an emotional complexity that challenges our assumptions about herd animals."),
            ],
        ],
        "advanced": [
            [
                ("learner", "The persistence of stripe variation among zebra populations presents a compelling case study in evolutionary biology."),
                ("system", "Natural selection appears to have maintained multiple stripe patterns across different ecological niches."),
                ("learner", "One might argue that this polymorphism is sustained by frequency-dependent selection pressures from predators and parasites."),
                ("system", "That multi-factorial explanation aligns with contemporary models of phenotypic diversity in ungulates."),
            ],
            [
                ("learner", "Were conservation efforts for the quagga, an extinct zebra subspecies, to have begun earlier, its fate might have been different."),
                ("system", "The Quagga Project in South Africa is attempting to selectively breed back its phenotype from plains zebras."),
                ("learner", "Whether such de-extinction efforts constitute genuine conservation or mere genetic nostalgia remains a contentious philosophical question."),
                ("system", "It raises fundamental issues about what we mean by species identity and the purpose of restoration ecology."),
            ],
            [
                ("learner", "The ecological ramifications of zebra population decline extend well beyond the loss of a single species."),
                ("system", "As key grazers, zebras shape grassland structure, which in turn affects countless other organisms."),
                ("learner", "It would be reductive to frame zebra conservation solely in terms of charismatic megafauna appeal rather than ecosystem function."),
                ("system", "A functional ecology perspective demands that we assess conservation priorities based on trophic interactions and biodiversity cascades."),
            ],
        ],
    },
    # =========================================================================
    # GIRAFFE
    # =========================================================================
    "giraffe": {
        "beginner": [
            [
                ("learner", "The giraffe is very tall."),
                ("system", "Yes! Giraffes are the tallest animals in the world."),
                ("learner", "It has a very long neck."),
                ("system", "Their long necks help them reach leaves high up in trees."),
            ],
            [
                ("learner", "I like the spots on the giraffe."),
                ("system", "Those brown spots are beautiful. No two giraffes have the same pattern."),
                ("learner", "The giraffe eats leaves from tall trees."),
                ("system", "They especially love acacia leaves, which grow in Africa."),
            ],
            [
                ("learner", "The baby giraffe is so cute."),
                ("system", "Baby giraffes are about two metres tall when they are born!"),
                ("learner", "It stands next to its mother."),
                ("system", "Baby giraffes can stand and walk within an hour of being born."),
            ],
        ],
        "elementary": [
            [
                ("learner", "The giraffe is drinking water at the pond."),
                ("system", "Giraffes have to spread their legs wide to reach the water."),
                ("learner", "Our guide told us that this makes them easy targets for predators."),
                ("system", "That is why giraffes are always on alert when they drink."),
            ],
            [
                ("learner", "I am reading a book about giraffes and other African animals."),
                ("system", "What is the most interesting fact you have learned?"),
                ("learner", "I learned that giraffes only sleep about thirty minutes a day."),
                ("system", "They sleep very little because they need to watch for danger."),
            ],
            [
                ("learner", "We visited the zoo last Sunday and saw a giraffe feeding show."),
                ("system", "Did you get to feed the giraffe yourself?"),
                ("learner", "Yes, I held a leaf up and it took it with its long tongue."),
                ("system", "Giraffe tongues can be almost half a metre long!"),
            ],
        ],
        "intermediate": [
            [
                ("learner", "I have learned that giraffes were recently reclassified into four separate species."),
                ("system", "Yes, genetic analysis revealed more diversity than scientists had assumed."),
                ("learner", "If this classification is accepted widely, conservation strategies would need to change significantly."),
                ("system", "Each species would require its own protection plan based on population size and range."),
            ],
            [
                ("learner", "Giraffes have experienced a silent extinction crisis that most people are unaware of."),
                ("system", "Their numbers have dropped by nearly forty percent in three decades."),
                ("learner", "If more awareness campaigns were launched, public support for giraffe conservation would grow."),
                ("system", "Many organisations are now working to bring attention to what they call a silent extinction."),
            ],
            [
                ("learner", "Have you ever noticed how gracefully giraffes move despite their unusual proportions?"),
                ("system", "Their gait is quite unique. Both legs on one side move together."),
                ("learner", "I have seen slow-motion footage that shows this unusual walking pattern clearly."),
                ("system", "That lateral gait prevents their long legs from tangling as they walk."),
            ],
        ],
        "upper_intermediate": [
            [
                ("learner", "It is often assumed that the giraffe's long neck evolved primarily for feeding, but that view has been challenged."),
                ("system", "The sexual selection hypothesis suggests necks lengthened due to male combat behaviour."),
                ("learner", "Male giraffes are known to engage in necking contests where they swing their heads at rivals."),
                ("system", "Both feeding advantage and sexual selection likely contributed to neck evolution over time."),
            ],
            [
                ("learner", "The giraffe's cardiovascular system is considered a marvel of biological engineering."),
                ("system", "Their hearts must pump blood nearly two metres up to reach the brain."),
                ("learner", "It was explained in a lecture that special valves in their neck prevent blood from rushing to the head when they bend down."),
                ("system", "Without those adaptations, giraffes would lose consciousness every time they drank water."),
            ],
            [
                ("learner", "A wildlife photographer mentioned that giraffes were far more social than people generally realise."),
                ("system", "Recent studies have revealed complex social networks among giraffe populations."),
                ("learner", "The research suggested that older females played a crucial role in group decision-making."),
                ("system", "This parallels the matriarchal structures observed in elephants and some whale species."),
            ],
        ],
        "advanced": [
            [
                ("learner", "The giraffe's peculiar anatomy has long served as a touchstone in debates about evolutionary mechanisms."),
                ("system", "Lamarck famously cited the giraffe's neck as evidence for his theory of acquired characteristics."),
                ("learner", "It is worth noting that even Darwin's gradualist explanation requires a plausible account of intermediate forms and selective pressures."),
                ("system", "Modern evo-devo research has identified specific genetic changes in the FGFRL1 gene that regulate both neck length and cardiovascular adaptations simultaneously."),
            ],
            [
                ("learner", "Were the taxonomic reclassification of giraffes into four species to gain universal acceptance, it would have profound implications for conservation triage."),
                ("system", "Some populations that appear stable under a single-species model would be reclassified as critically endangered."),
                ("learner", "This underscores how taxonomic decisions, far from being merely academic, carry real-world consequences for resource allocation and policy."),
                ("system", "The intersection of systematics and conservation policy remains one of the most consequential areas in applied biology."),
            ],
            [
                ("learner", "I would argue that the giraffe exemplifies the limitations of flagship species conservation as a paradigm."),
                ("system", "Despite their iconic status, giraffes receive a fraction of the funding directed toward elephants or rhinos."),
                ("learner", "Perhaps what is needed is a shift from species-centric to habitat-centric conservation models that protect entire ecosystems."),
                ("system", "Landscape-level approaches would benefit giraffes alongside the myriad less charismatic species that share their range."),
            ],
        ],
    },
    # =========================================================================
    # BACKPACK
    # =========================================================================
    "backpack": {
        "beginner": [
            [
                ("learner", "My backpack is blue and big."),
                ("system", "That sounds like a nice backpack! What do you keep in it?"),
                ("learner", "I keep my books and water bottle."),
                ("system", "It is important to carry water to school every day."),
            ],
            [
                ("learner", "I carry my backpack to school."),
                ("system", "Do you walk to school or take the bus?"),
                ("learner", "I walk with my friends every morning."),
                ("system", "Walking to school with friends sounds like fun."),
            ],
            [
                ("learner", "My new backpack has many pockets."),
                ("system", "Pockets help you organise your things neatly."),
                ("learner", "I put my pencils in the small pocket."),
                ("system", "That way you can find them quickly when you need them."),
            ],
        ],
        "elementary": [
            [
                ("learner", "I am looking for a new backpack for the school trip."),
                ("system", "What features are you looking for in a backpack?"),
                ("learner", "My father bought me one with padded straps last year."),
                ("system", "Padded straps are important because they protect your shoulders."),
            ],
            [
                ("learner", "My backpack is getting too heavy with all these textbooks."),
                ("system", "You should only carry the books you need each day."),
                ("learner", "Our teacher suggested we leave some books in our desk."),
                ("system", "That is a sensible idea to reduce the weight on your back."),
            ],
            [
                ("learner", "I am packing my backpack for the overnight camp tomorrow."),
                ("system", "Have you made a checklist of things to bring?"),
                ("learner", "I packed a torch, extra clothes, and my toothbrush already."),
                ("system", "Sounds like you are well prepared for a fun trip."),
            ],
        ],
        "intermediate": [
            [
                ("learner", "I have been searching for a waterproof backpack for my trekking trip."),
                ("system", "Waterproof backpacks are essential for hikes during the monsoon season."),
                ("learner", "If the material were not durable enough, the contents could get soaked."),
                ("system", "Look for backpacks rated at least IPX4 for reliable water resistance."),
            ],
            [
                ("learner", "Have you noticed how many students carry overloaded backpacks every day?"),
                ("system", "Yes, heavy backpacks can cause serious back problems over time."),
                ("learner", "Schools should consider providing lockers so children do not carry everything at once."),
                ("system", "Some schools in India have already adopted digital textbooks to reduce the burden."),
            ],
            [
                ("learner", "My backpack has lasted three years because I chose a good brand."),
                ("system", "Quality materials and stitching make a big difference in durability."),
                ("learner", "If I had bought the cheaper one, I would have replaced it twice by now."),
                ("system", "Investing in quality products often saves money in the long run."),
            ],
        ],
        "upper_intermediate": [
            [
                ("learner", "It is recommended that a child's backpack should not exceed ten percent of their body weight."),
                ("system", "Many health organisations have issued guidelines along those lines."),
                ("learner", "A study conducted in Tamil Nadu found that most schoolchildren were carrying bags far above the safe limit."),
                ("system", "The state government responded by introducing weight restrictions for school bags in recent years."),
            ],
            [
                ("learner", "The ergonomic backpack that was designed by the start-up has received positive reviews from physiotherapists."),
                ("system", "Ergonomic design is becoming a key selling point in the school bag market."),
                ("learner", "Parents reported that their children experienced less shoulder pain after switching to the new design."),
                ("system", "Such feedback demonstrates the real health benefits of well-engineered school products."),
            ],
            [
                ("learner", "Backpacks made from recycled ocean plastic are being sold at stores near my home."),
                ("system", "Sustainable products are gaining popularity among environmentally conscious consumers."),
                ("learner", "The manufacturer claims that each backpack removes approximately twenty plastic bottles from the ocean."),
                ("system", "If those claims are verified by independent auditors, it represents a meaningful contribution to waste reduction."),
            ],
        ],
        "advanced": [
            [
                ("learner", "The backpack, though seemingly mundane, serves as a lens through which one can examine issues of educational equity."),
                ("system", "In many rural areas, the inability to afford basic school supplies remains a barrier to attendance."),
                ("learner", "It is therefore imperative that government schemes distributing free backpacks and materials be evaluated for effectiveness rather than merely announced."),
                ("system", "Process audits and outcome tracking would ensure such programmes achieve their intended social objectives."),
            ],
            [
                ("learner", "The biomechanical research on load carriage in children has yielded findings that ought to inform school infrastructure policy."),
                ("system", "Studies linking heavy bags to spinal misalignment in developing bodies are particularly compelling."),
                ("learner", "Were school boards to mandate locker facilities and digital alternatives, the incidence of musculoskeletal complaints would likely decline."),
                ("system", "Implementing such changes requires both institutional will and sustained investment in digital infrastructure."),
            ],
            [
                ("learner", "One could argue that the proliferation of branded backpacks among schoolchildren reinforces socioeconomic stratification."),
                ("system", "Visible markers of economic status can indeed affect peer dynamics and self-esteem in educational settings."),
                ("learner", "A uniform school bag policy, though restrictive, might mitigate such disparities while promoting a sense of collective identity."),
                ("system", "Several institutions have adopted that approach, though the tension between uniformity and individual expression persists."),
            ],
        ],
    },
    # =========================================================================
    # UMBRELLA
    # =========================================================================
    "umbrella": {
        "beginner": [
            [
                ("learner", "I need my umbrella today."),
                ("system", "Is it going to rain?"),
                ("learner", "Yes, the sky is very cloudy."),
                ("system", "Good idea to carry your umbrella when it looks like rain."),
            ],
            [
                ("learner", "My umbrella is red and yellow."),
                ("system", "Those are bright and cheerful colours!"),
                ("learner", "I open it when the rain starts."),
                ("system", "A colourful umbrella makes rainy days more fun."),
            ],
            [
                ("learner", "My mother always carries an umbrella."),
                ("system", "She sounds well prepared for any weather."),
                ("learner", "She uses it for rain and sun."),
                ("system", "That is very smart. Umbrellas protect us from both."),
            ],
        ],
        "elementary": [
            [
                ("learner", "I am sharing my umbrella with my friend."),
                ("system", "That is very kind of you. Is the rain heavy?"),
                ("learner", "It started raining suddenly while we were walking home."),
                ("system", "Unexpected rain during the monsoon season is very common here."),
            ],
            [
                ("learner", "I forgot my umbrella at school yesterday."),
                ("system", "Did you get wet on the way home?"),
                ("learner", "My classmate lent me hers, so I stayed dry."),
                ("system", "It is nice to have helpful friends on rainy days."),
            ],
            [
                ("learner", "The wind is turning my umbrella inside out."),
                ("system", "Strong winds can easily damage a regular umbrella."),
                ("learner", "My father suggested I buy a windproof one next time."),
                ("system", "Windproof umbrellas have a special frame that flexes without breaking."),
            ],
        ],
        "intermediate": [
            [
                ("learner", "I have noticed that many people in Chennai use umbrellas more for sun than rain."),
                ("system", "The intense heat in South India makes sun protection essential."),
                ("learner", "If UV-blocking umbrellas were more widely available, skin health would improve."),
                ("system", "Some manufacturers now offer umbrellas with certified UV protection coatings."),
            ],
            [
                ("learner", "The monsoon season has become unpredictable over the past few years."),
                ("system", "Climate change has made weather patterns harder to forecast."),
                ("learner", "If the rains had come on time this year, the farmers would not have suffered losses."),
                ("system", "Irregular monsoons affect agriculture, water supply, and daily life across India."),
            ],
            [
                ("learner", "Have you ever seen the traditional paper umbrellas used in festivals?"),
                ("system", "Yes, they are beautiful. Some are hand-painted with elaborate designs."),
                ("learner", "Artisans in some parts of India have been making them for generations."),
                ("system", "These crafts represent a cultural heritage that deserves preservation and support."),
            ],
        ],
        "upper_intermediate": [
            [
                ("learner", "It has been observed that umbrella usage patterns vary significantly across different regions of India."),
                ("system", "Coastal areas tend to use them year-round, while northern plains use them seasonally."),
                ("learner", "A survey conducted in Kerala found that over ninety percent of commuters carried umbrellas daily."),
                ("system", "Kerala's frequent rainfall and strong sun make umbrellas an indispensable part of daily life."),
            ],
            [
                ("learner", "The collapsible umbrella, which was invented in the early twentieth century, revolutionised personal weather protection."),
                ("system", "Before that, umbrellas were large, heavy, and impractical to carry routinely."),
                ("learner", "It is often overlooked how such a simple innovation had a profound impact on urban mobility."),
                ("system", "Many everyday objects we take for granted were once considered remarkable technological advances."),
            ],
            [
                ("learner", "Umbrellas are increasingly being designed with sustainability in mind using recycled materials."),
                ("system", "The fashion industry is under pressure to adopt more environmentally responsible practices."),
                ("learner", "Consumers were told that the new range was made entirely from reclaimed plastic waste."),
                ("system", "Transparency about material sourcing is becoming a key factor in purchasing decisions."),
            ],
        ],
        "advanced": [
            [
                ("learner", "The umbrella occupies a curious position in material culture as both a utilitarian object and a symbol of social status."),
                ("system", "In Victorian England, the umbrella signified respectability, while in many Asian cultures it denotes authority."),
                ("learner", "One might trace its semiotic evolution from a marker of privilege to an emblem of everyday preparedness."),
                ("system", "Such trajectories illustrate how objects accumulate and shed cultural meanings across time and geography."),
            ],
            [
                ("learner", "Were municipal authorities to install covered walkways and weather shelters more systematically, the urban experience during monsoons would improve considerably."),
                ("system", "Cities like Singapore have invested heavily in sheltered pedestrian infrastructure for precisely that reason."),
                ("learner", "The absence of such planning in Indian cities reflects a broader neglect of pedestrian-centric urban design."),
                ("system", "Integrating weather protection into urban planning would benefit not only commuters but also street vendors and the elderly."),
            ],
            [
                ("learner", "It is paradoxical that a device designed to shield us from natural elements has itself become an environmental concern due to its disposable nature."),
                ("system", "Millions of broken umbrellas end up in landfills each year, contributing to plastic and metal waste."),
                ("learner", "A circular economy approach, wherein umbrella components are designed for repair and recycling, could mitigate this issue substantially."),
                ("system", "Some European companies have pioneered modular umbrella designs with replaceable canopies and recyclable frames."),
            ],
        ],
    },
    # =========================================================================
    # HANDBAG
    # =========================================================================
    "handbag": {
        "beginner": [
            [
                ("learner", "My mother has a brown handbag."),
                ("system", "What does she keep in her handbag?"),
                ("learner", "She keeps her phone and keys inside."),
                ("system", "Those are important things to carry every day."),
            ],
            [
                ("learner", "This handbag is very pretty."),
                ("system", "Where did you see it?"),
                ("learner", "I saw it in the shop window."),
                ("system", "Window shopping is a fun way to spend an afternoon."),
            ],
            [
                ("learner", "My sister got a new handbag."),
                ("system", "Is it for school or for going out?"),
                ("learner", "She uses it when she goes out."),
                ("system", "A nice handbag can make any outfit look good."),
            ],
        ],
        "elementary": [
            [
                ("learner", "My aunt is looking for a leather handbag in the market."),
                ("system", "The leather shops in your area have good collections."),
                ("learner", "She found a nice one but it was too expensive."),
                ("system", "Good leather bags can be costly, but they last a very long time."),
            ],
            [
                ("learner", "Someone left a handbag on the bus this morning."),
                ("system", "Did anyone try to return it to the owner?"),
                ("learner", "The conductor kept it and announced it on the speaker."),
                ("system", "That was the right thing to do. The owner must have been worried."),
            ],
            [
                ("learner", "I am helping my grandmother choose a handbag for her trip."),
                ("system", "What kind of bag does she need for travelling?"),
                ("learner", "She wanted one with a zip and a long strap."),
                ("system", "Cross-body bags with zips are very practical and secure for travel."),
            ],
        ],
        "intermediate": [
            [
                ("learner", "I have noticed that handbag styles change every fashion season."),
                ("system", "The fashion industry constantly introduces new trends to drive sales."),
                ("learner", "If people focused on quality rather than trends, they would save money."),
                ("system", "Classic designs that last for years are often a better investment."),
            ],
            [
                ("learner", "Handmade handbags from local artisans deserve more recognition."),
                ("system", "Indian craftspeople produce stunning bags using traditional weaving and embroidery."),
                ("learner", "If these products were marketed online effectively, artisans could earn much more."),
                ("system", "E-commerce platforms have already helped many small artisans reach global customers."),
            ],
            [
                ("learner", "Have you considered the environmental cost of producing leather handbags?"),
                ("system", "Leather production involves significant water usage and chemical processing."),
                ("learner", "Vegan leather alternatives have improved substantially in recent years."),
                ("system", "Some plant-based leathers made from mushrooms and pineapple fibres are now quite durable."),
            ],
        ],
        "upper_intermediate": [
            [
                ("learner", "The handbag industry is estimated to be worth hundreds of billions of dollars globally."),
                ("system", "Luxury brands account for a disproportionate share of that market value."),
                ("learner", "It has been argued that the markup on designer handbags far exceeds any justifiable cost of materials or craftsmanship."),
                ("system", "Brand perception and exclusivity drive pricing in the luxury segment far more than production costs."),
            ],
            [
                ("learner", "Counterfeit handbags were reported to account for a significant portion of goods seized at customs."),
                ("system", "The counterfeit market undermines legitimate businesses and often funds criminal networks."),
                ("learner", "Consumers who knowingly purchase counterfeits are sometimes unaware of the ethical implications involved."),
                ("system", "Raising awareness about the labour conditions behind counterfeit goods could influence purchasing decisions."),
            ],
            [
                ("learner", "A designer who had originally trained as an engineer created a handbag with modular compartments."),
                ("system", "Cross-disciplinary thinking often produces the most innovative product designs."),
                ("learner", "The product was praised for its functionality and was said to have won a design award."),
                ("system", "Functionality and aesthetics together make a product truly outstanding."),
            ],
        ],
        "advanced": [
            [
                ("learner", "The handbag functions as a gendered artefact whose cultural significance extends well beyond its practical utility."),
                ("system", "Sociologists have examined how handbags reinforce and sometimes subvert gender norms in different cultures."),
                ("learner", "It is noteworthy that the growing adoption of bags by men challenges entrenched assumptions about fashion and masculinity."),
                ("system", "The blurring of gendered accessories reflects broader societal shifts toward more fluid expressions of identity."),
            ],
            [
                ("learner", "Were the true environmental cost of fast fashion accessories to be reflected in their prices, consumer behaviour would change dramatically."),
                ("system", "Externalised costs such as pollution, waste, and exploitative labour are systematically hidden from consumers."),
                ("learner", "Mandatory environmental impact labelling, akin to nutritional labels on food, could empower consumers to make informed choices."),
                ("system", "The European Union is currently piloting such transparency measures for textiles and accessories."),
            ],
            [
                ("learner", "I would contend that the fetishisation of luxury handbags in popular culture perpetuates materialistic values that undermine genuine well-being."),
                ("system", "Psychological research has consistently shown that materialistic pursuits correlate negatively with life satisfaction."),
                ("learner", "Nevertheless, one must acknowledge that such objects carry deep personal meaning for many individuals beyond mere status signalling."),
                ("system", "The relationship between material possessions and emotional attachment is indeed more nuanced than reductive critiques suggest."),
            ],
        ],
    },
    # =========================================================================
    # TIE
    # =========================================================================
    "tie": {
        "beginner": [
            [
                ("learner", "My father wears a tie to work."),
                ("system", "Many offices require men to wear ties."),
                ("learner", "His tie is dark blue and smooth."),
                ("system", "A dark blue tie goes well with most shirts."),
            ],
            [
                ("learner", "I wear a tie to school every day."),
                ("system", "Is it part of your school uniform?"),
                ("learner", "Yes, we all wear the same tie."),
                ("system", "School ties help everyone look neat and tidy."),
            ],
            [
                ("learner", "I cannot tie my tie by myself."),
                ("system", "Would you like someone to teach you?"),
                ("learner", "My older brother helps me every morning."),
                ("system", "With practice, you will learn to do it on your own soon."),
            ],
        ],
        "elementary": [
            [
                ("learner", "My uncle is buying a new tie for a wedding."),
                ("system", "Weddings are a good occasion to wear a special tie."),
                ("learner", "He chose a silk tie with small golden patterns on it."),
                ("system", "That sounds elegant and perfect for a celebration."),
            ],
            [
                ("learner", "I am learning how to make a Windsor knot."),
                ("system", "The Windsor knot is one of the most popular tie knots."),
                ("learner", "My teacher showed us a video and I practised at home."),
                ("system", "Watching videos and practising in front of a mirror really helps."),
            ],
            [
                ("learner", "The shop near my house sells ties in many colours."),
                ("system", "Do they sell ties for children too?"),
                ("learner", "Yes, I bought a striped one for my school uniform last week."),
                ("system", "Striped ties are a classic choice that never goes out of style."),
            ],
        ],
        "intermediate": [
            [
                ("learner", "I have started to appreciate how a good tie can change the look of an outfit."),
                ("system", "Accessories like ties add personality to formal clothing."),
                ("learner", "If I had known this earlier, I would have paid more attention to matching colours."),
                ("system", "Colour coordination between shirts, ties, and suits is an art worth learning."),
            ],
            [
                ("learner", "The tradition of wearing ties dates back hundreds of years."),
                ("system", "Croatian mercenaries in the 17th century are often credited with popularising the necktie."),
                ("learner", "Isn't it fascinating that a military accessory evolved into a symbol of professionalism?"),
                ("system", "Many fashion items have unexpected origins in military or workwear history."),
            ],
            [
                ("learner", "Some technology companies have abandoned the tie as part of their dress code."),
                ("system", "Casual dress codes have become common in the tech industry worldwide."),
                ("learner", "If all workplaces adopted casual dress codes, would the tie industry survive?"),
                ("system", "Ties would likely remain popular for formal events, weddings, and cultural ceremonies."),
            ],
        ],
        "upper_intermediate": [
            [
                ("learner", "It is often said that the way a person ties their knot reveals something about their personality."),
                ("system", "Fashion psychologists have studied the relationship between clothing choices and self-perception."),
                ("learner", "An article I read suggested that people who chose bolder tie patterns were more likely to be extroverted."),
                ("system", "While such correlations are interesting, they should be interpreted cautiously as they can reinforce stereotypes."),
            ],
            [
                ("learner", "Traditional Indian formal wear does not include a tie, yet it has been adopted widely in professional settings."),
                ("system", "Colonial history played a significant role in establishing Western dress codes in Indian offices."),
                ("learner", "It could be argued that retaining such dress codes reflects an uncritical acceptance of inherited norms."),
                ("system", "There has been a growing movement to embrace Indian formal wear in corporate and government settings."),
            ],
            [
                ("learner", "The tie was originally designed as a purely decorative accessory with no functional purpose."),
                ("system", "That is correct. Unlike belts or buttons, ties serve no structural role in clothing."),
                ("learner", "Sociologists have noted that it persists primarily as a cultural signifier of formality and authority."),
                ("system", "Its survival despite lacking utility is a testament to the power of social convention."),
            ],
        ],
        "advanced": [
            [
                ("learner", "The necktie serves as a compelling case study in how arbitrary symbols acquire normative force within institutional settings."),
                ("system", "Bourdieu's concept of cultural capital is particularly applicable to dress codes in professional environments."),
                ("learner", "One could argue that mandatory tie-wearing constitutes a form of soft coercion that privileges certain cultural aesthetics over others."),
                ("system", "That critique resonates especially in postcolonial contexts where Western dress norms were imposed and subsequently internalised."),
            ],
            [
                ("learner", "Were workplaces to deconstruct the semiotics of formal attire, they might discover that productivity is entirely unrelated to neckwear."),
                ("system", "Research on workplace dress codes has indeed found no correlation between tie-wearing and job performance."),
                ("learner", "The persistence of such requirements suggests that institutional aesthetics serve primarily to reinforce hierarchical structures."),
                ("system", "Dress codes function as boundary markers that delineate insider status and organisational belonging."),
            ],
            [
                ("learner", "The environmental footprint of the global tie industry, though modest compared to fast fashion, merits scrutiny nonetheless."),
                ("system", "Silk production in particular raises concerns about water usage, pesticides, and animal welfare."),
                ("learner", "A shift toward sustainably sourced or recycled textile alternatives would align the industry with broader environmental commitments."),
                ("system", "Several boutique manufacturers have already begun offering ties made from organic and upcycled materials."),
            ],
        ],
    },
    # =========================================================================
    # SUITCASE
    # =========================================================================
    "suitcase": {
        "beginner": [
            [
                ("learner", "I have a big red suitcase."),
                ("system", "A bright colour makes it easy to find at the airport!"),
                ("learner", "I pack my clothes inside it."),
                ("system", "Do you fold your clothes neatly before packing?"),
            ],
            [
                ("learner", "My family is packing our suitcases."),
                ("system", "Are you going on a trip somewhere?"),
                ("learner", "We are going to visit my grandparents."),
                ("system", "How exciting! I hope you have a wonderful visit."),
            ],
            [
                ("learner", "This suitcase has four wheels."),
                ("system", "Four wheels make it much easier to pull along."),
                ("learner", "I can push it with one hand."),
                ("system", "Wheeled suitcases are great for carrying heavy loads."),
            ],
        ],
        "elementary": [
            [
                ("learner", "I am trying to close my suitcase but it is too full."),
                ("system", "Maybe you packed more than you need."),
                ("learner", "My mother told me to take out some clothes and pack light."),
                ("system", "Packing light is always a good idea, especially for short trips."),
            ],
            [
                ("learner", "We are waiting for our suitcase at the baggage claim."),
                ("system", "Can you see it on the conveyor belt?"),
                ("learner", "I spotted it because of the ribbon my father tied on the handle."),
                ("system", "Marking your suitcase is a clever way to identify it quickly."),
            ],
            [
                ("learner", "My cousin gave me his old suitcase for my school trip."),
                ("system", "That was generous of him. Is it in good condition?"),
                ("learner", "It has a small scratch, but the wheels and zip work perfectly."),
                ("system", "Reusing a suitcase is practical and good for the environment."),
            ],
        ],
        "intermediate": [
            [
                ("learner", "I have always struggled with packing efficiently for long trips."),
                ("system", "Rolling clothes instead of folding them saves a lot of space."),
                ("learner", "If I had learned that technique earlier, I would not have overpacked so many times."),
                ("system", "Packing cubes are another useful tool for keeping everything organised."),
            ],
            [
                ("learner", "Airlines have become increasingly strict about suitcase weight limits."),
                ("system", "Extra baggage fees can be very expensive on budget airlines."),
                ("learner", "Investing in a lightweight suitcase could save travellers money over time."),
                ("system", "Modern polycarbonate suitcases are both lightweight and extremely durable."),
            ],
            [
                ("learner", "Have you ever had a suitcase lost by an airline?"),
                ("system", "Unfortunately, yes. It took three days for them to locate it."),
                ("learner", "I always keep essentials in my carry-on in case my checked bag goes missing."),
                ("system", "That is a wise precaution that every frequent traveller should follow."),
            ],
        ],
        "upper_intermediate": [
            [
                ("learner", "Smart suitcases equipped with GPS tracking and built-in scales have been introduced to the market."),
                ("system", "Technology is transforming even the most traditional travel accessories."),
                ("learner", "However, some airlines banned suitcases with non-removable lithium batteries due to safety concerns."),
                ("system", "Regulations have since been updated, and most smart luggage now features removable battery packs."),
            ],
            [
                ("learner", "The suitcase that had been left unattended at the railway station caused a security scare."),
                ("system", "Unattended bags are treated as potential threats in public transport areas."),
                ("learner", "It was later reported that the owner had simply forgotten it while buying a ticket."),
                ("system", "Such incidents highlight the importance of keeping personal belongings in sight at all times."),
            ],
            [
                ("learner", "A documentary explored how suitcase design has evolved from heavy leather trunks to ultralight hard shells."),
                ("system", "The shift mirrors broader changes in transportation from ships and trains to commercial aviation."),
                ("learner", "Each era's travel requirements directly influenced the materials and dimensions of luggage produced."),
                ("system", "Today's overhead bin size restrictions have become the primary constraint shaping carry-on suitcase design."),
            ],
        ],
        "advanced": [
            [
                ("learner", "The suitcase, as both a practical object and a cultural symbol, encapsulates narratives of migration, aspiration, and displacement."),
                ("system", "In literature and film, the suitcase frequently represents the distillation of one's life into portable form."),
                ("learner", "For refugees and immigrants, the act of packing a single suitcase carries a weight of meaning that transcends mere logistics."),
                ("system", "That emotional dimension has been powerfully captured in museum exhibitions dedicated to migration stories worldwide."),
            ],
            [
                ("learner", "Were the luggage industry to adopt truly circular manufacturing principles, the volume of non-recyclable waste generated annually would decline significantly."),
                ("system", "Most conventional suitcases combine materials in ways that make end-of-life recycling prohibitively difficult."),
                ("learner", "Designing for disassembly, where each component can be separated and recycled independently, offers a viable path forward."),
                ("system", "A few pioneering brands have committed to take-back programmes, though industry-wide adoption remains a distant prospect."),
            ],
            [
                ("learner", "I would argue that the proliferation of ultra-cheap luggage has contributed to a throwaway culture that normalises wastefulness in travel."),
                ("system", "The average lifespan of a budget suitcase is reportedly fewer than five trips before a component fails."),
                ("learner", "Incentivising repairability through extended producer responsibility legislation could disrupt this unsustainable pattern."),
                ("system", "The right-to-repair movement, which has gained momentum in electronics, could plausibly extend to durable goods like luggage."),
            ],
        ],
    },
    # =========================================================================
    # FRISBEE
    # =========================================================================
    "frisbee": {
        "beginner": [
            [
                ("learner", "I play with a frisbee in the park."),
                ("system", "Playing frisbee outdoors is great exercise."),
                ("learner", "I throw it to my friend."),
                ("system", "Catching a frisbee takes good hand-eye coordination."),
            ],
            [
                ("learner", "My frisbee is green and light."),
                ("system", "Light frisbees are easier to throw far."),
                ("learner", "It flies very far in the wind."),
                ("system", "The wind can carry a frisbee across the whole field!"),
            ],
            [
                ("learner", "We play frisbee after school every day."),
                ("system", "That sounds like a fun way to spend the afternoon."),
                ("learner", "My dog likes to catch it too."),
                ("system", "Dogs love chasing frisbees! They are very good at catching them."),
            ],
        ],
        "elementary": [
            [
                ("learner", "We are playing frisbee on the beach this weekend."),
                ("system", "The beach is a perfect place for frisbee because of the open space."),
                ("learner", "Last time the wind carried it into the water and I had to swim to get it."),
                ("system", "Playing near the water always adds some extra excitement."),
            ],
            [
                ("learner", "Our PE teacher is teaching us how to throw a frisbee properly."),
                ("system", "Did you learn the backhand throw first?"),
                ("learner", "Yes, and then we practised catching it with both hands."),
                ("system", "A firm two-handed catch is the best way to start."),
            ],
            [
                ("learner", "I bought a glow-in-the-dark frisbee for evening games."),
                ("system", "That must look amazing when it flies through the air at night."),
                ("learner", "We played with it in the garden after dinner yesterday."),
                ("system", "Glow frisbees make evening outdoor activities much more enjoyable."),
            ],
        ],
        "intermediate": [
            [
                ("learner", "I have recently become interested in ultimate frisbee as a competitive sport."),
                ("system", "Ultimate frisbee has grown rapidly and is even being considered for the Olympics."),
                ("learner", "If our school formed a team, I would be the first to sign up."),
                ("system", "You should talk to your PE teacher about starting a club."),
            ],
            [
                ("learner", "The physics of frisbee flight involves principles of aerodynamics and angular momentum."),
                ("system", "The spin creates gyroscopic stability, which keeps the disc level."),
                ("learner", "If the disc were thrown without enough spin, it would wobble and fall quickly."),
                ("system", "That relationship between spin rate and stability is what makes frisbee technique so important."),
            ],
            [
                ("learner", "Disc golf, which uses frisbee-like discs, has become popular in many countries."),
                ("system", "There are now thousands of disc golf courses around the world."),
                ("learner", "I have tried it once and found it more challenging than regular frisbee."),
                ("system", "The precision required in disc golf is comparable to traditional golf."),
            ],
        ],
        "upper_intermediate": [
            [
                ("learner", "Ultimate frisbee is notable for its spirit of the game principle, which relies on self-officiation."),
                ("system", "Players are expected to call their own fouls, which promotes honesty and sportsmanship."),
                ("learner", "It has been argued that this model could be adopted by other sports to reduce referee controversies."),
                ("system", "While idealistic, self-officiation works best in communities where fair play is deeply valued."),
            ],
            [
                ("learner", "The frisbee was originally inspired by pie tins that university students threw to each other in the 1940s."),
                ("system", "The Frisbie Pie Company tins became the unlikely origin of a global sport."),
                ("learner", "It is remarkable that such a casual pastime was eventually formalised into a sport with international governing bodies."),
                ("system", "The journey from a pie tin to an Olympic consideration captures the organic evolution of recreational culture."),
            ],
            [
                ("learner", "A coach explained that mastering the forehand flick was considered essential for competitive ultimate players."),
                ("system", "The forehand throw offers speed and angles that the backhand cannot easily achieve."),
                ("learner", "Players who relied exclusively on backhand throws were reported to be at a significant tactical disadvantage."),
                ("system", "Versatility in throwing technique is what separates advanced players from intermediate ones."),
            ],
        ],
        "advanced": [
            [
                ("learner", "Ultimate frisbee's rejection of referees constitutes a radical experiment in cooperative sports governance."),
                ("system", "It challenges the assumption that competitive sport inherently requires external authority to function fairly."),
                ("learner", "Were this model to prove scalable to professional leagues, it would fundamentally reshape our understanding of sportsmanship."),
                ("system", "However, sceptics argue that financial stakes at the professional level would inevitably erode the self-officiation ethos."),
            ],
            [
                ("learner", "The aerodynamic properties of a frisbee disc offer a surprisingly rich domain for applied physics research."),
                ("system", "Bernoulli's principle, the Magnus effect, and precession all interact in complex ways during disc flight."),
                ("learner", "I would suggest that frisbee dynamics could serve as an engaging pedagogical tool for introducing undergraduate students to fluid mechanics."),
                ("system", "Several engineering programmes have already incorporated disc flight analysis into their introductory physics curricula."),
            ],
            [
                ("learner", "The democratising ethos of ultimate frisbee, with its emphasis on accessibility and gender equity, sets it apart from many established sports."),
                ("system", "Mixed-gender competition is integrated into the sport at nearly every level, which is rare in organised athletics."),
                ("learner", "It is worth examining whether this inclusive structure has translated into genuinely equitable participation or merely performative inclusivity."),
                ("system", "Empirical studies suggest meaningful gains in gender equity, though disparities in leadership and media coverage persist."),
            ],
        ],
    },
    # =========================================================================
    # SKIS
    # =========================================================================
    "skis": {
        "beginner": [
            [
                ("learner", "Skis are long and thin."),
                ("system", "Yes! They help people slide on snow."),
                ("learner", "People use them on snowy mountains."),
                ("system", "Skiing is a popular winter sport in cold countries."),
            ],
            [
                ("learner", "I saw skis on television today."),
                ("system", "Were you watching a winter sports programme?"),
                ("learner", "Yes, the skiers went very fast downhill."),
                ("system", "Downhill skiing is exciting to watch and even more thrilling to try."),
            ],
            [
                ("learner", "I want to try skiing one day."),
                ("system", "There are some ski resorts in North India you could visit."),
                ("learner", "My teacher told us about Gulmarg in Kashmir."),
                ("system", "Gulmarg has beautiful snow and is a great place for beginners."),
            ],
        ],
        "elementary": [
            [
                ("learner", "My cousin is learning to ski in Manali this winter."),
                ("system", "Manali has some good beginner slopes for new skiers."),
                ("learner", "She sent me photos of herself wearing skis and a warm jacket."),
                ("system", "Proper clothing is just as important as having the right equipment."),
            ],
            [
                ("learner", "We are watching the Winter Olympics skiing events tonight."),
                ("system", "Which event are you most excited to see?"),
                ("learner", "I want to see the slalom race because it looks very challenging."),
                ("system", "Slalom skiers weave between gates at incredible speed and precision."),
            ],
            [
                ("learner", "The ski rental shop had many different sizes of skis on display."),
                ("system", "Ski length depends on the skier's height and skill level."),
                ("learner", "The instructor picked shorter skis for me because I was a beginner."),
                ("system", "Shorter skis are easier to turn and control when you are learning."),
            ],
        ],
        "intermediate": [
            [
                ("learner", "I have always been fascinated by cross-country skiing as a form of exercise."),
                ("system", "Cross-country skiing is considered one of the best full-body workouts available."),
                ("learner", "If there were facilities closer to my city, I would take it up as a hobby."),
                ("system", "India's Auli resort in Uttarakhand offers cross-country trails during winter months."),
            ],
            [
                ("learner", "Ski technology has evolved remarkably over the past few decades."),
                ("system", "Modern skis use carbon fibre and advanced composites for better performance."),
                ("learner", "If wooden skis were still the standard, the sport would look very different today."),
                ("system", "Material science has transformed not just skiing but nearly every competitive sport."),
            ],
            [
                ("learner", "Climate change has shortened ski seasons in many traditional winter destinations."),
                ("system", "Several European resorts have had to close early due to lack of snow."),
                ("learner", "Artificial snow machines have become essential for keeping ski resorts operational."),
                ("system", "However, snowmaking requires enormous amounts of water and energy, which raises sustainability concerns."),
            ],
        ],
        "upper_intermediate": [
            [
                ("learner", "It is estimated that the global ski industry generates over sixty billion dollars in annual revenue."),
                ("system", "That figure includes equipment, resorts, tourism, and related services."),
                ("learner", "However, the industry's dependence on reliable snowfall makes it increasingly vulnerable to climate variability."),
                ("system", "Many resorts are diversifying into year-round mountain tourism to mitigate seasonal revenue risks."),
            ],
            [
                ("learner", "The biomechanics of skiing place considerable stress on the anterior cruciate ligament of the knee."),
                ("system", "ACL injuries are among the most common and serious injuries in competitive skiing."),
                ("learner", "Advances in binding design were specifically aimed at reducing the forces transmitted to the knee joint."),
                ("system", "Modern release bindings have significantly lowered injury rates compared to earlier fixed designs."),
            ],
            [
                ("learner", "Ski jumping, which originated in Norway in the nineteenth century, has evolved into a highly technical sport."),
                ("system", "Jumpers must optimise their body position for both distance and aerodynamic efficiency."),
                ("learner", "The V-style technique, which was introduced in the 1990s, was initially ridiculed before being universally adopted."),
                ("system", "Innovation in sports often faces resistance before its advantages become undeniable."),
            ],
        ],
        "advanced": [
            [
                ("learner", "The environmental paradox of skiing, a sport that celebrates nature yet depends on infrastructure that degrades it, warrants critical examination."),
                ("system", "Resort development involves deforestation, water diversion, and habitat fragmentation in alpine ecosystems."),
                ("learner", "Were the industry to internalise its environmental externalities, the true cost of a lift ticket would be substantially higher."),
                ("system", "Some resorts have begun carbon offset programmes, though their efficacy and transparency remain subjects of debate."),
            ],
            [
                ("learner", "The socioeconomic exclusivity of skiing raises legitimate questions about sport accessibility and class stratification."),
                ("system", "Equipment costs, travel expenses, and lift tickets make skiing prohibitively expensive for much of the world's population."),
                ("learner", "Initiatives to democratise winter sports in developing nations face the structural barrier of limited infrastructure and warm climates."),
                ("system", "Indoor ski facilities and dry slopes offer partial solutions, though they cannot replicate the full mountain experience."),
            ],
            [
                ("learner", "It is imperative that ski resort planning integrate ecological impact assessments into every stage of development."),
                ("system", "The Alps have seen irreversible ecological damage from decades of unchecked resort expansion."),
                ("learner", "A precautionary approach, guided by the principle that pristine alpine environments are irreplaceable, should govern future developments."),
                ("system", "Balancing economic interests with ecological preservation demands regulatory frameworks informed by rigorous environmental science."),
            ],
        ],
    },
    # =========================================================================
    # SNOWBOARD
    # =========================================================================
    "snowboard": {
        "beginner": [
            [
                ("learner", "A snowboard is a flat board for snow."),
                ("system", "That's right! You stand on it and slide down hills."),
                ("learner", "It looks fun but a little scary."),
                ("system", "Beginners can start on gentle slopes and learn slowly."),
            ],
            [
                ("learner", "I saw snowboarding on television yesterday."),
                ("system", "Was it an extreme sports show?"),
                ("learner", "Yes, they did jumps and tricks."),
                ("system", "Professional snowboarders practise for many years to do those tricks."),
            ],
            [
                ("learner", "My friend has a picture of a snowboard."),
                ("system", "Has your friend ever tried snowboarding?"),
                ("learner", "No, but he wants to learn someday."),
                ("system", "Maybe you can both learn together when you visit the mountains."),
            ],
        ],
        "elementary": [
            [
                ("learner", "Snowboarding looks different from skiing because you use one board."),
                ("system", "Yes, both feet are attached to a single board in snowboarding."),
                ("learner", "My cousin tried snowboarding in Auli and said the balance was difficult."),
                ("system", "Balancing sideways on a board takes some getting used to."),
            ],
            [
                ("learner", "We are watching the snowboarding halfpipe event at the Olympics."),
                ("system", "The halfpipe is one of the most spectacular snowboarding events."),
                ("learner", "The athletes flew so high above the pipe and did incredible spins."),
                ("system", "They can reach heights of over six metres above the halfpipe wall."),
            ],
            [
                ("learner", "I read that snowboarding started as a combination of surfing and skiing."),
                ("system", "That's correct. It was invented in the 1960s in America."),
                ("learner", "It became an Olympic sport only about thirty years ago."),
                ("system", "Snowboarding brought a youthful energy to the Winter Olympics."),
            ],
        ],
        "intermediate": [
            [
                ("learner", "I have been watching snowboarding tutorials online to prepare for a trip."),
                ("system", "Video tutorials can teach you the basics before you hit the slopes."),
                ("learner", "If I master the heel-side turn first, the rest should come naturally."),
                ("system", "The heel-side turn is indeed the foundation for all snowboarding techniques."),
            ],
            [
                ("learner", "Snowboard design has incorporated aerospace materials to improve performance."),
                ("system", "Carbon fibre cores and sintered bases are now standard on premium boards."),
                ("learner", "If the price of advanced boards came down, more young people could compete."),
                ("system", "Some brands offer affordable entry-level boards with decent technology for beginners."),
            ],
            [
                ("learner", "The rivalry between skiers and snowboarders was quite intense in the early years."),
                ("system", "Many ski resorts initially banned snowboarders from their slopes."),
                ("learner", "Thankfully, that conflict has largely disappeared as both communities learned to coexist."),
                ("system", "Today, most resorts welcome both skiers and snowboarders equally."),
            ],
        ],
        "upper_intermediate": [
            [
                ("learner", "It has been reported that snowboard injuries predominantly affect the wrists and upper body."),
                ("system", "This differs from skiing, where lower limb injuries are more prevalent."),
                ("learner", "Wrist guards, which are commonly worn in skateboarding, were subsequently adopted by snowboarders."),
                ("system", "The transfer of safety equipment between similar sports reflects practical cross-pollination of knowledge."),
            ],
            [
                ("learner", "The snowboarding community has historically defined itself in opposition to traditional winter sports culture."),
                ("system", "Its roots in skateboarding and surf culture gave it a counter-cultural identity."),
                ("learner", "However, commercialisation and Olympic inclusion have been criticised for diluting that rebellious ethos."),
                ("system", "Balancing mainstream appeal with subcultural authenticity is a tension many youth sports face."),
            ],
            [
                ("learner", "A new type of snowboard was designed that allows riders to switch between alpine and freestyle modes."),
                ("system", "Versatile equipment appeals to riders who want variety without owning multiple boards."),
                ("learner", "The manufacturer claimed that this innovation was inspired by adjustable suspension systems in mountain bikes."),
                ("system", "Cross-industry inspiration is a hallmark of modern sports equipment engineering."),
            ],
        ],
        "advanced": [
            [
                ("learner", "The commercialisation of snowboarding culture illustrates how capitalism co-opts countercultural movements through branding and spectacle."),
                ("system", "What began as grassroots self-expression has become a multi-billion-dollar global industry."),
                ("learner", "One must question whether the sport's original values of freedom and creativity can survive within the constraints of corporate sponsorship."),
                ("system", "This tension between authenticity and commerce is not unique to snowboarding; it recurs across music, art, and sport."),
            ],
            [
                ("learner", "The biomechanical demands of snowboard tricks necessitate a sophisticated understanding of rotational physics."),
                ("system", "Angular momentum conservation governs how athletes initiate and control spins in mid-air."),
                ("learner", "Were athletes to receive formal physics education alongside physical training, their intuitive grasp of these principles might translate into measurable performance gains."),
                ("system", "Sports science programmes at several universities now integrate biomechanical analysis into athlete training curricula."),
            ],
            [
                ("learner", "The environmental footprint of snowboard manufacturing, from petrochemical-based resins to carbon fibre production, merits greater transparency."),
                ("system", "Life cycle assessments of snowboard production reveal significant energy consumption and chemical waste."),
                ("learner", "It is incumbent upon manufacturers to pursue bio-based alternatives and closed-loop production processes."),
                ("system", "A few independent makers have experimented with bamboo cores and bio-resins, though scalability remains a challenge."),
            ],
        ],
    },
    # =========================================================================
    # SPORTS BALL
    # =========================================================================
    "sports ball": {
        "beginner": [
            [
                ("learner", "I play with a ball every day."),
                ("system", "What kind of ball game do you play?"),
                ("learner", "I play cricket with my friends."),
                ("system", "Cricket is the most popular sport in India!"),
            ],
            [
                ("learner", "The ball is round and red."),
                ("system", "A red ball is used in test cricket matches."),
                ("learner", "I kick it with my foot sometimes."),
                ("system", "That sounds more like football! Both are great sports."),
            ],
            [
                ("learner", "We need a ball for sports day."),
                ("system", "What event are you taking part in?"),
                ("learner", "I am in the throw ball team."),
                ("system", "Throw ball is a fun team sport. Good luck!"),
            ],
        ],
        "elementary": [
            [
                ("learner", "My brother is practising football with a new ball in the ground."),
                ("system", "Does he play for the school football team?"),
                ("learner", "He joined the team last year and scored three goals so far."),
                ("system", "That is impressive for his first year on the team."),
            ],
            [
                ("learner", "We are playing a tennis ball cricket match after school."),
                ("system", "Tennis ball cricket is very popular in streets and open grounds."),
                ("learner", "I bowled five overs yesterday and took two wickets."),
                ("system", "Two wickets in five overs is a great performance for any bowler."),
            ],
            [
                ("learner", "The volleyball bounced over the net and landed out of bounds."),
                ("system", "Was it a close call or clearly out?"),
                ("learner", "It was very close, so both teams argued about it for a while."),
                ("system", "Close calls are part of the excitement in any ball game."),
            ],
        ],
        "intermediate": [
            [
                ("learner", "I have noticed that different ball designs affect how they move through the air."),
                ("system", "Ball aerodynamics is actually a well-studied field in sports science."),
                ("learner", "If the surface of a cricket ball were perfectly smooth, swing bowling would be impossible."),
                ("system", "The raised seam and differential polish on each side create the pressure imbalance needed for swing."),
            ],
            [
                ("learner", "The evolution of football design from leather panels to synthetic materials has changed the game significantly."),
                ("system", "Modern footballs are lighter, more consistent, and more water-resistant."),
                ("learner", "Some goalkeepers have complained that newer balls move unpredictably in the air."),
                ("system", "The reduced panel count in recent designs can create unusual aerodynamic effects."),
            ],
            [
                ("learner", "India's performance in team ball sports has improved dramatically over the past decade."),
                ("system", "Investment in grassroots programmes and professional leagues has made a difference."),
                ("learner", "If the government continued funding sports academies, we could see Olympic medals in more ball sports."),
                ("system", "Sustained investment in talent development is the key to international success."),
            ],
        ],
        "upper_intermediate": [
            [
                ("learner", "The controversy surrounding ball-tampering in cricket has raised important questions about sportsmanship."),
                ("system", "Several high-profile incidents have led to bans and public outrage."),
                ("learner", "It was argued that the pressure to win at the international level created an environment where such behaviour was tolerated."),
                ("system", "The governing bodies have since introduced stricter monitoring and more severe penalties."),
            ],
            [
                ("learner", "The introduction of smart balls with embedded sensors is transforming how sports performance is analysed."),
                ("system", "These balls can track speed, spin rate, trajectory, and impact force in real time."),
                ("learner", "Data collected from smart balls has been used to challenge umpiring decisions in professional cricket."),
                ("system", "Technology-assisted decision-making is becoming the norm across most major ball sports."),
            ],
            [
                ("learner", "The selection of an official ball for a tournament is a process that involves rigorous scientific testing."),
                ("system", "FIFA and ICC both have certification standards that balls must meet before approval."),
                ("learner", "Manufacturers that win tournament contracts are reported to see enormous increases in consumer sales."),
                ("system", "The commercial value of being the official ball supplier drives intense competition among manufacturers."),
            ],
        ],
        "advanced": [
            [
                ("learner", "The physics of ball spin encompasses complex interactions between the Magnus effect, surface roughness, and atmospheric conditions."),
                ("system", "Research into cricket ball aerodynamics alone has produced hundreds of peer-reviewed papers."),
                ("learner", "It is fascinating that practitioners, through intuition and experience, exploit physical principles that took scientists decades to formally describe."),
                ("system", "The gap between embodied expertise and theoretical understanding remains a productive area of inquiry in sports science."),
            ],
            [
                ("learner", "Were access to quality sports equipment more equitably distributed, talent identification in developing nations would improve substantially."),
                ("system", "Many potential athletes in rural areas lack even basic equipment to develop their skills."),
                ("learner", "Programmes that redistribute used professional-grade equipment to underserved communities address both waste and inequity simultaneously."),
                ("system", "Such initiatives, when paired with coaching infrastructure, have demonstrably expanded the talent pipeline in several sports."),
            ],
            [
                ("learner", "The cultural significance of specific ball sports in shaping national identity cannot be overstated, particularly in the case of cricket in South Asia."),
                ("system", "Cricket in India transcends sport; it functions as a unifying cultural force across linguistic and regional divides."),
                ("learner", "I would argue that this centrality, while powerful, inadvertently marginalises other sports and limits the diversification of India's athletic culture."),
                ("system", "The tension between cricket's dominance and the development of alternative sports is a defining challenge for Indian sports policy."),
            ],
        ],
    },
    # =========================================================================
    # KITE
    # =========================================================================
    "kite": {
        "beginner": [
            [
                ("learner", "I fly my kite on windy days."),
                ("system", "Windy days are the best time to fly a kite!"),
                ("learner", "My kite is orange and has a long tail."),
                ("system", "The tail helps the kite stay balanced in the air."),
            ],
            [
                ("learner", "We fly kites on Pongal every year."),
                ("system", "Kite flying is a wonderful tradition during Pongal."),
                ("learner", "I fly my kite from the roof."),
                ("system", "Rooftops give you more wind and open space."),
            ],
            [
                ("learner", "My grandfather makes kites from paper and bamboo."),
                ("system", "That is a wonderful skill! Does he teach you too?"),
                ("learner", "Yes, I helped him make one yesterday."),
                ("system", "Making kites by hand is a traditional craft worth learning."),
            ],
        ],
        "elementary": [
            [
                ("learner", "We are going to the beach to fly kites this weekend."),
                ("system", "The sea breeze makes the beach perfect for kite flying."),
                ("learner", "Last time my kite went so high I could barely see it."),
                ("system", "That means you had good wind and excellent string control."),
            ],
            [
                ("learner", "I am making a kite for the school competition this Friday."),
                ("system", "What design are you planning for your kite?"),
                ("learner", "I painted a peacock on it with watercolours."),
                ("system", "A peacock design sounds beautiful and very creative."),
            ],
            [
                ("learner", "The kite festival in Ahmedabad attracts visitors from all over India."),
                ("system", "The Uttarayan kite festival is famous worldwide."),
                ("learner", "People flew thousands of colourful kites and the sky looked amazing."),
                ("system", "It is one of the most spectacular cultural festivals in the country."),
            ],
        ],
        "intermediate": [
            [
                ("learner", "Kite flying has a rich cultural history across many Asian countries."),
                ("system", "In India, China, and Japan, kites have been flown for centuries."),
                ("learner", "If I visited the kite museum in Ahmedabad, I could see designs from many different traditions."),
                ("system", "That museum houses an impressive collection of kites from around the world."),
            ],
            [
                ("learner", "The manja thread used in competitive kite flying has caused injuries to birds and people."),
                ("system", "Many cities have now banned glass-coated strings for safety reasons."),
                ("learner", "If safer alternatives were promoted more effectively, kite fighting could continue without the harm."),
                ("system", "Cotton thread and biodegradable options are now being encouraged by festival organisers."),
            ],
            [
                ("learner", "Have you ever considered how kite flying teaches children about wind patterns and aerodynamics?"),
                ("system", "It is one of the earliest hands-on encounters children have with physics concepts."),
                ("learner", "Schools could incorporate kite-making into their science curriculum very effectively."),
                ("system", "Project-based learning through kite design would make physics tangible and enjoyable."),
            ],
        ],
        "upper_intermediate": [
            [
                ("learner", "Power kites, which generate significant pull from the wind, are being explored as a source of renewable energy."),
                ("system", "Airborne wind energy systems use tethered kites to access stronger winds at higher altitudes."),
                ("learner", "It was reported that a European start-up had successfully powered a small community using kite-based turbines."),
                ("system", "The technology is still in its early stages, but the potential for low-cost wind energy is promising."),
            ],
            [
                ("learner", "The tradition of kite fighting, which involves cutting the strings of rival kites, is deeply embedded in South Asian culture."),
                ("system", "Competitive kite flying requires skill, strategy, and quick reflexes."),
                ("learner", "Cultural historians have noted that the practice served as a form of social bonding across class boundaries."),
                ("system", "Public kite festivals historically brought together people from all walks of life on equal footing."),
            ],
            [
                ("learner", "A ban on kite flying was once imposed in certain regions for fear it would distract workers from their duties."),
                ("system", "Such restrictions reveal how authorities have historically viewed leisure activities with suspicion."),
                ("learner", "The resilience of kite-flying traditions despite periodic prohibitions speaks to their deep cultural significance."),
                ("system", "Cultural practices that serve important social functions tend to persist regardless of official restrictions."),
            ],
        ],
        "advanced": [
            [
                ("learner", "The kite occupies a liminal space in material culture, existing simultaneously as a children's toy, a competitive instrument, and a spiritual symbol."),
                ("system", "In Japanese tradition, kites are flown to celebrate births and ward off evil spirits."),
                ("learner", "This multiplicity of meanings suggests that objects derive significance not from inherent properties but from the social contexts in which they are deployed."),
                ("system", "That constructionist perspective aligns with anthropological theories of material culture as a medium for social negotiation."),
            ],
            [
                ("learner", "Were governments to invest in airborne wind energy research at scale, kite-based power generation could complement existing renewable infrastructure."),
                ("system", "Preliminary analyses suggest that high-altitude wind resources are more consistent and powerful than ground-level ones."),
                ("learner", "The engineering challenges of maintaining structural integrity and control at altitude, however, remain formidable."),
                ("system", "Advances in autonomous flight systems and lightweight materials are progressively addressing those technical barriers."),
            ],
            [
                ("learner", "I would argue that the regulatory response to manja-related injuries exemplifies the broader challenge of balancing cultural preservation with public safety."),
                ("system", "Outright bans risk erasing traditions, while permissive approaches risk preventable harm."),
                ("learner", "A collaborative approach involving artisans, safety engineers, and community leaders would yield more culturally sensitive and effective regulation."),
                ("system", "Stakeholder-inclusive policymaking has proven more durable and legitimate than top-down prohibitions in analogous cases."),
            ],
        ],
    },
    # =========================================================================
    # BASEBALL BAT
    # =========================================================================
    "baseball bat": {
        "beginner": [
            [
                ("learner", "A baseball bat is long and heavy."),
                ("system", "Yes, it is made of wood or metal."),
                ("learner", "Players use it to hit the ball."),
                ("system", "A good swing can send the ball very far!"),
            ],
            [
                ("learner", "I saw a baseball bat in a shop."),
                ("system", "Did you want to buy it?"),
                ("learner", "Yes, but it was too big for me."),
                ("system", "There are smaller bats made for younger players."),
            ],
            [
                ("learner", "My cousin plays baseball in America."),
                ("system", "Baseball is very popular in the United States."),
                ("learner", "He sends me videos of his games."),
                ("system", "It must be exciting to watch your cousin play!"),
            ],
        ],
        "elementary": [
            [
                ("learner", "I am watching a baseball game on television for the first time."),
                ("system", "What do you think of the sport so far?"),
                ("learner", "The batter just hit the ball over the fence for a home run."),
                ("system", "Home runs are the most thrilling moments in baseball."),
            ],
            [
                ("learner", "Our sports teacher brought a baseball bat to class today."),
                ("system", "Is your school introducing baseball as a new sport?"),
                ("learner", "She wanted us to try different sports from around the world."),
                ("system", "Trying new sports is a great way to discover hidden talents."),
            ],
            [
                ("learner", "The wooden baseball bat cracked during the practice match."),
                ("system", "Wooden bats can break if the ball hits the wrong spot."),
                ("learner", "The coach said aluminium bats are stronger and last much longer."),
                ("system", "That is true, though professional players are required to use wooden bats."),
            ],
        ],
        "intermediate": [
            [
                ("learner", "Baseball has never gained the same popularity in India as cricket, despite some similarities."),
                ("system", "Both involve a bat, a ball, and fielding, yet the cultures around them are very different."),
                ("learner", "If baseball leagues were established in India, they might attract cricket fans looking for variety."),
                ("system", "A few grassroots baseball programmes have already started in Mumbai and Delhi."),
            ],
            [
                ("learner", "The physics behind hitting a baseball involves reaction time, bat speed, and impact angle."),
                ("system", "Professional batters have less than half a second to decide whether to swing."),
                ("learner", "I have read that the sweet spot of a bat is where vibration is minimised."),
                ("system", "Hitting the sweet spot transfers maximum energy to the ball and feels effortless to the batter."),
            ],
            [
                ("learner", "The transition from wooden to aluminium bats in amateur baseball sparked a long debate."),
                ("system", "Aluminium bats increase ball speed, which raises safety concerns for pitchers and fielders."),
                ("learner", "If safety regulations had not been updated, serious injuries could have become more common."),
                ("system", "Performance standards now limit how fast the ball can travel off an aluminium bat."),
            ],
        ],
        "upper_intermediate": [
            [
                ("learner", "The economics of the baseball bat industry are closely tied to the supply of ash and maple timber."),
                ("system", "The emerald ash borer beetle has devastated ash tree populations in North America."),
                ("learner", "It was reported that this pest had caused a significant shift toward maple as the preferred bat material."),
                ("system", "Environmental threats to natural resources can have cascading effects on industries that depend on them."),
            ],
            [
                ("learner", "Baseball analytics, which is commonly known as sabermetrics, has transformed how batting performance is evaluated."),
                ("system", "Statistics like exit velocity and launch angle are now central to player assessment."),
                ("learner", "The widespread adoption of data analytics was popularised by the Moneyball approach in the early 2000s."),
                ("system", "That data-driven revolution has since spread to virtually every professional sport worldwide."),
            ],
            [
                ("learner", "A museum exhibit on the history of the baseball bat revealed how its shape and weight have evolved over a century."),
                ("system", "Early bats were much heavier and had varied shapes before regulations standardised the design."),
                ("learner", "The curator explained that each era's bat reflected the prevailing hitting philosophy of the time."),
                ("system", "Equipment evolution and tactical evolution in sport are deeply intertwined and mutually reinforcing."),
            ],
        ],
        "advanced": [
            [
                ("learner", "The baseball bat, as a cultural artefact, embodies the intersection of craftsmanship, material science, and sporting tradition."),
                ("system", "Master bat makers are revered in baseball culture for their understanding of wood grain and balance."),
                ("learner", "One could argue that the persistence of wooden bats in professional play represents a conscious privileging of tradition over technological optimisation."),
                ("system", "That choice reflects a broader tension in sport between preserving historical integrity and embracing innovation."),
            ],
            [
                ("learner", "Were baseball to gain a foothold in the Indian sporting landscape, it would necessitate a fundamental rethinking of how bat-and-ball sports are promoted and funded."),
                ("system", "The dominance of cricket creates a structural barrier that any competing bat-and-ball sport must overcome."),
                ("learner", "International baseball federations should perhaps leverage the transferable skills between cricket and baseball to recruit crossover athletes."),
                ("system", "Several successful cricket-to-baseball transitions have demonstrated the viability of that talent development pathway."),
            ],
            [
                ("learner", "The metallurgical engineering behind composite baseball bats raises questions about where legitimate equipment improvement ends and unfair advantage begins."),
                ("system", "Regulatory bodies face the perpetual challenge of defining acceptable performance boundaries as materials science advances."),
                ("learner", "This dilemma is analogous to debates in other sports about technology doping, from swimsuits to running shoes."),
                ("system", "The fundamental question of whether sport should test human ability or technological innovation remains philosophically unresolved."),
            ],
        ],
    },
    # =========================================================================
    # BASEBALL GLOVE
    # =========================================================================
    "baseball glove": {
        "beginner": [
            [
                ("learner", "A baseball glove is big and brown."),
                ("system", "Yes, it is made of leather and fits on one hand."),
                ("learner", "Players use it to catch the ball."),
                ("system", "The glove protects the hand and helps grip the ball."),
            ],
            [
                ("learner", "My uncle gave me a baseball glove."),
                ("system", "That was a thoughtful gift! Have you used it yet?"),
                ("learner", "I practise catching with my brother."),
                ("system", "Playing catch is a great way to learn how to use a glove."),
            ],
            [
                ("learner", "The baseball glove has a pocket inside."),
                ("system", "That pocket is where the ball lands when you catch it."),
                ("learner", "I close my hand fast to keep the ball."),
                ("system", "Quick reflexes are important for catching in any sport."),
            ],
        ],
        "elementary": [
            [
                ("learner", "I am learning to catch with my new baseball glove at the park."),
                ("system", "Are you enjoying it so far?"),
                ("learner", "My friend threw the ball and I caught it on my first try."),
                ("system", "That is a great start! Catching gets easier with practice."),
            ],
            [
                ("learner", "The glove felt stiff when I first put it on."),
                ("system", "New leather gloves need to be broken in before they feel comfortable."),
                ("learner", "My father told me to put a ball inside and wrap it with a rubber band overnight."),
                ("system", "That is a classic technique for softening a new glove."),
            ],
            [
                ("learner", "We watched a baseball movie where the boy treasured his old glove."),
                ("system", "In American culture, a baseball glove often carries sentimental value."),
                ("learner", "His grandfather passed it down to him from many years ago."),
                ("system", "Heirlooms like that connect generations through shared experiences."),
            ],
        ],
        "intermediate": [
            [
                ("learner", "I have learned that different fielding positions in baseball require different glove sizes."),
                ("system", "Catchers use large mitts while infielders prefer smaller, more flexible gloves."),
                ("learner", "If I played as an outfielder, I would need a larger glove to reach high catches."),
                ("system", "Outfielder gloves have longer fingers to extend the player's reach."),
            ],
            [
                ("learner", "The craftsmanship that goes into making a professional baseball glove is impressive."),
                ("system", "High-end gloves are hand-stitched and use premium steerhide leather."),
                ("learner", "A well-maintained glove can last a player's entire career."),
                ("system", "Professional players often develop a deep attachment to their gloves."),
            ],
            [
                ("learner", "Have you noticed that left-handed players wear their glove on the right hand?"),
                ("system", "Yes, the glove goes on the non-throwing hand so the dominant hand stays free."),
                ("learner", "Finding left-handed gloves used to be difficult, but manufacturers now make them readily available."),
                ("system", "Inclusivity in equipment design has improved significantly across all sports."),
            ],
        ],
        "upper_intermediate": [
            [
                ("learner", "The introduction of webbed gloves in the early twentieth century fundamentally changed defensive play in baseball."),
                ("system", "Before webbed designs, fielders caught balls barehanded or with minimal padding."),
                ("learner", "It was argued at the time that using gloves was unsportsmanlike and made the game too easy."),
                ("system", "Resistance to protective equipment has been a recurring pattern in sports history."),
            ],
            [
                ("learner", "Modern glove manufacturers use computer-aided design to optimise the pocket shape for different positions."),
                ("system", "Technology has enabled a level of customisation that was impossible with traditional methods."),
                ("learner", "Professional players can now have gloves tailored to the exact dimensions of their hands and playing style."),
                ("system", "Such personalisation gives elite athletes marginal gains that can make a difference at the highest level."),
            ],
            [
                ("learner", "A documentary explored how the baseball glove industry has been affected by the rise of synthetic materials."),
                ("system", "Synthetic alternatives are lighter and cheaper but lack the durability and feel of genuine leather."),
                ("learner", "Traditionalists maintained that the tactile feedback of leather was irreplaceable for professional play."),
                ("system", "The debate between natural and synthetic materials extends across many sports equipment categories."),
            ],
        ],
        "advanced": [
            [
                ("learner", "The baseball glove serves as a compelling example of how protective equipment reshapes the tactical possibilities within a sport."),
                ("system", "The evolution of the glove directly enabled more aggressive fielding strategies and acrobatic plays."),
                ("learner", "One might argue that equipment innovation does not merely assist athletes but fundamentally redefines the game itself."),
                ("system", "This perspective challenges the notion of sport as a fixed set of rules mediated by unchanging human capability."),
            ],
            [
                ("learner", "Were the environmental impact of leather production to be fully accounted for, the true cost of a premium baseball glove would be substantially higher."),
                ("system", "Cattle ranching for leather contributes to deforestation, methane emissions, and water pollution."),
                ("learner", "The development of lab-grown leather presents a potentially transformative solution that preserves the material properties without the ecological burden."),
                ("system", "Bio-fabricated materials are approaching commercial viability and could disrupt the luxury leather goods market within a decade."),
            ],
            [
                ("learner", "The sentimental attachment people form with their baseball gloves raises interesting questions about the phenomenology of sporting objects."),
                ("system", "Heidegger's concept of equipment as ready-to-hand describes how tools become extensions of the self through habitual use."),
                ("learner", "A well-worn glove, moulded to its owner's hand, instantiates that philosophical principle in a remarkably tangible way."),
                ("system", "The embodied relationship between athlete and equipment offers fertile ground for phenomenological and cognitive science research."),
            ],
        ],
    },
    # =========================================================================
    # SKATEBOARD
    # =========================================================================
    "skateboard": {
        "beginner": [
            [
                ("learner", "I want to ride a skateboard."),
                ("system", "Skateboarding is a fun activity! Have you tried it before?"),
                ("learner", "No, but my friend has one."),
                ("system", "Maybe your friend can teach you the basics."),
            ],
            [
                ("learner", "The skateboard has four small wheels."),
                ("system", "Those wheels help it roll smoothly on flat surfaces."),
                ("learner", "It goes fast on the road."),
                ("system", "That is why wearing a helmet is very important."),
            ],
            [
                ("learner", "I see children skating in the park."),
                ("system", "Parks with smooth paths are great for skateboarding."),
                ("learner", "They can do many tricks on it."),
                ("system", "Learning tricks takes a lot of practice and patience."),
            ],
        ],
        "elementary": [
            [
                ("learner", "My older sister is teaching me to balance on a skateboard."),
                ("system", "Balance is the most important skill to learn first."),
                ("learner", "I fell twice yesterday but I did not give up."),
                ("system", "Everyone falls when they start. Keeping at it shows real determination."),
            ],
            [
                ("learner", "We are watching skateboarding videos to learn new tricks."),
                ("system", "Which trick are you trying to learn?"),
                ("learner", "I want to learn the ollie because it is the most basic jump trick."),
                ("system", "The ollie is the foundation for almost every other skateboard trick."),
            ],
            [
                ("learner", "The new skate park in our neighbourhood opened last month."),
                ("system", "Do many young people use it?"),
                ("learner", "It is full every evening with children and teenagers practising."),
                ("system", "Skate parks provide a safe space for young people to enjoy the sport."),
            ],
        ],
        "intermediate": [
            [
                ("learner", "Skateboarding was finally included in the Olympics, which was a milestone for the sport."),
                ("system", "It debuted at the 2020 Tokyo Olympics and attracted a huge audience."),
                ("learner", "If skateboarding continues to grow in India, we might see Indian athletes competing internationally."),
                ("system", "A few Indian skateboarders are already making a name for themselves on the international circuit."),
            ],
            [
                ("learner", "I have noticed that skateboarding culture has a strong connection to art and music."),
                ("system", "Deck art, graffiti, and punk rock have all been closely tied to skating."),
                ("learner", "The creative expression associated with skateboarding makes it more than just a sport."),
                ("system", "Many skateboarders see it as a lifestyle and a form of self-expression."),
            ],
            [
                ("learner", "Building skate parks in Indian cities could provide recreational spaces for urban youth."),
                ("system", "Several NGOs have already built parks in cities like Bangalore and Kovalam."),
                ("learner", "If local governments supported these initiatives, skateboarding could become more accessible."),
                ("system", "Community skateboarding programmes have shown positive social outcomes in underserved areas."),
            ],
        ],
        "upper_intermediate": [
            [
                ("learner", "The skateboarding community in India has grown significantly since the sport gained Olympic recognition."),
                ("system", "Media coverage and corporate sponsorship have both contributed to this growth."),
                ("learner", "A documentary about Indian skateboarders was credited with inspiring many young people to take up the sport."),
                ("system", "Representation in media plays a crucial role in expanding participation in non-traditional sports."),
            ],
            [
                ("learner", "Skateboard deck construction involves multiple layers of maple wood pressed together under high pressure."),
                ("system", "The typical deck uses seven plies of North American maple for strength and flexibility."),
                ("learner", "Manufacturers have experimented with bamboo and fibreglass composites to reduce environmental impact."),
                ("system", "Alternative materials are gaining traction as sustainability becomes a priority for younger consumers."),
            ],
            [
                ("learner", "It is often overlooked that skateboarding provides significant cardiovascular and coordination benefits."),
                ("system", "Studies have shown it engages core muscles and improves balance more effectively than many traditional exercises."),
                ("learner", "The perception that it is merely a recreational pastime rather than a legitimate form of exercise is slowly changing."),
                ("system", "Olympic inclusion has helped elevate its status as both a competitive sport and a fitness activity."),
            ],
        ],
        "advanced": [
            [
                ("learner", "Skateboarding's trajectory from countercultural rebellion to Olympic discipline encapsulates the complex dynamics of subcultural mainstreaming."),
                ("system", "This process involves simultaneous legitimisation and loss of the anti-establishment identity that defined the culture."),
                ("learner", "Were one to apply Hebdige's theory of subcultural incorporation, skateboarding's Olympic moment represents a textbook case of ideological recuperation."),
                ("system", "That theoretical lens reveals how institutions absorb and neutralise oppositional cultural forms through recognition and commodification."),
            ],
            [
                ("learner", "The question of who has access to skateboarding infrastructure reveals underlying patterns of spatial inequality in urban planning."),
                ("system", "Skate parks are disproportionately located in affluent neighbourhoods with political influence over municipal budgets."),
                ("learner", "Equitable distribution of recreational infrastructure should be recognised as a matter of urban justice rather than discretionary amenity provision."),
                ("system", "Participatory planning processes that centre youth voices from marginalised communities offer a path toward more just spatial outcomes."),
            ],
            [
                ("learner", "The biomechanical analysis of skateboard tricks reveals a sophisticated interplay between kinetic energy, angular momentum, and proprioceptive feedback."),
                ("system", "The ollie alone requires precisely coordinated ankle flexion, knee extension, and weight transfer within milliseconds."),
                ("learner", "It is remarkable that athletes develop such refined motor programmes through repetition alone, without formal biomechanical instruction."),
                ("system", "Implicit motor learning in action sports offers valuable insights for neuroscience and rehabilitative medicine."),
            ],
        ],
    },
    # =========================================================================
    # SURFBOARD
    # =========================================================================
    "surfboard": {
        "beginner": [
            [
                ("learner", "A surfboard is long and flat."),
                ("system", "Yes! People use it to ride ocean waves."),
                ("learner", "Surfers stand on it in the water."),
                ("system", "Standing on a surfboard takes good balance."),
            ],
            [
                ("learner", "I saw surfing on television yesterday."),
                ("system", "Did the surfers ride big waves?"),
                ("learner", "Yes, the waves were very tall and fast."),
                ("system", "Big wave surfing is one of the most exciting sports to watch."),
            ],
            [
                ("learner", "My friend has a picture of a surfboard."),
                ("system", "Has your friend ever been to a beach with surfing?"),
                ("learner", "She went to Kovalam beach last summer."),
                ("system", "Kovalam in Kerala is a popular spot for beginner surfers."),
            ],
        ],
        "elementary": [
            [
                ("learner", "Surfing is becoming popular in some parts of India now."),
                ("system", "Coastal towns in Tamil Nadu and Kerala are attracting surfers."),
                ("learner", "My neighbour went to Mahabalipuram and took a surfing lesson there."),
                ("system", "Mahabalipuram has gentle waves that are perfect for learning."),
            ],
            [
                ("learner", "The surfboard rental shop at the beach had boards of many different sizes."),
                ("system", "Bigger boards are easier for beginners to balance on."),
                ("learner", "The instructor chose a long foam board for me because I was new."),
                ("system", "Foam boards are softer and safer for learning the basics."),
            ],
            [
                ("learner", "I am reading a story about a girl who learned to surf in India."),
                ("system", "Is it based on a true story?"),
                ("learner", "Yes, she grew up in a fishing village and became a champion surfer."),
                ("system", "That is an inspiring story of talent and determination."),
            ],
        ],
        "intermediate": [
            [
                ("learner", "I have been watching surfing competitions and the skill level is extraordinary."),
                ("system", "Professional surfers make incredibly difficult manoeuvres look effortless."),
                ("learner", "If India invested more in coastal sports infrastructure, we could develop competitive surfers."),
                ("system", "The Indian Surfing Federation has already started talent development programmes along the coast."),
            ],
            [
                ("learner", "Surfboard design has changed dramatically from solid wood planks to lightweight fibreglass constructions."),
                ("system", "Hawaiian surfers originally used boards carved from single tree trunks."),
                ("learner", "Modern shaping techniques allow boards to be customised for specific wave conditions."),
                ("system", "Each design variable, from rocker to fin placement, affects how the board performs."),
            ],
            [
                ("learner", "Surfing has become a way of life for some fishing communities along the Indian coast."),
                ("system", "Children who grew up in the ocean are naturally comfortable on surfboards."),
                ("learner", "If surfing tourism grows responsibly, it could provide economic opportunities for these communities."),
                ("system", "Sustainable surf tourism that benefits locals rather than displacing them is the ideal model."),
            ],
        ],
        "upper_intermediate": [
            [
                ("learner", "The environmental impact of surfboard manufacturing is a growing concern within the surfing community."),
                ("system", "Polyurethane foam and polyester resin, the standard materials, are petroleum-based and toxic."),
                ("learner", "Several shapers have transitioned to bio-based resins and recycled foam cores in response to these concerns."),
                ("system", "The eco-surfboard movement reflects a broader shift toward environmental responsibility in action sports."),
            ],
            [
                ("learner", "It is argued that surfing's inclusion in the Olympics has fundamentally altered the culture of the sport."),
                ("system", "Traditionalists worry that competitive structures undermine surfing's soul as a free and individual pursuit."),
                ("learner", "The tension between institutionalisation and the freedom ethos of surfing is unlikely to be resolved easily."),
                ("system", "Similar debates have accompanied the Olympic inclusion of skateboarding and climbing."),
            ],
            [
                ("learner", "A study was conducted on how wave prediction technology has changed the way surfers plan their sessions."),
                ("system", "Accurate swell forecasts allow surfers to be at the right beach at the right time."),
                ("learner", "However, critics have suggested that this technology has contributed to overcrowding at popular surf breaks."),
                ("system", "When everyone has the same forecast, the best spots become saturated, which creates tension in the water."),
            ],
        ],
        "advanced": [
            [
                ("learner", "Surfing occupies a unique position in the philosophy of sport as an activity fundamentally mediated by an uncontrollable natural element."),
                ("system", "Unlike field sports where conditions are standardised, surfing requires constant adaptation to an ever-changing ocean."),
                ("learner", "This contingency arguably makes surfing a more authentic expression of human engagement with the natural world than any stadium-based sport."),
                ("system", "That perspective resonates with phenomenological accounts of embodied interaction with the environment."),
            ],
            [
                ("learner", "Were coastal development regulations in India to prioritise marine ecosystem health, the quality of surf breaks could be preserved for future generations."),
                ("system", "Poorly planned coastal construction has already destroyed wave-forming reef structures at several locations."),
                ("learner", "The concept of surfing reserves, analogous to wildlife reserves, merits serious consideration as a conservation mechanism."),
                ("system", "Australia has pioneered the legal protection of surf breaks, setting a precedent that other nations could follow."),
            ],
            [
                ("learner", "The democratisation of surfing in India challenges entrenched caste and class hierarchies in unexpected ways."),
                ("system", "Fishing community children competing alongside affluent urban surfers disrupts traditional social boundaries."),
                ("learner", "Sport, in this context, functions as a site of social contestation where embodied skill transcends inherited status."),
                ("system", "The emancipatory potential of sport is most vividly realised when it creates genuinely meritocratic spaces within stratified societies."),
            ],
        ],
    },
    # =========================================================================
    # TENNIS RACKET
    # =========================================================================
    "tennis racket": {
        "beginner": [
            [
                ("learner", "I hold the tennis racket with both hands."),
                ("system", "Some beginners use two hands for a stronger grip."),
                ("learner", "I hit the ball over the net."),
                ("system", "Well done! Hitting the ball over the net is the first step."),
            ],
            [
                ("learner", "My tennis racket is light and blue."),
                ("system", "A light racket is good for young players."),
                ("learner", "I play tennis in the morning."),
                ("system", "Morning is a great time to play before it gets too hot."),
            ],
            [
                ("learner", "My sister takes tennis lessons every Saturday."),
                ("system", "Does she enjoy her lessons?"),
                ("learner", "Yes, she likes her coach very much."),
                ("system", "A good coach makes learning any sport more enjoyable."),
            ],
        ],
        "elementary": [
            [
                ("learner", "I am practising my forehand swing at the tennis court."),
                ("system", "The forehand is the most important stroke in tennis."),
                ("learner", "My coach corrected my grip and now the ball goes straighter."),
                ("system", "Proper grip is the foundation of every good tennis stroke."),
            ],
            [
                ("learner", "We watched the Wimbledon final on television last week."),
                ("system", "Wimbledon is one of the most prestigious tennis tournaments."),
                ("learner", "The players hit the ball so hard that I could hear the sound on the screen."),
                ("system", "Professional tennis players generate incredible power and spin."),
            ],
            [
                ("learner", "My father bought me a new tennis racket for my birthday."),
                ("system", "What a wonderful birthday present! Is it a junior racket?"),
                ("learner", "Yes, the shopkeeper helped us choose the right size for my height."),
                ("system", "Using the correct racket size prevents injuries and improves your game."),
            ],
        ],
        "intermediate": [
            [
                ("learner", "I have been playing tennis for two years and my backhand has finally improved."),
                ("system", "The backhand often takes longer to develop than the forehand."),
                ("learner", "If I had started lessons earlier, I would probably be competing in tournaments by now."),
                ("system", "It is never too late to improve. Many successful players started in their teens."),
            ],
            [
                ("learner", "Tennis racket technology has evolved from wooden frames to carbon fibre composites."),
                ("system", "Modern rackets are lighter, stiffer, and generate more power."),
                ("learner", "If players from the 1970s used today's rackets, they would be amazed by the difference."),
                ("system", "The change in equipment has made the game faster and more physically demanding."),
            ],
            [
                ("learner", "Tennis is one of the few sports where Indian players have achieved international recognition."),
                ("system", "Players like Sania Mirza and Leander Paes have inspired a generation."),
                ("learner", "Their success has encouraged many families to enrol their children in tennis academies."),
                ("system", "Role models play a crucial role in popularising sports among young people."),
            ],
        ],
        "upper_intermediate": [
            [
                ("learner", "String tension in a tennis racket significantly affects the control and power a player can generate."),
                ("system", "Higher tension provides more control while lower tension offers more power."),
                ("learner", "Professional players are known to adjust their string tension based on court surface and weather conditions."),
                ("system", "Such fine-tuning reflects the level of detail that elite athletes consider in their preparation."),
            ],
            [
                ("learner", "The introduction of electronic line calling has been transforming how tennis matches are officiated."),
                ("system", "Automated systems have eliminated many of the controversial calls that once disrupted matches."),
                ("learner", "It was reported that player satisfaction with officiating has increased significantly since the technology was adopted."),
                ("system", "The accuracy of electronic systems far exceeds human line judges in detecting close calls."),
            ],
            [
                ("learner", "The physical demands of professional tennis have increased to the point where career longevity is a major concern."),
                ("system", "Modern players face gruelling schedules with tournaments spread across the globe year-round."),
                ("learner", "Sports scientists have argued that the current tour schedule was designed without adequate consideration for player welfare."),
                ("system", "Discussions about restructuring the tour calendar to reduce burnout are ongoing among governing bodies."),
            ],
        ],
        "advanced": [
            [
                ("learner", "The evolution of tennis racket technology raises a philosophical question about the extent to which equipment should be permitted to augment human performance."),
                ("system", "The International Tennis Federation has imposed size and material restrictions to maintain competitive balance."),
                ("learner", "Were these restrictions to be lifted, the resulting equipment arms race could fundamentally alter the character of the sport."),
                ("system", "The regulation of equipment is ultimately an exercise in defining what kind of game tennis ought to be."),
            ],
            [
                ("learner", "The globalisation of tennis, while expanding the talent pool, has exacerbated economic disparities within the sport."),
                ("system", "Players from wealthy nations benefit from superior coaching, facilities, and tournament access."),
                ("learner", "A more equitable distribution of development funding by the governing bodies would help level the competitive landscape."),
                ("system", "Structural reforms are needed to ensure that talent rather than economic circumstance determines success in the sport."),
            ],
            [
                ("learner", "I would contend that the aesthetic dimension of tennis, the elegance of a well-executed stroke, constitutes an underappreciated aspect of its enduring appeal."),
                ("system", "David Foster Wallace wrote compellingly about the beauty of tennis as a form of kinetic art."),
                ("learner", "The reduction of sport to mere statistical analysis, while useful, risks effacing the embodied artistry that makes athletic performance genuinely captivating."),
                ("system", "That tension between quantitative evaluation and qualitative appreciation is central to contemporary debates in sports aesthetics."),
            ],
        ],
    },
    # =========================================================================
    # BOTTLE
    # =========================================================================
    "bottle": {
        "beginner": [
            [
                ("learner", "I bring a water bottle to school."),
                ("system", "Drinking water during the day keeps you healthy."),
                ("learner", "My bottle is green and has a lid."),
                ("system", "A lid prevents spills inside your backpack."),
            ],
            [
                ("learner", "This bottle is made of plastic."),
                ("system", "Many bottles are plastic, but steel bottles are better for the environment."),
                ("learner", "My teacher says we should use steel bottles."),
                ("system", "Your teacher is right. Reusable bottles reduce plastic waste."),
            ],
            [
                ("learner", "I fill my bottle every morning before school."),
                ("system", "That is a healthy habit to have."),
                ("learner", "I drink water during every break time."),
                ("system", "Staying hydrated helps you focus better in class."),
            ],
        ],
        "elementary": [
            [
                ("learner", "I am looking for a bottle that keeps water cold for many hours."),
                ("system", "Insulated steel bottles can keep water cold all day."),
                ("learner", "My mother bought one last week and it keeps water cold for twelve hours."),
                ("system", "Vacuum-insulated bottles are great for hot Indian summers."),
            ],
            [
                ("learner", "Plastic bottles are polluting our rivers and oceans everywhere."),
                ("system", "Single-use plastic is one of the biggest environmental problems today."),
                ("learner", "Our school organised a campaign to collect and recycle plastic bottles."),
                ("system", "That is a wonderful initiative. Every small effort makes a difference."),
            ],
            [
                ("learner", "The shopkeeper arranged all the bottles neatly on the shelf."),
                ("system", "What kind of bottles were on display?"),
                ("learner", "There were glass bottles, plastic bottles, and copper bottles in different sizes."),
                ("system", "Copper bottles have become popular because some people believe they have health benefits."),
            ],
        ],
        "intermediate": [
            [
                ("learner", "I have started carrying a reusable bottle everywhere to reduce my plastic consumption."),
                ("system", "That is one of the simplest and most effective personal environmental choices."),
                ("learner", "If every student in India switched to reusable bottles, millions of plastic bottles would be saved annually."),
                ("system", "Collective small actions can create enormous environmental impact at a national scale."),
            ],
            [
                ("learner", "The design of water bottles has become surprisingly sophisticated in recent years."),
                ("system", "Features like built-in filters, infusers, and time markers are now common."),
                ("learner", "If somebody had told me five years ago that a bottle could remind me to drink water, I would have laughed."),
                ("system", "Smart bottles with hydration tracking are an example of technology solving everyday problems."),
            ],
            [
                ("learner", "Glass bottles are making a comeback as consumers become more aware of plastic-related health concerns."),
                ("system", "Studies have raised questions about chemicals leaching from plastic into beverages."),
                ("learner", "The inconvenience of glass being heavier and breakable is a trade-off that many are now willing to accept."),
                ("system", "Silicone sleeves and protective cases have made glass bottles much more practical for daily use."),
            ],
        ],
        "upper_intermediate": [
            [
                ("learner", "The bottled water industry has been criticised for commodifying a resource that should be freely accessible to all."),
                ("system", "Access to clean drinking water is recognised as a fundamental human right by the United Nations."),
                ("learner", "It has been argued that aggressive marketing by bottled water companies has eroded public trust in municipal tap water."),
                ("system", "In many developed countries, tap water actually undergoes more rigorous testing than bottled water."),
            ],
            [
                ("learner", "The lifecycle of a plastic bottle, from petroleum extraction to ocean pollution, illustrates the full scope of single-use waste."),
                ("system", "Most plastic bottles are used for just a few minutes but persist in the environment for centuries."),
                ("learner", "Extended producer responsibility legislation, which holds manufacturers accountable for disposal, has been implemented in several countries."),
                ("system", "Such policies shift the burden of waste management from consumers and municipalities to the companies creating the product."),
            ],
            [
                ("learner", "A start-up has developed edible water bottles made from seaweed as an alternative to plastic."),
                ("system", "Biodegradable packaging innovations are generating significant interest from investors and environmentalists."),
                ("learner", "The challenge, according to the founders, was scaling production while maintaining affordability and shelf life."),
                ("system", "Scalability and cost remain the primary barriers for most sustainable packaging alternatives."),
            ],
        ],
        "advanced": [
            [
                ("learner", "The plastic bottle encapsulates, perhaps more vividly than any other object, the contradictions of contemporary consumer capitalism."),
                ("system", "It embodies the tension between convenience and sustainability that defines modern consumption patterns."),
                ("learner", "One might argue that addressing the plastic crisis requires not merely technological substitution but a fundamental reorientation of our relationship with disposability."),
                ("system", "Deep ecologists would agree, contending that the problem is ontological rather than merely logistical."),
            ],
            [
                ("learner", "Were a comprehensive deposit-return scheme to be implemented across India, plastic bottle recycling rates could increase dramatically."),
                ("system", "Countries with deposit schemes consistently achieve recycling rates above ninety percent."),
                ("learner", "The political economy of waste management in India, however, is complicated by the informal recycling sector that already processes much of the plastic."),
                ("system", "Any formal scheme must integrate and protect the livelihoods of waste pickers who currently perform this essential function."),
            ],
            [
                ("learner", "The global trade in bottled water represents a striking paradox wherein water-scarce regions export water to wealthy markets while local populations lack adequate supply."),
                ("system", "This dynamic exemplifies how market mechanisms can exacerbate rather than alleviate resource inequality."),
                ("learner", "It is incumbent upon regulatory frameworks to ensure that the extraction of water for commercial bottling does not compromise local aquifer sustainability."),
                ("system", "Groundwater governance reform is urgently needed to prevent the privatisation of communal water resources."),
            ],
        ],
    },
}
