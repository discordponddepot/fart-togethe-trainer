from __future__ import annotations

import sys
from dataclasses import dataclass

from loguru import logger

GAME_EXE = "FartTogethe.exe"

try:
    import pymem  # type: ignore
    import pymem.process  # type: ignore
except ImportError:  # pragma: no cover - non-windows
    pymem = None  # type: ignore


@dataclass
class AttachedProcess:
    pid: int
    handle: object


def attach(pid: int | None = None) -> AttachedProcess | None:
    if sys.platform != "win32" or pymem is None:
        logger.warning("process attach unsupported on this platform")
        return None

    if pid is None:
        try:
            pm = pymem.Pymem(GAME_EXE)
        except pymem.exception.ProcessNotFound:
            logger.error("Fart Togethe is not running ({exe})", exe=GAME_EXE)
            return None
    else:
        pm = pymem.Pymem(pid=pid)

    logger.info("attached to Fart Togethe pid={pid}", pid=pm.process_id)
    return AttachedProcess(pid=pm.process_id, handle=pm)