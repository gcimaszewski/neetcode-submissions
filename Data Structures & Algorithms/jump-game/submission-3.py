class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # DFS: start from idx 0
        # try each of the possible jumps and keep going down the tree

        memo = {}
        # greedy algorithm
        goal = len(nums) - 1
        for i in range(len(nums) - 2, -1, -1):
            allowed_hops = nums[i]
            if i + allowed_hops >= goal:
                goal = i
        return goal==0
        # def dfs(i):
        #     if i in memo:
        #         return memo[i]
        #     if i >= len(nums) - 1:
        #         return True
        #     for h in range(1, nums[i] + 1):
        #         if dfs(i + h):
        #             memo[i] = True
        #             return True
        #     memo[i] = False
        #     return False
        
      #  return dfs(0)