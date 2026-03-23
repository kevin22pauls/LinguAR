#!/usr/bin/env python3
from __future__ import annotations
"""
Build sentence_bank.json for all 80 COCO objects from part files.
Uses g2p-en for phoneme tagging only — all sentences are hand-authored.
"""

import json
import re
import importlib
import sys
from pathlib import Path

DATA_DIR = Path(__file__).resolve().parent.parent / "backend" / "data"

try:
    from g2p_en import G2p
    g2p = G2p()
except ImportError:
    print("WARNING: g2p_en not installed. Run: pip install g2p-en")
    g2p = None


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


def build_sentence_bank(all_sentences):
    bank = {}
    for obj, levels in all_sentences.items():
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


def main():
    # Import all parts
    sys.path.insert(0, str(Path(__file__).parent))

    all_sentences = {}
    for i in range(1, 5):
        mod_name = f"sentences.part{i}"
        try:
            mod = importlib.import_module(mod_name)
            var_name = f"SENTENCES_PART{i}"
            part = getattr(mod, var_name)
            all_sentences.update(part)
            print(f"  Loaded {mod_name}: {len(part)} objects")
        except Exception as e:
            print(f"  ERROR loading {mod_name}: {e}")

    print(f"\nTotal objects: {len(all_sentences)}")

    print("Building sentence bank with phoneme tagging...")
    bank = build_sentence_bank(all_sentences)
    total = sum(len(s) for lv in bank.values() for s in lv.values())
    print(f"  -> {len(bank)} objects, {total} sentences")

    out_path = DATA_DIR / "sentence_bank.json"
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(bank, f, indent=2, ensure_ascii=False)
    print(f"  Written: {out_path}")
    print("Done!")


if __name__ == "__main__":
    main()
