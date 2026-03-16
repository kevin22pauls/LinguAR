"""
CrisperWhisper ASR model — singleton loader.

Uses nyrahealth/CrisperWhisper (gated, requires HF token + nyrahealth
transformers fork for accurate timestamps).

Model is loaded once and reused across requests (~3GB VRAM/RAM).

REQUIRES: CrisperWhisper
  - pip install git+https://github.com/nyrahealth/transformers.git@crisper_whisper
  - huggingface-cli login (accept license at https://huggingface.co/nyrahealth/CrisperWhisper)
"""

import torch
import logging

logger = logging.getLogger(__name__)

_pipeline = None


def get_asr_pipeline():
    """Return the cached ASR pipeline, loading it on first call."""
    global _pipeline
    if _pipeline is not None:
        return _pipeline

    from transformers import pipeline
    from backend.config import settings

    device = "cuda:0" if torch.cuda.is_available() else "cpu"
    torch_dtype = torch.float16 if torch.cuda.is_available() else torch.float32

    model_id = settings.whisper_model

    logger.info("Loading ASR model: %s on %s", model_id, device)

    _pipeline = pipeline(
        "automatic-speech-recognition",
        model=model_id,
        device=device,
        torch_dtype=torch_dtype,
        return_timestamps="word",
    )

    logger.info("ASR model loaded.")
    return _pipeline


# REQUIRES: CrisperWhisper
def adjust_pauses_for_hf_pipeline_output(pipeline_output: dict) -> dict:
    """
    Adjust CrisperWhisper word timestamps so pauses are correctly
    attributed to silence gaps between words rather than being absorbed
    into adjacent word boundaries.

    CrisperWhisper's raw HF pipeline output may extend word-end timestamps
    into the following pause. This function trims each word's end timestamp
    to not exceed the next word's start timestamp, and adjusts start
    timestamps similarly so they don't precede the previous word's end.

    Based on nyrahealth/CrisperWhisper README implementation.
    """
    if "chunks" not in pipeline_output:
        return pipeline_output

    chunks = pipeline_output["chunks"]
    if len(chunks) <= 1:
        return pipeline_output

    adjusted = []
    for i, chunk in enumerate(chunks):
        ts = chunk.get("timestamp", (None, None))
        start = ts[0] if ts[0] is not None else 0.0
        end = ts[1] if ts[1] is not None else start

        # Trim end: don't extend past next word's start
        if i < len(chunks) - 1:
            next_ts = chunks[i + 1].get("timestamp", (None, None))
            next_start = next_ts[0]
            if next_start is not None and end > next_start:
                end = next_start

        # Trim start: don't precede previous word's end
        if i > 0 and adjusted:
            prev_end = adjusted[-1]["timestamp"][1]
            if prev_end is not None and start < prev_end:
                start = prev_end

        adjusted.append({
            "text": chunk.get("text", ""),
            "timestamp": (start, end),
        })

    return {
        "text": pipeline_output.get("text", ""),
        "chunks": adjusted,
    }
