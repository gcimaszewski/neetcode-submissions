class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # for len(nums) terms, we have len(nums) different operations
        # explore all possible combinations with BFS + backtracking?
        memo = {}
        def traverse(i, current_sum):
            if i >= len(nums):
                return 1 if (current_sum==target) else 0
            # plus sign
         #   print(f'i {i} len nums: {nums} currents um: {sum_}')
            state = (i, current_sum)
            if state in memo:
                return memo[state]
            add = traverse(i+1, current_sum+nums[i])
            subtract = traverse(i+1, current_sum-nums[i])
            memo[state] = add + subtract
            return memo[state]
        return traverse(0, 0)
