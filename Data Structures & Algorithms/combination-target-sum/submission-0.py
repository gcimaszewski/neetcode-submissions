class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        solutions = []
        summands = []

        def backtrack(idx, sum_of_state):
            # idx tracks where we are in the list of numbers
            # by requiring that repeated numbers be adjacent to each other,
            # we can remove the duplicates problem
            if sum_of_state == target:
                solutions.append(summands[:])
                return
            
            for j in range(idx, len(nums)):
                n = nums[j]
                if target - (sum_of_state + n) >= 0:
                    summands.append(n)
                    backtrack(j, sum_of_state + n)
                    summands.pop()
        
        backtrack(0, 0)
        return solutions
