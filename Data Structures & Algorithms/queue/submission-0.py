class Deque:
    
    def __init__(self):
        self._front = []
        self._back = []
        self._size = 0

    def isEmpty(self) -> bool:
        return self._size == 0
        
    def _rebalance(self):
        # if either _front/_back is empty while the other is non-empty:
        # rebalance the queue contents for optimized pop/popLeft
        if len(self._front) == 0 and len(self._back) > 0:
            # push from back to front
            mid = len(self._back)//2
            for e in self._back[mid::-1]:
                self._front.append(e)
            self._back = self._back[mid+1:]
        elif len(self._back) == 0 and len(self._front) > 0:
            mid = len(self._front)//2
            for e in self._front[mid::-1]:
                self._back.append(e)
            self._front = self._front[mid+1:]
        else:
            return


    def append(self, value: int) -> None:
        self._back.append(value)
        self._size += 1

    def appendleft(self, value: int) -> None:
        self._front.append(value)
        self._size += 1

    def pop(self) -> int:
        if self._size == 0:
            return -1
        if not self._back:
            self._rebalance()
        val = self._back.pop()
        self._size -= 1
        return val


    def popleft(self) -> int:
        if self._size == 0:
            return -1
        if not self._front:
            self._rebalance()
        val = self._front.pop()
        self._size -= 1
        return val
