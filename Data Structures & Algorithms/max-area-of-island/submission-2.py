class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        nrows = len(grid)
        ncols = len(grid[0])
        stack=[]

        max_island_area = 0
        for i in range(nrows):
            for j in range(ncols):
                if grid[i][j]==0:
                    print(f'here {(i,j)}')
                    continue
                stack.append((i,j))
                grid[i][j]=0

                island_area = 0
                while stack:
                    x,y=stack.pop()
                    island_area +=1
                    if x > 0 and grid[x-1][y]==1:
                        grid[x-1][y]=0
                        stack.append((x-1,y))
                    if x < nrows-1 and grid[x+1][y]==1:
                        grid[x+1][y]=0
                        stack.append((x+1,y))
                    if y > 0 and grid[x][y-1]==1:
                        grid[x][y-1]=0
                        stack.append((x,y-1))
                    if y<ncols-1 and grid[x][y+1]==1:
                        grid[x][y+1]=0
                        stack.append((x,y+1))
                print(f'original {(i,j)} island area: {island_area}')
                max_island_area=max(max_island_area, island_area)
        return max_island_area
