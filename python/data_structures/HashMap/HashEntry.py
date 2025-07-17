from dataclasses import dataclass
from typing import Any


@dataclass
class HashEntry:
    """Represents a key-value entry in the hash map."""
    key: str
    value: Any

    def matches_key(self, key: str) -> bool:
        return self.key == key
