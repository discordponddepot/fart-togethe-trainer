from __future__ import annotations

import argparse
import sys

from loguru import logger

from trainer.bootstrap import bootstrap
from trainer.handlers import ui_handler


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    p = argparse.ArgumentParser(prog="fart-togethe-trainer")
    p.add_argument("--dry-run", action="store_true", help="Do not attach to game process")
    p.add_argument("--pid", type=int, default=None, help="Explicit Fart Togethe PID")
    p.add_argument("--headless", action="store_true", help="Skip Qt UI, run console loop")
    return p.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    ctx = bootstrap(dry_run=args.dry_run, pid=args.pid)
    logger.info("fart-togethe-trainer boot ok pid={pid}", pid=ctx.pid)
    if args.headless:
        from trainer.handlers import console_handler

        return console_handler.run(ctx)
    return ui_handler.run(ctx)


if __name__ == "__main__":
    sys.exit(main())