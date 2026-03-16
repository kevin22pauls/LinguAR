#!/usr/bin/env python3
from __future__ import annotations
"""
Build sentence_bank.json and dialogue_bank.json from hand-crafted sentences.
Only uses g2p-en for phoneme tagging — all sentence content is human-authored.
"""

import json
import re
from pathlib import Path

try:
    from g2p_en import G2p
    g2p = G2p()
except ImportError:
    print("WARNING: g2p_en not installed. Run: pip install g2p-en")
    g2p = None

DATA_DIR = Path(__file__).resolve().parent.parent / "backend" / "data"


def get_phonemes(sentence):
    if g2p is None:
        return []
    raw = g2p(sentence)
    seen = set()
    result = []
    for tok in raw:
        cleaned = re.sub(r"[^A-Z]", "", tok.upper())
        if cleaned and len(cleaned) >= 2:
            base = cleaned.rstrip("012")
            if base and base not in seen:
                seen.add(base)
                result.append(base)
    return result


# ═══════════════════════════════════════════════════════════════════════════
#  HAND-CRAFTED SENTENCES — 8 school objects × 5 levels × 10 sentences
# ═══════════════════════════════════════════════════════════════════════════

SENTENCES = {

    "sharpner": {
        "beginner": [
            ("I need a sharpner.", "simple present"),
            ("The sharpner is small.", "copula + adjective"),
            ("This sharpner is blue.", "demonstrative"),
            ("My sharpner is new.", "possessive"),
            ("Where is the sharpner?", "question word"),
            ("I lost my sharpner today.", "past simple"),
            ("Give me the sharpner, please.", "imperative"),
            ("The sharpner is on the desk.", "preposition"),
            ("I have two sharpners.", "have + plural"),
            ("Can I use your sharpner?", "request"),
        ],
        "elementary": [
            ("My pencil is blunt, so I need a sharpner.", "cause and effect"),
            ("I always keep a sharpner in my pencil box.", "frequency adverb"),
            ("This sharpner makes my pencils very sharp.", "cause and result"),
            ("I bought a new sharpner from the school shop.", "past simple"),
            ("The sharpner fell under the bench during class.", "past simple + preposition"),
            ("Please do not throw sharpner shavings on the floor.", "negative imperative"),
            ("My friend gave me a bright yellow sharpner.", "indirect object"),
            ("There are many types of sharpners in the shop.", "there are"),
            ("I sharpened three pencils with this sharpner.", "past simple + number"),
            ("Be careful when you use the sharpner.", "imperative + when clause"),
        ],
        "intermediate": [
            ("The sharpner that my mother bought is better than the old one.", "relative clause + comparative"),
            ("I have been using this sharpner since the beginning of the school year.", "present perfect continuous"),
            ("If you forget your sharpner, you can borrow mine during the test.", "first conditional"),
            ("Could you lend me your sharpner for a moment, please?", "polite request"),
            ("Although this sharpner looks simple, it works very well.", "concessive clause"),
            ("The teacher asked us to keep a sharpner in our pencil boxes.", "reported speech"),
            ("I would rather buy a metal sharpner than a plastic one.", "would rather"),
            ("My sharpner broke while I was sharpening my colour pencil.", "past continuous"),
            ("Have you ever used a sharpner with two different-sized holes?", "present perfect + ever"),
            ("The sharpner needs to be replaced because the blade has become dull.", "because clause + present perfect"),
        ],
        "upper_intermediate": [
            ("The sharpner, which I had been using for over a year, finally broke during the exam.", "non-defining relative clause"),
            ("Had I brought a spare sharpner, I would not have had to borrow one.", "inverted conditional"),
            ("Despite being very small, a good sharpner can make a real difference to your writing.", "despite + gerund"),
            ("Not only does a sharp pencil write neatly, but it also helps you draw better lines.", "not only...but also"),
            ("I wish I had bought a better sharpner instead of the cheap one that broke.", "wish + past perfect"),
            ("It is surprising how something as small as a sharpner can be so important in class.", "it is + adjective + how"),
            ("The quality of a sharpner depends on the sharpness of its blade.", "depends on"),
            ("Whoever lost their sharpner on the floor should come and collect it.", "whoever"),
            ("Were it not for this tiny sharpner, I would not have been able to finish my drawing.", "subjunctive inversion"),
            ("The number of students who forget their sharpners has increased this term.", "present perfect passive"),
        ],
        "advanced": [
            ("It is remarkable that such an inexpensive tool as a sharpner plays such a vital role in every student's daily routine.", "it is + adjective + that"),
            ("One could argue that the design of the modern sharpner, with its compact size and replaceable blade, represents an efficient solution to a simple problem.", "one could argue"),
            ("The sharpner that had been sitting in my pencil case for months turned out to be the only one sharp enough to use during the final examination.", "past perfect continuous + turned out"),
            ("No sooner had I lent my sharpner to my classmate than the tip of my own pencil broke.", "no sooner...than"),
            ("Regardless of whether students prefer mechanical pencils or traditional ones, a reliable sharpner remains an essential part of any pencil box.", "regardless of whether"),
        ],
    },

    "ballpen": {
        "beginner": [
            ("I write with a ballpen.", "simple present"),
            ("The ballpen is black.", "copula + adjective"),
            ("This is my ballpen.", "demonstrative + possessive"),
            ("My ballpen ran out of ink.", "past simple"),
            ("Where did you keep my ballpen?", "past simple question"),
            ("I found a ballpen on the floor.", "past simple"),
            ("Give me a blue ballpen.", "imperative"),
            ("The ballpen is inside my bag.", "preposition"),
            ("I like this ballpen very much.", "like + adverb"),
            ("Can I borrow your ballpen?", "request"),
        ],
        "elementary": [
            ("I always write my homework with a blue ballpen.", "frequency adverb"),
            ("My teacher said we must use a black ballpen for the test.", "reported speech simple"),
            ("The ink in my ballpen finished during the exam.", "past simple"),
            ("I bought a pack of five ballpens from the shop.", "past simple + number"),
            ("Please write your name with a ballpen, not a pencil.", "imperative + not"),
            ("My ballpen stopped working in the middle of the page.", "past simple"),
            ("Do not press the ballpen too hard on the paper.", "negative imperative"),
            ("She lent me her favourite red ballpen.", "past simple + indirect object"),
            ("There were no ballpens left in the stationery shop.", "there were + negative"),
            ("I prefer ballpens because they write more smoothly.", "preference + because"),
        ],
        "intermediate": [
            ("The ballpen that I bought last week writes much better than the old one.", "relative clause + comparative"),
            ("I have been looking for my ballpen since the morning.", "present perfect continuous"),
            ("If the ballpen does not work, try shaking it gently.", "first conditional + imperative"),
            ("Could you please return the ballpen you borrowed yesterday?", "polite request + relative clause"),
            ("Although ballpens are cheap, some of them write very badly.", "concessive clause"),
            ("The teacher told us that we should not use red ballpens in the answer sheet.", "reported speech + should not"),
            ("I would prefer a ballpen with a grip because my fingers get tired.", "would prefer + because"),
            ("My ballpen leaked and left a big ink stain on my shirt.", "past simple + and"),
            ("Have you ever tried writing with a ballpen that has three different colours?", "present perfect + ever"),
            ("The ballpen needs a refill because the ink has completely run out.", "because + present perfect"),
        ],
        "upper_intermediate": [
            ("The ballpen, which was a gift from my grandmother, has sentimental value that no other pen could replace.", "non-defining relative clause"),
            ("Had I checked my pencil box before leaving home, I would have noticed that my ballpen was missing.", "inverted conditional"),
            ("Despite being the most common writing instrument in classrooms, the ballpen is often taken for granted.", "despite + gerund"),
            ("Not only did the ballpen leak all over my notebook, but it also stained the cover of the textbook underneath.", "not only...but also"),
            ("I wish I had kept the cap on the ballpen, as the ink has now dried out completely.", "wish + past perfect"),
            ("It is frustrating when a brand-new ballpen stops working after just a few pages.", "it is + adjective + when"),
            ("The invention of the ballpen revolutionised the way people write, making fountain pens less common.", "past simple + gerund"),
            ("Whoever took my ballpen from the desk should return it before the next class.", "whoever + should"),
            ("Were it not for ballpens, students would still be dipping nibs into inkwells.", "subjunctive inversion"),
            ("The number of ballpens discarded each year contributes significantly to plastic waste.", "contributes to"),
        ],
        "advanced": [
            ("It is worth noting that the humble ballpen, invented in the 1930s, transformed everyday writing by eliminating the mess and inconvenience of fountain pens.", "it is worth noting"),
            ("One might argue that the widespread availability of cheap ballpens has led to a throwaway culture where writing instruments are treated as disposable rather than treasured.", "one might argue"),
            ("The ballpen that I had been searching for all morning was eventually discovered wedged between the pages of my science textbook.", "past perfect continuous"),
            ("No sooner had the teacher distributed the question papers than my ballpen ran out of ink, leaving me in a state of panic.", "no sooner...than"),
            ("Regardless of advances in digital technology, the ballpen continues to be an indispensable tool in classrooms around the world.", "regardless of"),
        ],
    },

    "book": {
        "beginner": [
            ("I read a book every night.", "simple present"),
            ("The book has many pictures.", "have/has"),
            ("This book is very thick.", "demonstrative + adjective"),
            ("My favourite book is about animals.", "possessive + about"),
            ("Where is my English book?", "question word"),
            ("I left my book at home.", "past simple"),
            ("Open your book to page ten.", "imperative"),
            ("The book is on the shelf.", "preposition"),
            ("I got a new book for my birthday.", "past simple"),
            ("Can I read your book?", "request"),
        ],
        "elementary": [
            ("I finished reading the book before the bell rang.", "past simple + before"),
            ("My teacher gave us a new English book this term.", "indirect object"),
            ("The pages of this book are torn and dirty.", "compound adjective"),
            ("I always cover my books with brown paper.", "frequency adverb"),
            ("Please return the library book by Friday.", "imperative + by"),
            ("There are twelve chapters in this book.", "there are + number"),
            ("She borrowed my science book and forgot to return it.", "past simple + and"),
            ("Do not write anything on the pages of the textbook.", "negative imperative"),
            ("I enjoy reading books about space and planets.", "enjoy + gerund"),
            ("The book fell from the table and the cover came off.", "past simple + and"),
        ],
        "intermediate": [
            ("The book that my father bought me last week is about the history of India.", "relative clause"),
            ("I have been reading this book for two weeks and I am still on the third chapter.", "present perfect continuous"),
            ("If you read one book every month, you will read twelve books in a year.", "first conditional"),
            ("Could you recommend a good book for someone who enjoys adventure stories?", "polite request + relative clause"),
            ("Although the book looks boring from the cover, the story inside is actually very exciting.", "concessive clause"),
            ("The teacher suggested that we should read at least one book during the holidays.", "reported speech + should"),
            ("I would rather read a story book than a textbook during my free time.", "would rather + than"),
            ("My book got wet because I left it near the open window when it rained.", "because clause"),
            ("Have you ever read a book that changed the way you think about something?", "present perfect + ever"),
            ("The book needs to be returned to the library because it is already overdue.", "because + already"),
        ],
        "upper_intermediate": [
            ("The book, which was written by a famous Tamil author, has been translated into more than twenty languages.", "non-defining relative clause + present perfect passive"),
            ("Had I started reading the book earlier, I would have finished it before the exam.", "inverted conditional"),
            ("Despite being published over a hundred years ago, this book remains popular among young readers.", "despite + gerund"),
            ("Not only does reading books improve your vocabulary, but it also strengthens your imagination.", "not only...but also"),
            ("I wish I had taken better care of my books, as many of them are now damaged beyond repair.", "wish + past perfect"),
            ("It is widely believed that children who read books regularly perform better in school.", "it is + adverb + believed"),
            ("The number of books in our school library has doubled since the new principal arrived.", "present perfect + since"),
            ("Whoever finds the missing library book should hand it over to the class monitor.", "whoever + should"),
            ("Were it not for books, much of the knowledge from ancient times would have been lost forever.", "subjunctive inversion"),
            ("The book I was given as a prize turned out to be one of the most interesting stories I have ever read.", "turned out + superlative"),
        ],
        "advanced": [
            ("It strikes me as remarkable that a single well-written book can shape the thoughts and values of an entire generation of young readers.", "it strikes me"),
            ("One could argue that the gradual shift from printed books to digital screens has both advantages and disadvantages for the development of reading habits in children.", "one could argue"),
            ("The book that had been sitting on my desk for weeks, collecting dust, turned out to be exactly the one my teacher recommended for the summer reading list.", "past perfect continuous + turned out"),
            ("No sooner had I reached the final chapter of the book than the power went out, forcing me to wait until morning to read the ending.", "no sooner...than"),
            ("Regardless of whether one prefers fiction or non-fiction, the act of reading a book demands a level of concentration and imagination that few other activities can match.", "regardless of whether"),
        ],
    },

    "eraser": {
        "beginner": [
            ("I need an eraser.", "simple present"),
            ("The eraser is white.", "copula + adjective"),
            ("This is a big eraser.", "demonstrative"),
            ("My eraser is very soft.", "possessive + adjective"),
            ("Where is my eraser?", "question word"),
            ("I dropped my eraser.", "past simple"),
            ("Pass me the eraser, please.", "imperative"),
            ("The eraser is inside the box.", "preposition"),
            ("I bought a new eraser today.", "past simple + time"),
            ("Can I use your eraser?", "request"),
        ],
        "elementary": [
            ("I made a mistake, so I used my eraser.", "cause and effect"),
            ("My eraser smells like strawberry.", "sensory verb"),
            ("This eraser does not rub out ink marks.", "negative simple present"),
            ("I always carry a spare eraser in my pencil case.", "frequency adverb"),
            ("Please do not break the eraser into small pieces.", "negative imperative"),
            ("She gave me a pink eraser shaped like a heart.", "past simple + adjective"),
            ("There are many colourful erasers in the shop.", "there are + adjective"),
            ("I rubbed too hard and tore the paper with the eraser.", "past simple + and"),
            ("My eraser keeps slipping off the desk during class.", "present continuous"),
            ("Do you prefer a soft eraser or a hard one?", "preference question"),
        ],
        "intermediate": [
            ("The eraser that I bought from the book fair works much better than the one I had before.", "relative clause + comparative"),
            ("I have been looking for my eraser since the maths period started.", "present perfect continuous"),
            ("If you press too hard with the eraser, you will tear the paper.", "first conditional"),
            ("Could you please return the eraser you took from my desk?", "polite request + relative clause"),
            ("Although erasers are meant to correct mistakes, some of them leave ugly smudges on the page.", "concessive clause"),
            ("The teacher reminded us to bring an eraser for the drawing class.", "reported speech"),
            ("I would rather have a good eraser than a fancy pencil.", "would rather + than"),
            ("My eraser wore down completely because I had to correct so many mistakes.", "because + past simple"),
            ("Have you ever seen an eraser that can rub out ballpen ink?", "present perfect + ever"),
            ("The eraser needs to be soft enough to clean the paper without damaging it.", "enough + infinitive"),
        ],
        "upper_intermediate": [
            ("The eraser, which was barely the size of my thumbnail, somehow lasted the entire examination.", "non-defining relative clause"),
            ("Had I not had a spare eraser in my bag, I would have had to submit the paper with all my mistakes.", "inverted conditional"),
            ("Despite being one of the cheapest items in a pencil box, a good eraser is surprisingly hard to find.", "despite + gerund"),
            ("Not only did the eraser fail to remove the mark, but it also smeared graphite all over the page.", "not only...but also"),
            ("I wish I had not lent my eraser to my classmate, as he returned it in a terrible condition.", "wish + past perfect"),
            ("It is ironic that the more mistakes you make, the faster your eraser disappears.", "it is + adjective + that"),
            ("The quality of an eraser can be judged by how cleanly it removes pencil marks without leaving residue.", "can be judged by"),
            ("Whoever keeps breaking erasers into tiny pieces and throwing them around will be given detention.", "whoever + future"),
            ("Were it not for the humble eraser, every pencil mistake would be permanent.", "subjunctive inversion"),
            ("The number of erasers that go missing in a classroom is astonishing.", "that clause + adjective"),
        ],
        "advanced": [
            ("It is often overlooked that the eraser, a seemingly insignificant item, gives students the confidence to attempt difficult problems knowing they can correct their mistakes.", "it is + adverb + overlooked"),
            ("One might argue that the eraser embodies an important lesson for young learners: that making mistakes is a natural part of the learning process and can always be corrected.", "one might argue"),
            ("The eraser that had been wedged between the pages of my notebook for months was discovered just when I needed it most during the final examination.", "past perfect passive + just when"),
            ("No sooner had I finished correcting my answer than the eraser slipped from my fingers and rolled under the bench in front of me.", "no sooner...than"),
            ("Regardless of how advanced digital tools become, the simple eraser will likely remain a staple in classrooms for generations to come.", "regardless of how"),
        ],
    },

    "notebook": {
        "beginner": [
            ("I write in my notebook.", "simple present"),
            ("The notebook has many pages.", "have/has"),
            ("This is a new notebook.", "demonstrative"),
            ("My notebook is green.", "possessive + adjective"),
            ("Where is my maths notebook?", "question word"),
            ("I forgot my notebook at school.", "past simple"),
            ("Open your notebook now.", "imperative"),
            ("The notebook is in my bag.", "preposition"),
            ("I finished one full notebook.", "past simple + adjective"),
            ("Can I see your notebook?", "request"),
        ],
        "elementary": [
            ("I always write the date on top of each page in my notebook.", "frequency adverb"),
            ("My teacher checked all our notebooks after the class.", "past simple"),
            ("The pages of my notebook are getting torn and messy.", "present continuous"),
            ("I need to buy a new notebook for science.", "need + infinitive"),
            ("Please write neatly in your notebook.", "imperative + adverb"),
            ("There are four different notebooks in my school bag.", "there are + number"),
            ("She copied the notes from my notebook.", "past simple"),
            ("Do not tear pages out of your notebook.", "negative imperative"),
            ("I keep a separate notebook for English grammar.", "keep + for"),
            ("My notebook got wet in the rain and the ink spread everywhere.", "past simple + and"),
        ],
        "intermediate": [
            ("The notebook that I use for English has a bright orange cover.", "relative clause"),
            ("I have been writing in this notebook since January.", "present perfect continuous + since"),
            ("If you keep your notebook neat, it will be easier to revise before the exam.", "first conditional"),
            ("Could you show me how you organised your notes in your notebook?", "polite request + how clause"),
            ("Although the notebook looks thin, it actually has two hundred pages.", "concessive clause"),
            ("The teacher told us to leave two lines between each answer in our notebooks.", "reported speech"),
            ("I would rather use a ruled notebook than a plain one for writing.", "would rather + than"),
            ("My notebook fell into a puddle and half the pages became unreadable.", "past simple + and"),
            ("Have you ever kept a notebook just for writing your own stories and poems?", "present perfect + ever"),
            ("The notebook needs a new cover because the old one has completely torn off.", "because + present perfect"),
        ],
        "upper_intermediate": [
            ("The notebook, which my grandfather gave me on my birthday, has become my most treasured possession.", "non-defining relative clause"),
            ("Had I labelled my notebooks properly, I would not have brought the wrong one to class.", "inverted conditional"),
            ("Despite being filled with scratchy handwriting and doodles, my old notebook brings back many fond memories.", "despite + gerund"),
            ("Not only did the notebook get soaked in the rain, but some of the most important notes were washed away completely.", "not only...but also"),
            ("I wish I had written more carefully in my notebook, as I cannot read some of my own notes now.", "wish + past perfect"),
            ("It is interesting to see how a student's handwriting improves by comparing the first and last pages of their notebook.", "it is + adjective + infinitive"),
            ("The condition of a student's notebook often reflects their attitude towards learning.", "reflects"),
            ("Whoever left their notebook on the library table should collect it before it is thrown away.", "whoever + should"),
            ("Were it not for my well-organised notebook, I would have struggled to revise for the final exam.", "subjunctive inversion"),
            ("The number of notebooks a student uses in a year depends on how much they write in class.", "depends on + how much"),
        ],
        "advanced": [
            ("It is fascinating to look back at old notebooks and trace the gradual development of one's handwriting, vocabulary, and ability to express complex ideas.", "it is + adjective + infinitive"),
            ("One could argue that the notebook serves not merely as a record of lessons taught, but as a personal archive of a student's intellectual growth over the course of an academic year.", "one could argue"),
            ("The notebook that had been gathering dust on my shelf for years turned out to contain the very notes I needed for my project on Indian history.", "past perfect continuous + turned out"),
            ("No sooner had the teacher announced a surprise test than every student frantically began flipping through their notebooks in search of the relevant chapter.", "no sooner...than"),
            ("Regardless of whether one prefers digital note-taking or traditional handwriting, the physical notebook remains a powerful tool for memory retention and active learning.", "regardless of whether"),
        ],
    },

    "pencil": {
        "beginner": [
            ("I draw with a pencil.", "simple present"),
            ("The pencil is long and yellow.", "copula + compound adjective"),
            ("This pencil is very sharp.", "demonstrative + adjective"),
            ("My pencil broke during class.", "past simple"),
            ("Where is my pencil?", "question word"),
            ("I sharpened my pencil.", "past simple"),
            ("Give me a pencil, please.", "imperative"),
            ("The pencil is on the table.", "preposition"),
            ("I have three pencils in my box.", "have + number"),
            ("Can I borrow a pencil?", "request"),
        ],
        "elementary": [
            ("I always keep extra pencils in my bag.", "frequency adverb"),
            ("My pencil keeps breaking whenever I sharpen it.", "present simple + whenever"),
            ("This pencil is darker than the other one.", "comparative"),
            ("I finished the test using only a pencil.", "past simple + gerund"),
            ("Please use a pencil for the rough work.", "imperative + for"),
            ("There were no pencils left in the box.", "there were + negative"),
            ("She drew a beautiful flower with her pencil.", "past simple"),
            ("Do not chew on the end of your pencil.", "negative imperative"),
            ("I prefer pencils for drawing because they are easy to erase.", "preference + because"),
            ("The pencil rolled off the desk and fell on the floor.", "past simple + and"),
        ],
        "intermediate": [
            ("The pencil that I was using during the art class suddenly snapped in half.", "relative clause + past simple"),
            ("I have been using the same pencil for nearly three weeks now.", "present perfect continuous"),
            ("If you hold the pencil correctly, your handwriting will improve.", "first conditional"),
            ("Could you please pick up the pencil that fell behind your chair?", "polite request + relative clause"),
            ("Although pencils seem simple, they are one of the most useful inventions.", "concessive clause"),
            ("The teacher suggested that we use pencils instead of pens for the diagram.", "reported speech + that"),
            ("I would rather write with a sharp pencil than a blunt one.", "would rather + than"),
            ("My pencil lead kept breaking because I was pressing too hard.", "because + past continuous"),
            ("Have you ever wondered how the graphite gets inside a pencil?", "present perfect + ever"),
            ("The pencil should be sharp enough to draw thin, clean lines.", "should + enough"),
        ],
        "upper_intermediate": [
            ("The pencil, which appeared to be an ordinary writing tool, was actually a mechanical one with a twist mechanism.", "non-defining relative clause"),
            ("Had I brought a softer pencil, the shading in my drawing would have looked much smoother.", "inverted conditional"),
            ("Despite being one of the oldest writing instruments, the pencil continues to be widely used in modern classrooms.", "despite + gerund"),
            ("Not only is the pencil useful for writing, but it is also essential for sketching, shading, and technical drawing.", "not only...but also"),
            ("I wish I had not pressed so hard with my pencil, as the deep marks are now impossible to erase.", "wish + past perfect"),
            ("It is estimated that a single pencil can draw a line approximately fifty-six kilometres long.", "it is estimated + that"),
            ("The graphite in a pencil determines how dark or light the marks will be.", "determines + how"),
            ("Whoever sharpened all the pencils before the exam deserves a word of thanks.", "whoever + deserves"),
            ("Were it not for pencils, the art of sketching and drafting would be far more difficult.", "subjunctive inversion"),
            ("The quality of a pencil can be judged by how smoothly it glides across the paper.", "can be judged by"),
        ],
        "advanced": [
            ("It is a testament to the elegance of simple design that the pencil, virtually unchanged for centuries, remains one of the most reliable tools for creative expression and academic work.", "it is + a testament"),
            ("One could argue that the humble pencil, with its capacity for both precision and correction, mirrors the learning process itself, where trial and error lead to eventual mastery.", "one could argue"),
            ("The pencil that had been rolling around the bottom of my drawer for months turned out to be exactly the grade I needed for my still-life drawing.", "past perfect continuous + turned out"),
            ("No sooner had the teacher asked us to begin sketching than I realised that every pencil in my case was either broken or blunt.", "no sooner...than"),
            ("Regardless of how sophisticated digital drawing tablets become, many artists maintain that nothing quite compares to the tactile experience of a graphite pencil on paper.", "regardless of how"),
        ],
    },

    "pointer": {
        "beginner": [
            ("The teacher has a pointer.", "have/has"),
            ("The pointer is long and thin.", "copula + compound adjective"),
            ("That is the teacher's pointer.", "possessive"),
            ("My teacher uses a pointer.", "simple present"),
            ("Where is the pointer?", "question word"),
            ("The pointer fell on the floor.", "past simple"),
            ("Do not play with the pointer.", "negative imperative"),
            ("The pointer is near the board.", "preposition"),
            ("I can see a pointer on the desk.", "can + see"),
            ("The teacher picked up the pointer.", "past simple"),
        ],
        "elementary": [
            ("The teacher used the pointer to show us a word on the board.", "past simple + infinitive"),
            ("Our class teacher always keeps a pointer beside the whiteboard.", "frequency adverb"),
            ("The pointer is made of wood and has a rubber tip.", "made of + and"),
            ("Please bring the pointer from the staff room.", "imperative + from"),
            ("The pointer broke when it fell off the teacher's desk.", "past simple + when"),
            ("Do not use the pointer to hit the desks or the walls.", "negative imperative"),
            ("The science teacher pointed at the diagram with a long metal pointer.", "past simple + with"),
            ("There is a crack in the middle of the pointer.", "there is + preposition"),
            ("Some teachers prefer a laser pointer instead of a wooden one.", "preference"),
            ("The pointer helps the teacher show exactly where to look on the chart.", "helps + infinitive"),
        ],
        "intermediate": [
            ("The pointer that the teacher uses has a small flag attached to the end.", "relative clause"),
            ("I have never seen a pointer as long as the one our geography teacher carries.", "present perfect + never + comparative"),
            ("If the pointer breaks, the teacher will probably use a ruler instead.", "first conditional"),
            ("Could you hand the pointer to the teacher, please?", "polite request"),
            ("Although pointers are rarely used by students, they are common in most classrooms.", "concessive clause"),
            ("The teacher explained the map by sliding the pointer from one city to another.", "by + gerund"),
            ("I would rather the teacher use a pointer than tap on the board with a marker.", "would rather"),
            ("The pointer slipped out of the teacher's hand and landed on the front bench.", "past simple + and"),
            ("Have you ever noticed that the pointer always seems to end up on the wrong desk?", "present perfect + ever"),
            ("The pointer should be kept in a safe place so that it does not break.", "should + so that"),
        ],
        "upper_intermediate": [
            ("The pointer, which had belonged to our previous teacher, now sits unused in the corner of the classroom.", "non-defining relative clause"),
            ("Had the teacher brought the pointer to the science lab, explaining the human skeleton would have been much easier.", "inverted conditional"),
            ("Despite being a simple stick, the pointer commands attention the moment the teacher picks it up.", "despite + gerund"),
            ("Not only does the pointer help the teacher direct our attention, but it also serves as a visual cue to stay focused.", "not only...but also"),
            ("I wish the school had replaced the cracked pointer, as it looks quite unprofessional.", "wish + past perfect"),
            ("It is interesting how a simple pointer can change the way a class pays attention during a lesson.", "it is + adjective + how"),
            ("The effectiveness of a pointer depends entirely on how the teacher uses it.", "depends on + how"),
            ("Whoever finds the missing pointer should leave it on the teacher's table before the next period.", "whoever + should"),
            ("Were it not for the pointer, the teacher would have had difficulty showing the small details on the world map.", "subjunctive inversion"),
            ("A well-used pointer, combined with clear explanation, can make even the most difficult topic easy to understand.", "can make"),
        ],
        "advanced": [
            ("It is worth reflecting on how the presence of a simple pointer in a teacher's hand subtly shifts the dynamics of a classroom, directing collective attention with a single gesture.", "it is worth + gerund"),
            ("One might argue that the pointer is not merely a teaching aid, but a symbol of authority and guidance that has persisted in educational settings for centuries.", "one might argue"),
            ("The pointer that had been leaning against the blackboard all year finally broke on the very last day of school, as if it too had grown tired.", "past perfect continuous + as if"),
            ("No sooner had the teacher raised the pointer towards the map than every student in the room instinctively looked in the direction it was pointing.", "no sooner...than"),
            ("Regardless of whether classrooms adopt digital projectors or interactive whiteboards, the physical pointer retains a certain directness and simplicity that technology cannot entirely replicate.", "regardless of whether"),
        ],
    },

    "scale": {
        "beginner": [
            ("I draw lines with a scale.", "simple present"),
            ("The scale is thirty centimetres long.", "copula + measurement"),
            ("This is my new scale.", "demonstrative"),
            ("My scale is made of plastic.", "made of"),
            ("Where did I put my scale?", "past simple question"),
            ("I broke my scale yesterday.", "past simple"),
            ("Give me your scale for a minute.", "imperative"),
            ("The scale is inside my geometry box.", "preposition"),
            ("I need a scale to draw this line.", "need + infinitive"),
            ("Can I borrow your scale?", "request"),
        ],
        "elementary": [
            ("I used my scale to draw a straight line in my notebook.", "past simple + infinitive"),
            ("The markings on my old scale have faded.", "present perfect"),
            ("This scale has both centimetre and inch markings.", "has + both...and"),
            ("I always use a scale when I draw diagrams in science.", "frequency adverb + when"),
            ("Please draw the margin with a scale and a sharp pencil.", "imperative + with"),
            ("There are many colourful scales in the stationery shop.", "there are + adjective"),
            ("My scale cracked in the middle when I sat on it by mistake.", "past simple + when"),
            ("Do not use the scale to hit anyone.", "negative imperative"),
            ("A metal scale lasts longer than a plastic one.", "comparative"),
            ("The teacher measured the length of the paper with a scale.", "past simple + with"),
        ],
        "intermediate": [
            ("The scale that I keep in my geometry box is exactly fifteen centimetres long.", "relative clause + exactly"),
            ("I have been using this scale since the third grade.", "present perfect continuous + since"),
            ("If you do not use a scale, your lines will not be straight.", "first conditional + negative"),
            ("Could you measure this distance with your scale and tell me how long it is?", "polite request + and"),
            ("Although the scale looks ordinary, it is essential for drawing neat diagrams.", "concessive clause"),
            ("The teacher instructed us to underline the heading using a scale.", "reported speech + gerund"),
            ("I would rather use a transparent scale so that I can see through it.", "would rather + so that"),
            ("My scale snapped in two while I was trying to bend it.", "past simple + while"),
            ("Have you ever used a triangular scale that architects use for their drawings?", "present perfect + ever"),
            ("The scale should be placed flat on the paper before drawing any line.", "should + passive"),
        ],
        "upper_intermediate": [
            ("The scale, which I received as part of a geometry set, turned out to be the most frequently used tool in my pencil case.", "non-defining relative clause"),
            ("Had I brought my scale to the exam, I would not have drawn such crooked lines in the diagram.", "inverted conditional"),
            ("Despite being a very basic tool, the scale teaches students the importance of precision in measurement.", "despite + gerund"),
            ("Not only is the scale used for drawing lines, but it is also helpful for measuring lengths accurately.", "not only...but also"),
            ("I wish I had bought a sturdier scale, as the plastic one broke within the first week.", "wish + past perfect"),
            ("It is surprising how often students forget to bring their scale to class, even for geometry lessons.", "it is + adjective + how often"),
            ("The accuracy of a diagram depends largely on how carefully you place the scale on the paper.", "depends on + how"),
            ("Whoever borrowed my scale from the desk should return it before the drawing period.", "whoever + should"),
            ("Were it not for the scale, drawing precise geometric figures by hand would be nearly impossible.", "subjunctive inversion"),
            ("The steel scale that my father used during his school days is still in perfect condition after thirty years.", "that clause + after"),
        ],
        "advanced": [
            ("It is remarkable that such a simple instrument as a ruler can instil in young learners an appreciation for accuracy, measurement, and the mathematical principles that underpin the physical world.", "it is remarkable that"),
            ("One could argue that the scale represents one of the earliest introductions a child has to the concept of standardised measurement, bridging the gap between intuitive estimation and precise quantification.", "one could argue"),
            ("The scale that had been sitting at the bottom of my geometry box for the entire semester was the only tool I could find when the teacher announced a surprise diagram test.", "past perfect continuous"),
            ("No sooner had the teacher asked us to draw the construction than I discovered that my scale had a chip at the zero-centimetre mark, making accurate measurement impossible.", "no sooner...than"),
            ("Regardless of whether students eventually move on to computer-aided design tools, the foundational skill of using a scale to draw and measure by hand remains an essential part of early education.", "regardless of whether"),
        ],
    },

}


# ═══════════════════════════════════════════════════════════════════════════
#  HAND-CRAFTED DIALOGUES — 8 objects × 5 levels × 3 variants × 4 turns
# ═══════════════════════════════════════════════════════════════════════════

DIALOGUES = {

    "sharpner": {
        "beginner": [
            [("learner", "Can I use your sharpner?"), ("system", "Yes, here you go."), ("learner", "Thank you. My pencil is very blunt."), ("system", "You are welcome.")],
            [("learner", "Where is my sharpner?"), ("system", "I think it is in your pencil box."), ("learner", "Oh yes, I found it."), ("system", "Good. Now sharpen your pencil quickly.")],
            [("learner", "I lost my sharpner."), ("system", "Check under your desk."), ("learner", "It is not there."), ("system", "You can share mine for now.")],
        ],
        "elementary": [
            [("learner", "My sharpner broke during the maths class."), ("system", "That is unfortunate. What happened?"), ("learner", "The blade came out when I was sharpening my pencil."), ("system", "Be careful next time. You can buy a new one after school.")],
            [("learner", "Do you think this sharpner is good?"), ("system", "It looks fine. Is it new?"), ("learner", "Yes, I bought it yesterday from the bookshop."), ("system", "Try sharpening your pencil and see if it works well.")],
            [("learner", "I need a sharpner with two holes."), ("system", "Why do you need two holes?"), ("learner", "One is for thin pencils and the other is for thick colour pencils."), ("system", "That makes sense. The stationery shop near school has those.")],
        ],
        "intermediate": [
            [("learner", "I have been looking for a good sharpner for weeks."), ("system", "What kind of sharpner do you prefer?"), ("learner", "I want one with a container to catch the shavings."), ("system", "That is a smart choice. It keeps your desk clean.")],
            [("learner", "Could you recommend a sharpner that works well with colour pencils?"), ("system", "You should try a sharpner with a wider hole and a sharp blade."), ("learner", "Do they cost much more than regular sharpners?"), ("system", "Not really. They are only slightly more expensive.")],
            [("learner", "My sharpner always breaks the pencil tip instead of sharpening it."), ("system", "The blade might be dull. Have you tried replacing it?"), ("learner", "I did not know you could replace sharpner blades."), ("system", "Yes, some sharpners have a small screw that holds the blade in place.")],
        ],
        "upper_intermediate": [
            [("learner", "I find it interesting that something as small as a sharpner can affect the quality of your drawing."), ("system", "That is very true. A sharp pencil makes clean, precise lines."), ("learner", "I noticed my sketches improved after I started using a better sharpner."), ("system", "Good tools make a real difference, even simple ones like sharpners.")],
            [("learner", "Had I not forgotten my sharpner at home, I would have finished the diagram on time."), ("system", "That must have been frustrating during the test."), ("learner", "It was. I had to borrow one and it wasted several minutes."), ("system", "Perhaps keeping a spare in your school bag would prevent that from happening again.")],
            [("learner", "Do you think electric sharpners are better than manual ones?"), ("system", "They are faster, but they can over-sharpen and waste the pencil."), ("learner", "I suppose a manual sharpner gives you more control."), ("system", "Exactly. For drawing especially, manual sharpners are often preferred.")],
        ],
        "advanced": [
            [("learner", "It is remarkable how the design of sharpners has barely changed over the decades."), ("system", "That is because the basic mechanism is already very efficient."), ("learner", "I suppose there is an elegance in simplicity when it comes to everyday tools."), ("system", "Indeed. Sometimes the simplest solutions are the ones that endure the longest.")],
            [("learner", "One could argue that the quality of classroom stationery, including sharpners, reflects the resources available to a school."), ("system", "That is a thoughtful observation. Access to good tools does affect learning."), ("learner", "I noticed that students with better stationery tend to take more pride in their work."), ("system", "There is likely a connection between having the right tools and developing good study habits.")],
            [("learner", "Regardless of how advanced digital tools become, I believe physical tools like sharpners will always have a place in primary classrooms."), ("system", "I agree. Young children benefit from the tactile experience of writing and drawing by hand."), ("learner", "There is something satisfying about sharpening a pencil and seeing those clean curls of wood."), ("system", "Absolutely. It is a small ritual that connects the student to the act of creating.")],
        ],
    },

    "ballpen": {
        "beginner": [
            [("learner", "Can I borrow your ballpen?"), ("system", "Of course. Here it is."), ("learner", "Thank you. Mine stopped working."), ("system", "You are welcome. Return it after the class.")],
            [("learner", "I have a new blue ballpen."), ("system", "It looks nice. Where did you get it?"), ("learner", "My mother bought it for me."), ("system", "That is a good ballpen for writing.")],
            [("learner", "My ballpen is not writing."), ("system", "Try shaking it a little."), ("learner", "It is still not working."), ("system", "The ink may have run out. Use a pencil for now.")],
        ],
        "elementary": [
            [("learner", "Which colour ballpen should I use for the test?"), ("system", "The teacher said we must use blue or black."), ("learner", "I only have a red ballpen today."), ("system", "You can borrow my blue one. I have a spare.")],
            [("learner", "My ballpen leaked inside my pencil case."), ("system", "Oh no. Is everything stained?"), ("learner", "Yes, there is ink on my eraser and sharpner too."), ("system", "Let us clean it up before the next class starts.")],
            [("learner", "I think ballpens are better than pencils for writing."), ("system", "Why do you think so?"), ("learner", "Because ballpen writing looks neater and does not smudge."), ("system", "That is true, but pencils are easier to correct.")],
        ],
        "intermediate": [
            [("learner", "I have been searching for a ballpen that writes smoothly without skipping."), ("system", "Have you tried gel ballpens? They usually write very smoothly."), ("learner", "I have, but they tend to run out of ink faster than regular ones."), ("system", "That is the trade-off. Smooth writing often means more ink consumption.")],
            [("learner", "Could you explain why some ballpens stop working even when they still have ink?"), ("system", "It usually happens when air gets trapped in the refill tube."), ("learner", "Is there any way to fix it?"), ("system", "Sometimes warming the tip gently or scribbling on rough paper can help restart the flow.")],
            [("learner", "The teacher told us not to use ballpens for the geometry diagram."), ("system", "That makes sense. Pencil lines are easier to erase and correct."), ("learner", "But I find it difficult to draw neat lines with a pencil."), ("system", "Practice will help. Use a sharp pencil and a steady hand.")],
        ],
        "upper_intermediate": [
            [("learner", "The ballpen that my uncle gave me has a very smooth grip and writes beautifully."), ("system", "Good writing instruments can make a real difference to how you feel about writing."), ("learner", "I have noticed that I actually enjoy taking notes more when I use a comfortable pen."), ("system", "That is an interesting observation. The right tool can genuinely motivate you.")],
            [("learner", "Had the ballpen not leaked in my pocket, my school uniform would not have been ruined."), ("system", "That sounds like it was quite a disaster."), ("learner", "It was. The stain would not come off even after washing it twice."), ("system", "In the future, always keep the cap on tightly, especially when the pen is in your pocket.")],
            [("learner", "It concerns me that millions of plastic ballpens are thrown away every year around the world."), ("system", "That is a valid environmental concern."), ("learner", "Perhaps schools should encourage the use of refillable pens instead of disposable ones."), ("system", "That would be a practical step towards reducing plastic waste from classrooms.")],
        ],
        "advanced": [
            [("learner", "It is fascinating that the ballpoint pen was invented to solve the specific problem of fountain pen ink smudging on paper."), ("system", "Yes, and the rotating ball mechanism was a brilliantly simple engineering solution."), ("learner", "I read that early ballpens were considered luxury items and were quite expensive."), ("system", "That is correct. It took several decades of manufacturing improvements before they became affordable for everyone.")],
            [("learner", "One might argue that the shift from fountain pens to ballpens changed not only writing habits but also handwriting itself."), ("system", "That is an interesting perspective. Could you elaborate?"), ("learner", "Ballpens require less pressure variation, so the flowing, expressive strokes of fountain pen writing gradually disappeared."), ("system", "You make a compelling point. The tool we write with does shape how our writing looks and feels.")],
            [("learner", "Regardless of the rise of digital communication, I believe the physical act of writing with a ballpen engages the brain differently."), ("system", "Research does support that claim. Handwriting activates areas of the brain associated with memory and comprehension."), ("learner", "Perhaps that is why taking notes by hand often helps me remember things better than typing."), ("system", "Indeed. The slower pace of handwriting forces you to process and summarise information rather than just transcribing it.")],
        ],
    },

    "book": {
        "beginner": [
            [("learner", "I have a new book."), ("system", "What is it about?"), ("learner", "It is about animals in the forest."), ("system", "That sounds very interesting.")],
            [("learner", "Where is my English book?"), ("system", "Did you check your bag?"), ("learner", "Yes, I found it. It was at the bottom."), ("system", "Good. Open it to page twenty.")],
            [("learner", "Can I read your book?"), ("system", "Of course. I finished reading it yesterday."), ("learner", "Thank you. I will return it next week."), ("system", "Take your time. There is no hurry.")],
        ],
        "elementary": [
            [("learner", "I read three books during the holidays."), ("system", "That is wonderful. Which one did you like the most?"), ("learner", "I liked the story about a boy who travels around the world."), ("system", "Adventure stories are always fun to read.")],
            [("learner", "My book has a torn page in the middle."), ("system", "How did that happen?"), ("learner", "I think someone pulled it out by mistake."), ("system", "You can fix it with some tape. Be careful next time.")],
            [("learner", "The teacher asked us to read chapter five before tomorrow."), ("system", "Have you started reading it?"), ("learner", "Not yet. I will read it after dinner."), ("system", "Do not leave it too late or you might fall asleep.")],
        ],
        "intermediate": [
            [("learner", "I have been reading a book about the solar system and it is absolutely fascinating."), ("system", "What is the most interesting thing you have learned so far?"), ("learner", "I learned that Jupiter has more than seventy moons."), ("system", "That is incredible. Books are such a wonderful source of knowledge.")],
            [("learner", "Could you suggest a book that would help me improve my English vocabulary?"), ("system", "I would recommend reading story books with slightly challenging language."), ("learner", "Should I look up every new word in the dictionary?"), ("system", "Try to understand the meaning from context first. Look it up only if you are really stuck.")],
            [("learner", "The book I borrowed from the library is due tomorrow, but I am only halfway through."), ("system", "Can you renew it for another week?"), ("learner", "I am not sure. I will ask the librarian during the break."), ("system", "That would be a good idea. Most libraries allow at least one renewal.")],
        ],
        "upper_intermediate": [
            [("learner", "The book that won the national award this year was written by a teacher from a small village."), ("system", "That is inspiring. What is the book about?"), ("learner", "It tells the story of children in a rural school who overcome many challenges to pursue their dreams."), ("system", "Stories like that remind us that determination can triumph over difficult circumstances.")],
            [("learner", "Had I started the book a few days earlier, I would have had time to discuss it properly in class."), ("system", "Did you feel unprepared during the discussion?"), ("learner", "A little, yes. I had only skimmed the last three chapters."), ("system", "Next time, try setting a reading schedule so that you finish well before the deadline.")],
            [("learner", "It saddens me that many schools in rural areas do not have enough books in their libraries."), ("system", "That is an important issue. Access to books is essential for quality education."), ("learner", "I have been thinking about organising a book donation drive at our school."), ("system", "That is a wonderful idea. I am sure many students would be willing to contribute their old books.")],
        ],
        "advanced": [
            [("learner", "It is often said that a single book has the power to change the course of a person's life."), ("system", "Do you believe that from personal experience?"), ("learner", "Yes. A book about scientists inspired me to take a serious interest in physics."), ("system", "That is a perfect example of how literature can ignite a passion that shapes one's future.")],
            [("learner", "One could argue that the decline in recreational reading among children is a direct consequence of increased screen time."), ("system", "There is certainly data to support that view. Do you think anything can reverse the trend?"), ("learner", "I believe schools could dedicate a regular reading period where students read books of their own choice."), ("system", "Giving students autonomy in their reading choices is one of the most effective ways to foster a genuine love of books.")],
            [("learner", "Regardless of the format, whether printed or digital, the essence of a book lies in its ability to transport the reader to a different world."), ("system", "That is a beautifully expressed thought. Do you have a preference between the two formats?"), ("learner", "I prefer printed books because the physical sensation of turning pages adds to the experience."), ("system", "Many readers share that sentiment. There is an intimacy to holding a physical book that screens cannot quite replicate.")],
        ],
    },

    "eraser": {
        "beginner": [
            [("learner", "Can I use your eraser?"), ("system", "Yes, of course. Here you are."), ("learner", "Thank you. I made a mistake."), ("system", "No problem. Everyone makes mistakes.")],
            [("learner", "I lost my eraser."), ("system", "Look inside your desk."), ("learner", "I found it. It was under my book."), ("system", "Good. Try not to lose it again.")],
            [("learner", "My eraser smells like mango."), ("system", "Really? That is funny."), ("learner", "Yes, it is a fruit-shaped eraser."), ("system", "That is a cute eraser. Where did you buy it?")],
        ],
        "elementary": [
            [("learner", "My eraser is leaving marks on the paper instead of cleaning them."), ("system", "It might be too old or too hard."), ("learner", "Should I buy a new one?"), ("system", "Yes, a soft white eraser usually works the best.")],
            [("learner", "Someone took my eraser from my desk."), ("system", "Are you sure you did not drop it?"), ("learner", "I checked everywhere. It was definitely on my desk before the break."), ("system", "Ask your neighbours politely. They might have picked it up by mistake.")],
            [("learner", "Do you know why some erasers are pink and some are white?"), ("system", "The colour usually depends on the material they are made from."), ("learner", "Which type erases better?"), ("system", "White vinyl erasers are generally softer and cleaner.")],
        ],
        "intermediate": [
            [("learner", "I have been trying to erase this pencil mark but it will not come off completely."), ("system", "You might have pressed too hard when you wrote it."), ("learner", "Is there a way to remove deep pencil marks?"), ("system", "A kneaded eraser might work better for heavy marks. It lifts the graphite gently.")],
            [("learner", "Could you explain why erasers can remove pencil marks but not ballpen ink?"), ("system", "Pencil marks sit on the surface as graphite particles, which the eraser can rub away."), ("learner", "And ballpen ink soaks into the paper fibres?"), ("system", "Exactly. That is why ink marks are much harder to remove.")],
            [("learner", "The teacher told us to erase our rough work before submitting the answer sheet."), ("system", "Did you manage to erase everything neatly?"), ("learner", "Most of it, but some faint marks are still visible."), ("system", "That should be fine. The teacher will understand.")],
        ],
        "upper_intermediate": [
            [("learner", "I find it interesting that erasers were originally made from natural rubber."), ("system", "Yes, that is actually where the word rubber comes from in British English."), ("learner", "So the act of rubbing out pencil marks literally gave the material its name?"), ("system", "Precisely. Language often preserves the history of how objects were originally used.")],
            [("learner", "Had I not had an eraser during the exam, my answer sheet would have looked terribly messy."), ("system", "A clean presentation does matter, especially in exams."), ("learner", "I agree. Being able to correct mistakes neatly gives you more confidence."), ("system", "It also shows the examiner that you care about the quality of your work.")],
            [("learner", "It seems wasteful that erasers get smaller and smaller until you cannot hold them anymore."), ("system", "That is true. Most of the eraser ends up as tiny crumbs on the desk."), ("learner", "I wonder if someone could design an eraser holder, like a pencil holder, to use the last bit."), ("system", "That is actually a clever idea. Some companies do make eraser holders for exactly that reason.")],
        ],
        "advanced": [
            [("learner", "It is worth noting that the eraser symbolises something important in education: the freedom to make mistakes without permanent consequences."), ("system", "That is a profound observation. The ability to correct encourages risk-taking in learning."), ("learner", "I think classrooms should celebrate mistakes as part of the learning process rather than penalising them."), ("system", "Many modern educational philosophies share that view. A growth mindset values effort and correction over perfection.")],
            [("learner", "One might argue that the eraser is a metaphor for resilience: no matter how many mistakes you make, you can always start again on a clean page."), ("system", "That is a beautiful way to think about it. Have you always seen everyday objects in such symbolic terms?"), ("learner", "I started thinking this way after reading an essay about how simple tools reflect deeper human values."), ("system", "Literature has a wonderful way of helping us see the extraordinary in the ordinary.")],
            [("learner", "Regardless of whether we move to entirely digital classrooms, I believe the concept behind the eraser, the ability to undo and revise, will always remain fundamental to learning."), ("system", "Absolutely. The undo button on a computer is essentially the digital descendant of the eraser."), ("learner", "That is an interesting parallel. Both serve the same psychological purpose of reducing the fear of making errors."), ("system", "And that freedom is precisely what allows learners to experiment, explore, and ultimately grow.")],
        ],
    },

    "notebook": {
        "beginner": [
            [("learner", "I need a new notebook."), ("system", "What happened to your old one?"), ("learner", "It is full. There are no more pages."), ("system", "Let us buy a new one after school.")],
            [("learner", "Where is my notebook?"), ("system", "Is it in your bag?"), ("learner", "No, I think I left it in class."), ("system", "Go and check before someone takes it.")],
            [("learner", "My notebook is very neat."), ("system", "That is great. Your teacher will be happy."), ("learner", "I write carefully every day."), ("system", "Keep up the good work.")],
        ],
        "elementary": [
            [("learner", "I spilled water on my notebook and the ink started spreading."), ("system", "Oh no. How many pages were damaged?"), ("learner", "About five or six pages. The writing is not readable anymore."), ("system", "Try drying it in the sun. You may need to rewrite those pages.")],
            [("learner", "How many notebooks do you use for school?"), ("system", "I use one for each subject, so about six in total."), ("learner", "That is a lot. I only use four."), ("system", "It depends on the school. Some teachers want separate notebooks for classwork and homework.")],
            [("learner", "The teacher asked us to bring a new notebook for project work."), ("system", "What size does she want?"), ("learner", "She said a big one with plain pages, not ruled ones."), ("system", "We can find one at the bookshop near the bus stop.")],
        ],
        "intermediate": [
            [("learner", "I have been maintaining a separate notebook for new English words I learn."), ("system", "That is an excellent habit. How many words have you collected so far?"), ("learner", "About a hundred and fifty. I also write the meaning and a sentence for each word."), ("system", "That is very thorough. Reviewing it regularly will help you remember them.")],
            [("learner", "Could you tell me how you keep your notebook so well organised?"), ("system", "I always write the date and topic at the top, and I leave space between sections."), ("learner", "I tend to write everything together without any gaps."), ("system", "Try using headings and bullet points. It makes revision much easier.")],
            [("learner", "The notebook I was using for maths ran out of pages right before the revision started."), ("system", "Did you start a new one?"), ("learner", "Yes, but now my notes are split across two notebooks, which is confusing."), ("system", "You could number the pages and create a small index at the back to help you find topics quickly.")],
        ],
        "upper_intermediate": [
            [("learner", "The notebook that I used throughout the year has become a kind of personal record of everything I learned."), ("system", "That is a wonderful way to look at it."), ("learner", "I sometimes flip through old notebooks and I am surprised by how much I have improved."), ("system", "Seeing your own progress is one of the most rewarding aspects of keeping good notes.")],
            [("learner", "Had I organised my notebook by topic instead of by date, revision would have been much more efficient."), ("system", "Organisation is something most students learn through trial and error."), ("learner", "I plan to use a different system next year with colour-coded sections."), ("system", "That sounds like a well-thought-out plan. Colour coding helps your brain retrieve information faster.")],
            [("learner", "It surprises me that some students throw away their notebooks at the end of the year."), ("system", "That is a shame. Old notebooks can be very useful for revision."), ("learner", "I always keep mine. They serve as a reference whenever I need to revisit a topic."), ("system", "That is a smart approach. Your future self will thank you for keeping them.")],
        ],
        "advanced": [
            [("learner", "It is fascinating how a notebook can serve as both a learning tool and a record of personal intellectual development."), ("system", "You raise an excellent point. Few objects capture a student's journey as directly as a notebook."), ("learner", "I read that many famous scientists and writers kept detailed notebooks throughout their lives."), ("system", "Indeed. Leonardo da Vinci's notebooks, for example, are considered some of the most remarkable documents in human history.")],
            [("learner", "One could argue that the practice of handwriting notes in a notebook engages the brain more deeply than typing on a screen."), ("system", "Research in cognitive science supports that claim."), ("learner", "The slower pace of writing forces you to think about and summarise information rather than just copying it."), ("system", "Exactly. That processing step is what strengthens understanding and long-term retention.")],
            [("learner", "Regardless of how technology transforms education, I believe the notebook will remain a cornerstone of the student experience."), ("system", "What makes you so confident about that?"), ("learner", "Because the act of writing by hand connects thinking to a physical action, which digital tools cannot fully replicate."), ("system", "That is a compelling argument. The notebook bridges the gap between thought and tangible expression in a way that feels uniquely personal.")],
        ],
    },

    "pencil": {
        "beginner": [
            [("learner", "I need a pencil."), ("system", "Here, take this one."), ("learner", "Thank you. My pencil broke."), ("system", "You are welcome. Be careful not to drop it.")],
            [("learner", "My pencil is very short."), ("system", "You have used it a lot."), ("learner", "Yes, I need a new one."), ("system", "Ask your mother to buy one today.")],
            [("learner", "I like drawing with a pencil."), ("system", "What do you like to draw?"), ("learner", "I draw trees and houses."), ("system", "That sounds lovely. Keep practising.")],
        ],
        "elementary": [
            [("learner", "My pencil keeps breaking every time I sharpen it."), ("system", "The lead inside might be cracked."), ("learner", "Should I throw it away?"), ("system", "Yes, get a new one. A good pencil should not break so easily.")],
            [("learner", "Do you know the difference between an HB pencil and a 2B pencil?"), ("system", "An HB pencil is harder and lighter, while a 2B is softer and darker."), ("learner", "Which one should I use for my drawings?"), ("system", "Use HB for outlines and 2B for shading and darker areas.")],
            [("learner", "I dropped my pencil during the test and it rolled away."), ("system", "Did you manage to get it back?"), ("learner", "Yes, but I wasted time looking for it under the benches."), ("system", "Next time, keep a spare pencil on your desk just in case.")],
        ],
        "intermediate": [
            [("learner", "I have been practising pencil shading for my art class."), ("system", "How is it going so far?"), ("learner", "It is getting better, but I still struggle with making smooth gradients."), ("system", "Try tilting the pencil and using the side of the lead. It gives a softer, more even shade.")],
            [("learner", "Could you explain why some pencils have an eraser on one end?"), ("system", "It is simply for convenience so that you do not need to carry a separate eraser."), ("learner", "But those built-in erasers never seem to work very well."), ("system", "You are right. They tend to be harder and can sometimes smear the graphite instead of removing it.")],
            [("learner", "The teacher mentioned that pencils were once considered very expensive writing tools."), ("system", "That is true. Before mass production, only wealthy people could afford them."), ("learner", "It is hard to imagine a time when a simple pencil was a luxury."), ("system", "Technology and manufacturing have made many everyday objects accessible that were once rare.")],
        ],
        "upper_intermediate": [
            [("learner", "I have noticed that the pencil I use for writing feels different from the one I use for art."), ("system", "That is because they likely have different graphite grades."), ("learner", "The writing pencil feels harder and leaves a lighter mark."), ("system", "Yes, writing pencils are usually HB grade for a balance of darkness and precision, while art pencils range from hard H to soft B.")],
            [("learner", "Had I used a softer pencil for the landscape drawing, the shadows would have looked more realistic."), ("system", "Pencil grade selection is an important skill in art."), ("learner", "I am starting to understand that the right tools matter as much as technique."), ("system", "Absolutely. A skilled artist knows how to match the pencil to the purpose.")],
            [("learner", "It occurred to me that the pencil is one of the few tools that is both creative and correctable."), ("system", "What do you mean by that?"), ("learner", "Unlike a pen, anything you write or draw with a pencil can be erased and redone."), ("system", "That is a keen observation. The pencil offers a unique combination of permanence and flexibility.")],
        ],
        "advanced": [
            [("learner", "It is a testament to the enduring design of the pencil that it has remained virtually unchanged for over four hundred years."), ("system", "Few inventions can claim such remarkable longevity."), ("learner", "I think its simplicity is precisely what has allowed it to survive in a world of constant technological change."), ("system", "You make an excellent point. True elegance in design often lies in doing one thing exceptionally well.")],
            [("learner", "One could argue that the pencil democratised education by making writing accessible to people of all social classes."), ("system", "That is a historically significant claim. Can you elaborate?"), ("learner", "Before cheap pencils became widely available, most people simply could not afford the tools needed to write or draw."), ("system", "And affordable pencils, combined with paper, opened the door to mass literacy. That is a powerful historical connection.")],
            [("learner", "Regardless of the rise of digital art tools, many professional artists still begin their work with a simple graphite pencil on paper."), ("system", "Why do you think that is?"), ("learner", "I believe it is because the directness and immediacy of pencil on paper allows ideas to flow without the barrier of technology."), ("system", "That resonates with what many artists describe as the intimacy of the creative process, a direct connection between hand and mind.")],
        ],
    },

    "pointer": {
        "beginner": [
            [("learner", "What is that long stick?"), ("system", "That is the teacher's pointer."), ("learner", "What does the teacher use it for?"), ("system", "She uses it to point at words on the board.")],
            [("learner", "The pointer is on the floor."), ("system", "Please pick it up."), ("learner", "Here it is. I will put it on the desk."), ("system", "Thank you. The teacher will need it soon.")],
            [("learner", "The teacher pointed at me with the pointer."), ("system", "She wanted you to answer the question."), ("learner", "I was scared for a moment."), ("system", "Do not worry. She just wanted your attention.")],
        ],
        "elementary": [
            [("learner", "Our teacher broke the pointer by accident today."), ("system", "What happened?"), ("learner", "She tapped it too hard on the desk and it snapped."), ("system", "I hope the school gives her a new one soon.")],
            [("learner", "Why does the teacher use a pointer instead of just her finger?"), ("system", "Because the board is too big and her hand might block the view."), ("learner", "That makes sense. The pointer reaches higher too."), ("system", "Exactly. It helps everyone in the class see clearly.")],
            [("learner", "Some teachers use a laser pointer instead of a wooden one."), ("system", "Yes, the red dot is easy to see on a screen."), ("learner", "I think laser pointers look more modern."), ("system", "They are useful, but you must never shine them in anyone's eyes.")],
        ],
        "intermediate": [
            [("learner", "I have noticed that the teacher uses the pointer more during map lessons."), ("system", "That is because maps have many small labels and details."), ("learner", "It does help us follow exactly where she is pointing."), ("system", "A pointer bridges the gap between the teacher and a large visual display.")],
            [("learner", "Could you imagine teaching a class without any pointer or similar tool?"), ("system", "It would be difficult, especially with large diagrams or charts."), ("learner", "I suppose the teacher would have to walk up to the board every time."), ("system", "That would slow down the lesson and break the flow of explanation.")],
            [("learner", "The pointer our teacher uses has the school name engraved on it."), ("system", "That is a nice touch. Is it a special one?"), ("learner", "I think it was a gift from the students of the previous batch."), ("system", "What a thoughtful gesture. It shows the bond between students and teachers.")],
        ],
        "upper_intermediate": [
            [("learner", "I find it fascinating how a simple pointer changes the dynamic of a classroom."), ("system", "In what way?"), ("learner", "When the teacher picks up the pointer, everyone instinctively looks at the board."), ("system", "That is a keen observation about non-verbal communication and classroom management.")],
            [("learner", "Had the pointer not been available during the geography lesson, explaining the river system would have been very confusing."), ("system", "Visual guidance is essential when dealing with complex diagrams."), ("learner", "The teacher traced the entire path of the river using the pointer, from source to sea."), ("system", "That kind of visual storytelling makes abstract information concrete and memorable.")],
            [("learner", "Do you think pointers will eventually be replaced entirely by interactive whiteboards?"), ("system", "Technology is certainly changing how teachers present information."), ("learner", "But I think there is something direct and personal about a teacher using a physical pointer."), ("system", "I agree. Technology enhances teaching, but human gestures and presence remain irreplaceable.")],
        ],
        "advanced": [
            [("learner", "It is interesting to consider the pointer as an extension of the teacher's hand, bridging the physical space between the educator and the material being taught."), ("system", "That is an insightful way to frame it."), ("learner", "In a sense, the pointer materialises the teacher's attention and directs the collective gaze of the class."), ("system", "You are describing something that education theorists call shared attention, and you are right that the pointer facilitates it beautifully.")],
            [("learner", "One might argue that the pointer is one of the oldest teaching technologies, predating even the blackboard itself."), ("system", "That is likely true. Pointing sticks have been used by teachers for centuries."), ("learner", "And yet, despite all the advances in educational technology, many teachers still reach for a simple wooden pointer."), ("system", "Perhaps because its simplicity is its strength. It does exactly one thing, and it does it well.")],
            [("learner", "Regardless of whether a teacher uses a traditional pointer, a laser, or a digital pen, the underlying purpose remains the same: to guide the student's focus."), ("system", "Absolutely. The tool changes, but the pedagogical function endures."), ("learner", "I think that speaks to something fundamental about teaching: it is ultimately about directing attention to what matters."), ("system", "That is a remarkably mature insight. Attention is indeed the foundation upon which all learning is built.")],
        ],
    },

    "scale": {
        "beginner": [
            [("learner", "Can I borrow your scale?"), ("system", "Yes, here it is."), ("learner", "Thank you. I need to draw a line."), ("system", "You are welcome. Give it back after you finish.")],
            [("learner", "My scale is broken."), ("system", "What happened to it?"), ("learner", "It cracked when I sat on it."), ("system", "Be more careful next time. Put it inside your box.")],
            [("learner", "How long is this scale?"), ("system", "It is thirty centimetres long."), ("learner", "That is enough for my drawing."), ("system", "Yes, thirty centimetres is the standard size.")],
        ],
        "elementary": [
            [("learner", "I used my scale to measure the length of my textbook."), ("system", "How long was it?"), ("learner", "It was about twenty-four centimetres."), ("system", "Good job. Measuring things around you is a great way to practise.")],
            [("learner", "My friend has a metal scale and I have a plastic one."), ("system", "Do you know which one is better?"), ("learner", "I think the metal one is stronger and does not bend."), ("system", "That is true, but metal scales can be heavier to carry around.")],
            [("learner", "The teacher asked us to draw a rectangle using a scale and pencil."), ("system", "Did you remember to mark the measurements first?"), ("learner", "Yes, I marked five centimetres and three centimetres for the sides."), ("system", "Well done. Always measure before you draw for accurate shapes.")],
        ],
        "intermediate": [
            [("learner", "I have been practising drawing parallel lines using my scale and set square."), ("system", "How is it going?"), ("learner", "It is tricky to keep the scale steady while drawing the line."), ("system", "Press down firmly with one hand and draw with the other. It takes practice to get it right.")],
            [("learner", "Could you tell me why architects use a triangular scale with three different measurement systems?"), ("system", "It allows them to measure in different scales without converting numbers."), ("learner", "So one edge might represent metres and another might represent centimetres?"), ("system", "Exactly. It saves time when working with blueprints at different scales.")],
            [("learner", "The markings on my scale are starting to fade after months of use."), ("system", "That happens with cheaper plastic scales over time."), ("learner", "Should I buy a new one or can I still use this one?"), ("system", "If the millimetre marks are unclear, it is best to replace it for accuracy.")],
        ],
        "upper_intermediate": [
            [("learner", "I find it satisfying to draw perfectly straight lines using a good scale and a sharp pencil."), ("system", "There is a certain pleasure in precision, is there not?"), ("learner", "Yes, especially when a geometry diagram comes out looking clean and professional."), ("system", "That attention to neatness often translates into better marks and clearer thinking.")],
            [("learner", "Had I used my scale properly instead of drawing freehand, the diagram would have been much more accurate."), ("system", "Did the teacher notice the difference?"), ("learner", "Yes, she pointed out that my angles were slightly off because the lines were not straight."), ("system", "In geometry, even small inaccuracies can lead to incorrect conclusions. The scale is not optional.")],
            [("learner", "It strikes me that the scale is one of the earliest tools a child learns to use in school."), ("system", "That is true. It is often introduced as early as the first or second grade."), ("learner", "And yet it remains relevant all the way through engineering and architecture courses."), ("system", "The principle of accurate measurement is foundational. The tool may become more sophisticated, but the concept stays the same.")],
        ],
        "advanced": [
            [("learner", "It is worth considering that the concept of standardised measurement, which the scale represents, was a revolutionary development in human civilisation."), ("system", "Absolutely. Before standardised units, trade and construction were far more prone to error and dispute."), ("learner", "The ability to measure consistently is what made large-scale engineering projects possible."), ("system", "From the pyramids to modern skyscrapers, every great structure began with a simple act of measurement.")],
            [("learner", "One could argue that the scale teaches children something deeper than just how to draw straight lines; it introduces the concept of precision and accountability."), ("system", "That is a perceptive observation. How do you see precision connecting to accountability?"), ("learner", "When you measure something, you commit to a specific value. There is no room for vagueness."), ("system", "And that discipline of mind, the habit of being exact and deliberate, carries over into many other areas of learning and life.")],
            [("learner", "Regardless of how advanced digital measurement tools become, I believe the physical scale will always be the first measuring instrument a child holds in their hands."), ("system", "Why do you feel so strongly about that?"), ("learner", "Because understanding measurement begins with the tangible experience of placing a ruler against an object and reading the numbers."), ("system", "You are describing what educators call embodied cognition, the idea that we learn best when our bodies are physically engaged in the process.")],
        ],
    },

}


# ═══════════════════════════════════════════════════════════════════════════
#  Build JSON with phoneme tagging
# ═══════════════════════════════════════════════════════════════════════════

def build_sentence_bank():
    bank = {}
    for obj, levels in SENTENCES.items():
        bank[obj] = {}
        for level, sents in levels.items():
            entries = []
            for idx, (sentence, grammar) in enumerate(sents, 1):
                entries.append({
                    "id": f"{obj.replace(' ', '_')}_{level[:3]}_{idx:03d}",
                    "sentence": sentence,
                    "grammar_focus": grammar,
                    "target_phonemes": get_phonemes(sentence),
                })
            bank[obj][level] = entries
    return bank


def build_dialogue_bank():
    bank = {}
    for obj, levels in DIALOGUES.items():
        bank[obj] = {}
        for level, variants in levels.items():
            dialogues = []
            for var_idx, turns in enumerate(variants, 1):
                dialogues.append({
                    "id": f"{obj.replace(' ', '_')}_dial_{level[:3]}_{var_idx:03d}",
                    "turns": [{"speaker": s, "line": l} for s, l in turns],
                })
            bank[obj][level] = dialogues
    return bank


def main():
    print("Building hand-crafted sentence bank...")
    sb = build_sentence_bank()
    total = sum(len(s) for lv in sb.values() for s in lv.values())
    print(f"  -> {len(sb)} objects, {total} sentences")

    print("Building hand-crafted dialogue bank...")
    db = build_dialogue_bank()
    total_d = sum(len(d) for lv in db.values() for d in lv.values())
    print(f"  -> {len(db)} objects, {total_d} dialogues")

    with open(DATA_DIR / "sentence_bank.json", "w", encoding="utf-8") as f:
        json.dump(sb, f, indent=2, ensure_ascii=False)
    print(f"  Written: {DATA_DIR / 'sentence_bank.json'}")

    with open(DATA_DIR / "dialogue_bank.json", "w", encoding="utf-8") as f:
        json.dump(db, f, indent=2, ensure_ascii=False)
    print(f"  Written: {DATA_DIR / 'dialogue_bank.json'}")

    print("Done!")


if __name__ == "__main__":
    main()
