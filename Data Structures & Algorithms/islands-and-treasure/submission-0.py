from collections import deque

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        
        q = deque()
        m = len(grid)
        n = len(grid[0])

        land = (2**31) - 1
        treasure = 0
        idx_to_pathdist = {}
        for i in range(m):
            for j in range(n):
                cell = grid[i][j]
                if cell != land:
                    continue
                # we hit a land cell.
                # perform bfs to find the shortest route to the chest
                # we can use the result for other land cells encountered in the path
                q.appendleft((i,j, []))
                visited = set()
                reachable = False
                while q:
                    
                    (r,c, path) = q.popleft()
                    visited.add((r,c))
                #    print(f'initial {i},{j} checking {r},{c}')
                    if grid[r][c] == treasure:
                        reachable = True
                        q.appendleft(path)
                        break

                    path.append((r,c))
                    if r > 0 and grid[r-1][c] in (land, treasure) and (r-1,c) not in visited:
                        q.append((r-1, c, path[:]))
                    if r < m - 1 and grid[r+1][c] in (land, treasure) and (r+1,c) not in visited:
                        q.append((r+1, c, path[:]))
                    if c > 0 and grid[r][c-1] in (land, treasure) and (r,c-1) not in visited:
                        q.append((r, c-1, path[:] ))
                    if c < n - 1 and grid[r][c+1] in (land, treasure) and (r,c+1) not in visited:
                        q.append((r, c+1, path[:] ))
                
                
                if reachable:
                    path = q.popleft()
                    shortest_path_len = len(path)
                    for idx, (r,c) in enumerate(path):
                      #  grid[r][c] = shortest_path_len - idx
                        idx_to_pathdist[(r,c)] = shortest_path_len - idx
                q.clear()
                visited.clear()

        for (i,j), dist in idx_to_pathdist.items():
            grid[i][j] = dist