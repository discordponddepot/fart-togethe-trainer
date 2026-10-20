from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class TrainerState:
    pid: int | None
    attached: bool
    infinite_fart: bool = False
    fart_speed_mult: float = 1.0
    ghost_fart: bool = False
    log: list[str] = field(default_factory=list)

    def record(self, msg: str) -> None:
        self.log.append(msg)
        if len(self.log) > 200:
            self.log = self.log[-200:]