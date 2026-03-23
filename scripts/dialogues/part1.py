"""
Hand-crafted dialogues for the first 20 COCO objects.

Objects covered:
    person, bicycle, car, motorcycle, airplane, bus, train, truck, boat,
    traffic light, fire hydrant, stop sign, parking meter, bench, bird,
    cat, dog, horse, sheep, cow

Each object has 5 levels (beginner, elementary, intermediate,
upper_intermediate, advanced) with 3 dialogues per level.
Each dialogue is a list of 4 turns: learner, system, learner, system.
Total: 20 objects x 5 levels x 3 dialogues = 300 dialogues.
"""

DIALOGUES_PART1 = {
    # ──────────────────────────────────────────────
    # 1. PERSON
    # ──────────────────────────────────────────────
    "person": {
        "beginner": [
            [
                ("learner", "I see a tall person over there."),
                ("system", "Yes! Can you describe what they look like?"),
                ("learner", "The person is wearing a blue shirt."),
                ("system", "Good observation! Blue is a nice colour."),
            ],
            [
                ("learner", "That person is my neighbour."),
                ("system", "Oh, do you know their name?"),
                ("learner", "Yes, his name is Ravi."),
                ("system", "That is a nice name. How do you know him?"),
            ],
            [
                ("learner", "There is a person at the door."),
                ("system", "Who do you think it is?"),
                ("learner", "I think it is the postman."),
                ("system", "Let us go and check together."),
            ],
        ],
        "elementary": [
            [
                ("learner", "The person standing near the shop is waving at me."),
                ("system", "Do you recognise them from somewhere?"),
                ("learner", "I met that person at my cousin's wedding last month."),
                ("system", "That is interesting. Weddings are great for meeting people."),
            ],
            [
                ("learner", "A person was asking for directions this morning."),
                ("system", "Were you able to help them?"),
                ("learner", "I showed them the way to the bus stop nearby."),
                ("system", "That was very kind of you to help a stranger."),
            ],
            [
                ("learner", "The person next to me is reading a newspaper."),
                ("system", "That is becoming quite rare these days."),
                ("learner", "My grandfather was also a person who loved newspapers."),
                ("system", "Some people still enjoy holding a real paper."),
            ],
        ],
        "intermediate": [
            [
                ("learner", "I have never met a person who speaks six languages fluently."),
                ("system", "That is truly impressive. Which languages do they speak?"),
                ("learner", "If I could speak that many languages, I would travel the world."),
                ("system", "Learning languages certainly opens many doors for people."),
            ],
            [
                ("learner", "The person who interviewed me seemed very experienced."),
                ("system", "How did the interview go overall?"),
                ("learner", "I have prepared well, so I think it went smoothly."),
                ("system", "Confidence matters a lot when you meet new people."),
            ],
            [
                ("learner", "Every person in our team has a different skill set."),
                ("system", "That sounds like a well-balanced group."),
                ("learner", "We have worked together since the project started last year."),
                ("system", "Diverse teams often produce the best results."),
            ],
        ],
        "upper_intermediate": [
            [
                ("learner", "The person who was recommended by my professor has been hired."),
                ("system", "It sounds like the recommendation carried a lot of weight."),
                ("learner", "It was reported that several candidates were considered for the role."),
                ("system", "Having a strong reference can make all the difference."),
            ],
            [
                ("learner", "A person whose opinions I deeply respect disagreed with my proposal."),
                ("system", "How did you handle that disagreement?"),
                ("learner", "I was told that my argument needed stronger supporting evidence."),
                ("system", "Constructive criticism from someone you respect is invaluable."),
            ],
            [
                ("learner", "The person believed to have discovered the ruins was actually a farmer."),
                ("system", "That is a fascinating story. How was it discovered?"),
                ("learner", "It is said that he stumbled upon the ancient stones while ploughing."),
                ("system", "Remarkable discoveries are sometimes made by ordinary people."),
            ],
        ],
        "advanced": [
            [
                ("learner", "Were it not for that one person's tenacity, the entire initiative would have collapsed."),
                ("system", "Individual determination can sustain collective endeavours remarkably well."),
                ("learner", "It is imperative that we recognise such contributions before they fade from institutional memory."),
                ("system", "Indeed, acknowledging unsung contributors fosters a more equitable organisational culture."),
            ],
            [
                ("learner", "The notion that any single person can remain wholly objective is fundamentally flawed."),
                ("system", "Are you suggesting that subjectivity is inherent in all human judgement?"),
                ("learner", "I would argue that even the most disciplined person harbours unconscious biases."),
                ("system", "That perspective aligns with contemporary research in cognitive psychology."),
            ],
            [
                ("learner", "Should a person be held accountable for decisions made under extreme duress?"),
                ("system", "That is a profound ethical question with no straightforward answer."),
                ("learner", "Philosophers have long debated whether moral culpability diminishes under coercion."),
                ("system", "The interplay between free will and circumstance remains one of the deepest questions in ethics."),
            ],
        ],
    },

    # ──────────────────────────────────────────────
    # 2. BICYCLE
    # ──────────────────────────────────────────────
    "bicycle": {
        "beginner": [
            [
                ("learner", "I ride my bicycle to school."),
                ("system", "That is a healthy way to travel!"),
                ("learner", "My bicycle is red and black."),
                ("system", "Those are very nice colours for a bicycle."),
            ],
            [
                ("learner", "The bicycle has a flat tyre."),
                ("system", "Oh no. Do you know how to fix it?"),
                ("learner", "My father can fix the tyre."),
                ("system", "That is good. He can teach you too."),
            ],
            [
                ("learner", "I want a new bicycle for my birthday."),
                ("system", "What kind of bicycle do you want?"),
                ("learner", "I want a bicycle with gears."),
                ("system", "A geared bicycle is great for hills."),
            ],
        ],
        "elementary": [
            [
                ("learner", "I was riding my bicycle when it started raining."),
                ("system", "Did you get very wet?"),
                ("learner", "I stopped under a tree and waited for the rain."),
                ("system", "That was a smart thing to do for safety."),
            ],
            [
                ("learner", "My sister is learning to ride a bicycle this week."),
                ("system", "Is someone helping her balance?"),
                ("learner", "I held the seat while she practised in the park."),
                ("system", "She will learn quickly with your help."),
            ],
            [
                ("learner", "Many people are cycling on the new bicycle lane downtown."),
                ("system", "The city built that lane last month, right?"),
                ("learner", "Yes, it made cycling much safer for everyone."),
                ("system", "Dedicated lanes encourage more people to cycle."),
            ],
        ],
        "intermediate": [
            [
                ("learner", "I have been cycling to work every day for the past three months."),
                ("system", "Have you noticed any health benefits so far?"),
                ("learner", "If the weather stays dry, I will continue cycling through summer."),
                ("system", "Regular cycling can significantly improve cardiovascular fitness."),
            ],
            [
                ("learner", "My old bicycle has served me well, but the brakes need replacing."),
                ("system", "Brake maintenance is really important for safety."),
                ("learner", "I would have replaced them earlier if the parts had been available."),
                ("system", "Sometimes finding the right spare parts can be a challenge."),
            ],
            [
                ("learner", "The city has introduced a bicycle sharing programme near the metro stations."),
                ("system", "That sounds like a great last-mile connectivity solution."),
                ("learner", "Commuters have responded well since the programme launched in January."),
                ("system", "Combining cycling with public transport reduces congestion effectively."),
            ],
        ],
        "upper_intermediate": [
            [
                ("learner", "The bicycle that was stolen from the campus has been recovered by the police."),
                ("system", "That must be a relief for the owner."),
                ("learner", "It was reported that a series of thefts had been occurring in the area."),
                ("system", "Universities should consider installing more secure bicycle parking facilities."),
            ],
            [
                ("learner", "A bicycle designed specifically for rough terrain was showcased at the expo."),
                ("system", "Mountain biking has been gaining popularity in India lately."),
                ("learner", "The engineer said that the frame had been reinforced with carbon fibre."),
                ("system", "Advanced materials have transformed the cycling industry dramatically."),
            ],
            [
                ("learner", "It is believed that cycling infrastructure could reduce urban pollution significantly."),
                ("system", "Several European cities have proven that model already."),
                ("learner", "Experts suggest that Indian cities should be redesigned to prioritise non-motorised transport."),
                ("system", "The challenge lies in balancing rapid urbanisation with sustainable planning."),
            ],
        ],
        "advanced": [
            [
                ("learner", "Had the municipality invested in cycling infrastructure a decade ago, congestion would be far less severe today."),
                ("system", "Hindsight often reveals missed opportunities in urban planning."),
                ("learner", "It is essential that policymakers treat the bicycle not as a relic but as a cornerstone of sustainable mobility."),
                ("system", "Reframing the bicycle as modern infrastructure rather than a symbol of poverty is long overdue."),
            ],
            [
                ("learner", "The proposition that a bicycle can rival motorised vehicles in urban efficiency is well supported by empirical data."),
                ("system", "Particularly for distances under five kilometres, the data is compelling."),
                ("learner", "One might argue that the psychological barrier to cycling outweighs the practical obstacles in many Indian cities."),
                ("system", "Changing cultural perceptions of cycling requires deliberate policy interventions and public campaigns."),
            ],
            [
                ("learner", "Were the government to subsidise electric bicycles, adoption rates among commuters would surge dramatically."),
                ("system", "Electric bicycles bridge the gap between effort and distance effectively."),
                ("learner", "Nevertheless, without adequate charging infrastructure, even subsidised e-bikes risk becoming underutilised assets."),
                ("system", "A holistic approach addressing both incentives and infrastructure is indispensable for long-term success."),
            ],
        ],
    },

    # ──────────────────────────────────────────────
    # 3. CAR
    # ──────────────────────────────────────────────
    "car": {
        "beginner": [
            [
                ("learner", "My uncle has a white car."),
                ("system", "White is the most popular car colour here."),
                ("learner", "He drives his car to work every day."),
                ("system", "Does he drive far to reach his office?"),
            ],
            [
                ("learner", "There are many cars on the road."),
                ("system", "Yes, traffic is heavy during rush hour."),
                ("learner", "I like sitting in the front seat."),
                ("system", "The front seat gives a better view of the road."),
            ],
            [
                ("learner", "That car is moving very fast."),
                ("system", "Speeding is quite dangerous on busy roads."),
                ("learner", "We should always wear a seat belt."),
                ("system", "You are absolutely right about that."),
            ],
        ],
        "elementary": [
            [
                ("learner", "My mother was washing the car when I came home."),
                ("system", "Does she wash it often?"),
                ("learner", "She washes it every Saturday morning without fail."),
                ("system", "Keeping a car clean helps it last longer too."),
            ],
            [
                ("learner", "We are going to Chennai by car this weekend."),
                ("system", "That is a long drive. How many hours will it take?"),
                ("learner", "It usually takes about five hours from our town."),
                ("system", "Make sure to take breaks along the highway."),
            ],
            [
                ("learner", "The car broke down in the middle of the road yesterday."),
                ("system", "That must have been very stressful for you."),
                ("learner", "A mechanic came and fixed the engine within an hour."),
                ("system", "It is good to have a reliable mechanic nearby."),
            ],
        ],
        "intermediate": [
            [
                ("learner", "I have been saving money to buy a car for over two years now."),
                ("system", "Are you looking at any particular brand or model?"),
                ("learner", "If the prices drop during the festival season, I will buy one then."),
                ("system", "Dealers often offer the best discounts around Diwali and Pongal."),
            ],
            [
                ("learner", "Electric cars have become increasingly popular in Indian cities recently."),
                ("system", "The lower running costs are attracting many first-time buyers."),
                ("learner", "However, the lack of charging stations has slowed adoption in smaller towns."),
                ("system", "Infrastructure development needs to keep pace with vehicle technology."),
            ],
            [
                ("learner", "If I had known about the traffic jam, I would have taken the bypass road."),
                ("system", "Navigation apps can help you avoid congested routes in real time."),
                ("learner", "I have started using one, and it has saved me a lot of time already."),
                ("system", "Technology has truly changed how we plan our daily commutes."),
            ],
        ],
        "upper_intermediate": [
            [
                ("learner", "The car that was parked outside the hospital was towed away by the authorities."),
                ("system", "No-parking zones near hospitals are strictly enforced these days."),
                ("learner", "The owner was informed that a fine had been imposed along with towing charges."),
                ("system", "Such penalties are necessary to keep emergency access routes clear."),
            ],
            [
                ("learner", "It is widely acknowledged that car emissions contribute significantly to urban air pollution."),
                ("system", "Many cities are now introducing stricter emission standards for vehicles."),
                ("learner", "Analysts predict that combustion engine cars will be phased out within the next two decades."),
                ("system", "The transition will depend heavily on battery technology and energy grid capacity."),
            ],
            [
                ("learner", "A car designed with advanced safety features was awarded the highest crash test rating."),
                ("system", "Safety ratings have become a major factor in purchase decisions."),
                ("learner", "Consumers are reported to be willing to pay a premium for vehicles with better safety records."),
                ("system", "That shift in priorities reflects a growing awareness of road safety risks."),
            ],
        ],
        "advanced": [
            [
                ("learner", "Were autonomous cars to become mainstream, the entire insurance industry would need to be restructured."),
                ("system", "Liability frameworks would shift from individual drivers to manufacturers and software developers."),
                ("learner", "It is imperative that regulators anticipate these disruptions rather than react to them after the fact."),
                ("system", "Proactive regulation is essential, yet notoriously difficult in fast-evolving technological domains."),
            ],
            [
                ("learner", "The assertion that car ownership is a fundamental marker of middle-class identity warrants critical examination."),
                ("system", "In many Indian families, purchasing a car remains a deeply aspirational milestone."),
                ("learner", "One could argue that shared mobility platforms are gradually decoupling status from ownership."),
                ("system", "Cultural shifts in consumption patterns tend to lag behind technological availability by a generation."),
            ],
            [
                ("learner", "Had stricter fuel efficiency norms been enforced two decades ago, our cities would not be grappling with this level of pollution."),
                ("system", "Delayed regulation often compounds environmental and public health costs exponentially."),
                ("learner", "It remains to be seen whether the current push toward electrification will be sufficient to reverse the damage already done."),
                ("system", "Electrification alone is necessary but insufficient without parallel investments in clean energy generation."),
            ],
        ],
    },

    # ──────────────────────────────────────────────
    # 4. MOTORCYCLE
    # ──────────────────────────────────────────────
    "motorcycle": {
        "beginner": [
            [
                ("learner", "My brother rides a motorcycle to college."),
                ("system", "Does he wear a helmet every time?"),
                ("learner", "Yes, he always wears his helmet."),
                ("system", "That is very responsible of him."),
            ],
            [
                ("learner", "The motorcycle makes a loud noise."),
                ("system", "Some motorcycles are louder than others."),
                ("learner", "I cover my ears when it starts."),
                ("system", "Loud engines can indeed be quite startling."),
            ],
            [
                ("learner", "I see a black motorcycle parked outside."),
                ("system", "Do you know whose motorcycle it is?"),
                ("learner", "It belongs to my neighbour's son."),
                ("system", "Black is a very popular colour for motorcycles."),
            ],
        ],
        "elementary": [
            [
                ("learner", "My father bought a new motorcycle last week."),
                ("system", "That is exciting! What model did he choose?"),
                ("learner", "He was looking at many options before he decided."),
                ("system", "Choosing a motorcycle takes a lot of research."),
            ],
            [
                ("learner", "Two people were riding a motorcycle without helmets."),
                ("system", "That is very dangerous and also against the law."),
                ("learner", "The police stopped them at the traffic signal."),
                ("system", "Helmet rules exist to protect riders from serious injuries."),
            ],
            [
                ("learner", "The motorcycle is using less fuel than our old car."),
                ("system", "Motorcycles are generally more fuel-efficient for daily commuting."),
                ("learner", "My father is saving a lot of money on petrol now."),
                ("system", "That is one of the main advantages of two-wheelers."),
            ],
        ],
        "intermediate": [
            [
                ("learner", "I have always wanted to go on a long motorcycle trip across the Western Ghats."),
                ("system", "That route is famous among touring enthusiasts in India."),
                ("learner", "If I manage to get leave next month, I will plan the journey."),
                ("system", "Make sure your motorcycle is serviced thoroughly before a long ride."),
            ],
            [
                ("learner", "The motorcycle industry in India has grown rapidly over the past decade."),
                ("system", "India is one of the largest two-wheeler markets in the world now."),
                ("learner", "Affordable models have made personal transport accessible to millions of families."),
                ("system", "Mobility and economic empowerment are closely connected in developing nations."),
            ],
            [
                ("learner", "If the road had been repaired earlier, the motorcycle accident could have been avoided."),
                ("system", "Poor road conditions are a leading cause of two-wheeler accidents."),
                ("learner", "Riders have complained about those potholes for several months already."),
                ("system", "Timely maintenance of roads is crucial for rider safety."),
            ],
        ],
        "upper_intermediate": [
            [
                ("learner", "The motorcycle that was involved in the collision was found to have defective brakes."),
                ("system", "That raises serious questions about the manufacturer's quality control."),
                ("learner", "It was revealed that several complaints had been filed about the same model."),
                ("system", "Regulatory bodies should mandate recalls when patterns of defects emerge."),
            ],
            [
                ("learner", "Electric motorcycles are being marketed as the future of urban commuting in India."),
                ("system", "The lower maintenance costs make them attractive to daily riders."),
                ("learner", "However, concerns about battery range and charging time have not been fully addressed."),
                ("system", "Consumer confidence will grow as the technology matures and infrastructure expands."),
            ],
            [
                ("learner", "A documentary exploring motorcycle culture across rural India was screened at the film festival."),
                ("system", "Motorcycles play a unique cultural role in many Indian villages."),
                ("learner", "The filmmaker was quoted as saying that the motorcycle represents freedom for young rural men."),
                ("system", "That symbolism resonates deeply in communities where mobility was historically limited."),
            ],
        ],
        "advanced": [
            [
                ("learner", "Were manufacturers to prioritise safety engineering over aesthetic appeal, fatality rates among riders would decline substantially."),
                ("system", "The tension between marketability and safety is a persistent challenge in the industry."),
                ("learner", "It is incumbent upon regulators to mandate crash-resistant designs rather than rely on voluntary compliance."),
                ("system", "History has shown that the industry rarely self-regulates when profitability is at stake."),
            ],
            [
                ("learner", "The romanticisation of motorcycle culture often obscures the sobering reality of road accident statistics."),
                ("system", "India accounts for a disproportionately high share of global two-wheeler fatalities."),
                ("learner", "One must question whether the cultural narrative around motorcycles inadvertently normalises reckless riding behaviour."),
                ("system", "Disentangling cultural identity from risky behaviour requires nuanced public health communication."),
            ],
            [
                ("learner", "Had comprehensive rider training been integrated into the licensing process, countless accidents would have been prevented."),
                ("system", "The current licensing system in many states is widely regarded as inadequate."),
                ("learner", "It is essential that we overhaul the system to include mandatory practical training and road awareness modules."),
                ("system", "Licensing reform, coupled with strict enforcement, remains the most effective lever for improving road safety."),
            ],
        ],
    },

    # ──────────────────────────────────────────────
    # 5. AIRPLANE
    # ──────────────────────────────────────────────
    "airplane": {
        "beginner": [
            [
                ("learner", "I can see an airplane in the sky."),
                ("system", "It looks very small from down here!"),
                ("learner", "The airplane is flying very high."),
                ("system", "Airplanes fly about ten kilometres above the ground."),
            ],
            [
                ("learner", "I want to fly in an airplane someday."),
                ("system", "Where would you like to go?"),
                ("learner", "I want to visit my aunt in Delhi."),
                ("system", "Flying to Delhi takes about two hours from Chennai."),
            ],
            [
                ("learner", "The airplane has two big wings."),
                ("system", "Those wings help it stay up in the air."),
                ("learner", "It also has a long white tail."),
                ("system", "The tail helps the airplane steer and stay balanced."),
            ],
        ],
        "elementary": [
            [
                ("learner", "We are taking an airplane to Mumbai next Friday."),
                ("system", "Have you booked your tickets already?"),
                ("learner", "My mother booked them online last night."),
                ("system", "Online booking is so much easier than going to the office."),
            ],
            [
                ("learner", "The airplane landed safely despite the heavy rain."),
                ("system", "Pilots are highly trained to handle bad weather."),
                ("learner", "I was watching it from the airport window nervously."),
                ("system", "Modern airplanes have advanced systems to help with landings."),
            ],
            [
                ("learner", "My cousin is studying to become an airplane pilot."),
                ("system", "That is a very exciting career choice!"),
                ("learner", "She started her training at an aviation school in Bengaluru."),
                ("system", "India needs many more trained pilots for its growing airlines."),
            ],
        ],
        "intermediate": [
            [
                ("learner", "I have flown on an airplane only twice in my entire life."),
                ("system", "Do you remember your first flight experience?"),
                ("learner", "If the tickets had been cheaper, I would have flown more often."),
                ("system", "Budget airlines have made flying more affordable in recent years."),
            ],
            [
                ("learner", "The airplane was delayed by three hours because of fog at the airport."),
                ("system", "Winter fog causes major disruptions at north Indian airports."),
                ("learner", "Passengers have been complaining about the lack of timely updates from the airline."),
                ("system", "Better communication during delays would significantly improve the passenger experience."),
            ],
            [
                ("learner", "If I had chosen a window seat, I could have seen the mountains during the flight."),
                ("system", "The Himalayan views from an airplane are truly breathtaking."),
                ("learner", "Next time, I will book my seat well in advance to get a window."),
                ("system", "Many airlines now let you pick your seat at the time of booking."),
            ],
        ],
        "upper_intermediate": [
            [
                ("learner", "The airplane that was grounded due to engine trouble has been cleared for service."),
                ("system", "Aircraft maintenance protocols are extremely rigorous for good reason."),
                ("learner", "It was announced that the technical fault had been identified and fully rectified."),
                ("system", "Transparency in reporting such incidents builds public trust in airline safety."),
            ],
            [
                ("learner", "India's domestic airplane fleet is expected to double within the next eight years."),
                ("system", "The expansion reflects rising demand from smaller cities and towns."),
                ("learner", "Industry analysts suggest that regional connectivity has been the primary driver of growth."),
                ("system", "Government schemes linking tier-two cities by air have played a significant role."),
            ],
            [
                ("learner", "An airplane designed to run on sustainable aviation fuel completed its maiden test flight."),
                ("system", "Sustainable fuels could dramatically reduce aviation's carbon footprint."),
                ("learner", "Researchers believe that blended fuels will be commercially viable within this decade."),
                ("system", "The transition will require massive investment in production and supply chains."),
            ],
        ],
        "advanced": [
            [
                ("learner", "Were the aviation industry to achieve carbon neutrality, it would necessitate a fundamental rethinking of propulsion technology."),
                ("system", "Electric and hydrogen-powered aircraft are still decades away from commercial viability at scale."),
                ("learner", "It is therefore incumbent upon the industry to pursue interim solutions such as carbon offsetting and fuel blending."),
                ("system", "Pragmatic incrementalism may prove more effective than waiting for a single transformative breakthrough."),
            ],
            [
                ("learner", "The democratisation of air travel, while economically beneficial, has exacerbated the sector's environmental impact considerably."),
                ("system", "Balancing accessibility with sustainability is perhaps the defining challenge for modern aviation."),
                ("learner", "One might contend that imposing a progressive carbon levy on frequent flyers would be both equitable and effective."),
                ("system", "Such a policy would face fierce opposition from industry lobbies but could shift behaviour meaningfully."),
            ],
            [
                ("learner", "Had international regulations been harmonised decades ago, the fragmented nature of airspace management would not persist."),
                ("system", "Sovereignty concerns have always complicated the standardisation of global aviation rules."),
                ("learner", "Nonetheless, the increasing frequency of cross-border flights demands a more cohesive regulatory framework."),
                ("system", "Multilateral cooperation in aviation governance is essential yet perpetually constrained by national interests."),
            ],
        ],
    },

    # ──────────────────────────────────────────────
    # 6. BUS
    # ──────────────────────────────────────────────
    "bus": {
        "beginner": [
            [
                ("learner", "I take the bus to school every morning."),
                ("system", "What time does your bus arrive?"),
                ("learner", "The bus comes at eight o'clock sharp."),
                ("system", "It is good that you are always on time."),
            ],
            [
                ("learner", "The bus is very crowded today."),
                ("system", "Rush hour buses are always packed."),
                ("learner", "I cannot find a seat to sit."),
                ("system", "Maybe the next bus will have more space."),
            ],
            [
                ("learner", "That big red bus goes to the market."),
                ("system", "Do you take it often for shopping?"),
                ("learner", "Yes, my mother and I take it together."),
                ("system", "The market bus is very convenient for families."),
            ],
        ],
        "elementary": [
            [
                ("learner", "I was waiting for the bus when it started to rain heavily."),
                ("system", "Was there a shelter at the bus stop?"),
                ("learner", "Luckily, a small shop nearby let me stand under their roof."),
                ("system", "That was very kind of the shopkeeper to help."),
            ],
            [
                ("learner", "The government is adding new buses to the city fleet this year."),
                ("system", "Are they replacing the older ones?"),
                ("learner", "Yes, the old buses were breaking down very often."),
                ("system", "New buses will make daily travel more reliable for passengers."),
            ],
            [
                ("learner", "My younger brother loves watching the buses go past our house."),
                ("system", "Children are often fascinated by large vehicles."),
                ("learner", "He knows the route numbers of all the buses on our street."),
                ("system", "That is an impressive memory for a young child!"),
            ],
        ],
        "intermediate": [
            [
                ("learner", "I have been using the city bus service for five years without any major complaints."),
                ("system", "That speaks well of the public transport system in your city."),
                ("learner", "If the frequency were increased during peak hours, it would be even better."),
                ("system", "Higher frequency would definitely reduce overcrowding on popular routes."),
            ],
            [
                ("learner", "The bus broke down halfway through the journey and we had to wait for a replacement."),
                ("system", "How long did you have to wait on the roadside?"),
                ("learner", "If the maintenance had been done properly, the breakdown could have been prevented."),
                ("system", "Regular servicing is essential to keep public buses running safely."),
            ],
            [
                ("learner", "Air-conditioned buses have been introduced on the airport route since last month."),
                ("system", "That must be a welcome change for passengers carrying luggage."),
                ("learner", "The fare is slightly higher, but the comfort has attracted many new riders."),
                ("system", "People are often willing to pay more for a pleasant travel experience."),
            ],
        ],
        "upper_intermediate": [
            [
                ("learner", "The bus service that was suspended during the monsoon has been restored with additional safety checks."),
                ("system", "Flooded roads make bus operations extremely hazardous."),
                ("learner", "It was reported that several routes had been rerouted to avoid waterlogged areas."),
                ("system", "Adaptive routing during the monsoon is critical for maintaining public transport continuity."),
            ],
            [
                ("learner", "An electric bus pilot programme is being rolled out across three major Indian cities."),
                ("system", "The shift to electric buses could transform urban public transport entirely."),
                ("learner", "Transport officials believe that the programme will be expanded if initial results are encouraging."),
                ("system", "Early success stories will be crucial for securing further government investment."),
            ],
            [
                ("learner", "Commuters whose daily route passes through the construction zone have been advised to expect delays."),
                ("system", "Construction along bus corridors always causes significant disruptions."),
                ("learner", "Temporary bus stops are being set up, but passengers have complained about the lack of signage."),
                ("system", "Clear communication during disruptions is just as important as the infrastructure work itself."),
            ],
        ],
        "advanced": [
            [
                ("learner", "Were the city to invest in a dedicated bus rapid transit system, commute times could be halved for millions of residents."),
                ("system", "Bus rapid transit has proven transformative in cities like Ahmedabad and Bogota."),
                ("learner", "The reluctance to allocate road space exclusively to buses reflects a deeper bias toward private vehicle ownership."),
                ("system", "Challenging that bias requires political will and a compelling narrative around shared mobility."),
            ],
            [
                ("learner", "The argument that privatising bus services improves efficiency overlooks the equity dimension of public transport."),
                ("system", "Private operators may optimise for profit, potentially abandoning unprofitable but socially essential routes."),
                ("learner", "It is precisely those marginalised communities that depend most heavily on subsidised bus access for their livelihoods."),
                ("system", "Any reform must therefore safeguard accessibility as a non-negotiable principle alongside efficiency gains."),
            ],
            [
                ("learner", "Had comprehensive data analytics been applied to route planning earlier, the chronic inefficiency of the bus network could have been mitigated."),
                ("system", "Data-driven optimisation of routes and schedules offers enormous untapped potential."),
                ("learner", "Nevertheless, algorithmic approaches must be tempered by ground-level understanding of community needs and travel patterns."),
                ("system", "The most effective transit planning synthesises quantitative data with qualitative insights from actual riders."),
            ],
        ],
    },

    # ──────────────────────────────────────────────
    # 7. TRAIN
    # ──────────────────────────────────────────────
    "train": {
        "beginner": [
            [
                ("learner", "I love watching trains at the station."),
                ("system", "Trains are fun to watch, especially the fast ones!"),
                ("learner", "The train is very long and blue."),
                ("system", "Some trains have more than twenty coaches."),
            ],
            [
                ("learner", "We are going by train to my village."),
                ("system", "How long is the train journey?"),
                ("learner", "The train ride takes about six hours."),
                ("system", "That is a nice way to see the countryside."),
            ],
            [
                ("learner", "The train horn is very loud."),
                ("system", "Yes, they sound the horn at every crossing."),
                ("learner", "I can hear it from my house."),
                ("system", "Living near the railway must be quite noisy."),
            ],
        ],
        "elementary": [
            [
                ("learner", "Our train arrived late because of a signal failure."),
                ("system", "Signal problems cause many delays in the Indian railways."),
                ("learner", "We were sitting on the platform for two extra hours."),
                ("system", "I hope you had something to eat while waiting."),
            ],
            [
                ("learner", "My grandmother is travelling by train from Madurai tomorrow."),
                ("system", "Did she get a confirmed reservation?"),
                ("learner", "Yes, my father booked a sleeper berth for her last week."),
                ("system", "She will be comfortable on the overnight journey."),
            ],
            [
                ("learner", "The new metro train is running between the airport and the city centre."),
                ("system", "That must make airport transfers much easier."),
                ("learner", "It is faster and cheaper than taking an auto-rickshaw."),
                ("system", "Metro trains are changing how people move around in big cities."),
            ],
        ],
        "intermediate": [
            [
                ("learner", "I have taken the Chennai-Mumbai express several times for work."),
                ("system", "That is one of the longest routes on the Indian railway network."),
                ("learner", "If they introduced a high-speed train on that route, it would save an entire day of travel."),
                ("system", "High-speed rail projects are under discussion for several key corridors."),
            ],
            [
                ("learner", "The train journey gave me an opportunity to read and relax without any distractions."),
                ("system", "Long train rides can be quite peaceful compared to flights."),
                ("learner", "I have finished three books during train journeys this year alone."),
                ("system", "Trains offer a rare chance to slow down in our busy lives."),
            ],
            [
                ("learner", "If the train had departed on time, we would have reached before sunset."),
                ("system", "Delays can really disrupt well-planned schedules."),
                ("learner", "The railways have promised to improve punctuality on this route."),
                ("system", "Consistent punctuality is the backbone of a reliable rail system."),
            ],
        ],
        "upper_intermediate": [
            [
                ("learner", "The heritage train service that was discontinued in 2018 has been revived as a tourist attraction."),
                ("system", "Heritage railways have become increasingly popular with both domestic and international visitors."),
                ("learner", "Local communities have reported that tourism-related income has increased since the revival."),
                ("system", "Preserving railway heritage can generate economic benefits for surrounding regions."),
            ],
            [
                ("learner", "A semi-high-speed train designed and built entirely in India was unveiled by the railway minister."),
                ("system", "Indigenous manufacturing capabilities in rail technology have advanced considerably."),
                ("learner", "Engineers claim that the train is equipped with an advanced collision avoidance system."),
                ("system", "Safety innovations are essential as train speeds and passenger numbers increase."),
            ],
            [
                ("learner", "Passengers who were stranded overnight due to the derailment were provided shelter by local villagers."),
                ("system", "Such acts of community solidarity are remarkable in times of crisis."),
                ("learner", "It was later confirmed that the derailment had been caused by a fractured rail section."),
                ("system", "Regular track inspection and maintenance are non-negotiable for railway safety."),
            ],
        ],
        "advanced": [
            [
                ("learner", "Were India to complete its proposed high-speed rail network, the economic geography of the subcontinent would be fundamentally reshaped."),
                ("system", "Reduced travel times between major cities would catalyse new patterns of investment and migration."),
                ("learner", "However, the astronomical cost and land acquisition challenges call into question whether the project is fiscally prudent."),
                ("system", "The tension between transformative infrastructure and fiscal responsibility is a perennial dilemma for developing economies."),
            ],
            [
                ("learner", "The romanticisation of train travel in Indian cinema belies the systemic inadequacies of the actual railway experience."),
                ("system", "There is certainly a gap between the nostalgic image and the daily reality for millions of commuters."),
                ("learner", "One must acknowledge that the Indian railways, despite its flaws, remains the lifeline of the nation's working class."),
                ("system", "Any modernisation effort must therefore centre the needs of ordinary passengers rather than privileged travellers."),
            ],
            [
                ("learner", "Had the railways embraced digital ticketing and demand-based pricing a decade earlier, revenue leakages would have been significantly curtailed."),
                ("system", "Legacy systems and institutional inertia have historically slowed technological adoption in public enterprises."),
                ("learner", "It is imperative that the next phase of reforms prioritise both operational efficiency and equitable access."),
                ("system", "Balancing commercial viability with the social mandate of public transport is the central challenge facing Indian railways."),
            ],
        ],
    },

    # ──────────────────────────────────────────────
    # 8. TRUCK
    # ──────────────────────────────────────────────
    "truck": {
        "beginner": [
            [
                ("learner", "A big truck is parked near our house."),
                ("system", "What colour is the truck?"),
                ("learner", "The truck is green with yellow letters."),
                ("system", "Trucks often have bright colours so they are easy to see."),
            ],
            [
                ("learner", "The truck carries vegetables to the market."),
                ("system", "That is how fresh food reaches shops every morning."),
                ("learner", "I can see tomatoes in the back."),
                ("system", "Those tomatoes will be on someone's plate soon."),
            ],
            [
                ("learner", "That truck is making a lot of noise."),
                ("system", "Big diesel engines are usually very loud."),
                ("learner", "It is moving very slowly up the hill."),
                ("system", "Heavy loads make trucks slow down on steep roads."),
            ],
        ],
        "elementary": [
            [
                ("learner", "A truck was blocking the entire road this morning."),
                ("system", "Was there an accident or a breakdown?"),
                ("learner", "The driver said the engine overheated because of the summer heat."),
                ("system", "Trucks need extra care during the hot months."),
            ],
            [
                ("learner", "My uncle drives a truck between Chennai and Hyderabad."),
                ("system", "That is a long haul. How many days does one trip take?"),
                ("learner", "He usually completes the round trip in three days."),
                ("system", "Long-distance truck drivers work incredibly hard."),
            ],
            [
                ("learner", "The delivery truck brought our new refrigerator yesterday."),
                ("system", "Did they carry it inside the house for you?"),
                ("learner", "Two workers helped bring it up the stairs carefully."),
                ("system", "Delivery services make buying large appliances much easier."),
            ],
        ],
        "intermediate": [
            [
                ("learner", "I have noticed that truck traffic increases dramatically at night on the national highway."),
                ("system", "Many cities restrict truck entry to nighttime hours to reduce congestion."),
                ("learner", "If better rest stops were available, drivers would be less fatigued during these shifts."),
                ("system", "Driver fatigue is one of the leading causes of highway accidents involving heavy vehicles."),
            ],
            [
                ("learner", "The government has introduced new emission standards for commercial trucks this year."),
                ("system", "Older trucks produce significantly more pollution than newer models."),
                ("learner", "Fleet operators have expressed concern about the cost of upgrading their vehicles."),
                ("system", "Transition periods and subsidies can help ease the financial burden on operators."),
            ],
            [
                ("learner", "If the bridge had been designed for heavier loads, the truck would not have been diverted."),
                ("system", "Weight limits on bridges are strictly enforced for structural safety."),
                ("learner", "Diversion routes add hours to the journey and increase transportation costs."),
                ("system", "Infrastructure capacity needs to match the demands of modern freight movement."),
            ],
        ],
        "upper_intermediate": [
            [
                ("learner", "The truck that overturned on the expressway was found to be carrying twice its permitted load."),
                ("system", "Overloading is a persistent and dangerous problem in the trucking industry."),
                ("learner", "It was revealed that the weigh station records had been falsified by a corrupt official."),
                ("system", "Corruption in enforcement undermines safety regulations that are designed to protect everyone."),
            ],
            [
                ("learner", "Automated trucks are being tested on closed highway circuits by several technology companies."),
                ("system", "Autonomous trucking could revolutionise the logistics industry within a decade."),
                ("learner", "However, unions have warned that millions of truck drivers could face displacement."),
                ("system", "The social impact of automation in transport demands careful planning and retraining programmes."),
            ],
            [
                ("learner", "A refrigerated truck used for vaccine distribution broke down in a remote district last week."),
                ("system", "Cold chain failures can compromise the efficacy of temperature-sensitive medicines."),
                ("learner", "Health officials confirmed that the vaccines were transferred to a backup vehicle within the safe time window."),
                ("system", "Redundancy planning in cold chain logistics is absolutely critical for public health delivery."),
            ],
        ],
        "advanced": [
            [
                ("learner", "Were the freight sector to fully electrify, the logistical challenge of battery weight versus payload capacity would need to be resolved."),
                ("system", "Current battery energy density is insufficient for long-haul heavy trucking applications."),
                ("learner", "Hydrogen fuel cells may ultimately prove more viable for heavy-duty freight than battery electric systems."),
                ("system", "The technological trajectory will depend on infrastructure investments and the relative economics of each energy source."),
            ],
            [
                ("learner", "The exploitation of truck drivers through exploitative payment structures and gruelling schedules constitutes a systemic labour rights issue."),
                ("system", "Many drivers work without formal contracts, social security, or regulated working hours."),
                ("learner", "It is unconscionable that an industry so vital to the economy treats its workforce with such disregard."),
                ("system", "Meaningful reform requires legislative action, unionisation, and consumer awareness of supply chain ethics."),
            ],
            [
                ("learner", "Had logistics companies adopted route optimisation technology earlier, both fuel consumption and delivery times would have improved markedly."),
                ("system", "The Indian trucking sector has historically been slow to embrace digital transformation."),
                ("learner", "Nevertheless, the rapid adoption of GPS tracking and fleet management platforms suggests that the tide is finally turning."),
                ("system", "Technology adoption accelerates once early adopters demonstrate tangible cost savings to the broader industry."),
            ],
        ],
    },

    # ──────────────────────────────────────────────
    # 9. BOAT
    # ──────────────────────────────────────────────
    "boat": {
        "beginner": [
            [
                ("learner", "I can see a boat on the river."),
                ("system", "Is it a big boat or a small one?"),
                ("learner", "It is a small fishing boat."),
                ("system", "Fishermen use small boats to catch fish every day."),
            ],
            [
                ("learner", "The boat is painted bright blue."),
                ("system", "Blue boats look beautiful on the water."),
                ("learner", "There are two men inside the boat."),
                ("system", "They are probably going out to fish."),
            ],
            [
                ("learner", "I want to ride in a boat someday."),
                ("system", "Have you been near the sea before?"),
                ("learner", "Yes, I went to the beach last summer."),
                ("system", "Maybe next time you can take a short boat ride."),
            ],
        ],
        "elementary": [
            [
                ("learner", "We took a boat ride on the lake during our school trip."),
                ("system", "That sounds like a wonderful experience!"),
                ("learner", "The boatman was rowing very smoothly through the calm water."),
                ("system", "Rowing takes a lot of skill and strength."),
            ],
            [
                ("learner", "The fishing boats are returning to the harbour with their catch."),
                ("system", "The fishermen must have been out since early morning."),
                ("learner", "My grandfather was a fisherman who owned his own boat."),
                ("system", "Fishing communities have a deep connection with the sea."),
            ],
            [
                ("learner", "A boat was stuck on the rocks near the shore yesterday."),
                ("system", "Was everyone on board safe?"),
                ("learner", "Yes, the coast guard helped all the passengers reach the shore."),
                ("system", "The coast guard does vital work protecting people at sea."),
            ],
        ],
        "intermediate": [
            [
                ("learner", "I have always been fascinated by the traditional boats used by fishermen in Kerala."),
                ("system", "The snake boats of Kerala are famous for their distinctive shape."),
                ("learner", "If I visit Alleppey this winter, I will take a houseboat cruise through the backwaters."),
                ("system", "The Kerala backwaters offer one of the most serene travel experiences in India."),
            ],
            [
                ("learner", "The ferry boat service has been disrupted due to strong winds and rough seas."),
                ("system", "Safety must always come first when weather conditions deteriorate."),
                ("learner", "Commuters who depend on the boat service have been stranded on the island."),
                ("system", "Alternative transport arrangements should be made during such disruptions."),
            ],
            [
                ("learner", "If the boat had been properly inspected before departure, the engine failure could have been avoided."),
                ("system", "Mechanical failures at sea can be extremely dangerous."),
                ("learner", "Marine safety regulations have been tightened following several recent incidents."),
                ("system", "Stricter enforcement of safety standards is essential for passenger confidence."),
            ],
        ],
        "upper_intermediate": [
            [
                ("learner", "The boat that was seized by the navy was allegedly being used for smuggling operations."),
                ("system", "Maritime security agencies patrol coastal waters to prevent illegal activities."),
                ("learner", "It was reported that the crew had been operating without valid permits or documentation."),
                ("system", "Undocumented vessels pose serious security risks to coastal nations."),
            ],
            [
                ("learner", "Traditional boat-building techniques passed down through generations are at risk of being lost."),
                ("system", "Many artisan trades face similar threats from modernisation and changing economies."),
                ("learner", "Craftsmen have appealed for institutional support to preserve their heritage skills."),
                ("system", "Documentation and apprenticeship programmes could help sustain these invaluable traditions."),
            ],
            [
                ("learner", "Solar-powered boats are being trialled for passenger transport on urban waterways in Kochi."),
                ("system", "Clean energy solutions for water transport are gaining attention worldwide."),
                ("learner", "Officials believe that the initiative could reduce both emissions and operating costs significantly."),
                ("system", "Successful pilots could serve as models for other coastal and riverine cities."),
            ],
        ],
        "advanced": [
            [
                ("learner", "Were coastal communities to lose access to traditional fishing grounds, the socioeconomic consequences would be devastating."),
                ("system", "Industrial trawling and coastal development have already displaced many small-scale fishing communities."),
                ("learner", "It is imperative that maritime policy balance commercial interests with the livelihoods of artisanal fishermen."),
                ("system", "The right to livelihood for fishing communities must be enshrined in coastal zone management frameworks."),
            ],
            [
                ("learner", "The narrative of the boat as a symbol of perilous migration underscores the desperation driving people across dangerous waters."),
                ("system", "Maritime migration crises reveal the profound failures of international refugee protection systems."),
                ("learner", "One cannot discuss boat crossings without confronting the structural inequalities that compel people to risk their lives."),
                ("system", "Addressing root causes rather than merely patrolling borders is essential for any humane and sustainable solution."),
            ],
            [
                ("learner", "Had the port authority invested in dredging and modernisation a decade ago, the harbour would accommodate larger vessels today."),
                ("system", "Port infrastructure directly determines a region's competitiveness in global trade."),
                ("learner", "The failure to anticipate growth in maritime freight has left several Indian ports operating well below their potential capacity."),
                ("system", "Strategic foresight in infrastructure planning is indispensable for capitalising on emerging trade opportunities."),
            ],
        ],
    },

    # ──────────────────────────────────────────────
    # 10. TRAFFIC LIGHT
    # ──────────────────────────────────────────────
    "traffic light": {
        "beginner": [
            [
                ("learner", "The traffic light is red now."),
                ("system", "We must stop and wait for it to change."),
                ("learner", "Now the light has turned green."),
                ("system", "Green means it is safe to cross the road."),
            ],
            [
                ("learner", "There are three colours on the traffic light."),
                ("system", "Can you name all three colours?"),
                ("learner", "Red, yellow, and green are the three colours."),
                ("system", "Very good! Each colour tells drivers what to do."),
            ],
            [
                ("learner", "I always wait for the green traffic light."),
                ("system", "That is the safest way to cross the street."),
                ("learner", "My teacher told us about road safety rules."),
                ("system", "Your teacher gave you very important advice."),
            ],
        ],
        "elementary": [
            [
                ("learner", "The traffic light at our school junction stopped working today."),
                ("system", "That must have caused a lot of confusion for drivers."),
                ("learner", "A traffic policeman was directing the vehicles by hand."),
                ("system", "Police officers step in when traffic lights fail."),
            ],
            [
                ("learner", "Some drivers are ignoring the red traffic light and speeding through."),
                ("system", "That is extremely dangerous for pedestrians and other drivers."),
                ("learner", "I think cameras should be installed at every traffic light."),
                ("system", "Automated cameras are very effective at catching violators."),
            ],
            [
                ("learner", "The new traffic light was installed at the busy intersection last week."),
                ("system", "Did it help reduce the congestion there?"),
                ("learner", "Yes, the traffic is flowing much more smoothly now."),
                ("system", "Properly placed traffic lights make a big difference in road safety."),
            ],
        ],
        "intermediate": [
            [
                ("learner", "I have noticed that the traffic light timing at this junction is poorly calibrated."),
                ("system", "Poorly timed signals can actually increase congestion instead of reducing it."),
                ("learner", "If the green phase for the main road were extended by ten seconds, the queue would clear faster."),
                ("system", "Adaptive traffic light systems can automatically adjust timing based on real-time traffic flow."),
            ],
            [
                ("learner", "The traffic light near the hospital should prioritise ambulance routes during emergencies."),
                ("system", "Some cities have implemented emergency vehicle preemption systems."),
                ("learner", "If such a system had been in place last week, the ambulance would not have been stuck."),
                ("system", "Saving even a few minutes can make a life-or-death difference in medical emergencies."),
            ],
            [
                ("learner", "Many pedestrians have complained that the traffic light changes too quickly for them to cross safely."),
                ("system", "Elderly people and children need more time at crossings."),
                ("learner", "The municipality has agreed to review the pedestrian signal duration at twenty major junctions."),
                ("system", "Inclusive design of traffic systems should account for the slowest and most vulnerable users."),
            ],
        ],
        "upper_intermediate": [
            [
                ("learner", "The smart traffic light system that was piloted in Bengaluru has been praised for reducing commute times."),
                ("system", "Artificial intelligence can optimise signal patterns far better than fixed timers."),
                ("learner", "It was reported that average waiting times at equipped junctions decreased by nearly thirty percent."),
                ("system", "Scaling such systems citywide could transform urban mobility considerably."),
            ],
            [
                ("learner", "Colour-blind drivers are at a disadvantage when traffic lights rely solely on colour coding."),
                ("system", "Accessibility in road infrastructure is an often-overlooked design consideration."),
                ("learner", "Experts have recommended that position, shape, and flashing patterns be used alongside colours for clarity."),
                ("system", "Universal design principles should guide all public safety infrastructure decisions."),
            ],
            [
                ("learner", "Intersections where traffic lights were replaced by roundabouts showed a reduction in fatal accidents."),
                ("system", "Roundabouts eliminate the high-speed perpendicular collisions that occur at signalled intersections."),
                ("learner", "Urban planners suggest that a mix of both solutions is needed depending on traffic volume."),
                ("system", "Context-sensitive design is always more effective than a one-size-fits-all approach."),
            ],
        ],
        "advanced": [
            [
                ("learner", "Were every traffic light in the city connected to a centralised adaptive network, congestion could be mitigated at a systemic level."),
                ("system", "Such a system would require enormous computational infrastructure and real-time data feeds."),
                ("learner", "The challenge lies not merely in the technology but in coordinating across fragmented municipal jurisdictions."),
                ("system", "Institutional fragmentation is often a more formidable obstacle than technological limitation in urban governance."),
            ],
            [
                ("learner", "The traffic light, seemingly a mundane piece of urban furniture, is in fact a microcosm of the social contract governing shared public space."),
                ("system", "Compliance with traffic signals reflects broader societal attitudes toward rules and collective well-being."),
                ("learner", "One could argue that habitual signal violation in certain cities indicates a deeper erosion of civic trust."),
                ("system", "Rebuilding civic discipline requires both enforcement and a cultural shift toward valuing shared safety."),
            ],
            [
                ("learner", "Had traffic management been integrated into urban planning from the outset, Indian cities would not suffer such chronic gridlock."),
                ("system", "Retrofitting traffic solutions onto organically grown urban layouts is inherently constrained."),
                ("learner", "It is therefore essential that new urban developments embed intelligent traffic systems at the design stage."),
                ("system", "Learning from past planning failures is the most pragmatic path to building liveable cities for the future."),
            ],
        ],
    },

    # ──────────────────────────────────────────────
    # 11. FIRE HYDRANT
    # ──────────────────────────────────────────────
    "fire hydrant": {
        "beginner": [
            [
                ("learner", "I see a red fire hydrant on the street."),
                ("system", "Fire hydrants help firefighters get water quickly."),
                ("learner", "The fire hydrant looks like a short post."),
                ("system", "Yes, they are made of strong metal to last many years."),
            ],
            [
                ("learner", "There is a fire hydrant near our school."),
                ("system", "That is important for keeping the school safe."),
                ("learner", "We should not park cars near it."),
                ("system", "Exactly. Firefighters need clear access to it at all times."),
            ],
            [
                ("learner", "The fire hydrant has a big round top."),
                ("system", "Firefighters connect their hoses to that part."),
                ("learner", "Water comes out very fast from it."),
                ("system", "The strong water pressure helps put out fires quickly."),
            ],
        ],
        "elementary": [
            [
                ("learner", "A fire hydrant was leaking water on our street yesterday."),
                ("system", "That is a problem that the water department should fix."),
                ("learner", "Some children were playing in the water coming out of it."),
                ("system", "That is understandable but the water is needed for emergencies."),
            ],
            [
                ("learner", "The fire truck connected a hose to the fire hydrant outside our building."),
                ("system", "Was there a fire in the neighbourhood?"),
                ("learner", "There was a small fire in a shop on the ground floor."),
                ("system", "Thank goodness the fire hydrant was nearby and working properly."),
            ],
            [
                ("learner", "I learned that fire hydrants are connected to underground water pipes."),
                ("system", "That is correct. They tap into the main water supply."),
                ("learner", "The water pressure inside the pipes must be very strong."),
                ("system", "High pressure is essential for the water to reach upper floors of buildings."),
            ],
        ],
        "intermediate": [
            [
                ("learner", "I have noticed that many fire hydrants in our area are poorly maintained."),
                ("system", "Non-functional hydrants are a serious safety hazard."),
                ("learner", "If a fire broke out, firefighters would have to find water from another source."),
                ("system", "Regular inspection and maintenance of hydrants should be a municipal priority."),
            ],
            [
                ("learner", "The fire department has mapped every fire hydrant location in the city using a digital database."),
                ("system", "That helps crews locate the nearest working hydrant during emergencies."),
                ("learner", "If this system had existed during last year's warehouse fire, response time would have been faster."),
                ("system", "Technology can significantly improve emergency response efficiency."),
            ],
            [
                ("learner", "Many residential areas in Indian cities lack adequate fire hydrant coverage."),
                ("system", "Urban planning often overlooks fire safety infrastructure in the rush to build."),
                ("learner", "Residents have petitioned the corporation to install more hydrants in their colony."),
                ("system", "Community advocacy is important for pushing municipal authorities to act."),
            ],
        ],
        "upper_intermediate": [
            [
                ("learner", "The fire hydrant that had been damaged by a reversing truck was repaired within twenty-four hours."),
                ("system", "Rapid repair of damaged hydrants is critical for community safety."),
                ("learner", "It was confirmed that the truck driver had been fined for the damage caused."),
                ("system", "Accountability for damaging public safety equipment should be strictly enforced."),
            ],
            [
                ("learner", "A survey conducted by the fire services revealed that forty percent of hydrants in the old city are non-operational."),
                ("system", "That is an alarmingly high rate of failure for essential safety equipment."),
                ("learner", "Authorities were urged to allocate emergency funds for a comprehensive rehabilitation programme."),
                ("system", "Investing in hydrant maintenance is far cheaper than dealing with the consequences of uncontrolled fires."),
            ],
            [
                ("learner", "Modern fire hydrant designs incorporate tamper-proof mechanisms to prevent vandalism and misuse."),
                ("system", "Vandalism of public utilities is a persistent problem in many urban areas."),
                ("learner", "Engineers believe that robust designs combined with community awareness can reduce damage significantly."),
                ("system", "Technical solutions work best when complemented by civic responsibility."),
            ],
        ],
        "advanced": [
            [
                ("learner", "Were municipalities to treat fire hydrant maintenance with the same urgency as road repairs, fire-related fatalities could be meaningfully reduced."),
                ("system", "The invisibility of preventive infrastructure often relegates it to the bottom of budget priorities."),
                ("learner", "It is a sobering indictment of governance that safety equipment is neglected until a tragedy compels action."),
                ("system", "Reactive governance carries a far higher human and financial cost than proactive investment."),
            ],
            [
                ("learner", "The fire hydrant serves as an apt metaphor for the broader challenge of maintaining public goods in a culture of fiscal austerity."),
                ("system", "Infrastructure maintenance lacks the political visibility of new construction projects."),
                ("learner", "Until civic leaders recognise that maintenance is not discretionary but essential, urban decay will continue to accelerate."),
                ("system", "Shifting the political incentive structure to reward upkeep over ribbon-cutting is a fundamental governance challenge."),
            ],
            [
                ("learner", "Had building codes mandated internal fire suppression systems alongside external hydrant access, the fire would not have spread so rapidly."),
                ("system", "Comprehensive fire safety requires multiple redundant layers of protection."),
                ("learner", "The catastrophic failure in this case underscores the need for a systemic overhaul of fire safety regulations in India."),
                ("system", "Piecemeal reforms have proven insufficient; only a holistic revision of codes and enforcement will yield lasting improvement."),
            ],
        ],
    },

    # ──────────────────────────────────────────────
    # 12. STOP SIGN
    # ──────────────────────────────────────────────
    "stop sign": {
        "beginner": [
            [
                ("learner", "I see a red stop sign at the corner."),
                ("system", "Stop signs tell drivers to stop their vehicles."),
                ("learner", "The sign has white letters on it."),
                ("system", "The word on it says 'STOP' in big letters."),
            ],
            [
                ("learner", "We must stop at the stop sign."),
                ("system", "Yes, every driver must come to a full stop."),
                ("learner", "Then we look left and right for safety."),
                ("system", "That is the correct way to use a stop sign."),
            ],
            [
                ("learner", "The stop sign has eight sides."),
                ("system", "That special shape is called an octagon."),
                ("learner", "It is easy to see from far away."),
                ("system", "The bright red colour and unique shape make it stand out."),
            ],
        ],
        "elementary": [
            [
                ("learner", "A driver ran the stop sign and nearly hit a pedestrian."),
                ("system", "That is incredibly dangerous behaviour."),
                ("learner", "The police officer gave him a ticket for the violation."),
                ("system", "Traffic fines exist to discourage such reckless driving."),
            ],
            [
                ("learner", "The stop sign at our colony entrance was knocked down by a truck."),
                ("system", "Did anyone report it to the local authorities?"),
                ("learner", "My father called the traffic department to get it replaced."),
                ("system", "Missing stop signs can lead to serious accidents at intersections."),
            ],
            [
                ("learner", "I noticed a new stop sign was put up near the school gate."),
                ("system", "School zones need extra safety measures for children."),
                ("learner", "Now the cars are slowing down before the crossing area."),
                ("system", "That small change could prevent a major accident."),
            ],
        ],
        "intermediate": [
            [
                ("learner", "I have observed that most drivers treat the stop sign as optional rather than mandatory."),
                ("system", "Rolling through stop signs is a common but dangerous habit."),
                ("learner", "If enforcement cameras were installed at these locations, compliance would improve dramatically."),
                ("system", "Visible enforcement is the most effective deterrent for traffic violations."),
            ],
            [
                ("learner", "The placement of stop signs should follow careful traffic engineering analysis."),
                ("system", "Improperly placed signs can confuse drivers and reduce overall compliance."),
                ("learner", "An overuse of stop signs actually leads drivers to disregard them altogether."),
                ("system", "Sign fatigue is a well-documented phenomenon in traffic psychology."),
            ],
            [
                ("learner", "If the stop sign had been visible around the blind curve, the collision might not have occurred."),
                ("system", "Obstructed signage is a contributing factor in many accidents."),
                ("learner", "Trees and bushes growing around signs need to be trimmed regularly."),
                ("system", "Vegetation management around traffic signs is a basic road maintenance task."),
            ],
        ],
        "upper_intermediate": [
            [
                ("learner", "The stop sign that was vandalised in the residential area has been replaced after residents complained."),
                ("system", "Vandalism of traffic signs puts entire communities at risk."),
                ("learner", "Neighbourhood associations have been asked to report damaged signs through a dedicated mobile application."),
                ("system", "Crowdsourcing maintenance reports can dramatically improve response times."),
            ],
            [
                ("learner", "Research suggests that the standardised octagonal shape of the stop sign is recognised across cultures and languages."),
                ("system", "Its distinctive geometry makes it identifiable even when the text is in an unfamiliar language."),
                ("learner", "The international standardisation of road signs was a remarkable achievement in global cooperation."),
                ("system", "The Vienna Convention on Road Signs established a universal visual language for traffic safety."),
            ],
            [
                ("learner", "Autonomous vehicles are programmed to detect stop signs using computer vision algorithms."),
                ("system", "Reliable sign detection is fundamental to safe self-driving technology."),
                ("learner", "However, adversarial attacks on sign recognition systems have been demonstrated by researchers."),
                ("system", "Cybersecurity in autonomous vehicles is an emerging field with profound safety implications."),
            ],
        ],
        "advanced": [
            [
                ("learner", "Were traffic infrastructure designed with autonomous vehicles as the primary user, physical stop signs might eventually become obsolete."),
                ("system", "Vehicle-to-infrastructure communication could replace visual signage with digital instructions."),
                ("learner", "However, the transition period during which human and autonomous drivers coexist will require hybrid solutions."),
                ("system", "Managing the coexistence of legacy and emerging technologies is one of the most complex challenges in transport engineering."),
            ],
            [
                ("learner", "The stop sign, in its elegant simplicity, embodies a principle of unconditional obligation rarely found in other domains of civic life."),
                ("system", "Its binary instruction — stop or be penalised — leaves no room for interpretation or negotiation."),
                ("learner", "One might argue that the erosion of compliance with such unambiguous directives reflects a broader cultural shift away from shared norms."),
                ("system", "The sociology of traffic behaviour offers a surprisingly rich lens through which to examine societal attitudes toward authority and collective welfare."),
            ],
            [
                ("learner", "Had intersection design prioritised pedestrian safety from the beginning, the stop sign would not bear the disproportionate burden it currently carries."),
                ("system", "The dominance of car-centric design in urban planning has marginalised the needs of pedestrians for decades."),
                ("learner", "Reimagining intersections as spaces shared equitably among all road users is both an engineering challenge and a philosophical imperative."),
                ("system", "The movement toward complete streets reflects a growing recognition that roads must serve communities, not merely vehicles."),
            ],
        ],
    },

    # ──────────────────────────────────────────────
    # 13. PARKING METER
    # ──────────────────────────────────────────────
    "parking meter": {
        "beginner": [
            [
                ("learner", "There is a parking meter next to the car."),
                ("system", "You need to pay to park in that spot."),
                ("learner", "My father puts coins into the meter."),
                ("system", "The coins buy you time to keep the car parked."),
            ],
            [
                ("learner", "The parking meter shows thirty minutes left."),
                ("system", "You should be back before the time runs out."),
                ("learner", "What happens when the time is over?"),
                ("system", "You might get a fine if you stay too long."),
            ],
            [
                ("learner", "I see a row of parking meters on the street."),
                ("system", "Each meter belongs to one parking space."),
                ("learner", "They are tall and silver in colour."),
                ("system", "Parking meters help manage space in busy areas."),
            ],
        ],
        "elementary": [
            [
                ("learner", "The parking meter was not accepting my coins this morning."),
                ("system", "Broken meters can be very frustrating for drivers."),
                ("learner", "I had to find another parking spot further down the road."),
                ("system", "You should report the broken meter to the municipal office."),
            ],
            [
                ("learner", "Many cities are replacing old parking meters with digital payment systems."),
                ("system", "Digital payments are more convenient for most people."),
                ("learner", "You can now pay for parking using a mobile phone app."),
                ("system", "Technology is making everyday tasks like parking much easier."),
            ],
            [
                ("learner", "A parking attendant was checking the meters along the main road."),
                ("system", "Attendants make sure people pay for their parking time."),
                ("learner", "He placed a fine ticket on a car that had exceeded its time."),
                ("system", "Overstaying at a meter always carries the risk of a fine."),
            ],
        ],
        "intermediate": [
            [
                ("learner", "I have always found it annoying that parking meters rarely give change back."),
                ("system", "That is a common complaint, especially with coin-operated meters."),
                ("learner", "If all meters accepted digital payments, that problem would disappear entirely."),
                ("system", "Modernising parking infrastructure benefits both users and city revenue collection."),
            ],
            [
                ("learner", "The revenue collected from parking meters funds road maintenance in our city."),
                ("system", "Most people do not realise where their parking fees actually go."),
                ("learner", "If the funds were used more transparently, public support for paid parking would increase."),
                ("system", "Transparency in how public revenue is spent builds trust with citizens."),
            ],
            [
                ("learner", "Some merchants have argued that parking meters discourage customers from visiting their shops."),
                ("system", "The relationship between parking policy and local business is complex."),
                ("learner", "Studies have shown that turnover-based parking actually increases foot traffic over time."),
                ("system", "Free parking that never turns over can paradoxically reduce the number of visitors."),
            ],
        ],
        "upper_intermediate": [
            [
                ("learner", "The parking meters that were installed along the commercial district have generated significant revenue for the municipality."),
                ("system", "Paid parking in high-demand areas is an effective demand management tool."),
                ("learner", "However, it has been argued that the fees disproportionately affect lower-income workers."),
                ("system", "Equity considerations should inform parking pricing policies alongside revenue goals."),
            ],
            [
                ("learner", "Smart parking meters that adjust pricing based on real-time demand are being tested in several pilot areas."),
                ("system", "Dynamic pricing ensures that spaces are always available for those willing to pay."),
                ("learner", "Critics contend that such systems prioritise wealthy drivers over ordinary commuters."),
                ("system", "The balance between efficient allocation and equitable access is a recurring policy tension."),
            ],
            [
                ("learner", "A court ruling determined that fines issued by a malfunctioning parking meter were to be refunded to affected motorists."),
                ("system", "That is a fair outcome when the equipment itself was at fault."),
                ("learner", "The case highlighted the need for regular auditing and calibration of metering equipment."),
                ("system", "Accountability for the reliability of public infrastructure should rest with the administering authority."),
            ],
        ],
        "advanced": [
            [
                ("learner", "Were cities to eliminate minimum parking requirements and allow market-priced metering, urban land use would be fundamentally transformed."),
                ("system", "Parking policy is one of the most underappreciated levers of urban planning."),
                ("learner", "The vast amount of land dedicated to free parking represents an enormous opportunity cost in terms of housing and green space."),
                ("system", "Rethinking parking as a scarce resource rather than an entitlement could reshape cities for the better."),
            ],
            [
                ("learner", "The parking meter, however pedestrian it may seem, encodes a profound philosophical question about the commodification of public space."),
                ("system", "Charging for parking effectively privatises what was once freely shared commons."),
                ("learner", "One must weigh the efficiency gains of pricing against the democratic principle that public space should be equally accessible to all."),
                ("system", "This tension between market efficiency and spatial justice lies at the heart of contemporary urban governance debates."),
            ],
            [
                ("learner", "Had parking been properly priced from the beginning of the automobile era, the sprawl that defines most modern cities could have been significantly curtailed."),
                ("system", "Free or underpriced parking subsidised car dependency and shaped development patterns for generations."),
                ("learner", "Reversing those entrenched patterns now requires a politically courageous reimagining of how we allocate urban space."),
                ("system", "The inertia of built environments makes retrospective correction orders of magnitude harder than prospective planning."),
            ],
        ],
    },

    # ──────────────────────────────────────────────
    # 14. BENCH
    # ──────────────────────────────────────────────
    "bench": {
        "beginner": [
            [
                ("learner", "There is a wooden bench in the park."),
                ("system", "That looks like a nice place to sit."),
                ("learner", "I like to sit on the bench and read."),
                ("system", "Reading in the park is very relaxing."),
            ],
            [
                ("learner", "The bench is under a big tree."),
                ("system", "The shade must keep it cool in summer."),
                ("learner", "My grandmother sits there every evening."),
                ("system", "It sounds like her favourite resting spot."),
            ],
            [
                ("learner", "Two people are sitting on the bench."),
                ("system", "They look like they are having a nice chat."),
                ("learner", "The bench is long enough for three people."),
                ("system", "Public benches help people rest and socialise."),
            ],
        ],
        "elementary": [
            [
                ("learner", "The park bench was freshly painted green last weekend."),
                ("system", "A fresh coat of paint makes everything look better."),
                ("learner", "I accidentally sat on it before the paint was dry."),
                ("system", "Oh no! Did the paint get on your clothes?"),
            ],
            [
                ("learner", "We were sitting on the bench when a squirrel ran past our feet."),
                ("system", "Squirrels in parks are often quite bold around people."),
                ("learner", "It climbed up the tree behind the bench in just a few seconds."),
                ("system", "They are incredibly fast climbers, especially when startled."),
            ],
            [
                ("learner", "The old stone bench near the temple has been there for many years."),
                ("system", "It must have seen so many people come and go."),
                ("learner", "My grandfather told me he used to sit on the same bench as a child."),
                ("system", "That is a beautiful connection across generations."),
            ],
        ],
        "intermediate": [
            [
                ("learner", "I have spent many afternoons on that park bench preparing for my exams."),
                ("system", "Studying outdoors can be very refreshing compared to a stuffy room."),
                ("learner", "If the park had better lighting, I could study there in the evenings too."),
                ("system", "Good lighting in public spaces extends their usability and improves safety."),
            ],
            [
                ("learner", "The municipality has installed new benches along the lakeside walking path."),
                ("system", "That must be a welcome addition for walkers and joggers."),
                ("learner", "Elderly visitors have particularly appreciated having places to rest at regular intervals."),
                ("system", "Thoughtful placement of benches makes public spaces accessible to people of all ages."),
            ],
            [
                ("learner", "If the benches had been made of weather-resistant material, they would not have rotted so quickly."),
                ("system", "Material choice is crucial for outdoor furniture that faces monsoon rains."),
                ("learner", "The replacement benches are being made of recycled plastic, which lasts much longer."),
                ("system", "Using recycled materials is both durable and environmentally responsible."),
            ],
        ],
        "upper_intermediate": [
            [
                ("learner", "The memorial bench that was dedicated to a local freedom fighter has become a landmark in the neighbourhood."),
                ("system", "Memorial benches carry both functional and emotional significance for communities."),
                ("learner", "Visitors have been observed pausing to read the inscription before sitting down."),
                ("system", "Such small gestures of remembrance help keep local history alive."),
            ],
            [
                ("learner", "Anti-homeless bench designs that prevent people from lying down have drawn criticism from social activists."),
                ("system", "Hostile architecture raises uncomfortable questions about who public spaces are really designed for."),
                ("learner", "It is argued that such designs criminalise poverty rather than address its root causes."),
                ("system", "Designing public spaces with empathy and inclusivity should be a core principle of urban planning."),
            ],
            [
                ("learner", "A community project invited local artists to paint murals on the concrete benches in the town square."),
                ("system", "Public art transforms ordinary infrastructure into cultural expressions."),
                ("learner", "The initiative was credited with revitalising interest in the previously neglected public space."),
                ("system", "Creative placemaking can change how communities perceive and use their shared spaces."),
            ],
        ],
        "advanced": [
            [
                ("learner", "Were urban planners to prioritise comfortable seating in public spaces, the social fabric of neighbourhoods would be noticeably strengthened."),
                ("system", "The humble bench is a surprisingly powerful catalyst for community interaction."),
                ("learner", "Research consistently demonstrates that the availability of seating correlates with increased social cohesion and reduced loneliness among the elderly."),
                ("system", "Investing in benches is arguably one of the most cost-effective public health interventions a city can undertake."),
            ],
            [
                ("learner", "The progressive removal of public seating in commercial districts reflects a broader trend of sanitising urban space for consumer activity."),
                ("system", "When rest becomes contingent on purchase, public space ceases to be truly public."),
                ("learner", "One must question whether a city designed exclusively for productivity and commerce can sustain genuine human flourishing."),
                ("system", "The erosion of non-commercial gathering spaces diminishes the democratic character of urban life."),
            ],
            [
                ("learner", "Had the original park design retained the circular bench arrangement around the central fountain, the space would have fostered face-to-face interaction."),
                ("system", "The spatial configuration of seating profoundly influences the nature of social encounters."),
                ("learner", "It is no coincidence that the most beloved public spaces in the world feature thoughtfully arranged seating that invites lingering."),
                ("system", "Great public spaces are rarely accidental; they are the product of deliberate, human-centred design."),
            ],
        ],
    },

    # ──────────────────────────────────────────────
    # 15. BIRD
    # ──────────────────────────────────────────────
    "bird": {
        "beginner": [
            [
                ("learner", "A small bird is sitting on the wall."),
                ("system", "What colour are its feathers?"),
                ("learner", "The bird has brown and white feathers."),
                ("system", "It might be a sparrow. They are very common here."),
            ],
            [
                ("learner", "I can hear a bird singing outside."),
                ("system", "Birds sing the most in the early morning."),
                ("learner", "The bird sounds very happy today."),
                ("system", "Birdsong makes any morning more beautiful."),
            ],
            [
                ("learner", "The bird is eating rice on the ground."),
                ("system", "Many birds enjoy eating grains and seeds."),
                ("learner", "My grandmother feeds the birds every day."),
                ("system", "That is a lovely tradition to keep."),
            ],
        ],
        "elementary": [
            [
                ("learner", "A crow was stealing food from the kitchen window this morning."),
                ("system", "Crows are known for being very clever birds."),
                ("learner", "My mother chased it away with a towel."),
                ("system", "Crows always come back once they find a food source."),
            ],
            [
                ("learner", "We spotted a beautiful kingfisher near the pond last Sunday."),
                ("system", "Kingfishers are stunning with their bright blue plumage."),
                ("learner", "It dived into the water and caught a tiny fish instantly."),
                ("system", "They are incredibly skilled hunters in the water."),
            ],
            [
                ("learner", "The bird built a nest on the ledge above our front door."),
                ("system", "What kind of bird is it?"),
                ("learner", "I think it is a pigeon because it is grey and plump."),
                ("system", "Pigeons often choose sheltered spots near human homes for nesting."),
            ],
        ],
        "intermediate": [
            [
                ("learner", "I have been birdwatching in Vedanthangal lake sanctuary for three years now."),
                ("system", "That is one of the oldest bird sanctuaries in India."),
                ("learner", "If migratory birds stop coming due to habitat loss, the ecosystem would suffer greatly."),
                ("system", "Wetland conservation is essential for sustaining migratory bird populations."),
            ],
            [
                ("learner", "The number of sparrows in our city has declined dramatically over the past decade."),
                ("system", "Urbanisation and the loss of nesting sites have contributed to their decline."),
                ("learner", "If more people installed nesting boxes on their balconies, it might help the population recover."),
                ("system", "Small individual actions can collectively make a meaningful difference for urban wildlife."),
            ],
            [
                ("learner", "Bird flu outbreaks have caused panic among poultry farmers in several districts this year."),
                ("system", "Avian influenza can devastate poultry populations and threaten farmer livelihoods."),
                ("learner", "The government has ordered culling in affected areas to prevent the virus from spreading."),
                ("system", "Rapid containment is critical, but compensation for affected farmers is equally important."),
            ],
        ],
        "upper_intermediate": [
            [
                ("learner", "The migratory bird species that was thought to have abandoned this wetland has been spotted again after a five-year absence."),
                ("system", "That is a hopeful sign for the health of the local ecosystem."),
                ("learner", "Conservationists believe that recent restoration efforts have made the habitat suitable once more."),
                ("system", "Ecological restoration, when done thoughtfully, can yield remarkable results."),
            ],
            [
                ("learner", "A bird strike caused an airplane engine to fail shortly after takeoff from the coastal airport."),
                ("system", "Bird strikes are a serious aviation hazard, particularly near wetlands."),
                ("learner", "Airport authorities are reported to be considering sonic deterrent systems to keep birds away from runways."),
                ("system", "Balancing aviation safety with the presence of natural habitats near airports is a complex challenge."),
            ],
            [
                ("learner", "Citizen science projects that track bird populations have contributed valuable data to ornithological research."),
                ("system", "Platforms like eBird have democratised bird monitoring on a global scale."),
                ("learner", "Indian birdwatchers are said to have submitted millions of observations through such platforms."),
                ("system", "The collective effort of amateur birdwatchers has filled critical gaps in scientific knowledge."),
            ],
        ],
        "advanced": [
            [
                ("learner", "Were the agricultural sector to reduce its dependence on pesticides, avian biodiversity in rural landscapes would recover substantially."),
                ("system", "Pesticide use has been implicated in the decline of insectivorous bird species worldwide."),
                ("learner", "The ecological services provided by birds, from pest control to pollination, far outweigh the cost of transitioning to sustainable farming."),
                ("system", "Quantifying ecosystem services in economic terms is essential for making a compelling case to policymakers."),
            ],
            [
                ("learner", "The canary in the coal mine is perhaps the most poignant illustration of how birds serve as sentinels of environmental health."),
                ("system", "Declining bird populations today signal broader ecological imbalances that will eventually affect human communities."),
                ("learner", "It is incumbent upon us to heed these warnings before the cascading effects become irreversible."),
                ("system", "Ecological tipping points, once crossed, are extraordinarily difficult and costly to reverse."),
            ],
            [
                ("learner", "Had colonial-era hunters not driven several endemic bird species to extinction, the Indian subcontinent's avifauna would be considerably richer."),
                ("system", "Historical extinctions serve as cautionary tales for contemporary conservation efforts."),
                ("learner", "The moral imperative to preserve what remains demands that we move beyond rhetoric to enforceable habitat protections."),
                ("system", "Conservation legislation without robust enforcement mechanisms amounts to little more than aspirational symbolism."),
            ],
        ],
    },

    # ──────────────────────────────────────────────
    # 16. CAT
    # ──────────────────────────────────────────────
    "cat": {
        "beginner": [
            [
                ("learner", "There is a cat sleeping on the chair."),
                ("system", "Cats love to sleep in warm, comfortable spots."),
                ("learner", "The cat is small and grey in colour."),
                ("system", "Grey cats are sometimes called silver tabbies."),
            ],
            [
                ("learner", "I see a cat near the fish shop."),
                ("system", "Cats are always attracted to the smell of fish."),
                ("learner", "The cat is waiting for some food."),
                ("system", "The shopkeeper probably feeds it every day."),
            ],
            [
                ("learner", "My friend has a pet cat at home."),
                ("system", "What is the cat's name?"),
                ("learner", "The cat's name is Mittens."),
                ("system", "That is a very cute name for a cat."),
            ],
        ],
        "elementary": [
            [
                ("learner", "A stray cat was crying outside our door last night."),
                ("system", "It was probably hungry or looking for shelter."),
                ("learner", "My mother gave it some milk and rice this morning."),
                ("system", "That was very compassionate of her to help the stray."),
            ],
            [
                ("learner", "The cat jumped from the wall and landed perfectly on its feet."),
                ("system", "Cats have an amazing ability to balance while falling."),
                ("learner", "I read that cats can twist their bodies in mid-air."),
                ("system", "Their flexible spine gives them that incredible agility."),
            ],
            [
                ("learner", "Our neighbour's cat had four kittens under our staircase."),
                ("system", "Kittens are so tiny and adorable when they are newborn."),
                ("learner", "The mother cat is protecting them very carefully."),
                ("system", "Mother cats are fiercely protective of their young ones."),
            ],
        ],
        "intermediate": [
            [
                ("learner", "I have been taking care of a stray cat for six months and it finally trusts me."),
                ("system", "Building trust with a stray animal takes patience and consistency."),
                ("learner", "If I had not fed it regularly, it would still be running away from me."),
                ("system", "Animals remember kindness and respond to it over time."),
            ],
            [
                ("learner", "The street cat population in our area has increased noticeably this year."),
                ("system", "Unchecked populations can lead to conflicts with residents."),
                ("learner", "Animal welfare groups have been conducting sterilisation drives to manage the numbers humanely."),
                ("system", "Trap-neuter-return programmes are the most effective and ethical approach to population control."),
            ],
            [
                ("learner", "Cats are far more independent than dogs, which is why some people prefer them as pets."),
                ("system", "Their self-sufficient nature suits people with busy lifestyles."),
                ("learner", "If I lived in a smaller apartment, I would choose a cat over a dog for that reason."),
                ("system", "Cats adapt well to indoor living and require less space than most dogs."),
            ],
        ],
        "upper_intermediate": [
            [
                ("learner", "The cat that was rescued from a collapsed building during the earthquake survived against all odds."),
                ("system", "Animals can endure remarkable conditions when trapped in disaster zones."),
                ("learner", "Rescue workers reported that the cat had survived for over a week without food or water."),
                ("system", "Such stories of survival often bring hope during otherwise tragic events."),
            ],
            [
                ("learner", "It is believed that cats were first domesticated in the ancient Near East around ten thousand years ago."),
                ("system", "Their role in controlling rodents around grain stores made them invaluable to early agricultural communities."),
                ("learner", "Historians suggest that the relationship between humans and cats evolved through mutual benefit rather than deliberate taming."),
                ("system", "The cat's domestication story is unique because they essentially domesticated themselves."),
            ],
            [
                ("learner", "A study conducted by a veterinary university found that feral cats are the primary predators of urban birds."),
                ("system", "The ecological impact of free-roaming cats on wildlife is well documented globally."),
                ("learner", "Environmentalists and animal welfare advocates remain divided on how best to address the issue."),
                ("system", "Finding a solution that protects both cats and wildlife requires careful stakeholder dialogue."),
            ],
        ],
        "advanced": [
            [
                ("learner", "Were municipalities to implement comprehensive feral cat management programmes, the ecological damage to urban bird populations could be substantially mitigated."),
                ("system", "The challenge lies in designing policies that satisfy both conservationist and animal welfare perspectives."),
                ("learner", "It is essential that any management approach be grounded in empirical evidence rather than emotional advocacy from either camp."),
                ("system", "Evidence-based policymaking is the only path through polarised debates on human-wildlife conflict."),
            ],
            [
                ("learner", "The cultural veneration of the cat in ancient Egypt, contrasted with its persecution in mediaeval Europe, illustrates how human attitudes toward animals are historically contingent."),
                ("system", "Societal treatment of animals often reflects prevailing religious, economic, and ideological frameworks."),
                ("learner", "One might argue that contemporary attitudes toward cats as pets reveal as much about human loneliness as they do about affection for animals."),
                ("system", "The modern pet industry thrives in no small part on the emotional void created by increasingly atomised social structures."),
            ],
            [
                ("learner", "Had toxoplasmosis research been communicated more responsibly, public attitudes toward cats would not have been distorted by sensationalised health fears."),
                ("system", "Media coverage of zoonotic risks often sacrifices nuance for attention-grabbing headlines."),
                ("learner", "It is incumbent upon the scientific community to contextualise findings clearly so that public health decisions are informed rather than fear-driven."),
                ("system", "Bridging the gap between scientific literacy and public understanding remains one of the great challenges of our time."),
            ],
        ],
    },

    # ──────────────────────────────────────────────
    # 17. DOG
    # ──────────────────────────────────────────────
    "dog": {
        "beginner": [
            [
                ("learner", "A brown dog is playing in the street."),
                ("system", "It looks like a friendly dog!"),
                ("learner", "The dog is wagging its tail happily."),
                ("system", "A wagging tail means the dog is excited."),
            ],
            [
                ("learner", "I see a dog sitting near the gate."),
                ("system", "Is it a pet or a stray dog?"),
                ("learner", "It has a collar, so it is a pet."),
                ("system", "The collar means someone takes care of it."),
            ],
            [
                ("learner", "The dog is drinking water from a bowl."),
                ("system", "Dogs need plenty of water, especially in summer."),
                ("learner", "I want to give it some biscuits."),
                ("system", "That is kind, but check with the owner first."),
            ],
        ],
        "elementary": [
            [
                ("learner", "Our neighbour's dog was barking loudly all night."),
                ("system", "It might have been scared or heard something unusual."),
                ("learner", "My father spoke to the neighbour about keeping the dog calm."),
                ("system", "Communication between neighbours helps resolve such issues peacefully."),
            ],
            [
                ("learner", "I am taking my dog for a walk in the evening today."),
                ("system", "Regular walks are important for a dog's health and happiness."),
                ("learner", "He loves running on the grass near the playground."),
                ("system", "Exercise keeps dogs fit and well-behaved at home."),
            ],
            [
                ("learner", "A street dog followed me all the way home from school."),
                ("system", "It probably sensed that you are a kind person."),
                ("learner", "I gave it some chapati and water at the gate."),
                ("system", "Feeding strays with care shows real compassion."),
            ],
        ],
        "intermediate": [
            [
                ("learner", "I have been thinking about adopting a dog from the local animal shelter."),
                ("system", "Adoption is a wonderful way to give a dog a second chance."),
                ("learner", "If my landlord permits pets, I will visit the shelter this weekend."),
                ("system", "Many shelters are overcrowded and urgently need people willing to adopt."),
            ],
            [
                ("learner", "The stray dog problem in Indian cities has become a matter of intense public debate."),
                ("system", "Opinions range from compassion-driven feeding to calls for aggressive removal."),
                ("learner", "The Animal Birth Control programme has been effective where it is implemented properly."),
                ("system", "Humane population management combined with vaccination is the recommended approach."),
            ],
            [
                ("learner", "If the dog had been vaccinated against rabies, the child would not have needed emergency treatment."),
                ("system", "Rabies is almost always fatal once symptoms appear, making vaccination critical."),
                ("learner", "Mass vaccination campaigns have successfully eliminated rabies in several countries."),
                ("system", "India accounts for a significant share of global rabies deaths, mostly from dog bites."),
            ],
        ],
        "upper_intermediate": [
            [
                ("learner", "The therapy dog programme that was introduced at the children's hospital has shown remarkable results."),
                ("system", "Animal-assisted therapy has been proven to reduce anxiety and improve recovery rates in patients."),
                ("learner", "Doctors reported that children who interacted with the dogs displayed lower stress hormone levels."),
                ("system", "The human-animal bond has therapeutic potential that is increasingly being recognised by mainstream medicine."),
            ],
            [
                ("learner", "Sniffer dogs trained to detect explosives were deployed at the airport during the high-security alert."),
                ("system", "The canine sense of smell is thousands of times more sensitive than any technological device."),
                ("learner", "Trainers said that it takes nearly two years to prepare a dog for professional detection work."),
                ("system", "The investment in training pays enormous dividends in terms of security outcomes."),
            ],
            [
                ("learner", "A legal petition demanding stricter penalties for cruelty against dogs was filed in the high court."),
                ("system", "Existing animal cruelty laws in India are widely regarded as insufficient."),
                ("learner", "Activists believe that stronger legal deterrents would reduce incidents of deliberate harm to animals."),
                ("system", "Legal reform must be accompanied by societal change in attitudes toward animal welfare."),
            ],
        ],
        "advanced": [
            [
                ("learner", "Were India to adopt a comprehensive and adequately funded rabies elimination strategy, it could save thousands of lives and billions of rupees annually."),
                ("system", "The economic burden of rabies treatment and lost productivity far exceeds the cost of prevention."),
                ("learner", "The failure to prioritise this eminently solvable public health crisis reflects a deeper neglect of preventive medicine in health policy."),
                ("system", "Political will and sustained funding are the primary barriers, not scientific knowledge or technical capacity."),
            ],
            [
                ("learner", "The centuries-long coevolution of dogs and humans has produced a species uniquely attuned to human emotional states."),
                ("system", "Dogs can read human facial expressions and vocal tones with remarkable accuracy."),
                ("learner", "One might contend that no other interspecies relationship in the animal kingdom approaches this depth of mutual understanding."),
                ("system", "The bond between humans and dogs offers a compelling case study in the evolutionary advantages of cross-species cooperation."),
            ],
            [
                ("learner", "Had indigenous Indian dog breeds been valued culturally rather than stigmatised, the demand for imported breeds would not have fuelled unethical breeding practices."),
                ("system", "The preference for foreign breeds is intertwined with colonial and class-based attitudes toward native species."),
                ("learner", "It is imperative that breed awareness campaigns highlight the health advantages and adaptability of Indian breeds."),
                ("system", "Celebrating indigenous biodiversity, whether in agriculture or animal husbandry, is an act of both ecological and cultural reclamation."),
            ],
        ],
    },

    # ──────────────────────────────────────────────
    # 18. HORSE
    # ──────────────────────────────────────────────
    "horse": {
        "beginner": [
            [
                ("learner", "I see a big brown horse on the road."),
                ("system", "Horses are strong and beautiful animals."),
                ("learner", "The horse is pulling a cart slowly."),
                ("system", "Horse-drawn carts are still used in some areas."),
            ],
            [
                ("learner", "The horse has a long black mane."),
                ("system", "A healthy mane means the horse is well cared for."),
                ("learner", "I want to touch the horse gently."),
                ("system", "Always approach a horse slowly and calmly."),
            ],
            [
                ("learner", "A white horse is standing near the field."),
                ("system", "White horses are sometimes called grey horses."),
                ("learner", "It is eating grass under the tree."),
                ("system", "Horses spend many hours eating grass every day."),
            ],
        ],
        "elementary": [
            [
                ("learner", "We saw decorated horses at the wedding procession yesterday."),
                ("system", "Horse processions are a wonderful part of Indian wedding traditions."),
                ("learner", "The horse was wearing a colourful cloth and flower garlands."),
                ("system", "Wedding horses are always beautifully adorned for the occasion."),
            ],
            [
                ("learner", "A horse was running very fast along the beach at Marina."),
                ("system", "Horse riding on the beach is a popular tourist activity."),
                ("learner", "The rider was holding the reins tightly to keep control."),
                ("system", "Controlling a horse requires both strength and trust between rider and animal."),
            ],
            [
                ("learner", "My grandfather worked with horses on the farm when he was young."),
                ("system", "Before tractors, horses were essential for farm work."),
                ("learner", "He told me stories about ploughing fields with a pair of horses."),
                ("system", "Those stories connect us to a way of life that is slowly disappearing."),
            ],
        ],
        "intermediate": [
            [
                ("learner", "I have always admired the Marwari horse breed, which is native to Rajasthan."),
                ("system", "The Marwari is known for its distinctive inward-curving ears."),
                ("learner", "If more breeders focused on preserving indigenous breeds, they would not be at risk of extinction."),
                ("system", "Preservation of native breeds is important for maintaining genetic diversity."),
            ],
            [
                ("learner", "The use of horses for pulling heavy loads in urban traffic has drawn criticism from animal rights groups."),
                ("system", "Working horses in cities often suffer from poor health and overexertion."),
                ("learner", "Several cities have banned horse-drawn carriages to protect animal welfare."),
                ("system", "Alternative livelihoods must be provided for the owners who depend on these animals."),
            ],
            [
                ("learner", "If the equestrian centre had been built closer to the city, more children would have access to riding lessons."),
                ("system", "Horse riding teaches children discipline, balance, and responsibility."),
                ("learner", "The few centres that exist cater mainly to wealthy families, which limits access."),
                ("system", "Making equestrian activities inclusive requires subsidised programmes and community partnerships."),
            ],
        ],
        "upper_intermediate": [
            [
                ("learner", "The horse that collapsed while pulling an overloaded cart was rescued by animal welfare volunteers."),
                ("system", "Overloading working animals is both cruel and illegal under prevention of cruelty laws."),
                ("learner", "It was later revealed that the horse had been working without rest for over twelve hours."),
                ("system", "Enforcement of existing animal protection laws remains woefully inadequate in most Indian cities."),
            ],
            [
                ("learner", "A horse therapy programme designed for children with cerebral palsy has been launched at a rehabilitation centre."),
                ("system", "Equine-assisted therapy, or hippotherapy, uses the horse's rhythmic movement to improve motor function."),
                ("learner", "Therapists report that the children showed improvements in balance and muscle coordination."),
                ("system", "The bond between child and horse also provides significant emotional and psychological benefits."),
            ],
            [
                ("learner", "Police mounted units on horseback are considered effective for crowd management during large public gatherings."),
                ("system", "The elevated position gives mounted officers a commanding view of the crowd."),
                ("learner", "However, animal welfare advocates question whether such deployment subjects horses to unnecessary stress."),
                ("system", "The wellbeing of service animals must be carefully monitored and prioritised by the units that employ them."),
            ],
        ],
        "advanced": [
            [
                ("learner", "Were India to establish a national breeding programme for indigenous horse breeds, it could preserve genetic resources of immense agricultural and cultural value."),
                ("system", "Indigenous breeds have evolved over centuries to thrive in local climatic and terrain conditions."),
                ("learner", "The neglect of these breeds in favour of imported varieties mirrors a broader pattern of devaluing native heritage across multiple domains."),
                ("system", "Reclaiming and investing in indigenous genetic resources is both a scientific imperative and a statement of cultural sovereignty."),
            ],
            [
                ("learner", "The horse occupies a paradoxical position in contemporary India, simultaneously revered in mythology and exploited in everyday commerce."),
                ("system", "That dissonance between cultural symbolism and lived reality is a recurring feature of human-animal relationships."),
                ("learner", "One must ask whether the ritualistic veneration of animals in cultural contexts absolves society of its ethical obligations toward their welfare."),
                ("system", "Ceremonial respect without material care is a hollow gesture that perpetuates suffering under the guise of tradition."),
            ],
            [
                ("learner", "Had mechanisation in agriculture been paired with rehabilitation programmes for displaced working horses, the welfare crisis could have been averted."),
                ("system", "Technological transitions that disregard the fate of displaced animals and workers create entirely predictable suffering."),
                ("learner", "It is incumbent upon the state to manage such transitions with a comprehensive plan that addresses both human and animal welfare."),
                ("system", "A just transition must account for all living beings affected by systemic economic change."),
            ],
        ],
    },

    # ──────────────────────────────────────────────
    # 19. SHEEP
    # ──────────────────────────────────────────────
    "sheep": {
        "beginner": [
            [
                ("learner", "I see a group of sheep in the field."),
                ("system", "A group of sheep is called a flock."),
                ("learner", "The sheep have thick white wool."),
                ("system", "Their wool keeps them warm in cold weather."),
            ],
            [
                ("learner", "The sheep are walking behind the shepherd."),
                ("system", "Sheep usually follow their shepherd closely."),
                ("learner", "The shepherd has a long stick in his hand."),
                ("system", "The stick helps him guide the flock safely."),
            ],
            [
                ("learner", "A small sheep is standing near its mother."),
                ("system", "A baby sheep is called a lamb."),
                ("learner", "The lamb looks very soft and fluffy."),
                ("system", "Lambs have the softest wool when they are young."),
            ],
        ],
        "elementary": [
            [
                ("learner", "We visited a sheep farm during our village trip last summer."),
                ("system", "What was the most interesting thing you saw there?"),
                ("learner", "The farmer was shearing the wool off the sheep with electric clippers."),
                ("system", "Shearing does not hurt the sheep and is done every year before summer."),
            ],
            [
                ("learner", "The shepherd was bringing his sheep down from the hills before sunset."),
                ("system", "Shepherds move their flocks to higher ground for better grazing."),
                ("learner", "His dog was running alongside the flock to keep them together."),
                ("system", "Sheepdogs are specially trained to herd and protect the flock."),
            ],
            [
                ("learner", "My grandmother makes sweaters from wool she buys at the local market."),
                ("system", "Hand-knitted wool sweaters are wonderfully warm."),
                ("learner", "She told me the wool comes from sheep raised in the Nilgiri hills."),
                ("system", "The Nilgiris have a long tradition of sheep farming and wool production."),
            ],
        ],
        "intermediate": [
            [
                ("learner", "I have read that sheep farming is a primary source of income for many pastoral communities in India."),
                ("system", "Communities like the Rabaris in Gujarat have herded sheep for generations."),
                ("learner", "If the government provided better veterinary services in remote areas, livestock losses would decrease."),
                ("system", "Access to basic animal healthcare is still a challenge in many rural regions."),
            ],
            [
                ("learner", "The demand for wool has declined because synthetic fabrics are cheaper to produce."),
                ("system", "This decline has severely affected traditional sheep-rearing communities."),
                ("learner", "If consumers valued natural fibres more, wool-based livelihoods would be more sustainable."),
                ("system", "Consumer awareness of sustainable fashion choices can revive demand for natural wool."),
            ],
            [
                ("learner", "Sheep grazing on common lands has sometimes led to conflicts with crop farmers in the region."),
                ("system", "Overgrazing can damage croplands and lead to soil degradation."),
                ("learner", "Both communities have agreed to a rotational grazing system to reduce friction."),
                ("system", "Collaborative land management is the most effective way to balance competing needs."),
            ],
        ],
        "upper_intermediate": [
            [
                ("learner", "A cross-breeding programme aimed at improving wool quality in native sheep breeds was launched by the agricultural university."),
                ("system", "Selective breeding can enhance desirable traits while preserving local adaptations."),
                ("learner", "Farmers participating in the programme reported higher wool yields within two breeding cycles."),
                ("system", "Scientific support for traditional livelihoods can make a tangible difference in farmer incomes."),
            ],
            [
                ("learner", "Nomadic shepherds whose migration routes cross state boundaries face bureaucratic obstacles and permit requirements."),
                ("system", "Pastoral migration is an ancient practice that predates modern administrative boundaries."),
                ("learner", "Advocates have called for a national pastoral policy that recognises and protects traditional migration corridors."),
                ("system", "Harmonising pastoral rights with modern governance frameworks remains a complex but necessary task."),
            ],
            [
                ("learner", "The sheep that were found abandoned in the drought-stricken district were relocated to a government relief camp."),
                ("system", "Drought forces many herders to abandon animals they can no longer feed."),
                ("learner", "It was reported that hundreds of livestock had perished before relief operations commenced."),
                ("system", "Timely drought response must include provisions for livestock, not just human populations."),
            ],
        ],
        "advanced": [
            [
                ("learner", "Were pastoral communities granted formal land rights over traditional grazing corridors, the ongoing encroachment on common lands could be halted."),
                ("system", "The erosion of commons has disproportionately harmed nomadic and semi-nomadic communities across India."),
                ("learner", "It is unconscionable that communities who have sustainably managed these lands for centuries are being dispossessed by commercial interests."),
                ("system", "Defending the commons is not merely an environmental issue but a fundamental question of social justice."),
            ],
            [
                ("learner", "The metaphor of the sheep as a passive follower, so prevalent in Western literature, does a disservice to an animal of considerable social intelligence."),
                ("system", "Research has demonstrated that sheep can recognise faces, form complex social bonds, and experience emotions."),
                ("learner", "Revising our cultural narratives about animals in light of scientific understanding is essential for more ethical interspecies relationships."),
                ("system", "How we speak about animals shapes how we treat them; language is never merely descriptive but constitutive of attitudes."),
            ],
            [
                ("learner", "Had the wool industry adapted to changing consumer preferences through innovation and branding, its decline in India might have been less precipitous."),
                ("system", "Industries built on traditional products must evolve or risk irrelevance in rapidly changing markets."),
                ("learner", "Nevertheless, the social cost of that decline, measured in displaced livelihoods and eroded cultural practices, cannot be reduced to market logic alone."),
                ("system", "Economic transitions demand holistic policies that account for human dignity alongside industrial efficiency."),
            ],
        ],
    },

    # ──────────────────────────────────────────────
    # 20. COW
    # ──────────────────────────────────────────────
    "cow": {
        "beginner": [
            [
                ("learner", "I see a cow eating grass in the field."),
                ("system", "Cows spend most of their day eating and resting."),
                ("learner", "The cow is big and has brown spots."),
                ("system", "Many Indian cow breeds have beautiful markings."),
            ],
            [
                ("learner", "A cow is standing in the middle of the road."),
                ("system", "That happens often in Indian towns and villages."),
                ("learner", "The cars are going around the cow carefully."),
                ("system", "Drivers are usually patient with cows on the road."),
            ],
            [
                ("learner", "My grandmother has a cow at her house."),
                ("system", "Does she get fresh milk from it every day?"),
                ("learner", "Yes, the cow gives milk every morning."),
                ("system", "Fresh milk from your own cow is very nutritious."),
            ],
        ],
        "elementary": [
            [
                ("learner", "The milkman was bringing fresh cow milk to our house this morning."),
                ("system", "Many families in India still prefer farm-fresh milk delivery."),
                ("learner", "My mother boiled it immediately to make it safe for drinking."),
                ("system", "Boiling raw milk is important to kill any harmful bacteria."),
            ],
            [
                ("learner", "A cow was lying down peacefully under the banyan tree near the temple."),
                ("system", "Cows often seek shade during the hottest part of the day."),
                ("learner", "Some people from the neighbourhood brought water and food for it."),
                ("system", "Caring for animals in the community is a cherished tradition."),
            ],
            [
                ("learner", "The farmer was taking his cows to the river for their bath."),
                ("system", "Bathing helps keep cows cool and healthy in summer."),
                ("learner", "He has five cows and three calves in his small dairy farm."),
                ("system", "Small dairy farms are the backbone of rural livelihoods in India."),
            ],
        ],
        "intermediate": [
            [
                ("learner", "I have learned that India is the largest producer of milk in the world."),
                ("system", "The dairy cooperative movement transformed India's milk production capacity."),
                ("learner", "If small farmers had better access to veterinary care, milk yields could improve further."),
                ("system", "Supporting smallholder dairy farmers is essential for sustaining India's milk revolution."),
            ],
            [
                ("learner", "Stray cows roaming city streets have become a growing concern for urban planners."),
                ("system", "Abandoned cows often cause traffic accidents and road blockages."),
                ("learner", "Many of these cows were abandoned by dairy farmers once they stopped producing milk."),
                ("system", "Responsible end-of-life care for cattle remains a contentious and unresolved issue."),
            ],
            [
                ("learner", "The cow shelter near our village provides care for over two hundred abandoned cattle."),
                ("system", "Running such shelters requires significant resources and dedicated volunteers."),
                ("learner", "If more people contributed to their upkeep, the shelters would not face constant funding shortages."),
                ("system", "Community support is vital for sustaining animal welfare organisations."),
            ],
        ],
        "upper_intermediate": [
            [
                ("learner", "The indigenous cow breed that was on the verge of decline has been revived through a conservation breeding programme."),
                ("system", "Native breeds are better adapted to local conditions and often more disease-resistant."),
                ("learner", "Scientists involved in the programme said that genetic diversity among indigenous breeds must be preserved urgently."),
                ("system", "Losing native genetic resources would limit future options for climate-resilient agriculture."),
            ],
            [
                ("learner", "A court ruling declared that transporting cattle across state borders without proper permits constitutes a punishable offence."),
                ("system", "Cattle transport regulations aim to prevent illegal slaughter and ensure animal welfare during transit."),
                ("learner", "However, critics argue that such restrictions have adversely affected legitimate livestock trade and farmer incomes."),
                ("system", "Balancing animal welfare, cultural sentiments, and economic livelihoods in cattle policy is extraordinarily complex."),
            ],
            [
                ("learner", "Dairy cooperatives modelled on the Amul success story are being replicated in several underserved districts."),
                ("system", "The cooperative model empowers small producers by giving them collective bargaining power."),
                ("learner", "Women-led cooperatives have been particularly effective in improving household incomes in rural areas."),
                ("system", "Empowering women in the dairy value chain creates ripple effects across health, education, and nutrition."),
            ],
        ],
        "advanced": [
            [
                ("learner", "Were the intersection of cultural reverence and economic utility in cattle management honestly examined, Indian dairy policy would be radically different."),
                ("system", "The gap between symbolic veneration and material treatment of cattle reveals deep contradictions in public discourse."),
                ("learner", "It is disingenuous to invoke cultural sanctity while simultaneously abandoning unproductive animals to suffer on the streets."),
                ("system", "Genuine respect for any living being demands consistency between professed values and actual practices."),
            ],
            [
                ("learner", "The methane emissions attributable to cattle farming present a significant challenge to India's climate commitments."),
                ("system", "Livestock contribute substantially to greenhouse gas emissions through enteric fermentation."),
                ("learner", "Addressing this requires not only technological interventions in feed management but also a broader conversation about consumption patterns."),
                ("system", "Climate-conscious agriculture must integrate emissions reduction with food security and livelihood protection."),
            ],
            [
                ("learner", "Had the dairy industry invested in value addition and quality assurance decades ago, Indian dairy products would command a stronger position in global markets."),
                ("system", "The dominance of the unorganised sector has historically limited quality standardisation and export potential."),
                ("learner", "It is imperative that the next phase of dairy development prioritise hygiene, traceability, and brand building alongside raw production volumes."),
                ("system", "Moving from quantity to quality is the defining transition that will determine the future competitiveness of Indian dairy."),
            ],
        ],
    },
}
