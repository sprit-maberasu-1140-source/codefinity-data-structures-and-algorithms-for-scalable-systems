class BloomFilter:
    def __init__(self, size, hash_count):
        self.size = size
        self.hash_count = hash_count
        self.bit_array = [0] * size

    def _hashes(self, item):
        # Two base hashes, combined to generate multiple indices
        h1 = hash(str(item))
        h2 = hash(str(item) + "salt")
        return [(h1 + i * h2) % self.size for i in range(self.hash_count)]

    def add(self, item):
        for idx in self._hashes(item):
            self.bit_array[idx] = 1

    def contains(self, item):
        return all(self.bit_array[idx] == 1 for idx in self._hashes(item))

# Sample usage
bf = BloomFilter(size=100, hash_count=3)
bf.add("apple")
bf.add("banana")

result_apple = bf.contains("apple")
result_banana = bf.contains("banana")
result_orange = bf.contains("orange")

print(result_apple)
print(result_banana)
print(result_orange)