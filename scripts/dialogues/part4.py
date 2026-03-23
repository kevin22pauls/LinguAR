"""
Hand-crafted dialogues for COCO objects — Part 4.

Objects covered (19):
  dining table, toilet, tv, laptop, mouse, keyboard, cell phone,
  microwave, oven, toaster, sink, refrigerator, book, clock, vase,
  scissors, teddy bear, hair drier, toothbrush

Each object has 5 levels x 3 dialogues x 4 turns = 60 turns per object.
Total: 19 objects x 15 dialogues = 285 dialogues.
"""

DIALOGUES_PART4 = {
    # ------------------------------------------------------------------ #
    #  DINING TABLE                                                       #
    # ------------------------------------------------------------------ #
    "dining table": {
        "beginner": [
            [
                ("learner", "The dining table is very big."),
                ("system", "Yes, it is! How many people can sit there?"),
                ("learner", "Six people sit at this table."),
                ("system", "That is a big family table. Very nice!"),
            ],
            [
                ("learner", "I eat dinner at the table."),
                ("system", "That is a good habit. What do you eat?"),
                ("learner", "We eat rice and curry every day."),
                ("system", "Rice and curry is a delicious meal!"),
            ],
            [
                ("learner", "Please put plates on the table."),
                ("system", "Sure! How many plates do we need?"),
                ("learner", "We need four plates for dinner."),
                ("system", "I will set four plates right away."),
            ],
        ],
        "elementary": [
            [
                ("learner", "I am setting the dining table for lunch."),
                ("system", "That is very helpful. Are you putting out glasses too?"),
                ("learner", "Yes, I placed glasses next to every plate."),
                ("system", "Wonderful. The table looks ready for the family."),
            ],
            [
                ("learner", "My mother cleaned the table after breakfast."),
                ("system", "Did you help her with the cleaning?"),
                ("learner", "I am wiping the table with a wet cloth now."),
                ("system", "Good job! Keeping the table clean is important."),
            ],
            [
                ("learner", "We bought a new dining table last week."),
                ("system", "That is exciting! What does it look like?"),
                ("learner", "It is round and made of dark brown wood."),
                ("system", "A round wooden table sounds very beautiful."),
            ],
        ],
        "intermediate": [
            [
                ("learner", "I have always preferred eating at the dining table instead of on the sofa."),
                ("system", "That is a healthy habit. Does your family eat together often?"),
                ("learner", "If everyone is home by seven, we always eat together at the table."),
                ("system", "Family meals at the dining table are a wonderful tradition to keep."),
            ],
            [
                ("learner", "Our old dining table has been in the family for over twenty years."),
                ("system", "That is remarkable! It must have a lot of memories attached to it."),
                ("learner", "If we ever move to a new house, we would take this table with us."),
                ("system", "Some furniture carries sentimental value that money cannot replace."),
            ],
            [
                ("learner", "I have noticed that we talk more when we sit at the dining table."),
                ("system", "Shared meals encourage conversation. Do you discuss your day?"),
                ("learner", "Yes, my father would ask about school if he arrived home on time."),
                ("system", "That daily check-in over dinner strengthens family bonds."),
            ],
        ],
        "upper_intermediate": [
            [
                ("learner", "The dining table is often considered the heart of a household."),
                ("system", "That is a lovely way to put it. Why do you think that is?"),
                ("learner", "It is said that families who eat together tend to communicate better."),
                ("system", "Research supports that claim. Shared mealtimes improve children's wellbeing."),
            ],
            [
                ("learner", "The new dining table that was delivered yesterday barely fits in our kitchen."),
                ("system", "Did you measure the space before ordering it?"),
                ("learner", "We had been told by the shop that it would fit without any problems."),
                ("system", "That is frustrating. You might want to ask the store about an exchange."),
            ],
            [
                ("learner", "At my grandmother's house, the dining table is where all important decisions are made."),
                ("system", "That sounds like a powerful family tradition."),
                ("learner", "She believes that people who are fed well are more likely to think clearly."),
                ("system", "Your grandmother's wisdom about food and thought is quite insightful."),
            ],
        ],
        "advanced": [
            [
                ("learner", "Were it not for the dining table as a gathering point, many families might struggle to find time to connect."),
                ("system", "That is an astute observation about modern life. Do you think technology is partly to blame?"),
                ("learner", "I would argue that the decline of shared mealtimes correlates with the rise of screen-based entertainment."),
                ("system", "A compelling point. Reclaiming the dining table as a device-free zone could help reverse that trend."),
            ],
            [
                ("learner", "The dining table in our ancestral home is a hand-carved teak piece that dates back three generations."),
                ("system", "Heirloom furniture like that carries immense cultural significance."),
                ("learner", "It is essential that such artefacts be preserved, lest we lose tangible connections to our heritage."),
                ("system", "Absolutely. Material objects can anchor cultural memory in ways that photographs alone cannot."),
            ],
            [
                ("learner", "Sociologists have long maintained that the communal dining table fosters a sense of belonging and shared identity."),
                ("system", "Indeed. How do you see this playing out in Indian households specifically?"),
                ("learner", "In Tamil culture, the practice of sitting together for meals embodies respect, hierarchy, and hospitality all at once."),
                ("system", "That multifaceted role of the dining table beautifully illustrates how everyday objects encode cultural values."),
            ],
        ],
    },

    # ------------------------------------------------------------------ #
    #  TOILET                                                             #
    # ------------------------------------------------------------------ #
    "toilet": {
        "beginner": [
            [
                ("learner", "Where is the toilet, please?"),
                ("system", "It is at the end of the hallway."),
                ("learner", "Thank you. I will go now."),
                ("system", "You are welcome. It is the blue door."),
            ],
            [
                ("learner", "The school toilet is very clean today."),
                ("system", "That is good to hear! Clean toilets are important."),
                ("learner", "We should keep it clean always."),
                ("system", "Yes, everyone must do their part."),
            ],
            [
                ("learner", "I wash my hands after using the toilet."),
                ("system", "That is a very good habit. Do you use soap?"),
                ("learner", "Yes, I use soap and water every time."),
                ("system", "Excellent! That keeps you healthy and safe."),
            ],
        ],
        "elementary": [
            [
                ("learner", "Excuse me, is there a toilet nearby?"),
                ("system", "Yes, there is one on the ground floor near the library."),
                ("learner", "I went there yesterday but it was locked."),
                ("system", "It is open now. The janitor unlocked it this morning."),
            ],
            [
                ("learner", "The toilet in our classroom building is not working."),
                ("system", "Oh no! What happened to it?"),
                ("learner", "The flush was broken, so water was leaking everywhere."),
                ("system", "I will tell the school office so they can fix it soon."),
            ],
            [
                ("learner", "My father is installing a new toilet at home."),
                ("system", "That sounds like a big project. Is he doing it alone?"),
                ("learner", "No, a plumber is helping him with the work."),
                ("system", "A professional plumber will make sure everything works properly."),
            ],
        ],
        "intermediate": [
            [
                ("learner", "I think every school should have clean toilets for all students."),
                ("system", "That is an important issue. Why do you feel so strongly about it?"),
                ("learner", "If toilets are dirty, many students would avoid using them all day."),
                ("system", "You are right. Poor sanitation in schools affects attendance and health."),
            ],
            [
                ("learner", "The government has built new toilet blocks in rural schools across Tamil Nadu."),
                ("system", "That is a positive step. Have you seen any of these new facilities?"),
                ("learner", "Our school received one last year, and it has made a big difference."),
                ("system", "Access to clean sanitation facilities is a basic right for every student."),
            ],
            [
                ("learner", "I have read that many girls drop out of school because of poor toilet facilities."),
                ("system", "Sadly, that is true in many parts of India. What could be done?"),
                ("learner", "If more funds were allocated to school sanitation, attendance would improve."),
                ("system", "Investing in proper toilet facilities is investing in education itself."),
            ],
        ],
        "upper_intermediate": [
            [
                ("learner", "It is widely reported that inadequate sanitation facilities disproportionately affect girls in rural schools."),
                ("system", "That is a well-documented problem. What solutions have you come across?"),
                ("learner", "Several NGOs have been working to ensure that separate toilet blocks are built for boys and girls."),
                ("system", "Gender-separated facilities with proper maintenance are essential for retaining female students."),
            ],
            [
                ("learner", "The new toilet facility at our school was inaugurated by the district collector last month."),
                ("system", "That must have been a significant event for the school."),
                ("learner", "The teachers said that it had been requested for several years before it was finally approved."),
                ("system", "Persistent advocacy by the school community clearly paid off in the end."),
            ],
            [
                ("learner", "In many countries, public toilet facilities are maintained by automated cleaning systems."),
                ("system", "Self-cleaning technology does exist. Do you think it would work in Indian schools?"),
                ("learner", "While the technology is promising, it is believed that regular manual maintenance would be more practical here."),
                ("system", "A combination of technology and trained maintenance staff might be the most effective approach."),
            ],
        ],
        "advanced": [
            [
                ("learner", "The Swachh Bharat campaign has fundamentally altered public discourse around sanitation and toilet usage in India."),
                ("system", "It has indeed raised awareness. Do you think the behavioural change has been lasting?"),
                ("learner", "Although infrastructure has improved significantly, sustained behavioural change demands that communities internalise hygiene as a value rather than a mandate."),
                ("system", "That distinction between compliance and conviction is crucial for long-term public health outcomes."),
            ],
            [
                ("learner", "Were adequate sanitation to be universally available in Indian schools, the impact on educational outcomes would be profound."),
                ("system", "What evidence supports that connection between sanitation and academic performance?"),
                ("learner", "Studies have demonstrated that improved toilet facilities reduce absenteeism, particularly among adolescent girls, thereby narrowing the gender gap in education."),
                ("system", "The link between basic infrastructure and equitable access to education is one of the most compelling arguments for increased sanitation funding."),
            ],
            [
                ("learner", "It is imperative that urban planning incorporate accessible and well-maintained public toilets as a fundamental component of civic infrastructure."),
                ("system", "Many cities still treat public restrooms as an afterthought. What would you prioritise?"),
                ("learner", "I would insist that every new public space be designed with gender-neutral, wheelchair-accessible toilet facilities that meet international standards of hygiene."),
                ("system", "Inclusive design from the outset is far more cost-effective than retrofitting, and it signals a society's commitment to dignity for all citizens."),
            ],
        ],
    },

    # ------------------------------------------------------------------ #
    #  TV                                                                 #
    # ------------------------------------------------------------------ #
    "tv": {
        "beginner": [
            [
                ("learner", "I watch TV after school every day."),
                ("system", "What do you like to watch on TV?"),
                ("learner", "I like cartoons and animal shows."),
                ("system", "Animal shows are fun and you learn a lot!"),
            ],
            [
                ("learner", "The TV in our class is very big."),
                ("system", "Does the teacher use it for lessons?"),
                ("learner", "Yes, we watch videos about science."),
                ("system", "Learning with videos makes science more exciting!"),
            ],
            [
                ("learner", "Please turn off the TV now."),
                ("system", "Why? Is it time for something else?"),
                ("learner", "Yes, I need to do my homework."),
                ("system", "That is a responsible choice. Good for you!"),
            ],
        ],
        "elementary": [
            [
                ("learner", "I was watching TV when the power went off."),
                ("system", "Oh no! What were you watching at that time?"),
                ("learner", "I was watching a cricket match and India was winning."),
                ("system", "That must have been so frustrating. Did the power come back soon?"),
            ],
            [
                ("learner", "My parents bought a new TV for the living room."),
                ("system", "That is exciting! Is it a smart TV?"),
                ("learner", "Yes, we can watch YouTube and movies on it."),
                ("system", "Smart TVs are great for streaming all kinds of shows."),
            ],
            [
                ("learner", "The TV remote is not working properly today."),
                ("system", "Have you tried changing the batteries?"),
                ("learner", "I changed them yesterday but it still does not work."),
                ("system", "Maybe the remote needs to be paired again. Check the manual."),
            ],
        ],
        "intermediate": [
            [
                ("learner", "I have stopped watching TV during exam week to focus on my studies."),
                ("system", "That takes real discipline. Has it helped your concentration?"),
                ("learner", "If I did not have the TV as a distraction, I would finish my revision much faster."),
                ("system", "Recognising distractions is the first step toward managing your time effectively."),
            ],
            [
                ("learner", "Our teacher has suggested that we watch English news on TV every evening."),
                ("system", "That is excellent advice for language learners. Have you tried it?"),
                ("learner", "I have been watching the English news for two weeks and my listening has improved."),
                ("system", "Consistent exposure to spoken English through TV is one of the best ways to improve comprehension."),
            ],
            [
                ("learner", "If there were no TV at home, we would probably read more books."),
                ("system", "That is an interesting thought. Do you think TV is entirely negative?"),
                ("learner", "Not at all. Documentaries have taught me things I never learned in school."),
                ("system", "Balance is the key. TV can educate just as much as it can distract."),
            ],
        ],
        "upper_intermediate": [
            [
                ("learner", "It is often argued that television has a negative influence on children's academic performance."),
                ("system", "That is a common concern. What is your perspective?"),
                ("learner", "While excessive screen time is known to reduce attention spans, curated educational content can actually enhance learning."),
                ("system", "The distinction between passive consumption and active, guided viewing is crucial."),
            ],
            [
                ("learner", "The TV in our school hall was donated by an alumni association last year."),
                ("system", "Alumni contributions make a real difference. How has the school used it?"),
                ("learner", "It has been used for screening educational films that are recommended by the state board."),
                ("system", "Integrating multimedia into classroom instruction is a proven way to engage students."),
            ],
            [
                ("learner", "My younger brother was told by the doctor to limit his TV time to one hour a day."),
                ("system", "Doctors do recommend screen time limits for children. Was he watching too much?"),
                ("learner", "He had been spending nearly four hours a day in front of the TV, which was affecting his eyesight."),
                ("system", "Prolonged screen exposure can strain young eyes. Following the doctor's advice is wise."),
            ],
        ],
        "advanced": [
            [
                ("learner", "The evolution of television from a unidirectional broadcast medium to an interactive, on-demand platform has fundamentally reshaped how content is consumed."),
                ("system", "Absolutely. How do you think this shift has affected younger audiences in India?"),
                ("learner", "I would contend that the proliferation of streaming services has fragmented shared cultural experiences that network television once provided."),
                ("system", "That fragmentation paradox is fascinating — more choice, yet less communal viewing. It mirrors broader individualistic trends in society."),
            ],
            [
                ("learner", "Were television purely an entertainment medium, its societal impact might be less contentious."),
                ("system", "What additional roles do you see TV playing beyond entertainment?"),
                ("learner", "Television functions as a vehicle for political persuasion, cultural normalisation, and ideological reinforcement, which necessitates critical media literacy among viewers."),
                ("system", "Your analysis underscores why media education should be embedded in school curricula from an early age."),
            ],
            [
                ("learner", "It is essential that parents model healthy television habits rather than merely imposing restrictions on their children."),
                ("system", "Modelling behaviour is indeed more effective than prohibition. Why do you think parents struggle with this?"),
                ("learner", "Adults themselves have become habituated to background television, making it difficult to advocate for screen-free time without appearing hypocritical."),
                ("system", "That tension between parental advice and parental practice is a growing challenge in the age of ubiquitous screens."),
            ],
        ],
    },

    # ------------------------------------------------------------------ #
    #  LAPTOP                                                             #
    # ------------------------------------------------------------------ #
    "laptop": {
        "beginner": [
            [
                ("learner", "I use a laptop for my homework."),
                ("system", "That is great! What subject do you work on?"),
                ("learner", "I type my English essays on it."),
                ("system", "Typing helps you practice spelling too!"),
            ],
            [
                ("learner", "The laptop is on the teacher's desk."),
                ("system", "Does the teacher use it in every class?"),
                ("learner", "Yes, she shows us pictures and videos."),
                ("system", "That makes learning more interesting for everyone!"),
            ],
            [
                ("learner", "My laptop has a blue cover on it."),
                ("system", "A cover protects it from scratches."),
                ("learner", "I carry it to school in my bag."),
                ("system", "Be careful with it. Laptops are delicate."),
            ],
        ],
        "elementary": [
            [
                ("learner", "I am learning to type faster on the laptop."),
                ("system", "That is a useful skill. How fast can you type now?"),
                ("learner", "I typed twenty words per minute in the test yesterday."),
                ("system", "That is a good start! Keep practising and you will improve quickly."),
            ],
            [
                ("learner", "The laptop in the computer lab stopped working this morning."),
                ("system", "What happened to it? Did you report the problem?"),
                ("learner", "The screen was flickering, so the teacher called the technician."),
                ("system", "A flickering screen usually means the display cable needs checking."),
            ],
            [
                ("learner", "My sister was using the laptop to attend her online class."),
                ("system", "Online classes have become very common now."),
                ("learner", "She needed the laptop all morning, so I read a book instead."),
                ("system", "Sharing devices requires patience, and reading is always a good choice."),
            ],
        ],
        "intermediate": [
            [
                ("learner", "I have been saving my pocket money to buy a laptop for college."),
                ("system", "That is very responsible of you. How much have you saved so far?"),
                ("learner", "If I save for six more months, I would have enough for a basic model."),
                ("system", "A basic laptop is all you need to start. You can always upgrade later."),
            ],
            [
                ("learner", "Our school has started a programme where every student gets a laptop."),
                ("system", "That is a wonderful initiative. How has it changed your learning?"),
                ("learner", "We have started using educational apps that were not available to us before."),
                ("system", "Digital tools can open up entirely new ways of understanding difficult subjects."),
            ],
            [
                ("learner", "If I had a laptop with better memory, I could run more programmes at once."),
                ("system", "How much memory does your current laptop have?"),
                ("learner", "It only has four gigabytes, which is barely enough for basic tasks."),
                ("system", "Upgrading the memory is often cheaper than buying a whole new laptop."),
            ],
        ],
        "upper_intermediate": [
            [
                ("learner", "The laptop that was assigned to me at school has several software restrictions imposed by the IT department."),
                ("system", "Schools often restrict access to prevent misuse. Does it limit your work?"),
                ("learner", "While I understand the reasoning, certain educational websites are unnecessarily blocked by the firewall."),
                ("system", "You could submit a request to the IT team to whitelist specific educational sites."),
            ],
            [
                ("learner", "It has been reported that prolonged laptop use without proper posture leads to chronic back pain."),
                ("system", "Ergonomics is often overlooked by students. How do you manage?"),
                ("learner", "I was advised by the school nurse to use a laptop stand and take breaks every thirty minutes."),
                ("system", "Following ergonomic guidelines now will prevent serious health issues in the future."),
            ],
            [
                ("learner", "Our teacher mentioned that laptops in classrooms are a double-edged sword."),
                ("system", "What did she mean by that?"),
                ("learner", "She explained that while laptops enhance research capabilities, they also provide distractions that are difficult to monitor."),
                ("system", "Balancing access with accountability is one of the biggest challenges in modern education."),
            ],
        ],
        "advanced": [
            [
                ("learner", "The digital divide in India is starkly illustrated by the disparity in laptop ownership between urban and rural students."),
                ("system", "That divide became even more visible during the pandemic. What solutions do you propose?"),
                ("learner", "I believe it is imperative that state governments subsidise laptops for students from economically weaker sections, lest the gap widen irreversibly."),
                ("system", "Subsidies coupled with digital literacy training would ensure the devices are used effectively rather than merely distributed."),
            ],
            [
                ("learner", "Were laptops to be integrated into the curriculum from primary school, students would develop computational thinking far earlier."),
                ("system", "Early exposure to technology is beneficial, but what about the associated costs?"),
                ("learner", "The long-term economic returns of a digitally literate workforce far outweigh the upfront investment in educational technology infrastructure."),
                ("system", "That macroeconomic argument is persuasive, though implementation challenges at the grassroots level should not be underestimated."),
            ],
            [
                ("learner", "The notion that a laptop alone can transform educational outcomes is a techno-utopian fallacy that ignores pedagogical fundamentals."),
                ("system", "A provocative claim. What do you see as the missing piece?"),
                ("learner", "Without adequately trained teachers who can meaningfully integrate technology into their instruction, laptops become expensive distractions rather than educational tools."),
                ("system", "Teacher training is indeed the linchpin. Technology amplifies existing teaching quality — it does not substitute for it."),
            ],
        ],
    },

    # ------------------------------------------------------------------ #
    #  MOUSE                                                              #
    # ------------------------------------------------------------------ #
    "mouse": {
        "beginner": [
            [
                ("learner", "I click the mouse to open games."),
                ("system", "Which games do you like to play?"),
                ("learner", "I play a painting game on the computer."),
                ("system", "Painting games are fun and creative!"),
            ],
            [
                ("learner", "The mouse is next to the keyboard."),
                ("system", "That is where it usually goes. Can you use it?"),
                ("learner", "Yes, I move it with my right hand."),
                ("system", "Good! Most people use their right hand too."),
            ],
            [
                ("learner", "This mouse has two buttons on top."),
                ("system", "Do you know what each button does?"),
                ("learner", "The left button is for clicking things."),
                ("system", "That is correct! The right button opens menus."),
            ],
        ],
        "elementary": [
            [
                ("learner", "The mouse in the computer lab is not moving smoothly."),
                ("system", "It might need cleaning. Is there dust underneath?"),
                ("learner", "I turned it over and found dirt on the sensor."),
                ("system", "Cleaning the sensor should fix the problem right away."),
            ],
            [
                ("learner", "My teacher showed me how to double-click the mouse."),
                ("system", "Double-clicking opens files and folders. Was it easy?"),
                ("learner", "It was difficult at first, but I practised many times."),
                ("system", "Practice makes perfect. You will get faster with time."),
            ],
            [
                ("learner", "I am using a wireless mouse for the first time."),
                ("system", "Wireless mice are convenient. Do you like it?"),
                ("learner", "Yes, but I forgot to charge it and it stopped working."),
                ("system", "Always charge it at night so it is ready for the next day."),
            ],
        ],
        "intermediate": [
            [
                ("learner", "I have always found it easier to use a mouse than a touchpad for precise work."),
                ("system", "Many people prefer the mouse for accuracy. What kind of work do you do?"),
                ("learner", "If I need to select small text or draw diagrams, the mouse gives me better control."),
                ("system", "An external mouse is definitely superior for tasks that require fine motor precision."),
            ],
            [
                ("learner", "The ergonomic mouse my father bought has reduced the pain in his wrist."),
                ("system", "Ergonomic designs can make a big difference. What makes it different?"),
                ("learner", "It has a vertical shape so his hand rests in a more natural position."),
                ("system", "Vertical mice reduce strain on the wrist tendons. That was a smart purchase."),
            ],
            [
                ("learner", "If the mouse cursor keeps freezing, there might be a problem with the driver."),
                ("system", "That is a good troubleshooting instinct. Have you tried updating the driver?"),
                ("learner", "I have reinstalled it twice, but the issue seems to be with the USB port instead."),
                ("system", "Try plugging the mouse into a different port to confirm if that is the cause."),
            ],
        ],
        "upper_intermediate": [
            [
                ("learner", "The computer mouse is often cited as one of the most transformative inventions in human-computer interaction."),
                ("system", "Douglas Engelbart's 1964 prototype changed everything. Why do you find it significant?"),
                ("learner", "It is believed that the mouse made computers accessible to people who had no programming knowledge."),
                ("system", "By enabling graphical interfaces, the mouse effectively democratised computing for the general public."),
            ],
            [
                ("learner", "Students were told by the IT instructor to avoid eating near the mouse and keyboard."),
                ("system", "Crumbs and spills can damage equipment. Do students follow the rule?"),
                ("learner", "Most students comply, although a few have been caught bringing snacks into the lab."),
                ("system", "Consistent enforcement is necessary to protect shared equipment from unnecessary damage."),
            ],
            [
                ("learner", "The gaming mouse that my friend uses has twelve programmable buttons on the side."),
                ("system", "Gaming peripherals have become very advanced. Does he really need all twelve?"),
                ("learner", "He claims that each button is assigned to a specific action, which gives him an advantage in competitive games."),
                ("system", "Customisable peripherals do offer measurable performance benefits for serious gamers."),
            ],
        ],
        "advanced": [
            [
                ("learner", "As touchscreens and voice interfaces proliferate, some futurists have predicted the obsolescence of the computer mouse."),
                ("system", "Yet the mouse persists. Why do you think it has survived these challenges?"),
                ("learner", "The mouse offers a combination of precision, speed, and tactile feedback that neither touch nor voice can replicate for productivity tasks."),
                ("system", "That resilience speaks to the enduring value of well-designed input devices that align with human motor capabilities."),
            ],
            [
                ("learner", "Were one to design a computer mouse from scratch today, the priorities would likely include sustainability and repairability."),
                ("system", "Interesting. How would that differ from current manufacturing practices?"),
                ("learner", "Most mice are designed with planned obsolescence in mind, whereas a modular design would allow users to replace individual components rather than discarding the entire device."),
                ("system", "The right-to-repair movement is gradually pushing manufacturers toward exactly that kind of modular, sustainable design philosophy."),
            ],
            [
                ("learner", "The evolution from mechanical ball mice to optical and laser sensors exemplifies how incremental innovation can transform a mature product category."),
                ("system", "Each generation addressed specific limitations. What do you see as the next frontier?"),
                ("learner", "I anticipate that haptic feedback and adaptive sensitivity will converge to create mice that dynamically respond to the user's context and intent."),
                ("system", "Context-aware peripherals represent a compelling direction, blurring the line between passive tools and intelligent assistants."),
            ],
        ],
    },

    # ------------------------------------------------------------------ #
    #  KEYBOARD                                                           #
    # ------------------------------------------------------------------ #
    "keyboard": {
        "beginner": [
            [
                ("learner", "I can see the keyboard on the desk."),
                ("system", "Can you find the letter A on it?"),
                ("learner", "Yes, it is on the left side."),
                ("system", "Good job! Now try to type your name."),
            ],
            [
                ("learner", "The keyboard has many keys on it."),
                ("system", "Do you know how many keys there are?"),
                ("learner", "My teacher said there are about one hundred."),
                ("system", "That is right! There are letters, numbers, and special keys."),
            ],
            [
                ("learner", "I press the space bar with my thumb."),
                ("system", "The space bar is the longest key. What does it do?"),
                ("learner", "It puts a space between two words."),
                ("system", "Exactly! You already know the basics of typing."),
            ],
        ],
        "elementary": [
            [
                ("learner", "I am practising typing on the keyboard every day."),
                ("system", "That is wonderful! Are you using all ten fingers?"),
                ("learner", "My computer teacher taught me the home row keys yesterday."),
                ("system", "The home row is the foundation of touch typing. Keep practising!"),
            ],
            [
                ("learner", "One key on the school keyboard is stuck and will not press down."),
                ("system", "That happens sometimes. Which key is it?"),
                ("learner", "It is the Enter key, and I cannot start a new line without it."),
                ("system", "Tell the lab assistant. A stuck key can usually be fixed quickly."),
            ],
            [
                ("learner", "I spilled water on the keyboard by accident last week."),
                ("system", "Oh no! Did it stop working after that?"),
                ("learner", "Some keys stopped working, so we had to replace it."),
                ("system", "Liquids and electronics do not mix. Try to keep drinks away from your desk."),
            ],
        ],
        "intermediate": [
            [
                ("learner", "I have memorised the keyboard layout so I can type without looking down."),
                ("system", "That is called touch typing. How long did it take you to learn?"),
                ("learner", "If I had started practising earlier, I would have learned it in a few weeks."),
                ("system", "Better late than never. Touch typing is a skill that benefits you for life."),
            ],
            [
                ("learner", "The mechanical keyboard my brother uses makes a loud clicking sound."),
                ("system", "Mechanical keyboards are popular among typists and gamers. Does the noise bother you?"),
                ("learner", "It used to bother me, but I have gotten accustomed to the sound over time."),
                ("system", "Some people find the clicking satisfying. There are also quieter mechanical switches available."),
            ],
            [
                ("learner", "If the keyboard shortcuts were taught in school, students would work much faster on computers."),
                ("system", "Keyboard shortcuts are incredibly useful. Which ones do you know?"),
                ("learner", "I know how to copy, paste, and undo, but there are many more that I want to learn."),
                ("system", "Learning even a few more shortcuts each week can dramatically speed up your workflow."),
            ],
        ],
        "upper_intermediate": [
            [
                ("learner", "The QWERTY keyboard layout was originally designed to prevent typewriter keys from jamming."),
                ("system", "That is correct. Do you think we should switch to a more efficient layout?"),
                ("learner", "Although alternatives like Dvorak have been shown to be faster, the cost of retraining billions of users makes a transition impractical."),
                ("system", "That is a classic example of path dependency, where historical choices constrain future options."),
            ],
            [
                ("learner", "Students in our school were taught that proper keyboard posture prevents repetitive strain injury."),
                ("system", "RSI is a serious concern for frequent computer users. What did the instructor recommend?"),
                ("learner", "We were advised to keep our wrists straight and to position the keyboard at elbow height."),
                ("system", "Those guidelines, combined with regular breaks, significantly reduce the risk of long-term injury."),
            ],
            [
                ("learner", "It is fascinating that a single keyboard can support multiple language scripts through software input methods."),
                ("system", "Indeed. Do you type in Tamil as well as English?"),
                ("learner", "I have been using a Tamil phonetic input method that maps English keystrokes to Tamil characters."),
                ("system", "Phonetic input methods make multilingual typing accessible without requiring a separate physical keyboard."),
            ],
        ],
        "advanced": [
            [
                ("learner", "The persistence of the physical keyboard in an era of voice recognition and gesture control speaks to the irreplaceable precision of tactile input."),
                ("system", "Voice and gesture each have advantages, yet they fall short in certain contexts. Which ones?"),
                ("learner", "In environments requiring silent operation, privacy, or high-throughput text entry, the keyboard remains unmatched by any alternative input modality."),
                ("system", "That functional niche ensures the keyboard's relevance well into the foreseeable future."),
            ],
            [
                ("learner", "Were the Indian government to mandate Tamil-script keyboard labelling on all devices sold domestically, it could significantly boost digital literacy in regional languages."),
                ("system", "An interesting policy proposal. What challenges do you foresee?"),
                ("learner", "Manufacturers would resist the additional cost, and standardising a single Tamil layout from the many competing options would itself be politically fraught."),
                ("system", "The tension between linguistic inclusion and commercial pragmatism is a recurring theme in technology policy across multilingual nations."),
            ],
            [
                ("learner", "The keyboard serves as a mediating technology between thought and text, and its design subtly shapes the way we compose written language."),
                ("system", "That is a profound observation. Can you give an example of this shaping effect?"),
                ("learner", "The ease of deletion and rearrangement on a keyboard encourages iterative writing, whereas the permanence of pen on paper historically demanded more deliberate composition."),
                ("system", "Your insight aligns with research showing that digital tools have shifted writing from a linear to an inherently recursive process."),
            ],
        ],
    },

    # ------------------------------------------------------------------ #
    #  CELL PHONE                                                         #
    # ------------------------------------------------------------------ #
    "cell phone": {
        "beginner": [
            [
                ("learner", "I can see a cell phone on the table."),
                ("system", "Whose cell phone is it? Do you know?"),
                ("learner", "It is my mother's cell phone."),
                ("system", "She must be looking for it. Let us return it."),
            ],
            [
                ("learner", "I call my grandmother on the phone."),
                ("system", "That is so sweet. How often do you call her?"),
                ("learner", "I call her every Sunday evening."),
                ("system", "She must be very happy to hear from you!"),
            ],
            [
                ("learner", "My cell phone has a small screen."),
                ("system", "Is it a new phone or an old one?"),
                ("learner", "It is my father's old phone."),
                ("system", "Old phones still work well for calls and messages!"),
            ],
        ],
        "elementary": [
            [
                ("learner", "I was playing a game on my cell phone during lunch."),
                ("system", "Are you allowed to use phones during school hours?"),
                ("learner", "No, the teacher collected it and gave it back after school."),
                ("system", "It is best to follow the school rules about phone use."),
            ],
            [
                ("learner", "My cell phone battery died while I was talking to my friend."),
                ("system", "That is annoying! Did you call your friend back?"),
                ("learner", "I charged it for ten minutes and then called him again."),
                ("system", "It is a good idea to charge your phone before it runs out completely."),
            ],
            [
                ("learner", "I am using my cell phone to take pictures of flowers."),
                ("system", "Photography is a great hobby. Are the pictures coming out well?"),
                ("learner", "Some are blurry because my hands were shaking."),
                ("system", "Try holding the phone with both hands and keeping your elbows steady."),
            ],
        ],
        "intermediate": [
            [
                ("learner", "I have been using my cell phone to listen to English podcasts every morning."),
                ("system", "That is an excellent way to improve your listening skills. Which podcasts do you enjoy?"),
                ("learner", "If I could find podcasts with slower speech, it would help me understand better."),
                ("system", "Many language-learning podcasts offer slow and normal speed versions of each episode."),
            ],
            [
                ("learner", "Our school has banned cell phones during class hours to reduce distractions."),
                ("system", "Many schools have similar policies. Do you agree with the ban?"),
                ("learner", "I think it is fair because most students would use their phones for games instead of learning."),
                ("system", "Self-regulation is difficult, so clear rules help students focus during school hours."),
            ],
            [
                ("learner", "If my cell phone had more storage, I could download all my textbooks as digital copies."),
                ("system", "Digital textbooks are convenient and lighter than carrying physical books."),
                ("learner", "I have already downloaded three books, but the phone ran out of space."),
                ("system", "You might try using a memory card or cloud storage to free up space."),
            ],
        ],
        "upper_intermediate": [
            [
                ("learner", "It is estimated that the average teenager spends over four hours a day on their cell phone."),
                ("system", "That is a striking figure. Do you think you spend that much time on yours?"),
                ("learner", "I was shocked to discover that my screen time report showed nearly five hours of daily usage last week."),
                ("system", "Awareness is the first step. Setting daily limits through the phone's built-in tools can help reduce screen time."),
            ],
            [
                ("learner", "Cell phones are now being used as learning tools in several progressive schools across India."),
                ("system", "That is a shift from the traditional view of phones as distractions. How are they being used?"),
                ("learner", "Students are given structured assignments that require them to use specific educational apps during class."),
                ("system", "When phone usage is guided by clear pedagogical goals, it can genuinely enhance the learning experience."),
            ],
            [
                ("learner", "My grandfather was told by the doctor to keep a cell phone with him at all times in case of an emergency."),
                ("system", "For elderly people living alone, a phone can be a lifeline."),
                ("learner", "We have programmed the emergency numbers so that he only needs to press one button to call for help."),
                ("system", "That is a thoughtful and practical arrangement for his safety."),
            ],
        ],
        "advanced": [
            [
                ("learner", "The cell phone has evolved from a communication device into an indispensable extension of human cognition and social identity."),
                ("system", "That is a powerful framing. Could you elaborate on the cognitive extension aspect?"),
                ("learner", "We have effectively outsourced memory, navigation, and even emotional regulation to our phones, which raises questions about what happens when that external scaffold is removed."),
                ("system", "The concept of cognitive offloading is well documented in psychology, and your point about dependency merits serious reflection."),
            ],
            [
                ("learner", "Were cell phone manufacturers to prioritise durability and repairability over planned obsolescence, the environmental impact of electronic waste would be substantially reduced."),
                ("system", "E-waste is a growing crisis. Do you see any movement in that direction?"),
                ("learner", "The European Union's recent legislation mandating replaceable batteries and standardised charging ports suggests that regulatory pressure may succeed where market forces have failed."),
                ("system", "Regulatory intervention often serves as the catalyst for industry-wide change when voluntary standards prove insufficient."),
            ],
            [
                ("learner", "It is incumbent upon educators to teach students not merely how to use cell phones but how to critically evaluate the information they encounter on these devices."),
                ("system", "Digital literacy and critical thinking are indeed essential. How would you integrate this into the curriculum?"),
                ("learner", "I would propose a dedicated media literacy module that requires students to identify misinformation, analyse source credibility, and understand algorithmic content curation."),
                ("system", "Such a module would equip students with the intellectual tools to navigate an information landscape that is growing more complex by the day."),
            ],
        ],
    },

    # ------------------------------------------------------------------ #
    #  MICROWAVE                                                          #
    # ------------------------------------------------------------------ #
    "microwave": {
        "beginner": [
            [
                ("learner", "The microwave is in the kitchen."),
                ("system", "What do you use the microwave for?"),
                ("learner", "I heat my milk in the microwave."),
                ("system", "Warm milk is nice! Be careful, it gets hot."),
            ],
            [
                ("learner", "Please do not put metal inside the microwave."),
                ("system", "That is very important! Do you know why?"),
                ("learner", "My mother said metal can cause a fire."),
                ("system", "She is right. Metal and microwaves are dangerous together."),
            ],
            [
                ("learner", "The microwave makes a beeping sound."),
                ("system", "What does the beeping mean?"),
                ("learner", "It means the food is ready to eat."),
                ("system", "Correct! The beep tells you the timer is done."),
            ],
        ],
        "elementary": [
            [
                ("learner", "I am heating leftover rice in the microwave for lunch."),
                ("system", "That is quick and easy. How long do you set the timer?"),
                ("learner", "I set it for two minutes, and the rice came out perfectly warm."),
                ("system", "Two minutes is usually just right for a bowl of rice."),
            ],
            [
                ("learner", "My mother taught me how to use the microwave safely."),
                ("system", "Safety is important. What rules did she teach you?"),
                ("learner", "She told me to always cover the food and never run it while empty."),
                ("system", "Those are excellent rules. Running it empty can damage the microwave."),
            ],
            [
                ("learner", "The microwave stopped working yesterday in the middle of cooking."),
                ("system", "That is inconvenient. What do you think happened?"),
                ("learner", "My father checked and found that the fuse had blown."),
                ("system", "A blown fuse is usually an easy fix. Hopefully it is working again soon."),
            ],
        ],
        "intermediate": [
            [
                ("learner", "I have learned that microwaves heat food by vibrating water molecules inside it."),
                ("system", "That is correct! Did you learn that in science class?"),
                ("learner", "Yes, and if the food has no water content, the microwave would not heat it effectively."),
                ("system", "Exactly. That is why dry foods sometimes heat unevenly in a microwave."),
            ],
            [
                ("learner", "Some people believe that microwaves destroy all the nutrients in food."),
                ("system", "That is a common myth. What have you found in your research?"),
                ("learner", "Studies have shown that microwaving actually preserves more nutrients than boiling because of the shorter cooking time."),
                ("system", "You are right. The brief exposure to heat is actually gentler on vitamins than prolonged cooking."),
            ],
            [
                ("learner", "If we had bought a microwave with a grill function, we could make crispy snacks at home."),
                ("system", "Convection microwaves can do that. Are you thinking of upgrading?"),
                ("learner", "My mother has been considering it since our current one can only reheat food."),
                ("system", "A convection microwave offers the best of both worlds — quick reheating and proper cooking."),
            ],
        ],
        "upper_intermediate": [
            [
                ("learner", "The microwave oven was reportedly invented by accident when an engineer noticed that his chocolate bar melted near a radar device."),
                ("system", "Percy Spencer and the magnetron — a classic accidental discovery. Why does that story interest you?"),
                ("learner", "It illustrates how many of the technologies we take for granted were not deliberately designed but discovered through unexpected observations."),
                ("system", "Serendipity in science is a fascinating topic. Curiosity and alertness turn accidents into inventions."),
            ],
            [
                ("learner", "In many Indian households, the microwave is used primarily for reheating rather than cooking from scratch."),
                ("system", "That is an interesting cultural observation. Why do you think that is?"),
                ("learner", "It has been suggested that Indian cooking, with its emphasis on slow-cooked spices and layered flavours, does not lend itself well to microwave preparation."),
                ("system", "The mismatch between microwave speed and the complexity of Indian cuisine is a compelling explanation."),
            ],
            [
                ("learner", "Parents are often warned that children should not operate the microwave without adult supervision."),
                ("system", "Hot liquids and steam can cause burns. At what age do you think children can use it safely?"),
                ("learner", "Once a child has been taught the safety rules and is tall enough to reach the controls, supervised use from age ten seems reasonable."),
                ("system", "Gradual, supervised introduction to kitchen appliances builds both confidence and responsibility."),
            ],
        ],
        "advanced": [
            [
                ("learner", "The microwave oven epitomises the twentieth-century ethos of convenience at the expense of culinary craftsmanship."),
                ("system", "A provocative view. Do you see convenience and quality as inherently opposed?"),
                ("learner", "Not necessarily, but the cultural shift toward speed over savour has arguably diminished the intergenerational transmission of traditional cooking knowledge."),
                ("system", "Your observation about the erosion of culinary heritage through technological convenience resonates with broader debates about tradition and modernity."),
            ],
            [
                ("learner", "Were microwave technology to be redesigned with energy efficiency as the primary criterion, the environmental footprint of domestic cooking could be reduced considerably."),
                ("system", "Current microwaves are already more efficient than conventional ovens. What improvements do you envision?"),
                ("learner", "Inverter technology and adaptive power systems that modulate energy output based on food volume and density could eliminate the wasteful cycling of conventional magnetrons."),
                ("system", "Precision energy delivery is already emerging in premium models, and its wider adoption would indeed yield significant aggregate energy savings."),
            ],
            [
                ("learner", "It is essential that consumer education accompany the sale of microwave ovens, particularly regarding the safe use of plastics and the avoidance of superheated liquids."),
                ("system", "Superheating is a genuine hazard that few users are aware of. How would you address this gap?"),
                ("learner", "Manufacturers should be mandated to include clear, multilingual safety instructions prominently on the appliance itself, rather than burying them in seldom-read manuals."),
                ("system", "On-device labelling in local languages would be especially impactful in a linguistically diverse market like India."),
            ],
        ],
    },

    # ------------------------------------------------------------------ #
    #  OVEN                                                               #
    # ------------------------------------------------------------------ #
    "oven": {
        "beginner": [
            [
                ("learner", "The oven is very hot right now."),
                ("system", "Be careful! You must not touch it."),
                ("learner", "I will wait until it cools down."),
                ("system", "That is very smart and safe of you."),
            ],
            [
                ("learner", "My mother bakes cakes in the oven."),
                ("system", "That sounds delicious! What kind of cakes?"),
                ("learner", "She makes chocolate cake for my birthday."),
                ("system", "A homemade chocolate cake is the best birthday treat!"),
            ],
            [
                ("learner", "We do not have an oven at home."),
                ("system", "Many Indian homes cook on a stove instead."),
                ("learner", "My aunt has an oven in her kitchen."),
                ("system", "Maybe you can bake something together at her house!"),
            ],
        ],
        "elementary": [
            [
                ("learner", "My sister is learning to bake cookies in the oven."),
                ("system", "That is exciting! What kind of cookies is she making?"),
                ("learner", "She made butter cookies yesterday and they tasted wonderful."),
                ("system", "Homemade cookies always taste better than store-bought ones."),
            ],
            [
                ("learner", "I watched my mother set the oven to the right temperature."),
                ("system", "Getting the temperature right is important for baking."),
                ("learner", "She heated it to one hundred and eighty degrees before putting the cake in."),
                ("system", "Preheating the oven ensures the cake bakes evenly from the start."),
            ],
            [
                ("learner", "The oven door was stuck and we could not open it."),
                ("system", "That sounds worrying. What happened next?"),
                ("learner", "My father used a cloth to pull it open after it cooled down."),
                ("system", "Heat can cause the door to expand. Waiting for it to cool was the right decision."),
            ],
        ],
        "intermediate": [
            [
                ("learner", "I have been watching baking tutorials online and I want to try using the oven myself."),
                ("system", "That is a great way to learn! What do you want to bake first?"),
                ("learner", "If I start with something simple like bread rolls, I would build my confidence gradually."),
                ("system", "Bread rolls are an excellent starting point. They teach you about dough, timing, and temperature."),
            ],
            [
                ("learner", "Our school has an oven in the home science lab that we use for cooking classes."),
                ("system", "Practical cooking experience is valuable. What have you made in class so far?"),
                ("learner", "We have baked muffins and a simple pizza, and both turned out quite well."),
                ("system", "Hands-on baking classes teach patience, measurement, and teamwork all at once."),
            ],
            [
                ("learner", "If ovens were more affordable in India, more families would try baking at home."),
                ("system", "Price is definitely a barrier. Are there affordable options available now?"),
                ("learner", "Small tabletop ovens have become cheaper, and I have seen many families buying them recently."),
                ("system", "The growing popularity of home baking in India is making ovens more accessible to the middle class."),
            ],
        ],
        "upper_intermediate": [
            [
                ("learner", "The clay tandoor can be considered the traditional Indian equivalent of the Western oven."),
                ("system", "That is an insightful comparison. How do they differ in function?"),
                ("learner", "While both use radiant heat, the tandoor is designed for much higher temperatures and imparts a distinctive smoky flavour."),
                ("system", "The flavour profile of tandoor cooking is indeed irreplaceable, which is why it remains central to North Indian cuisine."),
            ],
            [
                ("learner", "It has been observed that baking as a hobby surged in India during the pandemic lockdowns."),
                ("system", "Social media was filled with banana bread and sourdough. Did your family participate in the trend?"),
                ("learner", "My mother, who had never baked before, was inspired by YouTube videos and bought an oven during that period."),
                ("system", "The pandemic turned many reluctant cooks into enthusiastic bakers, and the habit seems to have persisted."),
            ],
            [
                ("learner", "Children should be taught by parents how to use the oven safely before they are allowed to operate it independently."),
                ("system", "Supervised learning is essential. What safety rules would you emphasise?"),
                ("learner", "Using oven mitts, never leaving the oven unattended, and keeping flammable materials away are the three rules I would prioritise."),
                ("system", "Those three rules form a solid foundation for safe oven use at any age."),
            ],
        ],
        "advanced": [
            [
                ("learner", "The adoption of the conventional oven in Indian households represents a fascinating case study in the globalisation of culinary technology."),
                ("system", "Indian cuisine evolved around stovetop and tandoor cooking. How has the oven been adapted?"),
                ("learner", "Rather than replacing traditional methods, the oven has been assimilated to create fusion dishes — tandoori chicken in a convection oven, for instance — that bridge cultural culinary boundaries."),
                ("system", "That adaptive integration, rather than wholesale replacement, reflects the resilience and creativity of Indian culinary traditions."),
            ],
            [
                ("learner", "Were energy-efficient induction ovens to become the standard, the carbon footprint of domestic cooking could be reduced by an order of magnitude."),
                ("system", "Induction technology is growing rapidly. What barriers remain?"),
                ("learner", "The primary obstacles are the upfront cost, the need for compatible cookware, and consumer reluctance to abandon gas cooking, which is deeply associated with culinary authenticity."),
                ("system", "Overcoming cultural attachment to gas flames may prove more challenging than the technological or economic barriers."),
            ],
            [
                ("learner", "The oven, in its capacity to transform raw ingredients through controlled heat, serves as a metaphor for the broader human impulse to impose order on nature."),
                ("system", "That is a philosophical reading of a kitchen appliance. How would you develop that metaphor?"),
                ("learner", "Just as the oven mediates between the rawness of nature and the refinement of culture, cooking itself has been identified by anthropologists as a defining characteristic of human civilisation."),
                ("system", "Claude Levi-Strauss's raw-cooked dichotomy comes to mind. Your ability to connect everyday objects to broader intellectual frameworks is impressive."),
            ],
        ],
    },

    # ------------------------------------------------------------------ #
    #  TOASTER                                                            #
    # ------------------------------------------------------------------ #
    "toaster": {
        "beginner": [
            [
                ("learner", "I put bread in the toaster every morning."),
                ("system", "Toast for breakfast is quick and easy!"),
                ("learner", "I like my toast with butter on top."),
                ("system", "Butter on warm toast is a classic treat!"),
            ],
            [
                ("learner", "The toaster makes the bread turn brown."),
                ("system", "Yes! The heat toasts the bread. Do you like it dark?"),
                ("learner", "No, I like it light and soft."),
                ("system", "You can use a lower setting for lighter toast."),
            ],
            [
                ("learner", "Be careful, the toaster is very hot."),
                ("system", "Good warning! Have you burned yourself before?"),
                ("learner", "No, but my brother touched it once."),
                ("system", "Ouch! Always let the toaster cool down before touching it."),
            ],
        ],
        "elementary": [
            [
                ("learner", "I am making toast for my little sister right now."),
                ("system", "That is very kind of you! Does she like toast?"),
                ("learner", "She wanted jam on her toast, so I spread some strawberry jam."),
                ("system", "Strawberry jam on warm toast sounds absolutely delicious."),
            ],
            [
                ("learner", "Our new toaster can toast four slices at the same time."),
                ("system", "A four-slice toaster is great for a big family!"),
                ("learner", "It saved a lot of time when we were rushing to school this morning."),
                ("system", "Efficiency in the morning routine makes the whole day start better."),
            ],
            [
                ("learner", "The toast got stuck inside the toaster and started to smoke."),
                ("system", "That must have been scary! What did you do?"),
                ("learner", "My mother unplugged it immediately and used a wooden spoon to remove it."),
                ("system", "Unplugging first was the safest thing to do. Never use metal to remove stuck toast."),
            ],
        ],
        "intermediate": [
            [
                ("learner", "I have experimented with toasting different types of bread to find my favourite."),
                ("system", "That sounds like a fun breakfast project! Which bread do you prefer?"),
                ("learner", "If I use thick whole wheat bread, the toast comes out crunchier and more flavourful."),
                ("system", "Whole wheat bread holds up better to toasting and is healthier too."),
            ],
            [
                ("learner", "Our toaster has been in the family for over five years and still works perfectly."),
                ("system", "That is impressive. Do you clean it regularly?"),
                ("learner", "My mother empties the crumb tray every week, which has probably kept it in good condition."),
                ("system", "Regular maintenance like emptying the crumb tray extends the life of any toaster."),
            ],
            [
                ("learner", "If someone invented a toaster that could also cook eggs, breakfast would be even quicker."),
                ("system", "Combination breakfast appliances actually exist! Have you seen them?"),
                ("learner", "I have seen them online, but they look complicated and difficult to clean."),
                ("system", "Sometimes simple single-purpose appliances are more practical than all-in-one gadgets."),
            ],
        ],
        "upper_intermediate": [
            [
                ("learner", "The toaster is often described as the most underappreciated appliance in the modern kitchen."),
                ("system", "It does its job quietly every morning. What makes you say that?"),
                ("learner", "Despite being used daily by millions, it is rarely mentioned in conversations about essential kitchen technology."),
                ("system", "Its very reliability makes it invisible. We tend to notice appliances only when they malfunction."),
            ],
            [
                ("learner", "It was explained to us in physics class that a toaster converts electrical energy into heat through resistance wires."),
                ("system", "The nichrome heating element is a simple but effective design. Did the class explore efficiency?"),
                ("learner", "We calculated that a typical toaster uses about eight hundred watts, which is surprisingly energy-efficient for the speed at which it works."),
                ("system", "The toaster's energy efficiency per unit of food prepared is actually better than using a full-sized oven for the same task."),
            ],
            [
                ("learner", "My grandmother is amazed by the pop-up toaster because she grew up toasting bread over an open flame."),
                ("system", "The generational difference in kitchen technology must be striking."),
                ("learner", "She says that bread toasted over coals had a smoky flavour that no electric toaster can replicate."),
                ("system", "Each method has its charm. Traditional techniques often produce flavours that modern appliances cannot reproduce."),
            ],
        ],
        "advanced": [
            [
                ("learner", "The humble toaster has been adopted by design theorists as a case study in the tension between form and function in consumer products."),
                ("system", "Dieter Rams and the Braun toasters come to mind. What aspect of that tension interests you?"),
                ("learner", "The proliferation of aesthetically driven toaster designs that sacrifice usability — such as transparent glass toasters — reveals how consumer culture prioritises visual novelty over ergonomic practicality."),
                ("system", "The triumph of aesthetics over utility in small appliances mirrors broader consumerist trends where appearance drives purchasing decisions."),
            ],
            [
                ("learner", "Were I to design a toaster for the Indian market, I would incorporate settings optimised for regional bread varieties such as pav and roti."),
                ("system", "Localising appliance design is an underexplored opportunity. How would the settings differ?"),
                ("learner", "Pav requires gentle, even warming rather than aggressive browning, which necessitates a lower wattage mode and wider slots to accommodate thicker, softer bread."),
                ("system", "Culturally informed product design like that could capture a significant market share in India, where most toasters are designed for Western-style sliced bread."),
            ],
            [
                ("learner", "Thomas Thwaites's project to build a toaster from scratch — mining ore, smelting metal, and synthesising plastic — powerfully illustrates the invisible complexity embedded in everyday objects."),
                ("system", "The Toaster Project is a brilliant commentary on industrial interdependence. What lesson do you draw from it?"),
                ("learner", "It demonstrates that even the simplest consumer product depends on a vast, interconnected global supply chain, and that our inability to replicate it individually should inspire humility about the systems we depend on."),
                ("system", "That humility, extended to all the technologies we take for granted, is a necessary corrective to the illusion of individual self-sufficiency."),
            ],
        ],
    },

    # ------------------------------------------------------------------ #
    #  SINK                                                               #
    # ------------------------------------------------------------------ #
    "sink": {
        "beginner": [
            [
                ("learner", "I wash my hands at the sink."),
                ("system", "Good! Do you use soap every time?"),
                ("learner", "Yes, I always use soap and water."),
                ("system", "Clean hands keep you healthy and safe!"),
            ],
            [
                ("learner", "The sink is full of dirty dishes."),
                ("system", "Who will wash the dishes today?"),
                ("learner", "I will help my mother wash them."),
                ("system", "That is very helpful of you. Good job!"),
            ],
            [
                ("learner", "Water comes out of the sink tap."),
                ("system", "Do you turn the tap off after use?"),
                ("learner", "Yes, we must not waste water."),
                ("system", "Saving water is very important. Well done!"),
            ],
        ],
        "elementary": [
            [
                ("learner", "I am filling the sink with warm water to wash the plates."),
                ("system", "That is the right way to do it. Are you adding soap?"),
                ("learner", "Yes, I squeezed some dish soap into the water."),
                ("system", "Good. Warm soapy water removes grease much better than cold water."),
            ],
            [
                ("learner", "The kitchen sink was clogged this morning and water would not drain."),
                ("system", "A clogged sink is a real problem. How did you fix it?"),
                ("learner", "My father poured hot water and baking soda to clear the blockage."),
                ("system", "That is a simple and effective home remedy for minor clogs."),
            ],
            [
                ("learner", "Our school has a row of sinks outside the canteen for hand washing."),
                ("system", "That is great for hygiene. Do all students use them?"),
                ("learner", "Most students wash their hands before and after eating lunch."),
                ("system", "Hand washing before meals is one of the best habits you can develop."),
            ],
        ],
        "intermediate": [
            [
                ("learner", "I have noticed that our kitchen sink wastes a lot of water because the tap drips constantly."),
                ("system", "A dripping tap can waste thousands of litres per year. Have you reported it?"),
                ("learner", "If we replaced the worn-out washer inside the tap, the dripping would stop immediately."),
                ("system", "That is a small and inexpensive fix that could save a significant amount of water."),
            ],
            [
                ("learner", "In our village, the community sink near the water pump is where everyone gathers in the morning."),
                ("system", "Shared water sources are important social spaces. What happens there?"),
                ("learner", "People wash clothes, fill water pots, and chat while waiting for their turn."),
                ("system", "The communal sink serves both a practical and a social function in village life."),
            ],
            [
                ("learner", "If every household installed a water-saving aerator on their sink taps, the city's water consumption would drop noticeably."),
                ("system", "Aerators are cheap and effective. Are they commonly used here?"),
                ("learner", "Very few people know about them, which is why awareness campaigns would be so valuable."),
                ("system", "Public education about simple water-saving devices could have a large cumulative impact."),
            ],
        ],
        "upper_intermediate": [
            [
                ("learner", "The kitchen sink is often referred to as the most heavily used fixture in any household."),
                ("system", "From cooking to cleaning, it sees constant use. Has your family experienced any issues with it?"),
                ("learner", "Our stainless steel sink has developed scratches over the years, though it has been maintained regularly with proper cleaning agents."),
                ("system", "Stainless steel is durable but not impervious. Regular maintenance extends its usable life considerably."),
            ],
            [
                ("learner", "It was reported in the news that several schools in rural areas lack even basic sink facilities for hand washing."),
                ("system", "Access to hand washing infrastructure is a public health necessity. What did the report suggest?"),
                ("learner", "The government was urged to prioritise the installation of sinks and soap dispensers in all schools as part of the hygiene initiative."),
                ("system", "The cost of installing sinks is minimal compared to the health benefits of improved hand hygiene among students."),
            ],
            [
                ("learner", "In commercial kitchens, separate sinks are designated for raw food, cooked food, and hand washing to prevent cross-contamination."),
                ("system", "Food safety regulations are strict in professional settings. Could homes benefit from similar practices?"),
                ("learner", "While having multiple sinks at home is impractical, the principle of separating raw and cooked food preparation areas should still be followed."),
                ("system", "Adapting professional hygiene principles to domestic kitchens is a sensible approach to food safety."),
            ],
        ],
        "advanced": [
            [
                ("learner", "The sink, as a site of daily ritual — from morning ablutions to evening dishwashing — occupies a uniquely intimate position in the geography of the home."),
                ("system", "You are framing the sink almost architecturally. How does its placement shape household dynamics?"),
                ("learner", "The kitchen sink's position typically dictates the workflow of cooking and cleaning, and in Indian homes, it is often the space where labour, predominantly performed by women, becomes most visible."),
                ("system", "Your observation connects domestic architecture to gender dynamics in a way that highlights the political dimensions of seemingly mundane household design."),
            ],
            [
                ("learner", "Were greywater recycling systems to be integrated into domestic sinks as standard, the strain on municipal water supplies in cities like Chennai could be meaningfully reduced."),
                ("system", "Chennai's water crisis makes this especially relevant. What does greywater recycling from sinks involve?"),
                ("learner", "Sink drainage water, once filtered of food particles and detergent, can be redirected for garden irrigation or toilet flushing, thereby reducing a household's freshwater demand by up to thirty percent."),
                ("system", "The simplicity of the technology makes the low adoption rate puzzling, suggesting that policy incentives and building code mandates may be necessary to drive uptake."),
            ],
            [
                ("learner", "The global disparity in access to clean running water at a sink underscores the extent to which basic infrastructure remains a privilege rather than a universal right."),
                ("system", "Water access is indeed one of the starkest indicators of inequality. How do you see this locally?"),
                ("learner", "Even within Chennai, the contrast between apartments with filtered water at every tap and slums where families share a single communal tap illustrates how proximity does not guarantee equity."),
                ("system", "That intra-city disparity is a sobering reminder that development statistics at the national level often mask deeply unequal realities at the neighbourhood level."),
            ],
        ],
    },

    # ------------------------------------------------------------------ #
    #  REFRIGERATOR                                                       #
    # ------------------------------------------------------------------ #
    "refrigerator": {
        "beginner": [
            [
                ("learner", "The refrigerator keeps our food cold."),
                ("system", "That is right! What food is inside it now?"),
                ("learner", "There is milk and fruit inside."),
                ("system", "Milk and fruit stay fresh in the refrigerator!"),
            ],
            [
                ("learner", "Please close the refrigerator door."),
                ("system", "Why is it important to close the door?"),
                ("learner", "Cold air goes out if it is open."),
                ("system", "That is correct! It also wastes electricity."),
            ],
            [
                ("learner", "I take cold water from the refrigerator."),
                ("system", "Cold water is refreshing on hot days!"),
                ("learner", "I drink a lot of water every day."),
                ("system", "Drinking enough water keeps you healthy."),
            ],
        ],
        "elementary": [
            [
                ("learner", "My mother is organising the refrigerator this afternoon."),
                ("system", "An organised fridge helps you find things quickly."),
                ("learner", "She put the vegetables on one shelf and the dairy on another."),
                ("system", "Separating food by type also helps prevent smells from mixing."),
            ],
            [
                ("learner", "The refrigerator started making a loud humming noise last night."),
                ("system", "That could mean the compressor is working too hard. Is it old?"),
                ("learner", "We bought it about ten years ago, so it might need a repair."),
                ("system", "A technician can check the compressor. Older refrigerators sometimes need servicing."),
            ],
            [
                ("learner", "I forgot to put the milk back in the refrigerator yesterday."),
                ("system", "Oh no! Did the milk go bad?"),
                ("learner", "Yes, it smelled sour this morning so we had to throw it away."),
                ("system", "Dairy products spoil quickly at room temperature. Try to put them back right after use."),
            ],
        ],
        "intermediate": [
            [
                ("learner", "Our old refrigerator has been replaced with an energy-efficient model that uses much less electricity."),
                ("system", "Energy-efficient appliances save money over time. Have you noticed a difference in the bill?"),
                ("learner", "My father said the electricity bill has gone down by about two hundred rupees a month since we switched."),
                ("system", "Those savings add up significantly over the lifetime of the appliance."),
            ],
            [
                ("learner", "If every family in our neighbourhood had a refrigerator, less food would be wasted."),
                ("system", "Food preservation is a major benefit. Is refrigerator ownership common in your area?"),
                ("learner", "Most families have one now, but some older households still rely on traditional methods like storing food in clay pots."),
                ("system", "Clay pot cooling is an ingenious traditional solution, though it cannot match a refrigerator for long-term preservation."),
            ],
            [
                ("learner", "I have read that the temperature inside a refrigerator should be below four degrees Celsius."),
                ("system", "That is the recommended range for food safety. Is yours set correctly?"),
                ("learner", "We checked with a thermometer and found it was too warm, so we adjusted the dial."),
                ("system", "Monitoring the temperature regularly ensures that food stays safe to eat."),
            ],
        ],
        "upper_intermediate": [
            [
                ("learner", "The refrigerator is considered one of the most significant household inventions of the twentieth century."),
                ("system", "It transformed food storage and dietary habits worldwide. What aspect interests you most?"),
                ("learner", "It is remarkable that before refrigeration, entire food cultures were built around preservation techniques like salting, pickling, and drying."),
                ("system", "The decline of those traditional methods is directly linked to the widespread adoption of refrigeration technology."),
            ],
            [
                ("learner", "The refrigerant gases used in older models were found to be harmful to the ozone layer."),
                ("system", "CFCs were a major environmental concern. How has the industry responded?"),
                ("learner", "Manufacturers have been required to switch to environmentally friendly refrigerants, though millions of older units still contain CFCs."),
                ("system", "The safe disposal and recycling of old refrigerators remains an important environmental challenge."),
            ],
            [
                ("learner", "In joint families, the refrigerator is often a shared resource that requires coordination among multiple household members."),
                ("system", "Managing shared kitchen space can be challenging. How does your family handle it?"),
                ("learner", "Each family unit in our household has been assigned a specific shelf, which prevents confusion and reduces food waste."),
                ("system", "That systematic approach to shared resources demonstrates how practical organisation can maintain harmony in joint families."),
            ],
        ],
        "advanced": [
            [
                ("learner", "The refrigerator fundamentally altered the temporal relationship between food production and consumption, enabling a disconnect that underpins modern global food supply chains."),
                ("system", "Cold chain logistics are the backbone of global food trade. How do you see this playing out in India?"),
                ("learner", "India's inadequate cold chain infrastructure results in approximately forty percent of perishable produce being lost before reaching consumers, a staggering inefficiency that perpetuates both waste and food insecurity."),
                ("system", "Investing in cold storage infrastructure from farm to market is one of the most impactful interventions for reducing food loss in developing economies."),
            ],
            [
                ("learner", "Were smart refrigerators with inventory tracking and expiry date monitoring to become affordable, household food waste could be reduced dramatically."),
                ("system", "IoT-enabled kitchens are emerging. What barriers do you see to adoption in India?"),
                ("learner", "Beyond cost, the primary barrier is the mismatch between smart refrigerator interfaces, which are designed for Western grocery systems, and the Indian practice of buying fresh produce daily from local markets."),
                ("system", "That cultural mismatch highlights the need for technology designers to understand local consumption patterns before deploying solutions across diverse markets."),
            ],
            [
                ("learner", "The refrigerator magnifies socioeconomic inequality in subtle ways: its contents reflect purchasing power, dietary choices, and even cultural capital."),
                ("system", "A sociological reading of the refrigerator — fascinating. Could you elaborate?"),
                ("learner", "An examination of refrigerator contents across income levels would reveal not merely differences in quantity but in the diversity of cuisines, the presence of imported goods, and the ability to store rather than immediately consume — all markers of economic privilege."),
                ("system", "That analysis transforms a mundane appliance into a lens for understanding class, consumption, and the material dimensions of inequality."),
            ],
        ],
    },

    # ------------------------------------------------------------------ #
    #  BOOK                                                               #
    # ------------------------------------------------------------------ #
    "book": {
        "beginner": [
            [
                ("learner", "I have a new book from the library."),
                ("system", "How exciting! What is the book about?"),
                ("learner", "It is a story about a brave lion."),
                ("system", "Lion stories are always exciting to read!"),
            ],
            [
                ("learner", "I read my book before I sleep."),
                ("system", "Reading before bed is a lovely habit."),
                ("learner", "My mother reads with me every night."),
                ("system", "That is a wonderful thing to share together!"),
            ],
            [
                ("learner", "Please give me that book on the shelf."),
                ("system", "Which one? The red one or the blue one?"),
                ("learner", "I want the blue book, please."),
                ("system", "Here you go! I hope you enjoy reading it."),
            ],
        ],
        "elementary": [
            [
                ("learner", "I am reading a book about space and planets."),
                ("system", "Space is fascinating! What have you learned so far?"),
                ("learner", "I learned that Jupiter is the biggest planet in our solar system."),
                ("system", "That is correct! Jupiter is so big that all other planets could fit inside it."),
            ],
            [
                ("learner", "I returned three books to the school library this morning."),
                ("system", "Were they due today? Did you finish all of them?"),
                ("learner", "I finished two of them, but the third one was too difficult."),
                ("system", "It is fine to put a difficult book aside and try it again when you are ready."),
            ],
            [
                ("learner", "My favourite book was torn because I left it in my bag with a water bottle."),
                ("system", "Oh no! Water and books do not mix well. Can it be fixed?"),
                ("learner", "My teacher helped me tape the torn pages back together."),
                ("system", "That was kind of your teacher. Try to keep your books in a separate pocket next time."),
            ],
        ],
        "intermediate": [
            [
                ("learner", "I have finished reading fifteen books this year, which is more than I expected."),
                ("system", "That is impressive! What kind of books do you enjoy most?"),
                ("learner", "If I had to choose one genre, I would say adventure stories are my favourite."),
                ("system", "Adventure stories fire up the imagination. Have you tried writing your own?"),
            ],
            [
                ("learner", "Our teacher has started a book club where students discuss one book every month."),
                ("system", "Book clubs encourage deeper thinking about what you read. What book are you discussing now?"),
                ("learner", "We are reading a novel about a boy who travels across India, which has sparked many interesting debates."),
                ("system", "Discussing different perspectives on the same book is one of the most valuable parts of reading."),
            ],
            [
                ("learner", "If public libraries were more accessible in rural areas, children there would have the same reading opportunities as city children."),
                ("system", "Library access is a significant equity issue. What solutions have you seen?"),
                ("learner", "Mobile library vans have been very successful in some districts of Tamil Nadu."),
                ("system", "Mobile libraries bring books directly to communities, removing the barrier of distance."),
            ],
        ],
        "upper_intermediate": [
            [
                ("learner", "It is often said that a book is the cheapest and most reliable form of education available to anyone."),
                ("system", "That sentiment has been expressed across cultures and centuries. Do you agree?"),
                ("learner", "While I believe in the transformative power of books, the statement overlooks the fact that many families cannot afford even a modest collection."),
                ("system", "Your nuanced response highlights the gap between the ideal of universal literacy and the economic reality of access."),
            ],
            [
                ("learner", "The transition from physical books to digital readers has been debated extensively in educational circles."),
                ("system", "Both formats have advantages. Where do you stand on the debate?"),
                ("learner", "Research has shown that retention is better with physical books, though digital formats offer unmatched convenience and portability."),
                ("system", "The optimal approach may be to use both formats strategically depending on the context and purpose of reading."),
            ],
            [
                ("learner", "A book that was recommended to me by my English teacher has completely changed the way I think about language learning."),
                ("system", "That is a strong endorsement. What was the book?"),
                ("learner", "It described how reading extensively in a second language is more effective than memorising grammar rules."),
                ("system", "The extensive reading approach is well supported by second language acquisition research."),
            ],
        ],
        "advanced": [
            [
                ("learner", "The physicality of a book — its weight, texture, and scent — engages sensory pathways that contribute to deeper encoding of its content."),
                ("system", "The embodied cognition argument for physical books is compelling. Is there empirical support?"),
                ("learner", "Studies have demonstrated that spatial memory cues provided by page position and book thickness facilitate recall in ways that scrolling on a screen cannot replicate."),
                ("system", "That spatial advantage of physical books is particularly relevant for educational settings where deep comprehension and retention are paramount."),
            ],
            [
                ("learner", "Were Tamil literature to be translated more widely and made available in affordable editions, it could achieve the global recognition that its literary heritage deserves."),
                ("system", "Tamil has one of the richest literary traditions in the world. What do you see as the main barrier?"),
                ("learner", "The paucity of skilled translators who can preserve the lyrical qualities of classical Tamil in English renders most translations inadequate representations of the originals."),
                ("system", "Translation is indeed an art, and the loss of nuance between languages is an inherent challenge that demands both linguistic mastery and cultural sensitivity."),
            ],
            [
                ("learner", "In an age of information abundance, the book remains distinctive as a medium that demands sustained, linear attention — a cognitive mode increasingly rare and therefore increasingly valuable."),
                ("system", "The contrast with fragmented digital reading is stark. Do you think deep reading is at risk?"),
                ("learner", "I would argue that the atrophy of deep reading capacity, driven by habitual exposure to bite-sized digital content, constitutes a genuine cognitive threat to this generation of learners."),
                ("system", "Your concern echoes Maryanne Wolf's research on the reading brain, which warns that the circuits supporting deep literacy require cultivation and can indeed be lost through disuse."),
            ],
        ],
    },

    # ------------------------------------------------------------------ #
    #  CLOCK                                                              #
    # ------------------------------------------------------------------ #
    "clock": {
        "beginner": [
            [
                ("learner", "The clock on the wall shows three."),
                ("system", "Three o'clock! Is it time for something?"),
                ("learner", "Yes, it is time for my snack."),
                ("system", "A snack at three sounds perfect. Enjoy!"),
            ],
            [
                ("learner", "I can tell the time on the clock."),
                ("system", "That is a great skill! What time is it now?"),
                ("learner", "It is half past four right now."),
                ("system", "Well done! You read the clock correctly."),
            ],
            [
                ("learner", "Our classroom has a big round clock."),
                ("system", "Can all the students see it from their desks?"),
                ("learner", "Yes, it helps us know when class ends."),
                ("system", "A clock in the classroom helps everyone stay on time."),
            ],
        ],
        "elementary": [
            [
                ("learner", "The clock in the hallway stopped working last week."),
                ("system", "Did someone fix it, or does it still show the wrong time?"),
                ("learner", "The caretaker changed the battery and it started again."),
                ("system", "A dead battery is the most common reason for a clock to stop."),
            ],
            [
                ("learner", "I am learning to read both digital and analogue clocks."),
                ("system", "That is important. Which one do you find easier?"),
                ("learner", "Digital clocks are easier, but my teacher wants us to learn the analogue one too."),
                ("system", "Analogue clocks help you understand the concept of time passing more visually."),
            ],
            [
                ("learner", "My grandfather gave me an old clock that chimes every hour."),
                ("system", "That sounds beautiful! Is it a pendulum clock?"),
                ("learner", "Yes, it swings back and forth and makes a ticking sound."),
                ("system", "Pendulum clocks are elegant. That must be a special gift from your grandfather."),
            ],
        ],
        "intermediate": [
            [
                ("learner", "I have become much more punctual since I started wearing a watch instead of relying on my phone."),
                ("system", "A watch is always visible on your wrist. How has it changed your habits?"),
                ("learner", "If I glance at my watch during class, I can manage my time without the distraction of a phone screen."),
                ("system", "That is a practical strategy. A watch gives you time information without the temptation of apps and notifications."),
            ],
            [
                ("learner", "The concept of standardised time zones was not adopted until the railways needed a common schedule."),
                ("system", "Before that, each town set its own time by the sun. How did you learn about this?"),
                ("learner", "Our history teacher explained how the expansion of railways in the nineteenth century forced countries to synchronise their clocks."),
                ("system", "The railway's need for coordination fundamentally changed how humanity relates to time."),
            ],
            [
                ("learner", "If the clock in our exam hall had been accurate, I would not have rushed through the last section."),
                ("system", "An inaccurate clock during an exam is a serious problem. What happened?"),
                ("learner", "The clock was fifteen minutes fast, so I thought time was almost up and hurried my answers."),
                ("system", "You should bring your own watch to exams so you do not have to depend on wall clocks."),
            ],
        ],
        "upper_intermediate": [
            [
                ("learner", "The shift from sundials to mechanical clocks represented a fundamental change in how societies organised labour and daily life."),
                ("system", "Clock time replaced natural time. How do you think that affected people?"),
                ("learner", "It is argued that mechanical clocks enabled the rigid work schedules that defined the Industrial Revolution."),
                ("system", "The clock as a tool of social control is a theme explored by many historians and sociologists."),
            ],
            [
                ("learner", "Students were reminded by the principal that the school operates strictly according to the clock."),
                ("system", "Punctuality is emphasised in most schools. Is it a problem at yours?"),
                ("learner", "Lateness has been increasing since the bus schedule was changed, which is beyond the students' control."),
                ("system", "Systemic issues like transportation should be considered before attributing lateness to individual irresponsibility."),
            ],
            [
                ("learner", "The atomic clock, which loses only one second over millions of years, is the most precise timekeeping device ever created."),
                ("system", "Atomic clocks underpin GPS and global communication networks. Why does their precision matter?"),
                ("learner", "Even a microsecond of drift in satellite clocks would result in significant positioning errors that could affect navigation and emergency services."),
                ("system", "The dependence of modern infrastructure on precise timekeeping is often invisible but absolutely critical."),
            ],
        ],
        "advanced": [
            [
                ("learner", "The clock, as a technology of temporal regimentation, has been critiqued by social theorists as an instrument that alienates individuals from the natural rhythms of their bodies and environment."),
                ("system", "E.P. Thompson's 'Time, Work-Discipline, and Industrial Capitalism' makes exactly that argument. Do you agree?"),
                ("learner", "While I acknowledge the disciplinary function of clock time, I would argue that it also liberated individuals by providing a shared framework for coordination that transcends personal or local idiosyncrasies."),
                ("system", "Your dialectical reading — the clock as both constraining and enabling — is more nuanced than either a purely critical or celebratory account."),
            ],
            [
                ("learner", "Were we to abandon clock-based scheduling in schools and adopt flexible, student-centred timetables, the rigid association between time and productivity might begin to dissolve."),
                ("system", "Some progressive schools have experimented with that approach. What outcomes do you predict?"),
                ("learner", "I suspect that while intrinsically motivated students would thrive, the absence of temporal structure could disadvantage those who rely on external frameworks to organise their learning."),
                ("system", "That equity concern is well founded. Flexibility often benefits the already privileged, while structure provides a scaffold for those who need it most."),
            ],
            [
                ("learner", "The philosophical implications of Einstein's demonstration that time is relative — that clocks at different velocities tick at different rates — remain profoundly unsettling to our intuitive experience of temporal uniformity."),
                ("system", "Relativity challenges our deepest assumptions about the world. How do you reconcile it with everyday experience?"),
                ("learner", "In practice, the discrepancies are imperceptible at human scales, yet the theoretical insight that simultaneity is frame-dependent undermines the very notion of a universal present that clock faces seem to promise."),
                ("system", "That tension between the lived experience of a shared now and the physics of observer-dependent time is one of the most fascinating intersections of science and philosophy."),
            ],
        ],
    },

    # ------------------------------------------------------------------ #
    #  VASE                                                               #
    # ------------------------------------------------------------------ #
    "vase": {
        "beginner": [
            [
                ("learner", "There is a pretty vase on the table."),
                ("system", "What colour is the vase?"),
                ("learner", "The vase is blue and white."),
                ("system", "Blue and white vases are very beautiful!"),
            ],
            [
                ("learner", "My mother put flowers in the vase."),
                ("system", "What kind of flowers are in it?"),
                ("learner", "She put red roses in the vase."),
                ("system", "Red roses in a vase look lovely!"),
            ],
            [
                ("learner", "Be careful with the glass vase, please."),
                ("system", "Why? Is it easy to break?"),
                ("learner", "Yes, glass breaks if you drop it."),
                ("system", "You are right. Handle glass things gently."),
            ],
        ],
        "elementary": [
            [
                ("learner", "I am arranging flowers in the vase for our dining table."),
                ("system", "That will make the table look beautiful. Which flowers did you choose?"),
                ("learner", "I picked marigolds and jasmine from our garden."),
                ("system", "Marigolds and jasmine are classic Indian flowers with wonderful fragrance."),
            ],
            [
                ("learner", "My little brother knocked the vase off the shelf by accident."),
                ("system", "Oh no! Did it break when it fell?"),
                ("learner", "Luckily it landed on the carpet, so it did not shatter."),
                ("system", "That was fortunate! Carpets can cushion a fall and prevent breakage."),
            ],
            [
                ("learner", "We bought a clay vase from a potter at the local market."),
                ("system", "Handmade pottery has a special character. Did you watch the potter make it?"),
                ("learner", "Yes, he shaped it on a spinning wheel and it was fascinating to watch."),
                ("system", "Pottery making is an ancient and beautiful craft that takes years to master."),
            ],
        ],
        "intermediate": [
            [
                ("learner", "I have always believed that a vase of fresh flowers can brighten any room instantly."),
                ("system", "Flowers do have that effect. Do you keep fresh flowers at home regularly?"),
                ("learner", "If there were a flower market closer to our house, I would buy flowers every week."),
                ("system", "Even a small bunch of seasonal flowers can transform the atmosphere of a room."),
            ],
            [
                ("learner", "The ceramic vase that my grandmother made by hand is the most treasured object in our home."),
                ("system", "Handmade objects carry special meaning. What makes it so special to your family?"),
                ("learner", "She made it before she passed away, and it has become a symbol of her creativity and love."),
                ("system", "Objects made by loved ones hold emotional value that no store-bought item can match."),
            ],
            [
                ("learner", "If ancient vases could speak, they would tell us so much about the civilisations that created them."),
                ("system", "Archaeologists learn a great deal from pottery. What interests you about ancient vases?"),
                ("learner", "The patterns and materials reveal what people valued, traded, and how they lived their daily lives."),
                ("system", "Pottery is one of the most durable records of human culture, surviving long after other materials decay."),
            ],
        ],
        "upper_intermediate": [
            [
                ("learner", "The vase, though purely decorative in most modern homes, has a long history as a functional storage vessel."),
                ("system", "Amphoras and urns served critical roles in ancient economies. When did the shift to decoration occur?"),
                ("learner", "It is believed that the transition began during the Renaissance, when ceramic arts were elevated to fine art and vases became objects of aesthetic contemplation."),
                ("system", "The journey from utilitarian vessel to art object mirrors broader cultural shifts in how we value form versus function."),
            ],
            [
                ("learner", "A vase that was donated to our school by a visiting dignitary is displayed in the principal's office."),
                ("system", "Diplomatic gifts often have cultural significance. Where is the vase from?"),
                ("learner", "It was described as a traditional Korean celadon vase, known for its distinctive jade-green glaze."),
                ("system", "Korean celadon represents one of the highest achievements in ceramic art. That is a meaningful gift."),
            ],
            [
                ("learner", "In traditional Tamil homes, brass and copper vessels that function as vases are often passed down through generations."),
                ("system", "Heirloom metalware carries deep cultural significance. Does your family have any?"),
                ("learner", "We have a brass kodam that was used by my great-grandmother and is now kept as a decorative piece filled with flowers."),
                ("system", "The transformation of a utilitarian vessel into a cherished heirloom beautifully illustrates how meaning accumulates over generations."),
            ],
        ],
        "advanced": [
            [
                ("learner", "John Keats's 'Ode on a Grecian Urn' demonstrates how a vase can serve as a philosophical meditation on the relationship between art, time, and permanence."),
                ("system", "Keats found eternity frozen in clay. What line resonates most with you?"),
                ("learner", "The assertion that 'Beauty is truth, truth beauty' encapsulates the Romantic conviction that aesthetic experience provides a form of knowledge inaccessible through rational inquiry alone."),
                ("system", "Your reading connects the decorative object to epistemology — the idea that beauty itself is a mode of understanding, not merely a sensory pleasure."),
            ],
            [
                ("learner", "Were the Indian government to invest in preserving traditional pottery techniques, artisan communities that have sustained these crafts for millennia might avoid the economic marginalisation they currently face."),
                ("system", "The economics of traditional crafts are precarious. What form should support take?"),
                ("learner", "Beyond financial subsidies, what is needed is a market infrastructure that connects rural artisans to urban and global consumers who value handmade ceramics over mass-produced alternatives."),
                ("system", "Digital marketplaces and fair-trade certification could provide that bridge, but the challenge lies in scaling access without eroding the authenticity that makes these crafts valuable."),
            ],
            [
                ("learner", "The vase, in its hollowness, embodies what Heidegger called the 'thingness of the thing' — its essence lies not in its material but in the void it creates and the gathering it performs."),
                ("system", "Heidegger's essay 'The Thing' is a profound meditation on objects. How do you interpret 'gathering'?"),
                ("learner", "The vase gathers earth in its clay, sky in the water it holds, and the divine in the ritual offering of flowers — it becomes a nexus where the fourfold of Heidegger's world converges."),
                ("system", "Your explication of the fourfold through the vase is remarkably precise. It demonstrates how philosophical attention to ordinary objects can reveal layers of meaning that habitual use conceals."),
            ],
        ],
    },

    # ------------------------------------------------------------------ #
    #  SCISSORS                                                           #
    # ------------------------------------------------------------------ #
    "scissors": {
        "beginner": [
            [
                ("learner", "I use scissors to cut paper in class."),
                ("system", "Cutting paper is fun! What are you making?"),
                ("learner", "I am making a birthday card for my friend."),
                ("system", "That is so thoughtful! Your friend will love it."),
            ],
            [
                ("learner", "Scissors are sharp, so I am careful."),
                ("system", "That is very wise. How do you hold them safely?"),
                ("learner", "I hold them by the handles, not the blades."),
                ("system", "Perfect! Always hold scissors by the handles."),
            ],
            [
                ("learner", "Can I borrow your scissors, please?"),
                ("system", "Of course! What do you need them for?"),
                ("learner", "I need to cut a picture from a magazine."),
                ("system", "Here you are. Be careful while cutting!"),
            ],
        ],
        "elementary": [
            [
                ("learner", "I was cutting shapes with scissors for my art project."),
                ("system", "Art projects are creative! What shapes did you cut?"),
                ("learner", "I cut circles and stars out of coloured paper."),
                ("system", "Circles and stars sound perfect for a decoration. Well done!"),
            ],
            [
                ("learner", "The scissors in my pencil box are not very sharp anymore."),
                ("system", "Blunt scissors make cutting difficult. Can they be sharpened?"),
                ("learner", "My mother said she will buy me a new pair from the shop."),
                ("system", "A new pair of scissors will make your craft work much easier."),
            ],
            [
                ("learner", "My teacher showed us how to pass scissors safely to another person."),
                ("system", "That is an important safety lesson. How should you do it?"),
                ("learner", "You hold the blades closed and offer the handles to the other person."),
                ("system", "Exactly right! That way nobody gets hurt when sharing scissors."),
            ],
        ],
        "intermediate": [
            [
                ("learner", "I have been practising cutting straight lines with scissors for my sewing class."),
                ("system", "Cutting fabric requires precision. Is it harder than cutting paper?"),
                ("learner", "Much harder, because the fabric moves and slides if you do not hold it firmly."),
                ("system", "Using sharp fabric scissors and pinning the material down can make it much easier."),
            ],
            [
                ("learner", "Left-handed students often struggle with regular scissors because the blades are designed for right-handed use."),
                ("system", "That is a real challenge. Does your school provide left-handed scissors?"),
                ("learner", "If the school stocked left-handed scissors, it would make a big difference for students like my friend Priya."),
                ("system", "Inclusivity in classroom supplies is something schools should prioritise for all students."),
            ],
            [
                ("learner", "The invention of scissors dates back thousands of years to ancient Egypt."),
                ("system", "That is fascinating historical knowledge. How did you learn about it?"),
                ("learner", "Our history textbook mentioned that early scissors were made from a single piece of bronze bent into a spring shape."),
                ("system", "Those spring scissors evolved into the cross-blade design we use today, which gives much more cutting control."),
            ],
        ],
        "upper_intermediate": [
            [
                ("learner", "Scissors are deceptively simple tools that embody fundamental principles of physics, including leverage and shearing force."),
                ("system", "The pivot point acts as a fulcrum. Did you study this in physics class?"),
                ("learner", "Yes, we were taught that the mechanical advantage of scissors depends on the ratio of handle length to blade length."),
                ("system", "That ratio explains why longer handles require less effort to cut — a direct application of lever mechanics."),
            ],
            [
                ("learner", "It is interesting that the word 'scissors' is always used in the plural form in English, even when referring to a single instrument."),
                ("system", "Pluralia tantum is the linguistic term. Can you think of other examples?"),
                ("learner", "Words like trousers, glasses, and tongs follow the same pattern, presumably because they consist of two symmetrical parts."),
                ("system", "Your observation about symmetrical parts is the most widely accepted etymological explanation for this grammatical pattern."),
            ],
            [
                ("learner", "Traditional barber scissors in India were handcrafted by blacksmiths who understood the precise angle needed for clean cutting."),
                ("system", "Artisan tool-making requires deep empirical knowledge. Is that craft still alive?"),
                ("learner", "Sadly, mass-produced stainless steel scissors have largely replaced handcrafted ones, and the skills of traditional scissor-smiths are being lost."),
                ("system", "The displacement of artisan craftsmanship by industrial production is a recurring narrative across many trades."),
            ],
        ],
        "advanced": [
            [
                ("learner", "Scissors occupy an interesting position in child development research as one of the first tools requiring bilateral coordination of asymmetric hand movements."),
                ("system", "The developmental milestone of using scissors is indeed significant. At what age is it typically achieved?"),
                ("learner", "Most children develop the fine motor control necessary for scissor use between ages three and four, though the quality of cutting continues to refine well into primary school."),
                ("system", "That prolonged refinement period underscores how seemingly simple tools can demand complex neuromotor coordination."),
            ],
            [
                ("learner", "Were scissors to be reimagined with universal design principles, accommodating users with arthritis, limited grip strength, or single-hand use, their accessibility could be dramatically expanded."),
                ("system", "Adaptive scissors do exist but are niche products. What would universal design look like?"),
                ("learner", "Spring-loaded, self-opening mechanisms with ergonomic grips should be the default rather than a specialty product, as the aging global population makes accessibility a mainstream concern."),
                ("system", "Designing for the margins benefits everyone — a principle that the universal design movement has long advocated."),
            ],
            [
                ("learner", "The scissors, as a tool that separates and divides, carries rich metaphorical weight in literature, from the Fates cutting the thread of life to Matisse cutting paper into art."),
                ("system", "The dual symbolism of destruction and creation is powerful. Which literary use strikes you most?"),
                ("learner", "Atropos severing the thread of life in Greek mythology imbues scissors with an almost sacred authority over finality, yet Matisse's paper cut-outs demonstrate that the act of cutting can simultaneously be an act of liberation and artistic genesis."),
                ("system", "That juxtaposition of mortality and creativity through a single tool reveals the profound ambivalence that everyday objects can carry in the human imagination."),
            ],
        ],
    },

    # ------------------------------------------------------------------ #
    #  TEDDY BEAR                                                         #
    # ------------------------------------------------------------------ #
    "teddy bear": {
        "beginner": [
            [
                ("learner", "My teddy bear is soft and brown."),
                ("system", "It sounds cuddly! Does it have a name?"),
                ("learner", "I call my teddy bear Brownie."),
                ("system", "Brownie is a perfect name for a brown teddy!"),
            ],
            [
                ("learner", "I sleep with my teddy bear every night."),
                ("system", "Your teddy bear keeps you company in bed!"),
                ("learner", "Yes, I hug it when I feel scared."),
                ("system", "Hugging a teddy bear always makes things better."),
            ],
            [
                ("learner", "My teddy bear sits on my bed."),
                ("system", "Does it stay there all day?"),
                ("learner", "Yes, it waits for me to come home."),
                ("system", "That is sweet! Your teddy is always ready for you."),
            ],
        ],
        "elementary": [
            [
                ("learner", "My grandmother gave me this teddy bear when I was born."),
                ("system", "That makes it a very special gift! How old is it now?"),
                ("learner", "It is ten years old, and I have taken care of it all this time."),
                ("system", "Ten years! That teddy bear must be full of wonderful memories."),
            ],
            [
                ("learner", "I was looking for my teddy bear everywhere this morning."),
                ("system", "Oh no! Where did you finally find it?"),
                ("learner", "It had fallen behind my bed while I was sleeping."),
                ("system", "At least you found it! A lost teddy bear is always a little emergency."),
            ],
            [
                ("learner", "My friend is collecting different types of teddy bears."),
                ("system", "That is a fun hobby! How many does she have?"),
                ("learner", "She has twelve teddy bears of different sizes and colours."),
                ("system", "Twelve teddy bears must look amazing all together on her shelf!"),
            ],
        ],
        "intermediate": [
            [
                ("learner", "I have kept my childhood teddy bear even though I am much older now."),
                ("system", "There is no age limit for sentimental attachments. What does it mean to you?"),
                ("learner", "If I ever feel stressed or homesick, seeing my teddy bear reminds me of simpler times."),
                ("system", "Objects from childhood carry emotional comfort that persists well into adulthood."),
            ],
            [
                ("learner", "The teddy bear was named after President Theodore Roosevelt, who refused to shoot a captured bear."),
                ("system", "That is a famous origin story! Where did you learn about it?"),
                ("learner", "I read about it in a book about the history of popular toys."),
                ("system", "The teddy bear's origin story is a wonderful example of how compassion can inspire an enduring cultural icon."),
            ],
            [
                ("learner", "If someone invented a teddy bear that could record bedtime stories, young children would love it."),
                ("system", "Talking teddy bears already exist! Have you seen them?"),
                ("learner", "I have seen some online, but they looked too expensive for most families to afford."),
                ("system", "A simpler version with basic recording features could be made more affordable and still delight children."),
            ],
        ],
        "upper_intermediate": [
            [
                ("learner", "The teddy bear is recognised by child psychologists as a transitional object that helps children manage separation anxiety."),
                ("system", "Winnicott's concept of transitional objects is well known. How does the teddy bear function in this role?"),
                ("learner", "It serves as a substitute for the caregiver's presence, providing a sense of security that enables the child to explore the world independently."),
                ("system", "The teddy bear bridges the gap between dependence and independence during a critical developmental stage."),
            ],
            [
                ("learner", "Teddy bears are often donated to hospitals and disaster relief shelters to comfort children in distress."),
                ("system", "The therapeutic use of soft toys is well documented. Have you participated in any such donation drive?"),
                ("learner", "Our school organised a collection last year, and over two hundred teddy bears were sent to a children's hospital in Chennai."),
                ("system", "That is a wonderful initiative. A familiar, soft object can provide immense comfort to a child in an unfamiliar and frightening environment."),
            ],
            [
                ("learner", "It is reported that the global teddy bear market generates billions of dollars annually, making it one of the most enduring toy categories in history."),
                ("system", "Over a century of commercial success is remarkable. What explains the teddy bear's staying power?"),
                ("learner", "Unlike trend-driven toys, the teddy bear satisfies a universal emotional need for comfort that transcends cultural and generational boundaries."),
                ("system", "That universality of emotional appeal is precisely what distinguishes timeless products from passing fads."),
            ],
        ],
        "advanced": [
            [
                ("learner", "The teddy bear, in its deliberate softening of the bear's natural ferocity into an object of comfort, represents a fascinating act of cultural domestication."),
                ("system", "Transforming a predator into a cuddle toy is indeed remarkable. What does this tell us about human psychology?"),
                ("learner", "It suggests that our capacity to recontextualise danger into safety through symbolic representation is a fundamental mechanism of psychological coping."),
                ("system", "Your analysis connects the teddy bear to broader theories of symbolic thought and the human need to master fear through representation."),
            ],
            [
                ("learner", "Were we to examine the teddy bear through the lens of material culture studies, its construction materials — from mohair to synthetic plush — would reveal shifts in manufacturing, trade, and consumer expectations over the past century."),
                ("system", "Material choices do encode economic and cultural history. What shift do you find most telling?"),
                ("learner", "The transition from individually hand-stitched mohair bears to mass-produced polyester ones mirrors the broader displacement of artisanal labour by industrial processes, with corresponding losses in tactile quality and uniqueness."),
                ("system", "That material degradation, paradoxically accompanied by greater accessibility, encapsulates the central tension of industrial modernity."),
            ],
            [
                ("learner", "The persistence of the teddy bear as a comfort object into adulthood challenges the cultural narrative that emotional attachment to inanimate objects is inherently childish."),
                ("system", "Adult attachment to childhood objects is more common than people admit. Why is it stigmatised?"),
                ("learner", "The stigma arises from a reductive equation of maturity with emotional detachment, whereas contemporary psychology recognises that maintaining connections to objects of comfort reflects healthy self-regulation rather than developmental regression."),
                ("system", "Reframing object attachment as adaptive rather than regressive is an important corrective that could reduce unnecessary shame around a perfectly normal human behaviour."),
            ],
        ],
    },

    # ------------------------------------------------------------------ #
    #  HAIR DRIER                                                         #
    # ------------------------------------------------------------------ #
    "hair drier": {
        "beginner": [
            [
                ("learner", "I use a hair drier after my bath."),
                ("system", "It helps dry your hair quickly!"),
                ("learner", "Yes, my hair dries in five minutes."),
                ("system", "That is much faster than waiting for it to dry!"),
            ],
            [
                ("learner", "The hair drier blows hot air on my hair."),
                ("system", "Be careful not to hold it too close."),
                ("learner", "I hold it far from my head."),
                ("system", "Good! That keeps your hair safe from too much heat."),
            ],
            [
                ("learner", "My mother uses the hair drier every morning."),
                ("system", "Does she dry her hair before going to work?"),
                ("learner", "Yes, she has long hair and it takes time."),
                ("system", "Long hair does need extra time to dry properly."),
            ],
        ],
        "elementary": [
            [
                ("learner", "I am drying my hair with the hair drier before school."),
                ("system", "Going to school with wet hair in the morning is uncomfortable."),
                ("learner", "I started using it last month because I kept catching colds."),
                ("system", "Drying your hair properly, especially in cool weather, is a smart habit."),
            ],
            [
                ("learner", "The hair drier made a strange noise and then stopped working."),
                ("system", "That does not sound good. What happened?"),
                ("learner", "My father said the motor inside was burned out."),
                ("system", "Motors can burn out from overuse. You might need a new hair drier."),
            ],
            [
                ("learner", "My sister borrowed my hair drier without asking me first."),
                ("system", "That can be annoying! Did you talk to her about it?"),
                ("learner", "I told her to ask me next time, and she agreed."),
                ("system", "Good communication solves most sharing problems at home."),
            ],
        ],
        "intermediate": [
            [
                ("learner", "I have learned that using a hair drier on the lowest heat setting causes less damage to hair."),
                ("system", "Heat damage is a real concern. Where did you learn that?"),
                ("learner", "If you always use high heat, the hair becomes dry and brittle over time."),
                ("system", "Using a lower setting with more distance protects the hair while still drying it effectively."),
            ],
            [
                ("learner", "Hair driers with ionic technology are supposed to reduce frizz and make hair smoother."),
                ("system", "Ionic driers are popular for that reason. Have you tried one?"),
                ("learner", "My aunt bought one, and she noticed a clear difference in how her hair looked afterward."),
                ("system", "The negative ions help break down water molecules faster, which reduces drying time and heat exposure."),
            ],
            [
                ("learner", "If there were a hair drier that automatically adjusted its temperature based on hair type, it would prevent a lot of damage."),
                ("system", "Smart appliances are heading in that direction. Would you buy one?"),
                ("learner", "I would, if the price were reasonable, because protecting hair health is worth the investment."),
                ("system", "Sensor-equipped driers already exist at the premium end of the market and will likely become more affordable soon."),
            ],
        ],
        "upper_intermediate": [
            [
                ("learner", "The hair drier is an appliance whose energy consumption is often underestimated by consumers."),
                ("system", "They do draw significant power. How much electricity does a typical one use?"),
                ("learner", "A standard hair drier operates at around fifteen hundred watts, which is comparable to a small room heater."),
                ("system", "When used daily by multiple family members, the energy cost can add up noticeably on the electricity bill."),
            ],
            [
                ("learner", "It is recommended by dermatologists that hair driers be held at least fifteen centimetres from the scalp to prevent thermal damage."),
                ("system", "Professional advice on hair care is important. Do most people follow this guideline?"),
                ("learner", "Most people are unaware of the recommendation, which is why manufacturers should include clearer usage instructions with the product."),
                ("system", "Better consumer education through packaging and user guides could significantly reduce inadvertent hair and scalp damage."),
            ],
            [
                ("learner", "In professional salons, the hair drier is considered a styling tool rather than merely a drying device."),
                ("system", "Stylists use specific techniques with the drier. Have you observed this?"),
                ("learner", "My hairdresser uses a round brush and the drier together to create volume and shape that I cannot achieve at home."),
                ("system", "The combination of directed airflow and brushing technique is what transforms a basic drier into a versatile styling instrument."),
            ],
        ],
        "advanced": [
            [
                ("learner", "The hair drier's evolution from a bulky, hazardous appliance to a sleek, ergonomically designed tool reflects broader trends in consumer electronics miniaturisation."),
                ("system", "Early models were indeed cumbersome. What drove the design improvements?"),
                ("learner", "Advances in motor efficiency, polymer engineering, and safety regulation converged to produce devices that are simultaneously more powerful, lighter, and safer than their predecessors."),
                ("system", "That convergence of multiple engineering disciplines in a single consumer product is a hallmark of mature industrial design."),
            ],
            [
                ("learner", "Were manufacturers to adopt modular designs with replaceable motors and heating elements, the environmental impact of disposable hair driers could be substantially mitigated."),
                ("system", "Repairability in small appliances is rare. What obstacles exist?"),
                ("learner", "The economic model of planned obsolescence, where replacement is cheaper than repair, disincentivises modularity and perpetuates a cycle of waste that is ecologically unsustainable."),
                ("system", "Breaking that cycle requires both regulatory mandates for repairability and a cultural shift in how consumers value longevity over novelty."),
            ],
            [
                ("learner", "The gendered marketing of hair driers — with functional models targeted at men and aesthetically embellished ones at women — reveals how consumer products reinforce and reproduce gender norms."),
                ("system", "The pink tax and gendered product design are well-documented phenomena. How would you challenge this?"),
                ("learner", "A truly equitable approach would market all hair driers on the basis of technical specifications alone, allowing consumers to choose based on performance rather than being channelled by gender-coded packaging."),
                ("system", "Specification-based marketing would not only challenge gender norms but would also empower consumers to make more informed purchasing decisions."),
            ],
        ],
    },

    # ------------------------------------------------------------------ #
    #  TOOTHBRUSH                                                         #
    # ------------------------------------------------------------------ #
    "toothbrush": {
        "beginner": [
            [
                ("learner", "I brush my teeth every morning."),
                ("system", "Great habit! Do you brush at night too?"),
                ("learner", "Yes, I brush two times a day."),
                ("system", "Brushing twice a day keeps your teeth healthy!"),
            ],
            [
                ("learner", "My toothbrush is green and small."),
                ("system", "A small toothbrush is good for reaching all teeth."),
                ("learner", "I like the colour green very much."),
                ("system", "It is nice to have a toothbrush you like!"),
            ],
            [
                ("learner", "I need a new toothbrush, please."),
                ("system", "Is your old one worn out already?"),
                ("learner", "Yes, the bristles are flat and bent."),
                ("system", "Flat bristles cannot clean well. Time for a new one!"),
            ],
        ],
        "elementary": [
            [
                ("learner", "My dentist told me to brush my teeth for two full minutes."),
                ("system", "Two minutes is the recommended time. Do you time yourself?"),
                ("learner", "I use a small sand timer that my mother put in the bathroom."),
                ("system", "A sand timer is a clever way to make sure you brush long enough!"),
            ],
            [
                ("learner", "I was brushing my teeth when the toothbrush slipped and fell on the floor."),
                ("system", "That happens sometimes! Did you pick it up and keep using it?"),
                ("learner", "No, I rinsed it carefully and then used a new one to be safe."),
                ("system", "That is a hygienic choice. It is always better to be cautious."),
            ],
            [
                ("learner", "Our school nurse showed us the correct way to hold a toothbrush."),
                ("system", "Proper technique is important. What did she teach you?"),
                ("learner", "She said to hold it at an angle and brush in small circles on each tooth."),
                ("system", "Circular motions clean better than scrubbing back and forth. Good advice!"),
            ],
        ],
        "intermediate": [
            [
                ("learner", "I have been using an electric toothbrush for three months and my teeth feel much cleaner."),
                ("system", "Electric toothbrushes can be more effective. What made you switch?"),
                ("learner", "My dentist recommended it because I was not brushing properly with a manual one."),
                ("system", "Electric toothbrushes compensate for imperfect technique with consistent oscillating motion."),
            ],
            [
                ("learner", "If every child in India had access to a toothbrush and toothpaste, dental disease rates would drop significantly."),
                ("system", "Oral hygiene access is a public health issue. What is the current situation?"),
                ("learner", "Many children in rural areas still use neem twigs because toothbrushes are either unavailable or unaffordable."),
                ("system", "Neem is a traditional alternative with some antibacterial properties, but modern dental tools offer more thorough cleaning."),
            ],
            [
                ("learner", "The dentist told me that I should replace my toothbrush every three months."),
                ("system", "Worn bristles are less effective. Do you follow that schedule?"),
                ("learner", "I have started marking the date on the handle so I remember when to change it."),
                ("system", "That is a practical system. Regular replacement ensures you always get the best cleaning."),
            ],
        ],
        "upper_intermediate": [
            [
                ("learner", "The toothbrush is considered one of the most important inventions in the history of personal hygiene."),
                ("system", "It has saved countless people from dental disease. When was it first developed?"),
                ("learner", "The modern nylon-bristle toothbrush was introduced in the late nineteen thirties, though earlier versions using animal hair date back centuries."),
                ("system", "The replacement of animal bristles with nylon was a breakthrough in both hygiene and manufacturing consistency."),
            ],
            [
                ("learner", "Children should be taught by parents to view toothbrushing not as a chore but as an essential act of self-care."),
                ("system", "Framing is important in building habits. How would you make it enjoyable for young children?"),
                ("learner", "Musical toothbrushes that play for two minutes and reward charts that track brushing consistency have been shown to increase compliance in young children."),
                ("system", "Gamification of hygiene routines leverages children's natural love of play to establish lifelong habits."),
            ],
            [
                ("learner", "The environmental impact of plastic toothbrushes is considerable, given that billions are discarded worldwide each year."),
                ("system", "Plastic waste from toothbrushes is a growing concern. What alternatives exist?"),
                ("learner", "Bamboo toothbrushes with biodegradable handles have been gaining popularity, though the bristles are still typically made of nylon."),
                ("system", "A fully biodegradable toothbrush remains an engineering challenge, but bamboo handles represent a meaningful step forward."),
            ],
        ],
        "advanced": [
            [
                ("learner", "The toothbrush exemplifies how a mundane object can encode complex negotiations between public health policy, individual behaviour, and commercial interests."),
                ("system", "That is an incisive framing. Could you unpack one of those intersections?"),
                ("learner", "The three-month replacement cycle recommended by dentists simultaneously serves public health by ensuring effective cleaning and commercial interests by guaranteeing sustained demand — a rare alignment that both parties have an incentive to promote."),
                ("system", "That convergence of medical advice and market logic is a fascinating case study in how health recommendations can inadvertently — or intentionally — serve economic functions."),
            ],
            [
                ("learner", "Were oral hygiene education to be universally integrated into primary school curricula across India, the long-term savings in dental healthcare costs would far exceed the investment in educational programmes."),
                ("system", "Preventive health education is consistently shown to be cost-effective. What barriers exist?"),
                ("learner", "The primary barriers are the absence of trained health educators in rural schools and the perception that oral hygiene is a private family matter rather than a public health priority."),
                ("system", "Overcoming that cultural boundary between public education and private hygiene requires framing dental health as a community concern with systemic economic implications."),
            ],
            [
                ("learner", "The ritualistic nature of toothbrushing — its fixed timing, repetitive motion, and position at the boundary between sleep and wakefulness — gives it an almost meditative quality that structures the transitions of daily life."),
                ("system", "Framing hygiene as ritual adds a phenomenological dimension. How does this affect the experience?"),
                ("learner", "By performing the act mindfully rather than mechanically, the twice-daily encounter with the toothbrush becomes an anchor of bodily awareness, a moment where the self attends deliberately to its own physical maintenance."),
                ("system", "Your phenomenological reading transforms a mundane act into a site of embodied self-care, suggesting that even our most automatic behaviours can become occasions for presence and intentionality."),
            ],
        ],
    },
}
