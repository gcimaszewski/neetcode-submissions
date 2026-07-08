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
        # do we have to take into account jagged or malformed grids?
        nrows = len(grid)
        ncols = len(grid[0])
        
        def getAdjacentLandCoords(r, c):
            coords = []
            if (r-1)>= 0 and grid[r-1][c] == '1':
                coords.append((r-1,c))
            if (r+1) < nrows and grid[r+1][c]=='1':
                coords.append((r+1,c))
            if c-1 >= 0 and grid[r][c-1]=='1':
                coords.append((r, c-1))
            if c+1 < ncols and grid[r][c+1]=='1':
                coords.append((r,c+1))
            return coords
        
        num_islands = 0
        for i in range(nrows):
            for j in range(ncols):
                if grid[i][j] == '0':
                    continue
                # bfs time
                # a coordinate's "children" are (x+-1),(y+-1)
                q.append((i,j))
                while len(q) > 0:
                    x,y = q.pop()
                    if grid[x][y] == '1':
                        grid[x][y] = '0'
                        q.extend(getAdjacentLandCoords(x,y))
                    #if (x,y) not in visited:
                   #     visited.add((x,y))
                    #    if grid[x][y] == '1':
                        #    q.extend(getAdjacentLandCoords(x,y))
                num_islands += 1
        
        return num_islands
                    






        
