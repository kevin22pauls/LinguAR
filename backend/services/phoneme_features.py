from __future__ import annotations

"""
Articulatory feature distances for ARPAbet phonemes.
Used for weighting substitution severity.

Features: manner, place, voicing (consonants); height, backness, rounding (vowels).
"""

# Consonant features: (manner, place, voicing)
CONSONANT_FEATURES = {
    "P":  ("stop", "bilabial", "voiceless"),
    "B":  ("stop", "bilabial", "voiced"),
    "T":  ("stop", "alveolar", "voiceless"),
    "D":  ("stop", "alveolar", "voiced"),
    "K":  ("stop", "velar", "voiceless"),
    "G":  ("stop", "velar", "voiced"),
    "CH": ("affricate", "postalveolar", "voiceless"),
    "JH": ("affricate", "postalveolar", "voiced"),
    "F":  ("fricative", "labiodental", "voiceless"),
    "V":  ("fricative", "labiodental", "voiced"),
    "TH": ("fricative", "dental", "voiceless"),
    "DH": ("fricative", "dental", "voiced"),
    "S":  ("fricative", "alveolar", "voiceless"),
    "Z":  ("fricative", "alveolar", "voiced"),
    "SH": ("fricative", "postalveolar", "voiceless"),
    "ZH": ("fricative", "postalveolar", "voiced"),
    "HH": ("fricative", "glottal", "voiceless"),
    "M":  ("nasal", "bilabial", "voiced"),
    "N":  ("nasal", "alveolar", "voiced"),
    "NG": ("nasal", "velar", "voiced"),
    "L":  ("lateral", "alveolar", "voiced"),
    "R":  ("approximant", "postalveolar", "voiced"),
    "W":  ("approximant", "bilabial", "voiced"),
    "Y":  ("approximant", "palatal", "voiced"),
}

# Vowel features: (height, backness, rounding)
VOWEL_FEATURES = {
    "IY": ("high", "front", "unrounded"),
    "IH": ("near-high", "front", "unrounded"),
    "EY": ("mid", "front", "unrounded"),
    "EH": ("mid", "front", "unrounded"),
    "AE": ("low", "front", "unrounded"),
    "AA": ("low", "back", "unrounded"),
    "AO": ("mid", "back", "rounded"),
    "OW": ("mid", "back", "rounded"),
    "UH": ("near-high", "back", "rounded"),
    "UW": ("high", "back", "rounded"),
    "AH": ("mid", "central", "unrounded"),
    "ER": ("mid", "central", "rounded"),
    "AW": ("low", "back", "unrounded"),      # diphthong
    "AY": ("low", "front", "unrounded"),      # diphthong
    "OY": ("mid", "back", "rounded"),         # diphthong
}

# Manner distance (how different two manners are, 0-3)
MANNER_DISTANCE = {}
_manners = ["stop", "affricate", "fricative", "nasal", "lateral", "approximant"]
for i, m1 in enumerate(_manners):
    for j, m2 in enumerate(_manners):
        MANNER_DISTANCE[(m1, m2)] = abs(i - j)

# Place distance
_places = ["bilabial", "labiodental", "dental", "alveolar", "postalveolar", "palatal", "velar", "glottal"]
PLACE_DISTANCE = {}
for i, p1 in enumerate(_places):
    for j, p2 in enumerate(_places):
        PLACE_DISTANCE[(p1, p2)] = abs(i - j)

# Height distance
_heights = ["high", "near-high", "mid", "low"]
HEIGHT_DISTANCE = {}
for i, h1 in enumerate(_heights):
    for j, h2 in enumerate(_heights):
        HEIGHT_DISTANCE[(h1, h2)] = abs(i - j)


def articulatory_distance(phone1: str, phone2: str) -> float:
    """
    Compute articulatory distance between two ARPAbet phones (0.0 = identical, 1.0 = maximally different).
    Stress digits are stripped before comparison.
    """
    p1 = phone1.rstrip("012")
    p2 = phone2.rstrip("012")

    if p1 == p2:
        return 0.0

    # Both consonants
    if p1 in CONSONANT_FEATURES and p2 in CONSONANT_FEATURES:
        f1 = CONSONANT_FEATURES[p1]
        f2 = CONSONANT_FEATURES[p2]
        manner_d = MANNER_DISTANCE.get((f1[0], f2[0]), 3) / 5
        place_d = PLACE_DISTANCE.get((f1[1], f2[1]), 4) / 7
        voice_d = 0 if f1[2] == f2[2] else 0.3
        return min(1.0, manner_d + place_d + voice_d)

    # Both vowels
    if p1 in VOWEL_FEATURES and p2 in VOWEL_FEATURES:
        f1 = VOWEL_FEATURES[p1]
        f2 = VOWEL_FEATURES[p2]
        height_d = HEIGHT_DISTANCE.get((f1[0], f2[0]), 3) / 3
        back_d = 0.3 if f1[1] != f2[1] else 0
        round_d = 0.2 if f1[2] != f2[2] else 0
        return min(1.0, height_d * 0.5 + back_d + round_d)

    # Consonant-vowel mismatch = maximum distance
    return 1.0
