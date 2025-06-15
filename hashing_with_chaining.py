class HashTable:
    def __init__(self, size=100):
        self.size = size
        self.buckets = [[] for _ in range(size)]

    def _hash(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        idx = self._hash(key)
        for i, (k, _) in enumerate(self.buckets[idx]):
            if k == key:
                self.buckets[idx][i] = (key, value)
                return
        self.buckets[idx].append((key, value))

    def search(self, key):
        idx = self._hash(key)
        for k, v in self.buckets[idx]:
            if k == key:
                return v
        return None

    def delete(self, key):
        idx = self._hash(key)
        self.buckets[idx] = [(k, v) for (k, v) in self.buckets[idx] if k != key]


# Test the HashTable
if __name__ == "__main__":
    ht = HashTable(size=10)

    # Insert key-value pairs
    ht.insert("apple", 5)
    ht.insert("banana", 7)
    ht.insert("orange", 3)
    ht.insert("banana", 10)  # update banana

    # Search values
    print("Search 'apple':", ht.search("apple"))      # should print 5
    print("Search 'banana':", ht.search("banana"))    # should print 10
    print("Search 'grape':", ht.search("grape"))      # should print None

    # Delete a key
    ht.delete("banana")
    print("After deleting 'banana':", ht.search("banana"))  # should print None
