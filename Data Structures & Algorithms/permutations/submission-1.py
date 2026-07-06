class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # to generate a permutation: 
        # we "try" each element of `nums` in the 0th element of the array
        # then, we try n-1 elements in the 1th element, n-2 elements in the 2nd, etc.
        
        solution = []
        permutation = []

        def backtrack(idxs_used):
            if len(permutation) == len(nums):
                solution.append(permutation[:])
                return

            for i in range(len(nums)):
                if i not in idxs_used:
                    idxs_used.add(i)
                    permutation.append(nums[i])
                    backtrack(idxs_used)
                    permutation.pop()
                    idxs_used.remove(i)
        
        backtrack(set())
        return solution