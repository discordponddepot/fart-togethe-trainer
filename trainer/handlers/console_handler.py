from __future__ import annotations

from loguru import logger

from trainer.bootstrap import TrainerContext
from trainer.services import cheat_service

MENU = """
[fart-togethe-trainer] console mode
1) toggle infinite fart
2) toggle fart speed
3) toggle ghost fart
q) quit
"""


def run(ctx: TrainerContext) -> int:
    svc = cheat_service.CheatService(ctx)
    print(MENU)
    while True:
        try:
            choice = input("> ").strip().lower()
        except (EOFError, KeyboardInterrupt):
            return 0
        if choice == "1":
            svc.toggle_infinite_fart()
        elif choice == "2":
            svc.toggle_fart_speed()
        elif choice == "3":
            svc.toggle_ghost_fart()
        elif choice == "q":
            return 0
        else:
            logger.info("unknown option {c}", c=choice)