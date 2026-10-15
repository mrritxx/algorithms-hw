class Deque:
    def __init__(self):
        self.items = []

    def add_front(self, value):
        self.items.insert(0, value)

    def add_back(self, value):
        self.items.append(value)

    def remove_front(self):
        return self.items.pop(0)

    def remove_back(self):
        return self.items.pop()

    def size(self):
        return len(self.items)
