#!/usr/bin/env python3
from __future__ import annotations
"""
Build dialogue_bank.json for all 80 COCO objects from part files.
Each object gets 3 dialogues per level × 5 levels = 15 dialogues.
"""

import json
import importlib
import sys
from pathlib import Path

DATA_DIR = Path(__file__).resolve().parent.parent / "backend" / "data"


def build_dialogue_bank(all_dialogues):
    bank = {}
    for obj, levels in all_dialogues.items():
        bank[obj] = {}
        for level, dialogues in levels.items():
            entries = []
            for idx, turns in enumerate(dialogues, 1):
                entries.append({
                    "id": f"{obj.replace(' ', '_')}_dial_{level[:3]}_{idx:03d}",
                    "turns": [
                        {"speaker": spk, "line": line}
                        for spk, line in turns
                    ],
                })
            bank[obj][level] = entries
    return bank


def main():
    sys.path.insert(0, str(Path(__file__).parent))

    all_dialogues = {}
    for i in range(1, 5):
        mod_name = f"dialogues.part{i}"
        try:
            mod = importlib.import_module(mod_name)
            var_name = f"DIALOGUES_PART{i}"
            part = getattr(mod, var_name)
            all_dialogues.update(part)
            print(f"  Loaded {mod_name}: {len(part)} objects")
        except Exception as e:
            print(f"  ERROR loading {mod_name}: {e}")

    print(f"\nTotal objects: {len(all_dialogues)}")

    print("Building dialogue bank...")
    bank = build_dialogue_bank(all_dialogues)
    total = sum(len(d) for lv in bank.values() for d in lv.values())
    print(f"  -> {len(bank)} objects, {total} dialogues")

    out_path = DATA_DIR / "dialogue_bank.json"
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(bank, f, indent=2, ensure_ascii=False)
    print(f"  Written: {out_path}")
    print("Done!")


if __name__ == "__main__":
    main()
