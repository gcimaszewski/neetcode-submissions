class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # to get to the ith step:
        # the cost is either:
        # cost2get2(i) = min(cost2get2(i-1) + costfrom[i-1], cost2get2(i-2)+cost[i-2])
        # cost2get2(0) = 0
        # cost2get2(1) = cost[0]
        # cost2get2(2) = min(cost2get2(1) + cost[1], cost2get2(0) + cost[0])
        # cost to get to step 1: cost[0]
        # cost to get to step 2: min(cost[0], )

        cost_to_reach = [0, 0] # [0, cost[0]]
        last_floor = len(cost)
        for i in range(2, last_floor + 1):
            cost_1step_up = cost_to_reach[i-1] + cost[i-1]
            cost_2step_up = cost_to_reach[i-2] + cost[i-2]
            cost_to_reach.append(min(cost_1step_up, cost_2step_up))
        return cost_to_reach[last_floor]