from collections import OrderedDict


class LRU_Cache(object):
    def __init__(self, capacity=1):
        # Initialize class variables
        self.cache = OrderedDict()
        if capacity > 0:
            self.capacity = capacity
        else:
            print("Warning: Cache capacity can't be zero or negative, set as 1")
            self.capacity = 1

    def get(self, key):
        # Retrieve item from provided key.
        if key in self.cache:
            self.cache.move_to_end(key)
            return self.cache[key]
        else:
            # Return -1 if nonexistent.
            return -1

    def set(self, key, value):
        # If the key is in the cache
        if key in self.cache:
            self.cache[key] = value
            self.cache.move_to_end(key)
        else:
            # If the cache is at capacity remove the oldest item.
            if len(self.cache) > self.capacity - 1:
                self.cache.popitem(last=False)
            # Set the value if the key is not present in the cache.
            self.cache[key] = value


if __name__ == '__main__':
    # test 1
    our_cache = LRU_Cache(5)

    our_cache.set(1, 1)
    our_cache.set(2, 2)
    our_cache.set(3, 3)
    our_cache.set(4, 4)

    print(our_cache.get(1))  # returns 1
    print(our_cache.get(2))  # returns 2
    print(our_cache.get(9))  # returns -1 because 9 is not present in the cache

    our_cache.set(5, 5)
    our_cache.set(6, 6)

    print(our_cache.get(3)) # returns -1 because the cache reached it's capacity and 3 was the least recently used entry

    # test 2
    our_cache = LRU_Cache(0)

    our_cache.set(1, 1)
    print(our_cache.get(1))  # returns 1

    our_cache.set(2, 2)
    print(our_cache.get(1))  # returns -1

    # test 3
    our_cache = LRU_Cache(-5)

    our_cache.set(1, 1)
    print(our_cache.get(1))  # returns 1

    our_cache.set(2, 2)
    print(our_cache.get(1))  # returns -1