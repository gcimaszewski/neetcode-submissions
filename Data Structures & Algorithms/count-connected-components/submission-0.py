class UnionFind:
    def __init__(self, size):
        self.parent = [i for i in range(size)]
        self.rank = [0 for _ in range(size)]
        self.num_components = size
    
    def find_set(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find_set(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        root_x = self.find_set(x)
        root_y = self.find_set(y)
        if root_x != root_y:
            if self.rank[root_x] > self.rank[root_y]:
                self.parent[root_y] = root_x
            else:
                self.parent[root_x] = root_y
                if self.rank[root_x] == self.rank[root_y]:
                    self.rank[root_y] += 1
            self.num_components -= 1
            return True
        return False


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        union_find = UnionFind(n)
        for (u, v) in edges:
            _ = union_find.union(u, v)
        
        return union_find.num_components
        