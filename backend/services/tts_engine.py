from __future__ import annotations

"""
TTS engine — generates reference audio using Piper TTS.

Voice: en_US-lessac-medium (clear American English pronunciation).
Voice models auto-download from HuggingFace on first use.

pip install piper-tts
"""

import io
import logging
import tempfile
import wave
from pathlib import Path

from backend.config import MODEL_CACHE_DIR

logger = logging.getLogger(__name__)

_piper = None
VOICE_MODEL = "en_US-lessac-medium"


def _get_piper():
    """Lazy-load Piper TTS."""
    global _piper
    if _piper is not None:
        return _piper

    try:
        from piper import PiperVoice

        model_dir = MODEL_CACHE_DIR / "piper"
        model_dir.mkdir(parents=True, exist_ok=True)

        model_path = model_dir / f"{VOICE_MODEL}.onnx"
        config_path = model_dir / f"{VOICE_MODEL}.onnx.json"

        if not model_path.exists():
            logger.info("Downloading Piper voice model: %s", VOICE_MODEL)
            _download_voice(VOICE_MODEL, model_dir)

        _piper = PiperVoice.load(str(model_path), config_path=str(config_path))
        logger.info("Piper TTS loaded: %s", VOICE_MODEL)
    except ImportError:
        logger.warning("piper-tts not installed. TTS unavailable.")
        _piper = None
    except Exception as e:
        logger.warning("Failed to load Piper TTS: %s", e)
        _piper = None

    return _piper


def _download_voice(voice_name: str, output_dir: Path):
    """Download Piper voice model from HuggingFace."""
    import urllib.request

    base_url = f"https://huggingface.co/rhasspy/piper-voices/resolve/main/en/en_US/lessac/medium"
    for filename in [f"{voice_name}.onnx", f"{voice_name}.onnx.json"]:
        url = f"{base_url}/{filename}"
        dest = output_dir / filename
        logger.info("Downloading %s", url)
        try:
            urllib.request.urlretrieve(url, str(dest))
        except Exception as e:
            logger.error("Failed to download %s: %s", url, e)
            raise


def synthesize(text: str) -> bytes | None:
    """
    Synthesize speech from text.
    Returns WAV bytes (16kHz mono 16-bit) or None if TTS unavailable.
    """
    voice = _get_piper()
    if voice is None:
        return None

    try:
        audio_buffer = io.BytesIO()

        with wave.open(audio_buffer, "wb") as wav_file:
            voice.synthesize(text, wav_file)

        return audio_buffer.getvalue()
    except Exception as e:
        logger.warning("TTS synthesis failed: %s", e)
        return None


def synthesize_to_file(text: str, output_path: str) -> bool:
    """Synthesize speech and save to WAV file."""
    wav_bytes = synthesize(text)
    if wav_bytes is None:
        return False

    Path(output_path).write_bytes(wav_bytes)
    return True
