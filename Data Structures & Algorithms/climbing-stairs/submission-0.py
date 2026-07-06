class Solution:
    def climbStairs(self, n: int) -> int:
        # idx into bottom_up: says how many ways there are to climb idx steps
        bottom_up = [0]
        for num_stairs in range(1, n + 1):
            if num_stairs == 1:
                bottom_up.append(1)
            elif num_stairs == 2:
                bottom_up.append(2)
            else:
                count = bottom_up[num_stairs - 1] + bottom_up[num_stairs - 2]
                bottom_up.append(count)
        
        return bottom_up[n]

