class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # frontier: contains cells by Atlantic ocean (bottom, right)
        # row = m - 1 or col = n-1
        # reaches pacific when row = 0 or col = 0

        m = len(heights)
        n = len(heights[0])

        frontier_pacific = (
            [(0, c) for c in range(n)] + 
            [(r, 0) for r in range(1, m)]
        )
        frontier_atlantic = (
            [(m-1, c) for c in range(n)] + 
            [(r, n-1) for r in range(m-1)]
        )
        
        def dfs_with_stack(stack, reachable):
            while stack:
                (r, c) = stack.pop()
                if (r,c) in reachable:
                    continue
                reachable.add((r,c))
                if r > 0 and heights[r-1][c] >= heights[r][c]:
                    stack.append((r-1,c))
                if r < m - 1 and heights[r+1][c] >= heights[r][c]:
                    stack.append((r+1,c))
                if c > 0 and heights[r][c-1] >= heights[r][c]:
                    stack.append((r, c-1))
                if c < n-1 and heights[r][c+1] >= heights[r][c]:
                    stack.append((r, c+1))
        flow_to_atlantic = set()
        flow_to_pacific = set()
        dfs_with_stack(frontier_pacific, flow_to_pacific)
        dfs_with_stack(frontier_atlantic, flow_to_atlantic)
        flow_to_both = flow_to_atlantic.intersection(flow_to_pacific)
        return [list(_) for _ in flow_to_both]

