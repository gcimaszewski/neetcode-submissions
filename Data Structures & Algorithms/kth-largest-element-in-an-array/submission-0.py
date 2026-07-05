import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        kth_largest = []
        for n in nums:
            if len(kth_largest) < k:
                heapq.heappush(kth_largest, n)
            else:
                curr = kth_largest[0]
                if n >= curr:
                    _ = heapq.heapreplace(kth_largest, n)
        return kth_largest[0]