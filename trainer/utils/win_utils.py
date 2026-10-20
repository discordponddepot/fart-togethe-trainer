from __future__ import annotations

import ctypes
import sys


def is_admin() -> bool:
    if sys.platform != "win32":
        return False
    try:
        return bool(ctypes.windll.shell32.IsUserAnAdmin())
    except Exception:
        return False


def require_admin() -> None:
    if not is_admin():
        raise PermissionError("fart-togethe-trainer needs admin for memory writes")
    </br>