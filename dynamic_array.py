class Array:
    def __init__(self):
        self.items = []

    def add(self, value):
        self.items.append(value)

    def get(self, index):
        return self.items[index]

    def set(self, index, value):
        self.items[index] = value

    def remove(self, index):
        return self.items.pop(index)

    def size(self):
        return len(self.items)
