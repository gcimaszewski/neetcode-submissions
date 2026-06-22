class DynamicArray:
    
    def __init__(self, capacity: int):
        self._items = []
        self.capacity = capacity
        self.size = 0

    def get(self, i: int) -> int:
        return self._items[i]

    def set(self, i: int, n: int) -> None:
        # clarify: self.size must be > index
        self._items[i] = n

    def pushback(self, n: int) -> None:
        if self.size == self.capacity:
            self.resize()
        self._items.append(n)
        self.size += 1

    def popback(self) -> int:
        elem = self._items.pop()
        self.size -= 1
        return elem

    def resize(self) -> None:
        self.capacity *= 2

    def getSize(self) -> int:
        return self.size
    
    def getCapacity(self) -> int:
        return self.capacity
