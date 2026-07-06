class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        range_xor = 0
        for i in range(len(nums) + 1):
            range_xor ^= i
        list_xor = 0
        for n in nums:
            list_xor ^= n
        return range_xor ^ list_xor