from __future__ import annotations

from dataclasses import dataclass

from loguru import logger

from trainer.adapters import process_adapter
from trainer.services import offset_service, state_service


@dataclass
class TrainerContext:
    pid: int | None
    dry_run: bool
    offsets: dict[str, int]
    state: state_service.TrainerState


def bootstrap(dry_run: bool = False, pid: int | None = None) -> TrainerContext:
    if dry_run:
        logger.warning("dry-run mode: no process attach")
        resolved_pid = None
        proc = None
    else:
        proc = process_adapter.attach(pid)
        resolved_pid = proc.pid

    offsets = offset_service.load_offsets()
    state = state_service.TrainerState(pid=resolved_pid, attached=proc is not None)
    return TrainerContext(pid=resolved_pid, dry_run=dry_run, offsets=offsets, state=state)