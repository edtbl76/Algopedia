from typing import Any, List, Optional


class HashMap:


    def __init__(self, size: int) -> None:
        self.size = size
        self.array: List[Optional[List[Any]]]  = [None for _ in range(size)]


    def assign(self, key: str, value: Any) -> None:
        array_index: int = self.compressor(self.hash_function(key))
        current_entry  = self.array[array_index]

        if current_entry is None:
            self.array[array_index] = [key, value]
            return

        if current_entry[0] == key:
            self.array[array_index] = [key, value]
            return

        collisions = 1

        while current_entry[0] != key:
            new_hash_code = self.hash_function(key, collisions)
            new_array_index = self.compressor(new_hash_code)
            current_entry  = self.array[new_array_index]

            if current_entry is None:
                self.array[new_array_index] = [key, value]
                return

            if current_entry[0] == key:
                self.array[new_array_index] = [key, value]
                return

            collisions += 1

        return



    def retrieve(self, key: str) -> Optional[Any]:
        array_index = self.compressor(self.hash_function(key))
        current_entry = self.array[array_index]

        if current_entry is None:
            return None

        if current_entry[0] == key:
            return current_entry[1]

        collisions = 1

        while current_entry[0] != key:
            new_hash_code = self.hash_function(key, collisions)
            new_array_index = self.compressor(new_hash_code)
            current_entry = self.array[new_array_index]

            if current_entry is None:
                return None

            if current_entry[0] == key:
                return current_entry[1]

            collisions += 1

        return None



    @staticmethod
    def hash_function(key: str, collision_count: int  = 0) -> int:
        key_bytes = key.encode()
        hash_code = sum(key_bytes)
        return hash_code + collision_count

    def compressor(self, hash_code: int) -> int:
        return hash_code % self.size

