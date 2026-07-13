import heapq
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        step_idx = 0
        max_at_step = []
        maxheap = []

        left = 0
        for right in range(len(nums)):
            elem = nums[right]
            heapq.heappush(maxheap, (-elem, right))

            while (right - left + 1 ) > k:
                left += 1
            
            if right - left + 1 == k:
                while True:
                    max_elem, idx = maxheap[0]
                    if left <= idx <= right:
                        max_at_step.append(-1*max_elem)
                        break
                    else:
                        _ = heapq.heappop(maxheap)
        
        return max_at_step
