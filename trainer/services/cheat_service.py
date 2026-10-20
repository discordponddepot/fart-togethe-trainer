from __future__ import annotations

from loguru import logger

from trainer.bootstrap import TrainerContext
from trainer.adapters.memory_adapter import MemoryAdapter


class CheatService:
    def __init__(self, ctx: TrainerContext) -> None:
        self._ctx = ctx
        self._mem = MemoryAdapter(ctx.state) if ctx.state.attached else None

    def _toggle(self, key: str) -> bool:
        st = self._ctx.state
        current = getattr(st, key)
        setattr(st, key, not current)
        logger.info("toggle {k} -> {v}", k=key, v=not current)
        st.record(f"{key}={not current}")
        return not current

    def toggle_infinite_fart(self) -> bool:
        on = self._toggle("infinite_fart")
        if on and self._mem:
            self._mem.write_int(self._ctx.offsets["fart_meter"], 9999)
        return on

    def toggle_fart_speed(self) -> bool:
        on = self._toggle("ghost_fart") if False else self._ctx.state.fart_speed_mult
        new_mult = 3.0 if self._ctx.state.fart_speed_mult == 1.0 else 1.0
        self._ctx.state.fart_speed_mult = new_mult
        if self._mem:
            self._mem.write_float(self._ctx.offsets["fart_speed"], new_mult)
        return new_mult > 1.0

    def toggle_ghost_fart(self) -> bool:
        on = self._toggle("ghost_fart")
        if self._mem:
            self._mem.write_int(self._ctx.offsets["ghost_flag"], 1 if on else 0)
        return on