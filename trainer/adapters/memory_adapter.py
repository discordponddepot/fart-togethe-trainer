from __future__ import annotations

from typing import Any

from loguru import logger


class MemoryAdapter:
    """Thin wrapper over pymem for typed reads/writes."""

    def __init__(self, process: Any) -> None:
        self._pm = process

    def read_int(self, address: int) -> int:
        return int(self._pm.read_int(address))

    def write_int(self, address: int, value: int) -> None:
        self._pm.write_int(address, value)

    def read_float(self, address: int) -> float:
        return float(self._pm.read_float(address))

    def write_float(self, address: int, value: float) -> None:
        self._pm.write_float(address, value)

    def scan_pattern(self, pattern: bytes, module: str) -> int | None:
        try:
            return int(self._pm.pattern_scan_module(pattern, module))
        except Exception as exc:  # pymem raises various
            logger.debug("pattern scan failed: {err}", err=exc)
            return None