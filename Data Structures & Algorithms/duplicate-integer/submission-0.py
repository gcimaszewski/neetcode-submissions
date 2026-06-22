class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for elem in nums:
            if elem in seen:
                return True
            seen.add(elem)
        return False