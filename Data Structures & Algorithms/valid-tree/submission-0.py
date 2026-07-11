class UnionFind:
    def __init__(self, size):
        self.parent = [_ for _ in range(size)]
        self.rank = [0 for _ in range(size)]
        self.num_components = size
    
    def find_set(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find_set(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        # returns a boolean, indicating if a union operation occurred,
        # False means x, y were already in same set.
        root_x = self.find_set(x)
        root_y = self.find_set(y)
        if root_x != root_y:
            rank_x = self.rank[root_x]
            rank_y = self.rank[root_y]
            if rank_y < rank_x:
                self.parent[root_y] = root_x
            else:
                self.parent[root_x] = root_y
                if rank_x == rank_y:
                    self.rank[root_y] += 1 

            self.num_components -= 1
            return True
        return False
     #   self.link(self.find_set(x), self.find_set(y))


class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        union_find = UnionFind(n)
        for (u, v) in edges:
            # if we try to call union(x, y) but find_set(x)==find_set(y), then there is a cycle
            absorbed = union_find.union(u, v)
            if not absorbed:
                print(f'edge {u},{v} added a cycle')
                return False

        # check that all nodes are in one component
        if union_find.num_components != 1:
            return False
        
        # check no cycles
        return True
