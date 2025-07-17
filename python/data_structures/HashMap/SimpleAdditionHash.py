from data_structures.HashMap.HashFunction import HashFunction


class SimpleAdditionHash(HashFunction):
    """Basic hash function implementation using byte addition."""

    def hash_key(self, key: str) -> int:
        return sum(key.encode())

    def handle_collision(self, key: str, attempt: int) -> int:
        """Linear probing collision resolution."""
        return self.hash_key(key) + attempt

