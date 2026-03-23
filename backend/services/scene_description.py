"""Category-aware multi-object scene description generator."""

from __future__ import annotations

import random
import logging

from backend.services.llm_prompt_generator import _normalize_level

logger = logging.getLogger(__name__)

# ── Object categories for the 80 COCO classes ─────────────────────

CATEGORY_MAP = {
    "person": "person",
    "bicycle": "vehicle",
    "car": "vehicle",
    "motorcycle": "vehicle",
    "airplane": "vehicle",
    "bus": "vehicle",
    "train": "vehicle",
    "truck": "vehicle",
    "boat": "vehicle",
    "traffic light": "outdoor",
    "fire hydrant": "outdoor",
    "stop sign": "outdoor",
    "parking meter": "outdoor",
    "bench": "outdoor",
    "bird": "animal",
    "cat": "animal",
    "dog": "animal",
    "horse": "animal",
    "sheep": "animal",
    "cow": "animal",
    "elephant": "animal",
    "bear": "animal",
    "zebra": "animal",
    "giraffe": "animal",
    "backpack": "accessory",
    "umbrella": "accessory",
    "handbag": "accessory",
    "tie": "accessory",
    "suitcase": "accessory",
    "frisbee": "sports",
    "skis": "sports",
    "snowboard": "sports",
    "sports ball": "sports",
    "kite": "sports",
    "baseball bat": "sports",
    "baseball glove": "sports",
    "skateboard": "sports",
    "surfboard": "sports",
    "tennis racket": "sports",
    "bottle": "kitchen",
    "wine glass": "kitchen",
    "cup": "kitchen",
    "fork": "kitchen",
    "knife": "kitchen",
    "spoon": "kitchen",
    "bowl": "kitchen",
    "banana": "food",
    "apple": "food",
    "sandwich": "food",
    "orange": "food",
    "broccoli": "food",
    "carrot": "food",
    "hot dog": "food",
    "pizza": "food",
    "donut": "food",
    "cake": "food",
    "chair": "furniture",
    "couch": "furniture",
    "potted plant": "furniture",
    "bed": "furniture",
    "dining table": "furniture",
    "tv": "electronic",
    "laptop": "electronic",
    "mouse": "electronic",
    "keyboard": "electronic",
    "cell phone": "electronic",
    "toilet": "appliance",
    "microwave": "appliance",
    "oven": "appliance",
    "toaster": "appliance",
    "sink": "appliance",
    "refrigerator": "appliance",
    "book": "household",
    "clock": "household",
    "vase": "household",
    "scissors": "household",
    "teddy bear": "household",
    "hair drier": "household",
    "toothbrush": "household",
}


def _get_category(label: str) -> str:
    return CATEGORY_MAP.get(label, "object")


# ── Category-aware sentence templates ──────────────────────────────
# Keys are (cat1, cat2) tuples. Values are {level: [templates]}.
# Templates use: {obj1} {obj2} {a_obj1} {a_obj2} {relation} {proximity}
#
# For person+X pairs, obj1 is always the person, obj2 is the other.

_PAIR_TEMPLATES = {
    ("person", "vehicle"): {
        "beginner": [
            "A person is standing {proximity} the {obj2}.",
            "I see someone near the {obj2}.",
            "There is a person beside the {obj2}.",
        ],
        "elementary": [
            "A person is waiting {proximity} the {obj2}.",
            "Someone is walking towards the {obj2}.",
            (
                "I can see a person standing"
                " {relation} the {obj2}."
            ),
        ],
        "intermediate": [
            (
                "There is a person who appears to be"
                " waiting near the {obj2}."
            ),
            (
                "I noticed someone standing quite"
                " close to the {obj2}."
            ),
            (
                "A person seems to be getting"
                " into the {obj2}."
            ),
        ],
        "upper_intermediate": [
            (
                "The person, who has been standing"
                " {proximity} the {obj2}, seems to"
                " be waiting for someone."
            ),
            (
                "It appears that the person positioned"
                " {relation} the {obj2} is about"
                " to leave."
            ),
        ],
        "advanced": [
            (
                "The individual standing adjacent to"
                " the {obj2} appears to be contemplating"
                " whether to proceed on foot."
            ),
        ],
    },
    ("person", "animal"): {
        "beginner": [
            "A person is {proximity} the {obj2}.",
            "I see someone with {a_obj2}.",
            "There is a person and {a_obj2}.",
        ],
        "elementary": [
            "A person is looking at the {obj2}.",
            (
                "Someone is standing {proximity}"
                " the {obj2}."
            ),
            (
                "I can see a person watching"
                " the {obj2}."
            ),
        ],
        "intermediate": [
            (
                "A person appears to be feeding"
                " the {obj2}."
            ),
            (
                "There is someone who seems interested"
                " in the {obj2} nearby."
            ),
            (
                "I noticed a person observing"
                " the {obj2} from a distance."
            ),
        ],
        "upper_intermediate": [
            (
                "The person standing {proximity} the"
                " {obj2} seems to be enjoying"
                " the sight."
            ),
            (
                "It looks as though the person and"
                " the {obj2} have been there"
                " for a while."
            ),
        ],
        "advanced": [
            (
                "The interaction between the person"
                " and the {obj2} suggests a familiar"
                " bond that has developed over time."
            ),
        ],
    },
    ("person", "furniture"): {
        "beginner": [
            "A person is sitting on the {obj2}.",
            "I see someone near the {obj2}.",
            "There is a person {proximity} the {obj2}.",
        ],
        "elementary": [
            "A person is resting on the {obj2}.",
            "Someone sat down on the {obj2}.",
            (
                "I can see a person leaning"
                " against the {obj2}."
            ),
        ],
        "intermediate": [
            (
                "A person has been sitting on"
                " the {obj2} for quite some time."
            ),
            (
                "There is someone who looks"
                " comfortable on the {obj2}."
            ),
        ],
        "upper_intermediate": [
            (
                "The person seated on the {obj2}"
                " appears to be deep in thought."
            ),
        ],
        "advanced": [
            (
                "One cannot help but notice the"
                " person reclining on the {obj2},"
                " seemingly oblivious to everything"
                " else in the room."
            ),
        ],
    },
    ("person", "electronic"): {
        "beginner": [
            "A person is using the {obj2}.",
            "I see someone with {a_obj2}.",
            "There is a person looking at the {obj2}.",
        ],
        "elementary": [
            "A person is working on the {obj2}.",
            "Someone is typing on the {obj2}.",
            (
                "I can see a person staring"
                " at the {obj2}."
            ),
        ],
        "intermediate": [
            (
                "A person has been using the {obj2}"
                " for the past few minutes."
            ),
            (
                "There is someone who seems"
                " focused on the {obj2}."
            ),
        ],
        "upper_intermediate": [
            (
                "The person using the {obj2} appears"
                " to be absorbed in whatever is"
                " on the screen."
            ),
        ],
        "advanced": [
            (
                "The individual engrossed in the"
                " {obj2} seems entirely unaware"
                " of the world around them."
            ),
        ],
    },
    ("person", "food"): {
        "beginner": [
            "A person is eating {a_obj2}.",
            "I see someone with {a_obj2}.",
            "There is a person holding {a_obj2}.",
        ],
        "elementary": [
            "A person is about to eat {a_obj2}.",
            (
                "Someone picked up {a_obj2}"
                " from the table."
            ),
            (
                "I can see a person enjoying"
                " {a_obj2}."
            ),
        ],
        "intermediate": [
            (
                "A person seems to be sharing"
                " {a_obj2} with someone."
            ),
            (
                "There is someone who has just"
                " finished eating {a_obj2}."
            ),
        ],
        "upper_intermediate": [
            (
                "The person holding the {obj2} appears"
                " to be deciding whether to eat it"
                " now or save it for later."
            ),
        ],
        "advanced": [
            (
                "One might infer from the person's"
                " expression that the {obj2} is"
                " particularly satisfying today."
            ),
        ],
    },
    ("person", "kitchen"): {
        "beginner": [
            "A person is holding {a_obj2}.",
            "I see someone with {a_obj2}.",
            "There is a person using {a_obj2}.",
        ],
        "elementary": [
            "A person is drinking from the {obj2}.",
            (
                "Someone picked up the {obj2}"
                " from the table."
            ),
            (
                "I can see a person reaching"
                " for the {obj2}."
            ),
        ],
        "intermediate": [
            (
                "A person has just placed the"
                " {obj2} on the table."
            ),
            (
                "There is someone who seems to be"
                " looking for the right {obj2}."
            ),
        ],
        "upper_intermediate": [
            (
                "The person who was using the {obj2}"
                " a moment ago has now set it aside."
            ),
        ],
        "advanced": [
            (
                "The careful way the person handles"
                " the {obj2} suggests a degree of"
                " mindfulness rarely seen in"
                " everyday actions."
            ),
        ],
    },
    ("person", "accessory"): {
        "beginner": [
            "A person is carrying {a_obj2}.",
            "I see someone with {a_obj2}.",
            "There is a person holding {a_obj2}.",
        ],
        "elementary": [
            "A person is wearing {a_obj2}.",
            "Someone just put down their {obj2}.",
            (
                "I can see a person picking"
                " up {a_obj2}."
            ),
        ],
        "intermediate": [
            (
                "A person appears to be looking for"
                " something in their {obj2}."
            ),
            (
                "The person with the {obj2} seems"
                " to be in a hurry."
            ),
        ],
        "upper_intermediate": [
            (
                "The person carrying the {obj2} looks"
                " as though they are about to leave"
                " on a trip."
            ),
        ],
        "advanced": [
            (
                "Judging by the way the person"
                " clutches the {obj2}, it likely"
                " contains something of"
                " great importance."
            ),
        ],
    },
    ("person", "sports"): {
        "beginner": [
            "A person is holding {a_obj2}.",
            "I see someone with {a_obj2}.",
            (
                "There is a person playing"
                " with {a_obj2}."
            ),
        ],
        "elementary": [
            (
                "A person is practising with"
                " the {obj2}."
            ),
            (
                "Someone is playing a game"
                " with the {obj2}."
            ),
            (
                "I can see a person throwing"
                " the {obj2}."
            ),
        ],
        "intermediate": [
            (
                "A person has been practising with"
                " the {obj2} all afternoon."
            ),
            (
                "There is someone who seems quite"
                " skilled with the {obj2}."
            ),
        ],
        "upper_intermediate": [
            (
                "The person handling the {obj2}"
                " appears to have been training"
                " for a competition."
            ),
        ],
        "advanced": [
            (
                "The fluid manner in which the"
                " person wields the {obj2} speaks"
                " to years of dedicated practice."
            ),
        ],
    },
    ("person", "household"): {
        "beginner": [
            "A person is holding {a_obj2}.",
            "I see someone with {a_obj2}.",
            "There is a person near the {obj2}.",
        ],
        "elementary": [
            "A person is reading the {obj2}.",
            "Someone picked up the {obj2}.",
            (
                "I can see a person looking"
                " at the {obj2}."
            ),
        ],
        "intermediate": [
            (
                "A person seems to be searching"
                " for something near the {obj2}."
            ),
            (
                "There is someone who has been"
                " using the {obj2} for a while."
            ),
        ],
        "upper_intermediate": [
            (
                "The person near the {obj2} appears"
                " to be lost in concentration."
            ),
        ],
        "advanced": [
            (
                "The manner in which the person"
                " interacts with the {obj2} reveals"
                " a quiet attentiveness."
            ),
        ],
    },
    ("person", "appliance"): {
        "beginner": [
            "A person is near the {obj2}.",
            "I see someone using the {obj2}.",
            "There is a person beside the {obj2}.",
        ],
        "elementary": [
            "A person is using the {obj2}.",
            (
                "Someone is standing in front"
                " of the {obj2}."
            ),
            (
                "I can see a person reaching"
                " for the {obj2}."
            ),
        ],
        "intermediate": [
            (
                "A person has just finished using"
                " the {obj2}."
            ),
            (
                "There is someone waiting for"
                " the {obj2} to finish."
            ),
        ],
        "upper_intermediate": [
            (
                "The person operating the {obj2}"
                " seems to know exactly"
                " what they are doing."
            ),
        ],
        "advanced": [
            (
                "The ease with which the person"
                " operates the {obj2} suggests"
                " a comfortable familiarity"
                " with the kitchen."
            ),
        ],
    },
    ("animal", "animal"): {
        "beginner": [
            "I see {a_obj1} and {a_obj2} together.",
            "The {obj1} is {proximity} the {obj2}.",
            "There is {a_obj1} and {a_obj2} here.",
        ],
        "elementary": [
            (
                "The {obj1} and the {obj2} are"
                " standing {proximity} each other."
            ),
            (
                "I can see {a_obj1} looking"
                " at the {obj2}."
            ),
            (
                "The {obj1} seems to be following"
                " the {obj2}."
            ),
        ],
        "intermediate": [
            (
                "The {obj1} and the {obj2} appear"
                " to be sharing the same space"
                " peacefully."
            ),
            (
                "I noticed that the {obj1} has been"
                " watching the {obj2} for a while."
            ),
        ],
        "upper_intermediate": [
            (
                "The {obj1}, which is standing"
                " {relation} the {obj2}, does not"
                " seem bothered by the other"
                " animal's presence."
            ),
        ],
        "advanced": [
            (
                "The coexistence of the {obj1} and"
                " the {obj2} in such close proximity"
                " offers a fascinating glimpse into"
                " interspecies dynamics."
            ),
        ],
    },
    ("food", "kitchen"): {
        "beginner": [
            "The {obj1} is in the {obj2}.",
            (
                "I see {a_obj1} {proximity}"
                " the {obj2}."
            ),
            (
                "There is {a_obj1} and {a_obj2}"
                " on the table."
            ),
        ],
        "elementary": [
            (
                "The {obj1} is sitting {proximity}"
                " the {obj2}."
            ),
            (
                "Someone placed the {obj1}"
                " {relation} the {obj2}."
            ),
            "I can see {a_obj1} beside the {obj2}.",
        ],
        "intermediate": [
            (
                "The {obj1} has been placed"
                " {proximity} the {obj2},"
                " ready to be served."
            ),
            (
                "It looks like someone is about to"
                " eat the {obj1} using the {obj2}."
            ),
        ],
        "upper_intermediate": [
            (
                "The {obj1}, which has been arranged"
                " {proximity} the {obj2}, suggests"
                " that a meal is about to begin."
            ),
        ],
        "advanced": [
            (
                "The deliberate placement of the"
                " {obj1} alongside the {obj2} reveals"
                " the care that has gone into"
                " setting this table."
            ),
        ],
    },
    ("furniture", "electronic"): {
        "beginner": [
            "The {obj2} is on the {obj1}.",
            (
                "I see {a_obj2} {proximity}"
                " the {obj1}."
            ),
            "There is {a_obj2} on the {obj1}.",
        ],
        "elementary": [
            (
                "The {obj2} has been placed on"
                " top of the {obj1}."
            ),
            (
                "Someone left the {obj2}"
                " on the {obj1}."
            ),
            (
                "I can see the {obj2} sitting"
                " on the {obj1}."
            ),
        ],
        "intermediate": [
            (
                "The {obj2} seems to have been left"
                " on the {obj1} by someone"
                " in a hurry."
            ),
            (
                "There is {a_obj2} resting on"
                " the {obj1}, still switched on."
            ),
        ],
        "upper_intermediate": [
            (
                "The {obj2}, which was placed on"
                " the {obj1}, appears to be"
                " running an update."
            ),
        ],
        "advanced": [
            (
                "The positioning of the {obj2} atop"
                " the {obj1} reflects the blurred"
                " boundary between living spaces"
                " and workspaces."
            ),
        ],
    },
    ("vehicle", "outdoor"): {
        "beginner": [
            "The {obj1} is {proximity} the {obj2}.",
            "I see {a_obj1} near the {obj2}.",
            "There is {a_obj1} beside the {obj2}.",
        ],
        "elementary": [
            (
                "The {obj1} is parked {proximity}"
                " the {obj2}."
            ),
            (
                "I can see {a_obj1} stopped"
                " near the {obj2}."
            ),
            (
                "Someone parked the {obj1} right"
                " next to the {obj2}."
            ),
        ],
        "intermediate": [
            (
                "The {obj1} appears to have stopped"
                " {proximity} the {obj2}."
            ),
            (
                "I noticed that the {obj1} has been"
                " waiting near the {obj2}"
                " for a while."
            ),
        ],
        "upper_intermediate": [
            (
                "The {obj1}, which is parked"
                " dangerously close to the {obj2},"
                " should probably be moved."
            ),
        ],
        "advanced": [
            (
                "The proximity of the {obj1} to"
                " the {obj2} raises questions about"
                " whether the driver was paying"
                " attention to road signage."
            ),
        ],
    },
    ("food", "food"): {
        "beginner": [
            (
                "I see {a_obj1} and {a_obj2}"
                " on the table."
            ),
            "The {obj1} is {proximity} the {obj2}.",
            (
                "There is {a_obj1} and {a_obj2}"
                " here."
            ),
        ],
        "elementary": [
            (
                "The {obj1} and the {obj2} are"
                " both on the plate."
            ),
            (
                "Someone placed the {obj1}"
                " {proximity} the {obj2}."
            ),
        ],
        "intermediate": [
            (
                "The {obj1} and the {obj2} have"
                " been arranged together, ready"
                " to be eaten."
            ),
        ],
        "upper_intermediate": [
            (
                "The pairing of the {obj1} with"
                " the {obj2} makes for a"
                " balanced snack."
            ),
        ],
        "advanced": [
            (
                "The combination of the {obj1} and"
                " the {obj2} reflects a thoughtful"
                " approach to nutrition."
            ),
        ],
    },
    ("kitchen", "kitchen"): {
        "beginner": [
            "The {obj1} is {proximity} the {obj2}.",
            "I see {a_obj1} and {a_obj2}.",
            (
                "There is {a_obj1} and {a_obj2}"
                " on the table."
            ),
        ],
        "elementary": [
            (
                "The {obj1} and the {obj2}"
                " are both on the table."
            ),
            (
                "Someone placed the {obj1}"
                " {proximity} the {obj2}."
            ),
        ],
        "intermediate": [
            (
                "The {obj1} has been set down"
                " {proximity} the {obj2}."
            ),
        ],
        "upper_intermediate": [
            (
                "The {obj1} and the {obj2},"
                " neatly arranged side by side,"
                " suggest that the table has"
                " been set with care."
            ),
        ],
        "advanced": [
            (
                "The orderly placement of the"
                " {obj1} alongside the {obj2}"
                " speaks to a well-organised"
                " dining arrangement."
            ),
        ],
    },
    ("furniture", "furniture"): {
        "beginner": [
            "The {obj1} is {proximity} the {obj2}.",
            (
                "I see {a_obj1} and {a_obj2}"
                " in the room."
            ),
        ],
        "elementary": [
            (
                "The {obj1} is placed {proximity}"
                " the {obj2}."
            ),
            (
                "I can see the {obj1} and"
                " the {obj2} in the room."
            ),
        ],
        "intermediate": [
            (
                "The {obj1} and the {obj2} are"
                " arranged neatly in the room."
            ),
        ],
        "upper_intermediate": [
            (
                "The {obj1} positioned {relation}"
                " the {obj2} gives the room"
                " a spacious feel."
            ),
        ],
        "advanced": [
            (
                "The spatial arrangement of"
                " the {obj1} relative to the {obj2}"
                " reflects a deliberate approach"
                " to interior design."
            ),
        ],
    },
    ("electronic", "electronic"): {
        "beginner": [
            "The {obj1} is {proximity} the {obj2}.",
            (
                "I see {a_obj1} and {a_obj2}"
                " on the desk."
            ),
        ],
        "elementary": [
            (
                "The {obj1} and the {obj2}"
                " are both on the desk."
            ),
            (
                "Someone left the {obj1}"
                " {proximity} the {obj2}."
            ),
        ],
        "intermediate": [
            (
                "The {obj1} has been placed"
                " {proximity} the {obj2}"
                " on the workstation."
            ),
        ],
        "upper_intermediate": [
            (
                "The {obj1} and the {obj2},"
                " both within easy reach,"
                " form a complete workstation."
            ),
        ],
        "advanced": [
            (
                "The arrangement of the {obj1}"
                " alongside the {obj2} suggests"
                " a workspace optimised"
                " for productivity."
            ),
        ],
    },
    ("electronic", "household"): {
        "beginner": [
            "The {obj1} is {proximity} the {obj2}.",
            "I see {a_obj1} near the {obj2}.",
        ],
        "elementary": [
            (
                "The {obj1} is sitting {proximity}"
                " the {obj2} on the desk."
            ),
        ],
        "intermediate": [
            (
                "I noticed the {obj1} has been"
                " placed {proximity} the {obj2}."
            ),
        ],
        "upper_intermediate": [
            (
                "The {obj1}, positioned {relation}"
                " the {obj2}, creates a cluttered"
                " but familiar desk scene."
            ),
        ],
        "advanced": [
            (
                "The juxtaposition of the {obj1}"
                " and the {obj2} on the same surface"
                " captures the essence of a"
                " modern study area."
            ),
        ],
    },
}

# ── Generic fallback templates ─────────────────────────────────────

_GENERIC_TEMPLATES = {
    "beginner": [
        "I see {a_obj1} and {a_obj2}.",
        (
            "There is {a_obj1} {proximity}"
            " {a_obj2}."
        ),
        "The {obj1} is {relation} the {obj2}.",
    ],
    "elementary": [
        (
            "The {obj1} is placed {relation}"
            " the {obj2}."
        ),
        (
            "I can see {a_obj1} and {a_obj2}"
            " in front of me."
        ),
        (
            "Someone put the {obj1} {proximity}"
            " the {obj2}."
        ),
    ],
    "intermediate": [
        (
            "I noticed that the {obj1} has been"
            " placed {relation} the {obj2}."
        ),
        (
            "The {obj1} and the {obj2} are both"
            " visible in the scene."
        ),
        (
            "If you look carefully, you will see"
            " the {obj1} {proximity} the {obj2}."
        ),
    ],
    "upper_intermediate": [
        (
            "The {obj1}, which is positioned"
            " {relation} the {obj2}, creates an"
            " interesting composition."
        ),
        (
            "Had the {obj1} not been {proximity}"
            " the {obj2}, I might not have"
            " noticed either of them."
        ),
    ],
    "advanced": [
        (
            "The juxtaposition of the {obj1} and"
            " the {obj2} creates an unexpectedly"
            " harmonious arrangement."
        ),
        (
            "One cannot help but observe the"
            " spatial interplay between the"
            " {obj1} and the {obj2}."
        ),
    ],
}


# ── Helper functions ───────────────────────────────────────────────

def _article(obj: str) -> str:
    """Return 'a' or 'an' for an object name."""
    vowels = "aeiou"
    return "an" if obj.strip().lower()[0] in vowels else "a"


def _fill_template(template: str, **kwargs) -> str:
    """Fill template with {a_obj1}, {A_obj1} article placeholders."""
    for key, val in list(kwargs.items()):
        if key.startswith("obj"):
            art = _article(val)
            kwargs[f"a_{key}"] = f"{art} {val}"
            kwargs[f"A_{key}"] = f"{art.capitalize()} {val}"
    return template.format(**kwargs)


def _compute_relation(box1: dict, box2: dict) -> str:
    """Compute spatial relation between two bounding boxes."""
    cx1 = box1["x"] + box1["width"] / 2
    cy1 = box1["y"] + box1["height"] / 2
    cx2 = box2["x"] + box2["width"] / 2
    cy2 = box2["y"] + box2["height"] / 2
    dx = cx1 - cx2
    dy = cy1 - cy2
    if abs(dx) > abs(dy):
        return "to the right of" if dx > 0 else "to the left of"
    return "below" if dy > 0 else "above"


def _compute_proximity(box1: dict, box2: dict) -> str:
    """Describe how close two objects are."""
    cx1 = box1["x"] + box1["width"] / 2
    cy1 = box1["y"] + box1["height"] / 2
    cx2 = box2["x"] + box2["width"] / 2
    cy2 = box2["y"] + box2["height"] / 2
    distance = ((cx1 - cx2) ** 2 + (cy1 - cy2) ** 2) ** 0.5
    avg_size = (
        box1["width"] + box1["height"]
        + box2["width"] + box2["height"]
    ) / 4
    ratio = distance / avg_size if avg_size > 0 else 10
    if ratio < 1.5:
        return "next to"
    if ratio < 3:
        return "near"
    return "far from"


def _get_pair_templates(
    cat1: str, cat2: str, level: str,
) -> list[str]:
    """Find matching templates for a category pair + level."""
    # Try exact pair match (both orderings)
    for pair_key, levels in _PAIR_TEMPLATES.items():
        c1, c2 = pair_key
        if (
            (cat1 == c1 and cat2 == c2)
            or (cat1 == c2 and cat2 == c1)
        ):
            tmpls = (
                levels.get(level)
                or levels.get("beginner", [])
            )
            if tmpls:
                return tmpls

    # No match — use generic templates
    return _GENERIC_TEMPLATES.get(
        level, _GENERIC_TEMPLATES["beginner"],
    )


# ── Main generator ─────────────────────────────────────────────────

def generate_scene_description(
    detections: list[dict],
    difficulty: str = "elementary",
) -> dict:
    """
    Generate a practice sentence describing the scene.

    detections: list of {label, confidence, x, y, width, height}
    difficulty: level name or CEFR code

    Returns: {sentence, objects, relations}
    """
    if not detections:
        return {
            "sentence": "I don't see any objects.",
            "objects": [],
            "relations": [],
        }

    level = _normalize_level(difficulty)

    # Deduplicate labels (keep highest confidence)
    unique = {}
    for det in detections:
        label = det["label"]
        if (
            label not in unique
            or det.get("confidence", 0)
            > unique[label].get("confidence", 0)
        ):
            unique[label] = det

    objects = list(unique.values())
    labels = [o["label"] for o in objects]

    if len(objects) == 1:
        art = _article(labels[0])
        sentence = f"I see {art} {labels[0]}."
        return {
            "sentence": sentence,
            "objects": labels,
            "relations": [],
        }

    # Sort by confidence, pick top detections
    top = sorted(
        objects,
        key=lambda o: o.get("confidence", 0),
        reverse=True,
    )

    obj1, obj2 = top[0], top[1]
    lab1, lab2 = obj1["label"], obj2["label"]
    cat1 = _get_category(lab1)
    cat2 = _get_category(lab2)

    # For person+X pairs, ensure person is obj1
    if cat2 == "person" and cat1 != "person":
        obj1, obj2 = obj2, obj1
        lab1, lab2 = lab2, lab1
        cat1, cat2 = cat2, cat1

    relation = _compute_relation(obj1, obj2)
    proximity = _compute_proximity(obj1, obj2)

    templates = _get_pair_templates(cat1, cat2, level)
    tmpl = random.choice(templates)

    sentence = _fill_template(
        tmpl,
        obj1=lab1,
        obj2=lab2,
        relation=relation,
        proximity=proximity,
    )

    relations = [{
        "obj1": lab1,
        "obj2": lab2,
        "spatial": relation,
        "proximity": proximity,
    }]

    # 3+ objects: add a second sentence about the third
    if len(top) >= 3:
        obj3 = top[2]
        lab3 = obj3["label"]
        cat3 = _get_category(lab3)

        rel3 = _compute_relation(obj3, obj1)
        prox3 = _compute_proximity(obj3, obj1)

        tmpls3 = _get_pair_templates(cat3, cat1, level)
        tmpl3 = random.choice(tmpls3)

        extra = _fill_template(
            tmpl3,
            obj1=lab3,
            obj2=lab1,
            relation=rel3,
            proximity=prox3,
        )
        sentence = f"{sentence} {extra}"

        relations.append({
            "obj1": lab3,
            "obj2": lab1,
            "spatial": rel3,
            "proximity": prox3,
        })

    return {
        "sentence": sentence,
        "objects": labels,
        "relations": relations,
    }
