class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # approach:
        # iterate through the array in row-major order
        # when we hit a "1": start bfs from that coordinate, extending the borders of the island
        # keep track of all indices scanned with a hash set
        # after the island is all discovered: continue on
        # the next time we see another "1", check if it was alreaady added to another island
        # if yes just continue; if no then do another bfs

        stack = []
        # do we have to take into account jagged or malformed grids?
        nrows = len(grid)
        ncols = len(grid[0])
        
        num_islands = 0
        for i in range(nrows):
            for j in range(ncols):
                if grid[i][j] == '0':
                    continue
                # bfs time
                # a coordinate's "children" are (x+-1),(y+-1)
                stack.append((i,j))
                while len(stack) > 0:
                    x,y = stack.pop()
                    if grid[x][y] == '1':
                        grid[x][y] = '0'
                        # small optimization: mark the grid as visited when you push on the stack
                        # that way multiple instances of the same point wont be added to the stack
                        if x > 0 and grid[x-1][y]=='1':
                            stack.append((x-1,y))
                        if x < nrows - 1 and grid[x+1][y]=='1':
                            stack.append((x+1,y))
                        if y > 0 and grid[x][y-1]=='1':
                            stack.append((x,y-1))
                        if y < ncols -1 and grid[x][y+1]=='1':
                            stack.append((x,y+1))

                num_islands += 1
        
        return num_islands