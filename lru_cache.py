from collections import OrderedDict


class LRUCache:
    def __init__(self, capacity):
        if capacity < 1:
            raise ValueError("Ёмкость кеша должна быть положительной")
        self.capacity = capacity
        self.items = OrderedDict()

    def get(self, key):
        if key not in self.items:
            return None
        self.items.move_to_end(key)
        return self.items[key]

    def put(self, key, value):
        self.items[key] = value
        self.items.move_to_end(key)

        if len(self.items) > self.capacity:
            self.items.popitem(last=False)


cache = LRUCache(2)
cache.put("a", 10)
cache.put("b", 20)
print(cache.get("a"))
cache.put("c", 30)
print(cache.get("b"))
