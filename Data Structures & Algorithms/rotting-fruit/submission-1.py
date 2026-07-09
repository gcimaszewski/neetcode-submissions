from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        q = deque()
        m=len(grid)
        n=len(grid[0])

        num_fresh_fruit = 0
        for i in range(m):
            for j in range(n):
                fruit = grid[i][j]
                if fruit == 2:
                    q.append((i,j))
                elif fruit == 1:
                    num_fresh_fruit += 1
        
        
        minutes = 0
        if num_fresh_fruit == 0:
            return 0
        while q:
            nlevel = len(q)
            minutes += 1
            for _ in range(nlevel):
                r, c = q.popleft()
                if r > 0 and grid[r-1][c] == 1:
                    num_fresh_fruit -= 1
                    grid[r-1][c]=2
                    q.append((r-1, c))
                if r < m -1 and grid[r+1][c] == 1:
                    num_fresh_fruit -= 1
                    grid[r+1][c]=2
                    q.append((r+1, c))
                if c > 0 and grid[r][c-1] == 1:
                    num_fresh_fruit -= 1
                    grid[r][c-1] = 2
                    q.append((r, c-1))
                if c < n - 1 and grid[r][c+1]==1:
                    num_fresh_fruit -= 1
                    grid[r][c+1]=2
                    q.append((r, c+1))
            if num_fresh_fruit == 0:
                break
        return minutes if num_fresh_fruit == 0 else -1

