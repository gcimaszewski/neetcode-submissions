class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # approach: use `nums` as a hash set itself
        # for each number: map it to its index num - 1
        # multiply that element of the array by -1 (this is ok because all values of nums constrained to be positive)
        # as we iterate over nums and test new elements:
        # if the element we next encounter already has its index set to negative, that means it's a duplicate
        for idx in range(len(nums)):
            n = abs(nums[idx])
            map_idx = n - 1
            if nums[map_idx] < 0:
                return n
            nums[map_idx] *= -1
        return -1
