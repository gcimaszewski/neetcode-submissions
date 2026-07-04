class Solution:
    """
    You are given an array of integers nums containing n + 1 integers.
    Each integer in nums is in the range [1, n] inclusive.
    
    There is exactly one repeated integer in nums, and every other integer appears at most once.
    Return the repeated integer.
    """

    def findDuplicate(self, nums: List[int]) -> int:
        # approach: use `nums` as a hash set itself
        # for each number: map it to its index num - 1
        # multiply that element of the array by -1 (this is ok because all values of nums constrained to be positive)
        # as we iterate over nums and test new elements:
        # if the element we next encounter already has its index set to negative, that means it's a duplicate
        
        slow = fast = nums[0]
        #fast = nums[nums[0]]
        slow_ct = 0
        while True:
       # while slow_ct <= len(nums):
            slow = nums[slow]
            fast = nums[nums[fast]]
            if fast == slow:
                break 

        # find entry point of the cycle
        slow = nums[0]
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        return slow

        # for idx in range(len(nums)):
        #     n = abs(nums[idx])
        #     map_idx = n - 1
        #     if nums[map_idx] < 0:
        #         return n
        #     nums[map_idx] *= -1
        # return -1
