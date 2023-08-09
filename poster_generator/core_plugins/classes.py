from dataclasses import dataclass

@dataclass(frozen=True,kw_only=True,slots=True)
class Dimension:
    px: int = 0
    percent: float = 0
    
    def to_pixels(self, size: int) -> int:
        return int(self.px + self.percent * size / 100)