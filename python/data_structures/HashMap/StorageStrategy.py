from abc import ABC, abstractmethod
from typing import Optional, List, Any, Tuple

from data_structures.HashMap.HashEntry import HashEntry


class StorageStrategy(ABC):
    """Abstract interface for hash map storage strategies."""

    @abstractmethod
    def __init__(self, capacity: int) -> None:
        """Initialize storage with given capacity."""
        pass

    @abstractmethod
    def find_slot(self, key: str, hash_function, compress_hash_func, for_insertion: bool = False) -> Tuple[
        int, Optional[HashEntry]]:
        """Find appropriate slot for a key, handling collisions according to the strategy.

        Args:
            key: Key to find slot for
            hash_function: Hash function to use
            compress_hash_func: Function to compress hash to array index
            for_insertion: Whether this search is for insertion

        Returns:
            Tuple of (slot_index, current_entry)
        """
        pass

    @abstractmethod
    def get(self, index: int, key: str) -> Optional[HashEntry]:
        """Get entry by index and key."""
        pass

    @abstractmethod
    def put(self, index: int, entry: HashEntry) -> bool:
        """Store entry at index. Returns True if new entry was added."""
        pass

    @abstractmethod
    def remove(self, index: int, key: str) -> bool:
        """Remove entry by index and key. Returns True if entry was removed."""
        pass

    @abstractmethod
    def get_all_values(self) -> List[Optional[Any]]:
        """Get all stored values."""
        pass

    @abstractmethod
    def is_slot_available(self, index: int) -> bool:
        """Check if slot at index is available for new entry."""
        pass

    @abstractmethod
    def get_capacity(self) -> int:
        """Get storage capacity."""
        pass
