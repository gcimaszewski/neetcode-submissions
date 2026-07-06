class Solution:
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
            while (idx < len(nums) - 1) and nums[idx] == nums[idx + 1]:
                idx += 1
            backtrack(idx + 1)
        
        backtrack(0)
        return subsets
