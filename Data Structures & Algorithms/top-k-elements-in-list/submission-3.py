import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # approach:
        # 1. intialize a minheap of capacity k, empty dict
        # 2. iterate through nums. track frequency of each num in dict
        # 3. compare frequency value to head of minheap.
        # 3. if freq < head: then it's not a top k frequency, just keep going
        # 3. if freq > head: then pop head of minheap, and add this freq. val. to it,
        # 3. reheapify as needed
        counts = {}
        top_k_heap = [(-1001, 'nil')] * k  # heap for storing the top k values
        for n in nums:  # O(len(nums))
            counts[n] = counts.get(n, 0) + 1
        
        # for n, freq in counts.items():
        #     # heap steps:
        #     # check the current minimum in the heap. 
        #     # if the frequency is bigger than that: pop the min, push the freq, reheapify
        #     smallest_top_k, _ = top_k_heap[0]
        #     if freq > smallest_top_k:
        #         _ = heapq.heappop(top_k_heap)  # O(log(k))
        #         heapq.heappush(top_k_heap, (freq, n)) #. o(log(k))
        # top_nums = [_[1] for _ in top_k_heap]
        # return top_nums
        

        # runtime analysis:
        # let n = len(nums)
        # O(n+ n*log k) 
        # = O( n(1 + log k) = O(n*log k)
        # space: O(m + k) (m = number of unique numbers in nums)


        # alternative approach with bucket sort
        buckets = [[] for _ in range(len(nums) + 1)]
        for num, freq in counts.items():
            buckets[freq].append(num)
        
        top_k_numbers = []
        for freq in range(len(nums), 0, -1):
        # for idx in range(len(buckets), -1, -1):
            for num in buckets[freq]:
                top_k_numbers.append(num)
            if len(top_k_numbers) >= k:
                break
        
        return top_k_numbers[:k]

