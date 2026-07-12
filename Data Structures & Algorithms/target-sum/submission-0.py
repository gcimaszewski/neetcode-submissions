class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # for len(nums) terms, we have len(nums) different operations
        # explore all possible combinations with BFS + backtracking?
        path=[]
        valid_sum_ways = 0
        def traverse(i, sum_):
            if i >= len(nums):
                return sum_==target
            # plus sign
         #   print(f'i {i} len nums: {nums} currents um: {sum_}')
            add = traverse(i+1, sum_+nums[i])
            subtract = traverse(i+1, sum_-nums[i])
            return add + subtract
        return traverse(0, 0)
