class Solution:
    def rob(self, nums: List[int]) -> int:
        # keys: (i, bool) where i is index on street,
        #                       bool indicates whether house i was robbed
        # value: the maximum amt of money with that last decision
        
        n = len(nums)
        dp = {
                (0, True): nums[0],
                (0, False): 0,
                # (1, True): nums[1],
                # (1, False): nums[0]
            }
        for i in range(1, n):
            dp[(i, True)] = dp[(i-1, False)] + nums[i]
            dp[(i, False)] = max(dp[(i-1, True)], dp[(i-1, False)])
        
        return max(dp[(n-1, True)], dp[(n-1, False)])