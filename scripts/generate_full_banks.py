#!/usr/bin/env python3
from __future__ import annotations
"""
Generate the full sentence bank, dialogue bank, and scene templates
for all 80 YOLO COCO objects with phoneme tagging via g2p-en.

Usage:
    python scripts/generate_full_banks.py

Outputs:
    backend/data/sentence_bank.json
    backend/data/dialogue_bank.json
    backend/data/scene_templates.json   (expanded)
"""

import json
import re
from pathlib import Path

# g2p-en for phoneme tagging
try:
    from g2p_en import G2p
    g2p = G2p()
except ImportError:
    print("WARNING: g2p_en not installed. Run: pip install g2p-en")
    print("Falling back to empty phoneme lists.")
    g2p = None

DATA_DIR = Path(__file__).resolve().parent.parent / "backend" / "data"

# ─── All 80 YOLO COCO class names ──────────────────────────────────────────

OBJECTS = [
    "person", "bicycle", "car", "motorcycle", "airplane", "bus", "train",
    "truck", "boat", "traffic light", "fire hydrant", "stop sign",
    "parking meter", "bench", "bird", "cat", "dog", "horse", "sheep", "cow",
    "elephant", "bear", "zebra", "giraffe", "backpack", "umbrella", "handbag",
    "tie", "suitcase", "frisbee", "skis", "snowboard", "sports ball", "kite",
    "baseball bat", "baseball glove", "skateboard", "surfboard",
    "tennis racket", "bottle", "wine glass", "cup", "fork", "knife", "spoon",
    "bowl", "banana", "apple", "sandwich", "orange", "broccoli", "carrot",
    "hot dog", "pizza", "donut", "cake", "chair", "couch", "potted plant",
    "bed", "dining table", "toilet", "tv", "laptop", "mouse", "remote",
    "keyboard", "cell phone", "microwave", "oven", "toaster", "sink",
    "refrigerator", "book", "clock", "vase", "scissors", "teddy bear",
    "hair drier", "toothbrush",
]


def get_phonemes(sentence: str) -> list[str]:
    """Extract unique ARPAbet phonemes from a sentence using g2p-en."""
    if g2p is None:
        return []
    raw = g2p(sentence)
    phones = []
    for tok in raw:
        # g2p returns phonemes and punctuation/spaces
        cleaned = re.sub(r"[^A-Z]", "", tok.upper())
        if cleaned and len(cleaned) >= 2:
            # Strip stress digits for matching
            base = cleaned.rstrip("012")
            if base:
                phones.append(base)
    # Return unique list preserving order
    seen = set()
    result = []
    for p in phones:
        if p not in seen:
            seen.add(p)
            result.append(p)
    return result


def tag_sentence(sentence: str) -> list[str]:
    """Get target phonemes for a sentence."""
    return get_phonemes(sentence)


# ─── Article helper ─────────────────────────────────────────────────────────

# Objects that are plural or uncountable (no article, special handling)
PLURAL_OBJECTS = {"scissors", "skis", "broccoli"}

def article(obj: str) -> str:
    """Return 'a' or 'an' based on the object name."""
    if obj in PLURAL_OBJECTS:
        return "some"
    vowels = "aeiou"
    first = obj.strip().lower()[0]
    return "an" if first in vowels else "a"


def a(obj: str) -> str:
    return f"{article(obj)} {obj}"


def plural(obj: str) -> str:
    """Simple pluralisation."""
    if obj in PLURAL_OBJECTS:
        return obj
    if obj.endswith("s") or obj.endswith("sh") or obj.endswith("ch") or obj.endswith("x"):
        return obj + "es"
    if obj.endswith("fe"):
        return obj[:-2] + "ves"  # knife -> knives
    if obj.endswith("f"):
        return obj[:-1] + "ves"
    if obj.endswith("y") and obj[-2] not in "aeiou":
        return obj[:-1] + "ies"
    return obj + "s"


# ─── Sentence Templates per Level ────────────────────────────────────────────
# Each level has templates with {obj} placeholder.
# Templates are grouped so we generate 10 per level per object.

SENTENCE_TEMPLATES = {
    "beginner": [
        ("This is {a_obj}.", "demonstratives"),
        ("I see {a_obj}.", "simple present"),
        ("The {obj} is big.", "copula + adjective"),
        ("I have {a_obj}.", "have"),
        ("The {obj} is on the table.", "prepositions"),
        ("My {obj} is red.", "possessives"),
        ("I like this {obj}.", "like + noun"),
        ("Is this your {obj}?", "yes/no questions"),
        ("The {obj} is here.", "here/there"),
        ("I can see {a_obj}.", "can + verb"),
    ],
    "elementary": [
        ("Can I use your {obj}, please?", "requests"),
        ("I forgot my {obj} at home today.", "past simple"),
        ("The {obj} is almost new.", "adverbs of degree"),
        ("This {obj} is very useful.", "adjective + noun"),
        ("Please put the {obj} on the shelf.", "imperatives"),
        ("There are two {objs} in the room.", "there are + plural"),
        ("I always bring my {obj} to school.", "frequency adverbs"),
        ("She bought {a_obj} yesterday.", "past simple irregular"),
        ("The {obj} belongs to my friend.", "possessive clauses"),
        ("Do not touch the {obj} on the desk.", "negative imperatives"),
    ],
    "intermediate": [
        ("Could you pass me the {obj}, please?", "polite requests"),
        ("The {obj} that you gave me is really good.", "relative clauses"),
        ("I have been using this {obj} for three months.", "present perfect continuous"),
        ("This {obj} is made of strong material.", "passive voice"),
        ("Although the {obj} looks old, it still works well.", "concessive clauses"),
        ("I need to buy {a_obj} because mine is broken.", "because + reason"),
        ("Have you ever thought about how a {obj} is made?", "present perfect + about"),
        ("The teacher asked us to bring {a_obj} to class.", "reported speech"),
        ("I would rather have a new {obj} than fix the old one.", "would rather"),
        ("If I had {a_obj}, I would use it every day.", "second conditional"),
    ],
    "upper_intermediate": [
        ("The {obj}, which was left on the table overnight, has been moved.", "non-defining relative clauses"),
        ("Had I not brought my {obj}, I would have been in trouble.", "inverted conditional"),
        ("Despite being quite old, this {obj} is surprisingly useful.", "despite + gerund"),
        ("It is estimated that millions of {objs} are sold every year.", "passive + estimated"),
        ("Not only is this {obj} practical, but it is also very affordable.", "not only...but also"),
        ("I wish I had bought a better {obj} when I had the chance.", "wish + past perfect"),
        ("The number of {objs} being used has increased over the past year.", "present perfect passive"),
        ("Whoever took my {obj} should return it before the end of the day.", "whoever, should"),
        ("The {obj} I was given at the event turned out to be quite valuable.", "turned out + infinitive"),
        ("Were it not for this {obj}, I would have had a much harder time.", "subjunctive inversion"),
    ],
    "advanced": [
        ("It strikes me as remarkable that such a simple {obj} can have so many different uses in daily life.", "it strikes me"),
        ("One could argue that the design of the modern {obj} represents a significant achievement in engineering.", "one could argue"),
        ("The {obj} that had been sitting on my desk all morning turned out to belong to someone from another class.", "past perfect continuous"),
        ("No sooner had I picked up the {obj} than I realised it was not the one I was looking for.", "no sooner...than"),
        ("Regardless of whether you prefer this type of {obj} or another, the important thing is that it serves its purpose.", "regardless of whether"),
    ],
}

# ─── Dialogue Templates ─────────────────────────────────────────────────────

DIALOGUE_TEMPLATES = {
    "beginner": [
        [
            ("learner", "Is this your {obj}?"),
            ("system", "Yes, it is. Thank you!"),
            ("learner", "The {obj} is very nice."),
            ("system", "I am glad you like it."),
        ],
        [
            ("learner", "I have {a_obj}."),
            ("system", "That is a good one."),
            ("learner", "Do you have {a_obj} too?"),
            ("system", "Yes, mine is at home."),
        ],
        [
            ("learner", "Where is my {obj}?"),
            ("system", "It is on the desk."),
            ("learner", "Oh, I can see the {obj} now."),
            ("system", "Good. Please do not forget it again."),
        ],
    ],
    "elementary": [
        [
            ("learner", "Can I borrow your {obj}?"),
            ("system", "Of course. Here you go."),
            ("learner", "Thank you. I will return it after class."),
            ("system", "No problem. Take your time."),
        ],
        [
            ("learner", "I lost my {obj} yesterday."),
            ("system", "Oh no. Where did you last see it?"),
            ("learner", "I think I left it in the classroom."),
            ("system", "Let us go and check together."),
        ],
        [
            ("learner", "This {obj} looks different from mine."),
            ("system", "How is it different?"),
            ("learner", "Mine is smaller and lighter."),
            ("system", "Interesting. They come in many sizes."),
        ],
    ],
    "intermediate": [
        [
            ("learner", "I have been looking for {a_obj} like this for a long time."),
            ("system", "What makes this one special?"),
            ("learner", "It is very well made and easy to use."),
            ("system", "I agree. Good quality makes a big difference."),
        ],
        [
            ("learner", "Could you tell me where you bought this {obj}?"),
            ("system", "I got it from the shop near the school."),
            ("learner", "How much did it cost, if you do not mind me asking?"),
            ("system", "It was quite affordable, actually."),
        ],
        [
            ("learner", "Do you think this {obj} is worth the price?"),
            ("system", "Absolutely. I have had mine for two years."),
            ("learner", "That is impressive. Mine broke after just a few months."),
            ("system", "Perhaps you should try a more durable brand."),
        ],
    ],
    "upper_intermediate": [
        [
            ("learner", "I have been reading about how {objs} are manufactured."),
            ("system", "That sounds fascinating. What did you learn?"),
            ("learner", "The process is more complex than I had imagined."),
            ("system", "Technology has made production much more efficient over the years."),
        ],
        [
            ("learner", "If you could redesign this {obj}, what would you change?"),
            ("system", "I would probably make it lighter and more sustainable."),
            ("learner", "That is a thoughtful answer. Sustainability is very important."),
            ("system", "Indeed. We all need to think about the environmental impact of everyday objects."),
        ],
        [
            ("learner", "Have you noticed how the design of {objs} has changed over time?"),
            ("system", "Yes, they have become much more streamlined and functional."),
            ("learner", "I think older designs had a certain charm that modern ones lack."),
            ("system", "That is a valid point. There is often a trade-off between form and function."),
        ],
    ],
    "advanced": [
        [
            ("learner", "It is remarkable how something as simple as {a_obj} can reveal so much about a culture."),
            ("system", "You raise an excellent point. Everyday objects often carry deep cultural significance."),
            ("learner", "I read that the evolution of the {obj} reflects changes in technology and social norms."),
            ("system", "That is a sophisticated observation. Material culture tells us a great deal about human history."),
        ],
        [
            ("learner", "One might argue that our relationship with objects like {objs} says something about consumerism."),
            ("system", "That is a thought-provoking perspective. Do you think we are too attached to material things?"),
            ("learner", "To some extent, yes. But I also believe that well-designed objects can improve quality of life."),
            ("system", "I agree. The key is finding a balance between utility and excess."),
        ],
        [
            ("learner", "Were we to examine the environmental cost of producing a single {obj}, the results might be surprising."),
            ("system", "Indeed. The carbon footprint of manufacturing is often underestimated."),
            ("learner", "Not only does production consume resources, but disposal creates additional problems."),
            ("system", "You have clearly thought deeply about this. Perhaps you could write an essay on the topic."),
        ],
    ],
}


def build_sentence_bank() -> dict:
    """Generate sentence bank for all 80 objects."""
    bank = {}
    for obj in OBJECTS:
        bank[obj] = {}
        art = a(obj)
        for level, templates in SENTENCE_TEMPLATES.items():
            sentences = []
            for idx, (template, grammar) in enumerate(templates, 1):
                # Build the sentence
                sent = (template
                    .replace("{a_obj}", art)
                    .replace("{objs}", plural(obj))
                    .replace("{obj}", obj)
                )
                # Tag with phonemes
                phonemes = tag_sentence(sent)
                sent_id = f"{obj.replace(' ', '_')}_{level[:3]}_{idx:03d}"
                sentences.append({
                    "id": sent_id,
                    "sentence": sent,
                    "grammar_focus": grammar,
                    "target_phonemes": phonemes,
                })
            bank[obj][level] = sentences
    return bank


def build_dialogue_bank() -> dict:
    """Generate dialogue bank for all 80 objects."""
    bank = {}
    for obj in OBJECTS:
        bank[obj] = {}
        art = a(obj)
        for level, variants in DIALOGUE_TEMPLATES.items():
            dialogues = []
            for var_idx, turns_template in enumerate(variants, 1):
                turns = []
                for speaker, line_template in turns_template:
                    line = (line_template
                        .replace("{a_obj}", art)
                        .replace("{objs}", plural(obj))
                        .replace("{obj}", obj)
                    )
                    turns.append({"speaker": speaker, "line": line})
                dial_id = f"{obj.replace(' ', '_')}_dial_{level[:3]}_{var_idx:03d}"
                dialogues.append({"id": dial_id, "turns": turns})
            bank[obj][level] = dialogues
    return bank


def build_scene_templates() -> dict:
    """Build expanded scene description templates."""
    templates = {
        "spatial_relations": {
            "horizontal": ["next to", "beside", "to the left of", "to the right of"],
            "vertical": ["above", "below", "on top of", "under"],
            "proximity": ["near", "close to", "far from"],
            "between": ["between"],
        },
        "two_objects": {
            "beginner": [
                {"id": "scene_2_beg_001", "template": "I see {a_obj1} and {a_obj2}.", "grammar_focus": "listing, articles"},
                {"id": "scene_2_beg_002", "template": "There is {a_obj1} and {a_obj2}.", "grammar_focus": "there is"},
                {"id": "scene_2_beg_003", "template": "The {obj1} is {relation} the {obj2}.", "grammar_focus": "prepositions"},
                {"id": "scene_2_beg_004", "template": "I can see {a_obj1} and {a_obj2} here.", "grammar_focus": "can + see"},
                {"id": "scene_2_beg_005", "template": "Look at the {obj1} and the {obj2}.", "grammar_focus": "imperatives"},
                {"id": "scene_2_beg_006", "template": "{A_obj1} is {relation} {a_obj2}.", "grammar_focus": "articles, prepositions"},
                {"id": "scene_2_beg_007", "template": "The {obj1} and the {obj2} are on the table.", "grammar_focus": "plural subject"},
                {"id": "scene_2_beg_008", "template": "Here is {a_obj1} and here is {a_obj2}.", "grammar_focus": "here is"},
                {"id": "scene_2_beg_009", "template": "I have {a_obj1} and {a_obj2}.", "grammar_focus": "have"},
                {"id": "scene_2_beg_010", "template": "This is {a_obj1} and that is {a_obj2}.", "grammar_focus": "this/that"},
            ],
            "elementary": [
                {"id": "scene_2_ele_001", "template": "The {obj1} is {relation} the {obj2} on the desk.", "grammar_focus": "compound prepositions"},
                {"id": "scene_2_ele_002", "template": "Can you see the {obj1} {relation} the {obj2}?", "grammar_focus": "questions"},
                {"id": "scene_2_ele_003", "template": "I put the {obj1} {relation} the {obj2} this morning.", "grammar_focus": "past simple"},
                {"id": "scene_2_ele_004", "template": "The {obj1} is bigger than the {obj2}.", "grammar_focus": "comparatives"},
                {"id": "scene_2_ele_005", "template": "Please move the {obj1} away from the {obj2}.", "grammar_focus": "polite imperatives"},
                {"id": "scene_2_ele_006", "template": "Someone left {a_obj1} {relation} the {obj2}.", "grammar_focus": "indefinite pronouns"},
                {"id": "scene_2_ele_007", "template": "I need the {obj1} that is {relation} the {obj2}.", "grammar_focus": "relative clauses"},
                {"id": "scene_2_ele_008", "template": "The {obj1} and the {obj2} both belong to me.", "grammar_focus": "both, possession"},
                {"id": "scene_2_ele_009", "template": "I found {a_obj1} and {a_obj2} in the classroom.", "grammar_focus": "past simple"},
                {"id": "scene_2_ele_010", "template": "Which one do you prefer, the {obj1} or the {obj2}?", "grammar_focus": "preferences"},
            ],
            "intermediate": [
                {"id": "scene_2_int_001", "template": "Could you move the {obj1} that is {relation} the {obj2}, please?", "grammar_focus": "modals, relative clauses"},
                {"id": "scene_2_int_002", "template": "I noticed that the {obj1} has been placed {relation} the {obj2}.", "grammar_focus": "present perfect passive"},
                {"id": "scene_2_int_003", "template": "The {obj1} should not be kept so close to the {obj2}.", "grammar_focus": "should, negation"},
                {"id": "scene_2_int_004", "template": "Have you seen the {obj1} that was {relation} the {obj2} earlier?", "grammar_focus": "present perfect"},
                {"id": "scene_2_int_005", "template": "If you look carefully, you will find the {obj1} {relation} the {obj2}.", "grammar_focus": "first conditional"},
                {"id": "scene_2_int_006", "template": "The {obj1} seems to have been moved away from the {obj2}.", "grammar_focus": "seem + perfect infinitive"},
                {"id": "scene_2_int_007", "template": "I always keep my {obj1} {relation} my {obj2} so I can find them easily.", "grammar_focus": "adverbs of frequency"},
                {"id": "scene_2_int_008", "template": "Do you think the {obj1} looks better {relation} the {obj2} or somewhere else?", "grammar_focus": "opinion questions"},
                {"id": "scene_2_int_009", "template": "The {obj1} was supposed to be {relation} the {obj2}, but someone moved it.", "grammar_focus": "was supposed to"},
                {"id": "scene_2_int_010", "template": "I remember putting the {obj1} {relation} the {obj2} before I left.", "grammar_focus": "remember + gerund"},
            ],
            "upper_intermediate": [
                {"id": "scene_2_upi_001", "template": "The {obj1}, which I had placed {relation} the {obj2}, appears to have been moved.", "grammar_focus": "non-defining relative, perfect"},
                {"id": "scene_2_upi_002", "template": "Had the {obj1} not been {relation} the {obj2}, I might not have noticed it.", "grammar_focus": "third conditional inverted"},
                {"id": "scene_2_upi_003", "template": "It occurred to me that the {obj1} and the {obj2} would look better side by side.", "grammar_focus": "it occurred to me"},
                {"id": "scene_2_upi_004", "template": "Whoever arranged the {obj1} {relation} the {obj2} clearly has a good eye for design.", "grammar_focus": "whoever"},
                {"id": "scene_2_upi_005", "template": "Not only was the {obj1} {relation} the {obj2}, but it was also blocking the view.", "grammar_focus": "not only...but also"},
            ],
            "advanced": [
                {"id": "scene_2_adv_001", "template": "The juxtaposition of the {obj1} and the {obj2} creates an unexpectedly harmonious visual effect.", "grammar_focus": "abstract nouns"},
                {"id": "scene_2_adv_002", "template": "One cannot help but notice that the {obj1} placed {relation} the {obj2} serves both a functional and an aesthetic purpose.", "grammar_focus": "one cannot help but"},
                {"id": "scene_2_adv_003", "template": "Were the {obj1} to be repositioned away from the {obj2}, the entire arrangement would lose its balance.", "grammar_focus": "subjunctive"},
            ],
        },
        "three_objects": {
            "beginner": [
                {"id": "scene_3_beg_001", "template": "I see {a_obj1}, {a_obj2}, and {a_obj3}.", "grammar_focus": "listing"},
                {"id": "scene_3_beg_002", "template": "There is {a_obj1}, {a_obj2}, and {a_obj3} here.", "grammar_focus": "there is"},
                {"id": "scene_3_beg_003", "template": "The {obj1}, the {obj2}, and the {obj3} are all on the table.", "grammar_focus": "plural subjects"},
                {"id": "scene_3_beg_004", "template": "I can count three things: {a_obj1}, {a_obj2}, and {a_obj3}.", "grammar_focus": "counting"},
                {"id": "scene_3_beg_005", "template": "Look at the {obj1}, the {obj2}, and the {obj3}.", "grammar_focus": "imperatives"},
            ],
            "elementary": [
                {"id": "scene_3_ele_001", "template": "The {obj1} is between the {obj2} and the {obj3}.", "grammar_focus": "between"},
                {"id": "scene_3_ele_002", "template": "Can you find the {obj1}, the {obj2}, and the {obj3}?", "grammar_focus": "questions"},
                {"id": "scene_3_ele_003", "template": "I need to move the {obj1}, the {obj2}, and the {obj3} before lunch.", "grammar_focus": "need to"},
                {"id": "scene_3_ele_004", "template": "The {obj2} is {relation} the {obj1} and the {obj3}.", "grammar_focus": "complex prepositions"},
                {"id": "scene_3_ele_005", "template": "Please bring me the {obj1}, the {obj2}, and the {obj3}.", "grammar_focus": "imperatives with lists"},
            ],
            "intermediate": [
                {"id": "scene_3_int_001", "template": "Could you arrange the {obj1}, the {obj2}, and the {obj3} neatly on the shelf?", "grammar_focus": "polite requests"},
                {"id": "scene_3_int_002", "template": "I noticed that the {obj1} has been placed between the {obj2} and the {obj3}.", "grammar_focus": "present perfect passive"},
                {"id": "scene_3_int_003", "template": "If you move the {obj1} next to the {obj2}, there will be room for the {obj3}.", "grammar_focus": "first conditional"},
                {"id": "scene_3_int_004", "template": "The {obj1}, the {obj2}, and the {obj3} all need to be put away before we leave.", "grammar_focus": "need to + passive"},
                {"id": "scene_3_int_005", "template": "Have you ever seen {a_obj1}, {a_obj2}, and {a_obj3} arranged together like that?", "grammar_focus": "present perfect"},
            ],
            "upper_intermediate": [
                {"id": "scene_3_upi_001", "template": "The arrangement of the {obj1}, the {obj2}, and the {obj3} suggests that someone organised them deliberately.", "grammar_focus": "suggests that"},
                {"id": "scene_3_upi_002", "template": "Had the {obj1} not been between the {obj2} and the {obj3}, the display would have looked quite different.", "grammar_focus": "third conditional inverted"},
                {"id": "scene_3_upi_003", "template": "Not only are the {obj1} and the {obj2} next to each other, but the {obj3} is also nearby.", "grammar_focus": "not only...but also"},
            ],
            "advanced": [
                {"id": "scene_3_adv_001", "template": "The spatial relationship between the {obj1}, the {obj2}, and the {obj3} reveals an underlying organisational principle.", "grammar_focus": "abstract language"},
                {"id": "scene_3_adv_002", "template": "One might argue that the positioning of the {obj1} relative to the {obj2} and the {obj3} is neither accidental nor arbitrary.", "grammar_focus": "neither...nor"},
            ],
        },
    }
    return templates


def main():
    print("Generating sentence bank for 80 objects...")
    sentence_bank = build_sentence_bank()
    total_sentences = sum(
        len(sents) for obj_data in sentence_bank.values() for sents in obj_data.values()
    )
    print(f"  -> {len(sentence_bank)} objects, {total_sentences} sentences total")

    print("Generating dialogue bank for 80 objects...")
    dialogue_bank = build_dialogue_bank()
    total_dialogues = sum(
        len(dials) for obj_data in dialogue_bank.values() for dials in obj_data.values()
    )
    print(f"  -> {len(dialogue_bank)} objects, {total_dialogues} dialogues total")

    print("Generating scene templates...")
    scene_templates = build_scene_templates()
    total_templates = sum(
        len(tmpl)
        for key, levels in scene_templates.items()
        if key != "spatial_relations"
        for tmpl in levels.values()
    )
    print(f"  -> {total_templates} scene templates total")

    # Write outputs
    out_sentence = DATA_DIR / "sentence_bank.json"
    out_dialogue = DATA_DIR / "dialogue_bank.json"
    out_scene = DATA_DIR / "scene_templates.json"

    with open(out_sentence, "w", encoding="utf-8") as f:
        json.dump(sentence_bank, f, indent=2, ensure_ascii=False)
    print(f"  Written: {out_sentence}")

    with open(out_dialogue, "w", encoding="utf-8") as f:
        json.dump(dialogue_bank, f, indent=2, ensure_ascii=False)
    print(f"  Written: {out_dialogue}")

    with open(out_scene, "w", encoding="utf-8") as f:
        json.dump(scene_templates, f, indent=2, ensure_ascii=False)
    print(f"  Written: {out_scene}")

    print("\nDone!")


if __name__ == "__main__":
    main()
