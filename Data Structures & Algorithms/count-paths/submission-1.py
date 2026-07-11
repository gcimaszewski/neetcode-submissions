class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # we can only move in 2 directions: down or right
        # we can reach a target square coming from a square to the left or up
        # let numPaths(s, t) = number of paths from source square s to target square t
        # numPaths(s, t) = numPaths(s, (t_row - 1, t_col)) + numPaths(s, (t_row, t_col-1)) 

        # base cases:
        # numPaths((t_row-1, t_col), t) = 1
        # numPaths((t_row, t_col-1), t) = 1

        # build a table bottom-up to compute the number of paths
        np = [[0 for c in range(n)] for r in range(m)]
        # top row: only can move to the right from (0,0)
        for c in range(n):
            np[0][c] = 1
        # leftmost column: only can move down from (0,0)
        for r in range(m):
            np[r][0] = 1
        
        for i in range(1, m):
            for j in range(1, n):
                num_paths_from_up = np[i-1][j]
                num_paths_from_left = np[i][j-1]
                np[i][j] = num_paths_from_up + num_paths_from_left
        
        return np[m-1][n-1]