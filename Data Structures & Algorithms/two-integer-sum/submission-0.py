class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        seen = {}
        for idx in range(len(nums)):
            num = nums[idx]
            diff = target - num
            if diff in seen:
                return [seen[diff], idx]
            else:
                seen[num] = idx
        