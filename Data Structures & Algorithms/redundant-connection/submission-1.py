class UnionFind:

    def __init__(self):
        self.parent = {}
        self.rank = {}
        self.num_components = 0
        # self.parent = [_ for _ in range(size)]
        # self.rank = [0 for _ in range(size)]
        # self.num_components = size

    def make_set(self, x):
        if x in self.parent:
            return 
        self.parent[x] = x
        self.rank[x] = 0
        self.num_components += 1

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
            self.num_components -=1
            return True
        return False

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        union_find = UnionFind()
        cycle_edges = []
        for u, v in edges:
            union_find.make_set(u)
            union_find.make_set(v)
            merged = union_find.union(u, v)
            if not merged:
                cycle_edges.append([u, v])
        if len(cycle_edges) == 0:
            return []
        return cycle_edges[-1]

