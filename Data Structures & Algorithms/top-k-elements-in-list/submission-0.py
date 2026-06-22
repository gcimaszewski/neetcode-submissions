class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        freqs = {}
        for n in nums:
            if n not in freqs:
                freqs[n] = 0
            freqs[n] += 1
        buckets = [[] for _ in range(len(nums))]
        for num, count in freqs.items():
            buckets[count - 1].append(num)
        
        top_k = []
        # get top k from buckets
        for idx in range(len(nums)):
            for item in buckets[len(nums) - 1 - idx]:
                if len(top_k) < k:
                    top_k.append(item)
            if len(top_k) == k:
                break
        return top_k
