class Solution:
    def jump(self, nums: List[int]) -> int:
        # intuitively: we can construct the shortest path to the goal
        # by finding the indices that allow us to hop the farthest
        # greedy: at index i, if we can jump to index j, we can also jump to i+1, ..., j-1
        # for each index: check if we can jump directly to the goal
        # otherwise: compute our jumping range. 
        # because we start from the back of the array, the number of hops for these spaces are already computed
        # pick the next hop that has the shortest path to goal
        # hop2goal(i) = min(hop2goal(i+1),hop2goal(i+2),...,hop2goal(j)) + 1

        # idea: store the "latest" hop that has a certain distance
        
        # last_idx_with_dist = {}
        goal = len(nums) - 1
        # dist = {goal: 0}

        if len(nums) == 1:
            return 0

        farthest = 0
        jump_frontier = 0
        dist = 0
        # logic: try all hops up to jump_frontier
        # update farthest= max(farthest, h + nums[h])
        # when the frontier fully explored: increment distance; set frontier to `farthest` from the last round
        # exit when farthest >= goal
        for i in range(len(nums) - 1):
            farthest = max(farthest, i + nums[i])
            if i == jump_frontier:
                dist += 1
                jump_frontier = farthest
                if jump_frontier >= goal:
                    break
            
        return dist

        # for i in range(len(nums) - 2, -1, -1):
        #     hop_range = nums[i]
        #     furthest_hop = i + hop_range
        #     if furthest_hop >= goal:
        #         last_idx_with_dist[1] = i
        #         dist[i] = 1
        #     elif hop_range == 0:
        #         # gulley - no-go zone
        #         dist[i] = float('inf')
        #     else:
        #         # we have other intermediate hop(s) to make
        #         best_next_dist = float('inf')
        #         for h in range(i+1,furthest_hop+1):
        #             best_next_dist = min(best_next_dist, dist[h])
        #         dist[i] = best_next_dist + 1
        # return dist[0]
