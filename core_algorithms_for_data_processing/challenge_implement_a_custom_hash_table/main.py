class HashTable:
    def __init__(self, size=8):
        self.size = size
        self.buckets = [[] for _ in range(self.size)]

    def _hash(self, key):
        return hash(key) % self.size

    def put(self, key, value):
        idx = self._hash(key)
        bucket = self.buckets[idx]
        for i, (k, _) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)
                return
        bucket.append((key, value))

    def get(self, key):
        idx = self._hash(key)
        bucket = self.buckets[idx]
        for k, v in bucket:
            if k == key:
                return v
        return None

    def delete(self, key):
        idx = self._hash(key)
        bucket = self.buckets[idx]
        for i, (k, _) in enumerate(bucket):
            if k == key:
                del bucket[i]
                return


# Example usage (not part of the task)
ht = HashTable(size=4)
ht.put("apple", 1)
ht.put("banana", 2)
print(ht.get("apple"))   # expected: 1
ht.delete("banana")
print(ht.get("banana"))  # expected: None