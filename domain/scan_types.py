from enum import Enum


class ScanType(Enum):
    NETWORK = "network"
    WEB = "web"
    CODE = "code"
    CONTAINER = "container"
    SSL = "ssl"

    @classmethod
    def list_values(cls):
        return [c.value for c in cls]

    @classmethod
    def from_str(cls, s: str):
        s = (s or "").strip().lower()
        for c in cls:
            if c.value == s:
                return c
        raise ValueError(f"Unknown ScanType: {s}")
