from __future__ import annotations

from pydantic import BaseModel, Field


class OffsetEntry(BaseModel):
    name: str
    module: str = "FartTogethe.exe"
    pattern: str
    offset: int = 0
    build: str = "2026.02"


class OffsetTable(BaseModel):
    version: str = "1.0"
    entries: list[OffsetEntry] = Field(default_factory=list)

    def as_dict(self) -> dict[str, int]:
        return {e.name: e.offset for e in self.entries}