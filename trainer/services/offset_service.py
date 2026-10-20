from __future__ import annotations

import json
from pathlib import Path

from loguru import logger

OFFSETS_FILE = Path(__file__).resolve().parents[2] / "offsets" / "patterns.json"

DEFAULT_OFFSETS: dict[str, int] = {
    "fart_meter": 0x0,
    "fart_speed": 0x0,
    "ghost_flag": 0x0,
}


def load_offsets(path: Path | None = None) -> dict[str, int]:
    p = path or OFFSETS_FILE
    if not p.exists():
        logger.warning("offsets file missing, using defaults: {p}", p=p)
        return dict(DEFAULT_OFFSETS)
    try:
        data = json.loads(p.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        logger.error("bad offsets json: {err}", err=exc)
        return dict(DEFAULT_OFFSETS)
    return {k: int(v) for k, v in data.items()}