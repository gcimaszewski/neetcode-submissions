import heapq
class MedianFinder:

    def __init__(self):
        self.left_maxheap = []
        self.right_minheap = []
        # at any time, abs(len(left) - len(right)) <= 1
        # if not: rebalance the array
        # take the longer
        # if longer = left: until (cond), e=left.popmax() and right.push(e)
        # if longer = right: e = right.popmin() and left.push(e)

    def _size(self):
        return len(self.left_maxheap) + len(self.right_minheap)

    def _unbalanced(self):
        return abs(len(self.left_maxheap) - len(self.right_minheap)) > 1

    def _rebalance(self):
        if not self._unbalanced():
            return # all good
        else:
            if len(self.left_maxheap) > len(self.right_minheap):
                while self._unbalanced():
                    e = heapq.heappop(self.left_maxheap)
                    heapq.heappush(self.right_minheap, -e)
            else:
                while self._unbalanced():
                    e = heapq.heappop(self.right_minheap)
                    heapq.heappush(self.left_maxheap, -e)


    def addNum(self, num: int) -> None:
        if self.right_minheap and num < self.right_minheap[0]:
            heapq.heappush(self.left_maxheap, -num)
        elif self.left_maxheap and num > -self.left_maxheap[0]:
            heapq.heappush(self.right_minheap, num)
        else:
            heapq.heappush(self.left_maxheap, -num)
        
        self._rebalance()

    def findMedian(self) -> float:
        if self._size() % 2 == 0:
            # even number: get max from left, min from right, average together
            left = -self.left_maxheap[0]
            right = self.right_minheap[0]
            return (left + right)/2
        else:
            if len(self.left_maxheap) > len(self.right_minheap):
                return -self.left_maxheap[0]
            else:
                return self.right_minheap[0]
        
        