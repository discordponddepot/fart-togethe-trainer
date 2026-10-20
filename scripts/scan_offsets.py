from __future__ import annotations

import sys

from trainer.adapters.process_adapter import attach
from trainer.adapters.memory_adapter import MemoryAdapter
from offsets.signatures import ALL


def main() -> int:
    proc = attach()
    if proc is None:
        print("attach failed", file=sys.stderr)
        return 1
    mem = MemoryAdapter(proc.handle)
    for sig in ALL:
        addr = mem.scan_pattern(sig.pattern, sig.module)
        print(f"{sig.name}: {hex(addr) if addr else 'not found'}")
    return 0


if __name__ == "__main__":
    sys.exit(main())