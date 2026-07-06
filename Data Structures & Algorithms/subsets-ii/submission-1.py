class Solution:
    """
    You are given an array nums of integers, which may contain duplicates. Return all possible subsets.

    The solution must not contain duplicate subsets. You may return the solution in any order.
    """
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        subsets = []
        state = []

        def backtrack(idx):
            if idx >= len(nums):
                subsets.append(state[:])
                return
            
            state.append(nums[idx])
            backtrack(idx + 1)
            state.pop()
            # intuition:
            # including a number -> excluding it in the next step
            # is equivalent to
            # excluding the number -> including it in the next step
            # to prevent generating duplicate subsets, skip over including this number
            # in the negative backtracking step if it has multiple occurrences in the array
            while (idx < len(nums) - 1) and nums[idx] == nums[idx + 1]:
                idx += 1
            backtrack(idx + 1)
        
        backtrack(0)
        return subsets
