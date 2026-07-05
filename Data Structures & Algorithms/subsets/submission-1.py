class Solution:
    """
    Given an array nums of unique integers, return all possible subsets of nums.

    The solution set must not contain duplicate subsets. You may return the solution in any order.

    """
    
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()
        subsets = []
        path = []

        def backtrack(bag, idx):
            subsets.append(path[:])
            # if idx >= len(bag):
            #     subsets.append(running_subset[:])
            #     return
            
            # advance idx to the last unique position of the number
            # (takes care of duplicate subsets)
            for i in range(idx, len(bag)):
                if i > idx and bag[i] == bag[i-1]:
                    continue # don't create another backtracking path here
                path.append(bag[i])
                backtrack(bag, i + 1)
                path.pop()

            # while idx < len(bag) - 1 and bag[idx] == bag[idx+1]:
            #     idx += 1
            # running_subset.append(bag[idx])
            # backtrack(bag, idx + 1, running_subset)

            # undo the last addition
            # running_subset.pop()
            # backtrack(bag, idx + 1, running_subset)
        
        backtrack(nums, 0)
        return subsets