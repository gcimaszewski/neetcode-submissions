class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        # invariant:
        # everything with idx <= left is less than target
        # idx >= right greater than or equal to target
        left = -1
        right = len(nums)
        while left + 1 < right:
            mid = left + (right - left)//2
            if nums[mid] >= target:
                right = mid
            else:
                left = mid
        if right < len(nums) and nums[right] == target:
            return right
        return -1
        