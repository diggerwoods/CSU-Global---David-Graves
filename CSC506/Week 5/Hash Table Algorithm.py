class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size

    def _hash(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        index = self._hash(key)
        if self.table[index] is None:
            self.table[index] = []
        for pair in self.table[index]:
            if pair[0] == key:
                pair[1] = value
                return
        self.table[index].append([key, value])

    def get(self, key):
        index = self._hash(key)
        if self.table[index] is None:
            return None
        for pair in self.table[index]:
            if pair[0] == key:
                return pair[1]
        return None

    def delete(self, key):
        index = self._hash(key)
        if self.table[index] is None:
            return False
        for i, pair in enumerate(self.table[index]):
            if pair[0] == key:
                del self.table[index][i]
                return True
        return False

# Example usage
hash_table = HashTable(10)
hash_table.insert("apple", 1)
hash_table.insert("banana", 2)
print(hash_table.get("apple"))  # Output: 1
print(hash_table.get("banana"))  # Output: 2
hash_table.delete("apple")
print(hash_table.get("apple"))  # Output: None
