"""
Benchmark validation script — SpeechOcean762 and L2-ARCTIC.

Usage:
    python -m scripts.benchmark_validation --dataset speechocean762 --data-dir /path/to/data
    python -m scripts.benchmark_validation --dataset l2arctic --data-dir /path/to/data

SpeechOcean762: reports Pearson correlation for 4 dimensions
    (accuracy, fluency, prosody, completeness)
L2-ARCTIC: reports MDD F1 on 6-speaker test set (target: ~65-70%)
"""

import argparse
import json
import logging
import sys
from pathlib import Path

import numpy as np

logger = logging.getLogger(__name__)


def evaluate_speechocean762(data_dir: str, max_samples: int = 0):
    """
    Evaluate on SpeechOcean762 dataset.
    Reports Pearson correlation between predicted and human scores
    for accuracy, fluency, prosody, completeness, and total.
    """
    from scipy.stats import pearsonr

    data_path = Path(data_dir)
    scores_file = data_path / "scores.json"
    wav_dir = data_path / "wav"

    if not scores_file.exists():
        print(f"ERROR: scores.json not found at {scores_file}")
        print("Download SpeechOcean762 from: https://www.openslr.org/101/")
        return

    with open(scores_file, encoding="utf-8") as f:
        ground_truth = json.load(f)

    from backend.services.speech_processing import analyze_recording

    predictions = {
        "accuracy": [], "fluency": [], "prosody": [],
        "completeness": [], "total": [],
    }
    actuals = {
        "accuracy": [], "fluency": [], "prosody": [],
        "completeness": [], "total": [],
    }

    samples = list(ground_truth.items())
    if max_samples > 0:
        samples = samples[:max_samples]

    for i, (utt_id, scores) in enumerate(samples):
        wav_path = wav_dir / f"{utt_id}.wav"
        if not wav_path.exists():
            continue

        text = scores.get("text", "")
        try:
            with open(wav_path, "rb") as f:
                audio_bytes = f.read()
            result = analyze_recording(audio_bytes, text, "")
        except Exception as e:
            logger.warning("Failed on %s: %s", utt_id, e)
            continue

        for dim in predictions:
            pred_val = result.get(dim)
            gt_val = scores.get(dim)
            if pred_val is not None and gt_val is not None:
                predictions[dim].append(pred_val)
                actuals[dim].append(gt_val)

        if (i + 1) % 50 == 0:
            print(f"  Processed {i + 1}/{len(samples)} utterances...")

    print("\n=== SpeechOcean762 Results ===")
    print(f"{'Dimension':<15} {'Pearson r':<12} {'p-value':<12} {'N samples'}")
    print("-" * 50)

    for dim in predictions:
        if len(predictions[dim]) >= 2:
            r, p = pearsonr(actuals[dim], predictions[dim])
            print(f"{dim:<15} {r:>10.4f}   {p:>10.4e}   {len(predictions[dim])}")
        else:
            print(f"{dim:<15} {'N/A':>10}   {'N/A':>10}   {len(predictions[dim])}")


def evaluate_l2arctic(data_dir: str, max_samples: int = 0):
    """
    Evaluate MDD on L2-ARCTIC 6-speaker test set.
    Reports phone-level Precision, Recall, F1 for error detection.
    """
    data_path = Path(data_dir)

    # L2-ARCTIC test speakers (6 speakers from the paper)
    test_speakers = ["YBAA", "ZHAA", "ASI", "RRBI", "SVBI", "TNI"]

    from backend.services.speech_processing import analyze_recording
    from backend.services.phoneme_lookup import get_phonemes_for_sentence

    tp, fp, fn = 0, 0, 0  # True positive, false positive, false negative errors
    total_phones = 0
    total_correct = 0

    for speaker in test_speakers:
        speaker_dir = data_path / speaker
        annotation_dir = speaker_dir / "annotation"
        wav_dir = speaker_dir / "wav"

        if not speaker_dir.exists():
            print(f"  Speaker {speaker} not found, skipping...")
            continue

        wav_files = sorted(wav_dir.glob("*.wav")) if wav_dir.exists() else []
        if max_samples > 0:
            wav_files = wav_files[:max_samples]

        for wav_path in wav_files:
            utt_id = wav_path.stem
            ann_path = annotation_dir / f"{utt_id}.TextGrid"

            # Load ground truth annotations
            if not ann_path.exists():
                continue

            try:
                gt_errors = _parse_l2arctic_annotation(ann_path)
            except Exception:
                continue

            # Get reference text
            txt_path = speaker_dir / "transcript" / f"{utt_id}.txt"
            if txt_path.exists():
                text = txt_path.read_text(encoding="utf-8").strip()
            else:
                continue

            try:
                with open(wav_path, "rb") as f:
                    audio_bytes = f.read()
                result = analyze_recording(audio_bytes, text, "")
            except Exception as e:
                logger.warning("Failed on %s/%s: %s", speaker, utt_id, e)
                continue

            # Compare predicted errors with ground truth
            pred_errors = set()
            if result.get("phone_errors"):
                for err in result["phone_errors"]:
                    if err.get("type") != "correct":
                        pred_errors.add((err.get("position", 0), err.get("canonical", "")))

            gt_error_set = set()
            for err in gt_errors:
                if err["type"] != "correct":
                    gt_error_set.add((err["position"], err["phone"]))

            # Count TP/FP/FN
            tp += len(pred_errors & gt_error_set)
            fp += len(pred_errors - gt_error_set)
            fn += len(gt_error_set - pred_errors)
            total_phones += len(gt_errors)
            total_correct += sum(1 for e in gt_errors if e["type"] == "correct")

        print(f"  Processed speaker {speaker}")

    print("\n=== L2-ARCTIC MDD Results ===")
    precision = tp / (tp + fp) if (tp + fp) > 0 else 0
    recall = tp / (tp + fn) if (tp + fn) > 0 else 0
    f1 = 2 * precision * recall / (precision + recall) if (precision + recall) > 0 else 0

    print(f"Total phones evaluated: {total_phones}")
    print(f"Precision: {precision:.4f}")
    print(f"Recall:    {recall:.4f}")
    print(f"F1:        {f1:.4f}")
    print(f"(Target F1: ~0.65-0.70 per Tu et al. 2025)")


def _parse_l2arctic_annotation(textgrid_path):
    """Parse L2-ARCTIC phone-level annotation TextGrid."""
    from praatio import textgrid

    tg = textgrid.openTextgrid(str(textgrid_path), includeEmptyIntervals=False)
    errors = []

    # L2-ARCTIC annotations have tiers for phones and error types
    for tier_name in tg.tierNames:
        tier = tg.getTier(tier_name)
        if "phone" in tier_name.lower() or "error" in tier_name.lower():
            for i, interval in enumerate(tier.entries):
                label = interval.label.strip()
                if not label:
                    continue
                # Parse error annotation format: "phone:error_type" or just "phone"
                if ":" in label:
                    phone, err_type = label.split(":", 1)
                else:
                    phone = label
                    err_type = "correct"

                errors.append({
                    "position": i,
                    "phone": phone.upper().strip(),
                    "type": err_type.strip(),
                    "start": interval.start,
                    "end": interval.end,
                })
            break  # Use first matching tier

    return errors


def main():
    parser = argparse.ArgumentParser(description="LinguAR benchmark validation")
    parser.add_argument("--dataset", choices=["speechocean762", "l2arctic"], required=True)
    parser.add_argument("--data-dir", required=True, help="Path to dataset directory")
    parser.add_argument("--max-samples", type=int, default=0,
                        help="Max samples per speaker (0=all)")
    args = parser.parse_args()

    logging.basicConfig(level=logging.INFO)

    if args.dataset == "speechocean762":
        evaluate_speechocean762(args.data_dir, args.max_samples)
    elif args.dataset == "l2arctic":
        evaluate_l2arctic(args.data_dir, args.max_samples)


if __name__ == "__main__":
    main()
