class MinStack:

    def __init__(self):
        self._elements = []
        self._prefix_min = [float('inf')]

    def push(self, val: int) -> None:
        curr_min = min(self._prefix_min[-1], val)
        self._elements.append(val)
        self._prefix_min.append(curr_min)

    def pop(self) -> None:
        _ = self._prefix_min.pop()
        return self._elements.pop()

    def top(self) -> int:
        return self._elements[-1] if self._elements else None

    def getMin(self) -> int:
        return self._prefix_min[-1] if self._prefix_min else None
