class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        base = nums[0]
        for i in range(1, len(nums)):
            base ^= nums[i]
        return base