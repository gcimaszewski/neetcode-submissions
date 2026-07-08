class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # approach:
        # iterate through the array in row-major order
        # when we hit a "1": start bfs from that coordinate, extending the borders of the island
        # keep track of all indices scanned with a hash set
        # after the island is all discovered: continue on
        # the next time we see another "1", check if it was alreaady added to another island
        # if yes just continue; if no then do another bfs

        q = []
        visited = set()

        # do we have to take into account jagged or malformed grids?
        nrows = len(grid)
        ncols = len(grid[0])
        
        def getAdjacentLandCoords(row_idx, col_idx):
            coords = []
            if (row_idx-1)>= 0:
                coords.append((row_idx-1,col_idx))
            if (row_idx+1) < nrows:
                coords.append((row_idx+1,col_idx))
            if col_idx-1 >= 0:
                coords.append((row_idx, col_idx-1))
            if col_idx+1 < ncols:
                coords.append((row_idx,col_idx+1))
            return coords
        
        num_islands = 0
        for i in range(nrows):
            for j in range(ncols):
                if (i, j) in visited:
                    continue
                if grid[i][j] == '0':
                    visited.add((i,j))
                    continue
                # bfs time
                # a coordinate's "children" are (x+-1),(y+-1)
                q.append((i,j))
                while len(q) > 0:
                    x,y = q.pop()
                    if (x,y) not in visited:
                        visited.add((x,y))
                        if grid[x][y] == '1':
                            q.extend(getAdjacentLandCoords(x,y))
                num_islands += 1
        
        return num_islands
                    






        
