from abc import ABC, abstractmethod

class HashFunction(ABC):
    """ Abstract base class for hash functions """

    @abstractmethod
    def hash_key(self, key: str) -> int:
        """ calculate hash code for the given key """
        pass

    @abstractmethod
    def handle_collision(self, key: str, attempt: int) -> int:
        """ handle hash collision. """
        pass

