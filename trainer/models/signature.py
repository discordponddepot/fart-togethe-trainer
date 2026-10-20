from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class Signature:
    name: str
    pattern: bytes
    module: str = "FartTogethe.exe"
    description: str = ""

    def as_hex(self) -> str:
        return " ".join(f"{b:02X}" for b in self.pattern)
</br>