from typing import Optional, Any, List, Tuple
from data_structures.HashMap.HashEntry import HashEntry
from data_structures.HashMap.StorageStrategy import StorageStrategy


class ArrayBasedStorage(StorageStrategy):
    """Storage implementation using array-based open addressing."""

    EMPTY_SLOT = None
    MAX_COLLISION_ATTEMPTS = 1000


    def __init__(self, capacity: int) -> None:
        """Initialize storage with given capacity."""
        self._capacity = capacity
        self._storage: List[Optional[HashEntry]] = [self.EMPTY_SLOT] * capacity

    def find_slot(self, key: str, hash_function, compress_hash_func, for_insertion: bool = False) -> Tuple[
        int, Optional[HashEntry]]:
        """Find appropriate slot for array-based storage, handling collisions.

        Uses open addressing with collision handling from the hash function.
        """
        collision_count = 0

        while collision_count < self.MAX_COLLISION_ATTEMPTS:
            hash_code = hash_function.handle_collision(key, collision_count)
            index = compress_hash_func(hash_code)
            current_entry = self._storage[index]

            if current_entry is self.EMPTY_SLOT or (current_entry is not None and current_entry.matches_key(key)):
                return index, current_entry

            if for_insertion and current_entry is None:
                return index, None

            collision_count += 1

        raise OverflowError("Hash map is full or maximum collision attempts reached")

    def get(self, index: int, key: str) -> Optional[HashEntry]:
        """Get entry by index and key."""
        entry = self._storage[index]
        if entry is not self.EMPTY_SLOT and entry is not None and entry.matches_key(key):
            return entry
        return None

    def put(self, index: int, entry: HashEntry) -> bool:
        """Store entry at index. Returns True if new entry was added."""
        existing_entry = self._storage[index]
        self._storage[index] = entry

        # Return True if this was a new entry (slot was empty)
        return existing_entry is self.EMPTY_SLOT

    def remove(self, index: int, key: str) -> bool:
        """Remove entry by index and key. Returns True if entry was removed."""
        entry = self._storage[index]
        if entry is not self.EMPTY_SLOT and entry is not None and entry.matches_key(key):
            self._storage[index] = self.EMPTY_SLOT
            return True
        return False

    def get_all_values(self) -> List[Optional[Any]]:
        """Get all stored values."""
        return [entry.value if entry else None for entry in self._storage]

    def is_slot_available(self, index: int) -> bool:
        """Check if slot at index is available for new entry."""
        return self._storage[index] is self.EMPTY_SLOT

    def get_capacity(self) -> int:
        """Get storage capacity."""
        return self._capacity

    def get_entry_at_index(self, index: int) -> Optional[HashEntry]:
        """Get entry at specific index (for collision handling)."""
        return self._storage[index]
