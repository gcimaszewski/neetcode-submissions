import heapq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.minheap = []
        # fills the heap with the k largest items from nums
        for n in nums:
            self._add_to_heap(n)
    
    def _add_to_heap(self, n: int): 
        heapq.heappush(self.minheap, n)
        if len(self.minheap) > self.k:
            _ = heapq.heappop(self.minheap)
 
    def add(self, val: int) -> int:
        self._add_to_heap(val)
        return self.minheap[0]        
