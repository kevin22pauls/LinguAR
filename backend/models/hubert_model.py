from __future__ import annotations

"""
HuBERT model — singleton loader for facebook/hubert-large-ls960-ft.

Used for:
  1. Frame-level embedding extraction (for retrieval-based MDD)
  2. CTC logits (for GOP scoring)

Uses a SINGLE HubertForCTC model for both tasks to save ~1.26GB memory
and avoid duplicate forward passes.

Model size: ~1.26GB. Loaded once at startup.
"""

import logging

import numpy as np
import torch

logger = logging.getLogger(__name__)

_ctc_model = None
_processor = None


def _get_device():
    return "cuda:0" if torch.cuda.is_available() else "cpu"


def get_hubert_ctc():
    """Return (ctc_model, processor). Single model for both embeddings and logits."""
    global _ctc_model, _processor
    if _ctc_model is not None:
        return _ctc_model, _processor

    from transformers import HubertForCTC, Wav2Vec2Processor
    from backend.config import settings

    device = _get_device()
    logger.info("Loading HuBERT model: %s on %s", settings.hubert_model, device)

    _processor = Wav2Vec2Processor.from_pretrained(settings.hubert_model)
    _ctc_model = HubertForCTC.from_pretrained(
        settings.hubert_model,
        output_hidden_states=True,
    ).to(device).eval()

    logger.info("HuBERT model loaded.")
    return _ctc_model, _processor


def extract_both(
    audio_array: np.ndarray,
    sr: int = 16000,
    layer: int = -1,
) -> tuple[np.ndarray, np.ndarray]:
    """
    Single forward pass → both embeddings and CTC logits.

    Returns:
        (embeddings, ctc_logits)
        embeddings: (num_frames, 1024)
        ctc_logits: (num_frames, vocab_size)
    """
    model, processor = get_hubert_ctc()
    device = _get_device()

    inputs = processor(
        audio_array,
        sampling_rate=sr,
        return_tensors="pt",
        padding=True,
    )
    input_values = inputs.input_values.to(device)

    with torch.no_grad():
        outputs = model(input_values)

    # Hidden states from encoder (for retrieval MDD)
    hidden_states = outputs.hidden_states[layer]  # (1, T, 1024)
    embeddings = hidden_states.squeeze(0).cpu().numpy()

    # CTC logits (for GOP scoring)
    logits = outputs.logits.squeeze(0).cpu().numpy()  # (T, vocab_size)

    return embeddings, logits


def extract_embeddings(
    audio_array: np.ndarray,
    sr: int = 16000,
    layer: int = -1,
) -> np.ndarray:
    """Extract frame-level hidden states from HuBERT. Shape: (num_frames, 1024)."""
    embeddings, _ = extract_both(audio_array, sr, layer)
    return embeddings


def extract_ctc_logits(
    audio_array: np.ndarray,
    sr: int = 16000,
) -> np.ndarray:
    """Extract CTC logits from HuBERT. Shape: (num_frames, vocab_size)."""
    _, logits = extract_both(audio_array, sr)
    return logits
