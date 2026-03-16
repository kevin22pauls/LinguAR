from __future__ import annotations

"""
Multi-object scene description generator.

Takes multiple YOLO detections from the browser and generates sentences
describing spatial relationships between objects, using pre-authored
templates from scene_templates.json.
"""

import random
import logging

from backend.services.llm_prompt_generator import (
    get_scene_templates,
    _normalize_level,
)

logger = logging.getLogger(__name__)


def _article(obj: str) -> str:
    """Return 'a' or 'an' for an object name."""
    return "an" if obj.strip().lower()[0] in "aeiou" else "a"


def _fill_template(template: str, **kwargs) -> str:
    """Fill a scene template, handling {a_obj1}, {A_obj1} article placeholders."""
    # Build article-aware replacements
    for key, val in list(kwargs.items()):
        if key.startswith("obj"):
            art = _article(val)
            kwargs[f"a_{key}"] = f"{art} {val}"
            kwargs[f"A_{key}"] = f"{art.capitalize()} {val}"
    return template.format(**kwargs)


def _compute_relation(box1: dict, box2: dict) -> str:
    """
    Compute spatial relationship between two bounding boxes.
    Each box has: {x, y, width, height} (pixel coords, origin top-left).
    """
    cx1 = box1["x"] + box1["width"] / 2
    cy1 = box1["y"] + box1["height"] / 2
    cx2 = box2["x"] + box2["width"] / 2
    cy2 = box2["y"] + box2["height"] / 2

    dx = cx1 - cx2
    dy = cy1 - cy2

    if abs(dx) > abs(dy):
        return "to the right of" if dx > 0 else "to the left of"
    else:
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
    elif ratio < 3:
        return "near"
    else:
        return "far from"


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
    templates = get_scene_templates()

    # Deduplicate labels (keep highest confidence per label)
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
        # Single object — use two_objects beginner simple
        sentence = f"I see a {labels[0]}."
        relations = []

    elif len(objects) == 2:
        relation = _compute_relation(objects[0], objects[1])
        proximity = _compute_proximity(objects[0], objects[1])

        # Pick from two_objects templates
        level_tmpls = templates.get(
            "two_objects", {}
        ).get(level, [])
        if not level_tmpls:
            level_tmpls = templates.get(
                "two_objects", {}
            ).get("beginner", [])

        if level_tmpls:
            tmpl = random.choice(level_tmpls)
            sentence = _fill_template(
                tmpl["template"],
                obj1=labels[0],
                obj2=labels[1],
                relation=relation,
            )
        else:
            art1, art2 = _article(labels[0]), _article(labels[1])
            sentence = (
                f"I see {art1} {labels[0]} and {art2} {labels[1]}."
            )

        relations = [{
            "obj1": labels[0],
            "obj2": labels[1],
            "spatial": relation,
            "proximity": proximity,
        }]

    else:
        # 3+ objects — pick top 3 by confidence
        top3 = sorted(
            objects,
            key=lambda o: o.get("confidence", 0),
            reverse=True,
        )[:3]
        top_labels = [o["label"] for o in top3]

        rel1 = _compute_relation(top3[0], top3[1])
        relations = [{
            "obj1": top_labels[0],
            "obj2": top_labels[1],
            "spatial": rel1,
            "proximity": _compute_proximity(
                top3[0], top3[1]
            ),
        }]

        rel2 = "near"
        if len(top3) >= 3:
            rel2 = _compute_relation(top3[2], top3[0])
            relations.append({
                "obj1": top_labels[2],
                "obj2": top_labels[0],
                "spatial": rel2,
                "proximity": _compute_proximity(
                    top3[2], top3[0]
                ),
            })

        # Pick from three_objects templates
        level_tmpls = templates.get(
            "three_objects", {}
        ).get(level, [])
        if not level_tmpls:
            level_tmpls = templates.get(
                "three_objects", {}
            ).get("beginner", [])

        if level_tmpls:
            tmpl = random.choice(level_tmpls)
            obj3 = (
                top_labels[2]
                if len(top_labels) >= 3
                else top_labels[0]
            )
            sentence = _fill_template(
                tmpl["template"],
                obj1=top_labels[0],
                obj2=top_labels[1],
                obj3=obj3,
                relation=rel1,
                relation1=rel1,
                relation2=rel2,
            )
        else:
            parts = [
                f"{_article(l)} {l}" for l in top_labels
            ]
            sentence = (
                f"I see {', '.join(parts[:-1])}, "
                f"and {parts[-1]}."
            )

    return {
        "sentence": sentence,
        "objects": labels,
        "relations": relations,
    }
