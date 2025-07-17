"""
TODO:
- I probably want to break this out into a library so that we can have various hash_functions, collision
mechanisms etc.
"""
from typing import Optional, List, Tuple, Any

from data_structures.HashMap.HashEntry import HashEntry
from data_structures.HashMap.HashFunction import HashFunction
from data_structures.HashMap.SimpleAdditionHash import SimpleAdditionHash


class HashMap:
    """A hash map implementation supporting pluggable hash functions."""

    EMPTY_SLOT = None
    MAX_COLLISION_ATTEMPTS = 1000

    def __init__(self, capacity: int, hash_function: Optional[HashFunction] = None) -> None:
        """Initialize HashMap with given capacity and optional hash function.

        Args:
            capacity: Initial size of the storage array
            hash_function: Custom hash function implementation (optional)
        """
        self._capacity = capacity
        self._storage: List[Optional[HashEntry]] = [self.EMPTY_SLOT] * capacity
        self._hash_function = hash_function or SimpleAdditionHash()
        self._size = 0


    def _compress_hash(self, hash_code: int) -> int:
        """Map hash code to valid array index."""
        return hash_code % self._capacity

    def _find_slot(self, key: str, for_insertion: bool = False) -> Tuple[int, Optional[HashEntry]]:
        """Find appropriate slot for a key, handling collisions.

        Args:
            key: Key to find slot for
            for_insertion: Whether this search is for insertion (affects collision handling)

        Returns:
            Tuple of (slot_index, current_entry)
        """
        collision_count = 0

        while collision_count < self.MAX_COLLISION_ATTEMPTS:
            hash_code = self._hash_function.handle_collision(key, collision_count)
            index = self._compress_hash(hash_code)
            current_entry = self._storage[index]

            if current_entry is self.EMPTY_SLOT or current_entry.matches_key(key):
                return index, current_entry

            if for_insertion and current_entry is None:
                return index, None

            collision_count += 1

        raise OverflowError("Hash map is full or maximum collision attempts reached")

    def __getitem__(self, key: str) -> Optional[Any]:
        """Retrieve value by key using dictionary syntax.

        Args:
            key: Key to look up

        Returns:
            Value associated with key or None if not found
        """
        index, entry = self._find_slot(key)

        if entry is self.EMPTY_SLOT or entry is None:
            return None

        return entry.value

    def __setitem__(self, key: str, value: Any) -> None:
        """Store value by key using dictionary syntax.

        Args:
            key: Key to store value under
            value: Value to store
        """
        index, existing_entry = self._find_slot(key, for_insertion=True)

        new_entry = HashEntry(key=key, value=value)
        self._storage[index] = new_entry

        if existing_entry is self.EMPTY_SLOT:
            self._size += 1

    @property
    def values(self) -> List[Optional[Any]]:
        """Get the underlying storage array.

        Returns:
            List of stored values
        """
        return [entry.value if entry else None for entry in self._storage]

    @property
    def size(self) -> int:
        """Get number of stored key-value pairs."""
        return self._size
