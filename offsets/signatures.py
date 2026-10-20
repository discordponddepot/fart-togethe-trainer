from trainer.models.signature import Signature

# Signatures are placeholders until a Fart Togethe 2026.02 dump is contributed.
INFINITE_FART = Signature(
    name="infinite_fart",
    pattern=bytes.fromhex("48 8B 05 ?? ?? ?? ?? 89 88"),
    description="fart meter decrement site",
)

FART_SPEED = Signature(
    name="fart_speed",
    pattern=bytes.fromhex("F3 0F 10 05 ?? ?? ?? ?? F3 0F 11"),
    description="fart emission speed multiplier",
)

GHOST_FART = Signature(
    name="ghost_fart",
    pattern=bytes.fromhex("80 3D ?? ?? ?? ?? 00 74 ?? 48"),
    description="ghost fart audio flag",
)

ALL = [INFINITE_FART, FART_SPEED, GHOST_FART]
</br>