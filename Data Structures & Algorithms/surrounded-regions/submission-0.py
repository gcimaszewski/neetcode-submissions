class UnionFind:
    def __init__(self):
        self.parent = {}
        self.rank = {}
        self.has_border_patch = {}

    def __iter__(self):
        for x in self.parent:
            yield x

    def make_set(self, coord, on_border):
        if coord in self.parent:
            return
        self.parent[coord] = coord
        self.rank[coord] = 0
        self.has_border_patch[coord] = on_border
    
    def find_set(self, coord):
        if self.parent[coord] != coord:
            self.parent[coord] = self.find_set(self.parent[coord])
        return self.parent[coord]
    
    def union(self, coord1, coord2):
        root_c1 = self.find_set(coord1)
        root_c2 = self.find_set(coord2)
        if root_c1 != root_c2:
            if self.rank[root_c1] > self.rank[root_c2]:
                self.parent[root_c2] = root_c1
            else:
                self.parent[root_c1] = root_c2
                if self.rank[root_c1]==self.rank[root_c2]:
                    self.rank[root_c2]+=1
            self.has_border_patch[root_c1] |= self.has_border_patch[root_c2]
            self.has_border_patch[root_c2] |= self.has_border_patch[root_c1]
            return True
        return False



class Solution:
    def solve(self, board: List[List[str]]) -> None:
        
        m = len(board)
        n = len(board[0])

        def coord_on_border(r, c):
            return (r == 0 or r == m-1) or (c==0 or c==n-1)
        
        union_find = UnionFind()
        for r in range(m):
            for c in range(n):
                if board[r][c] == 'O':
                    union_find.make_set((r, c), coord_on_border(r,c))
                    if r > 0 and board[r-1][c] == 'O':
                        union_find.union((r,c), (r-1,c))
                    if c>0 and board[r][c-1]=='O':
                        union_find.union((r,c),(r,c-1))
            
        for o in union_find:
            has_cell_on_border = union_find.has_border_patch[union_find.find_set(o)]
            if not has_cell_on_border:
                board[o[0]][o[1]] = 'X'
        
        