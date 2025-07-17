from abc import ABC
from typing import Optional, Any, List, Tuple
from data_structures.HashMap.HashEntry import HashEntry
from data_structures.HashMap.StorageStrategy import StorageStrategy


class SeparateChaining(StorageStrategy, ABC):
    """Storage implementation using separate chaining for collision resolution."""

    def __init__(self, capacity: int) -> None:
        """Initialize storage with given capacity."""
        self._capacity = capacity
        self._buckets: List[List[HashEntry]] = [[] for _ in range(capacity)]

    def find_slot(self, key: str, hash_function, compress_hash_func, for_insertion: bool = False) -> Tuple[
        int, Optional[HashEntry]]:
        """Find slot for separate chaining storage.

        For separate chaining, we simply hash the key once and look in that bucket.
        """
        hash_code = hash_function.hash_key(key)
        index = compress_hash_func(hash_code)
        entry = self.get(index, key)
        return index, entry

    def get(self, index: int, key: str) -> Optional[HashEntry]:
        """Get entry by index and key."""
        bucket = self._buckets[index]
        for entry in bucket:
            if entry.matches_key(key):
                return entry
        return None

    def put(self, index: int, entry: HashEntry) -> bool:
        """Store entry at index. Returns True if new entry was added."""
        bucket = self._buckets[index]

        # Check if key already exists and update
        for i, existing_entry in enumerate(bucket):
            if existing_entry.matches_key(entry.key):
                bucket[i] = entry
                return False  # Updated existing entry

        # Add new entry
        bucket.append(entry)
        return True  # New entry added

    def remove(self, index: int, key: str) -> bool:
        """Remove entry by index and key. Returns True if entry was removed."""
        bucket = self._buckets[index]
        for i, entry in enumerate(bucket):
            if entry.matches_key(key):
                bucket.pop(i)
                return True
        return False

    def get_all_values(self) -> List[Optional[Any]]:
        """Get all stored values."""
        values = []
        for bucket in self._buckets:
            for entry in bucket:
                values.append(entry.value)
        return values

    def is_slot_available(self, index: int) -> bool:
        """Check if slot at index is available for new entry."""
        # In separate chaining, slots are always available
        return True

    def get_capacity(self) -> int:
        """Get storage capacity."""
        return self._capacity
