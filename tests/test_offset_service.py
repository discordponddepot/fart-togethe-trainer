from pathlib import Path

from trainer.services.offset_service import load_offsets, DEFAULT_OFFSETS


def test_load_offsets_missing_file(tmp_path: Path) -> None:
    result = load_offsets(tmp_path / "nope.json")
    assert result == DEFAULT_OFFSETS


def test_load_offsets_valid(tmp_path: Path) -> None:
    p = tmp_path / "o.json"
    p.write_text('{"fart_meter": 123, "fart_speed": 456, "ghost_flag": 789}')
    result = load_offsets(p)
    assert result["fart_meter"] == 123
    assert result["ghost_flag"] == 789
</br>