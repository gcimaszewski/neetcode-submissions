class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()
        subsets = []

        def backtrack(bag, idx, running_subset):
            if idx >= len(bag):
                subsets.append(running_subset[:])
                return
            
            # advance idx to the last unique position of the number
            # (takes care of duplicate subsets)
            while idx < len(bag) - 1 and bag[idx] == bag[idx+1]:
                idx += 1
            running_subset.append(bag[idx])
            backtrack(bag, idx + 1, running_subset)

            # undo the last addition
            running_subset.pop()
            backtrack(bag, idx + 1, running_subset)
        
        backtrack(nums, 0, [])
        return subsets