from typing import Optional, List, Tuple, Any

from data_structures.HashMap.ArrayBasedStorage import ArrayBasedStorage
from data_structures.HashMap.HashEntry import HashEntry
from data_structures.HashMap.HashFunction import HashFunction
from data_structures.HashMap.SimpleAdditionHash import SimpleAdditionHash
from data_structures.HashMap.StorageStrategy import StorageStrategy


class HashMap:
    """A hash map implementation supporting pluggable hash functions and storage strategies."""

    def __init__(self, capacity: int, hash_function: Optional[HashFunction] = None,
                 storage_strategy: Optional[StorageStrategy] = None) -> None:
        """Initialize HashMap with given capacity, optional hash function, and storage strategy.

        Args:
            capacity: Initial size of the storage array
            hash_function: Custom hash function implementation (optional)
            storage_strategy: Storage strategy implementation (optional, defaults to ArrayBasedStorage)
        """
        self._capacity = capacity
        self._storage = storage_strategy or ArrayBasedStorage(capacity)
        self._hash_function = hash_function or SimpleAdditionHash()
        self._size = 0


    def _compress_hash(self, hash_code: int) -> int:
        """Map hash code to valid array index."""
        return hash_code % self._capacity


    def __getitem__(self, key: str) -> Optional[Any]:
        """Retrieve value by key using dictionary syntax.

        Args:
            key: Key to look up

        Returns:
            Value associated with key or None if not found
        """
        index, entry = self._storage.find_slot(key, self._hash_function, self._compress_hash)

        if entry is None:
            return None

        return entry.value

    def __setitem__(self, key: str, value: Any) -> None:
        """Store value by key using dictionary syntax.

        Args:
            key: Key to store value under
            value: Value to store
        """
        index, existing_entry = self._storage.find_slot(key, self._hash_function, self._compress_hash,
                                                        for_insertion=True)

        new_entry = HashEntry(key=key, value=value)
        is_new_entry = self._storage.put(index, new_entry)

        if is_new_entry:
            self._size += 1

    def __delitem__(self, key: str) -> None:
        """Remove entry by key.

        Args:
            key: Key to remove
        """
        index, entry = self._storage.find_slot(key, self._hash_function, self._compress_hash)


        if entry is not None:
            if self._storage.remove(index, key):
                self._size -= 1

    @property
    def values(self) -> List[Optional[Any]]:
        """Get all stored values.

        Returns:
            List of stored values
        """
        return self._storage.get_all_values()

    @property
    def size(self) -> int:
        """Get number of stored key-value pairs."""
        return self._size

    @property
    def capacity(self) -> int:
        """Get storage capacity."""
        return self._capacity

