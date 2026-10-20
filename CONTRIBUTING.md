# Contributing to fart-togethe-trainer

Thanks for wanting to help the Fart Togethe Trainer community.

## Ground rules

- This is a hobbyist trainer for Fart Togethe — treat it as educational modding research.
- Do not commit game binaries, dumps, or leaked offsets.
- Keep PRs scoped. One feature per PR.

## Dev setup

```powershell
py -3.11 -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python -m trainer.main --dry-run
```

## Code style

- Python 3.11+, type hints everywhere.
- `ruff` + `black` on save.
- Services should not import PySide6 directly — UI stays in handlers.

## Offsets

If you add a new cheat module, put the AOB signature in
`offsets/signatures.py` and document the game build it targets.
Signatures must be reproducible; paste the pattern you scanned in the PR.