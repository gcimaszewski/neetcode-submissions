"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    """
    Clone Graph

    Given a node in a connected undirected graph, return a deep copy of the graph.

    Each node in the graph contains an integer value and a list of its neighbors.

    """
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return

        idx_to_node = {}
        q = [node]
        while q:
            curr = q.pop(0)

            try:
                new_node = idx_to_node[curr.val]
            except KeyError:
                new_node = Node(curr.val)
                idx_to_node[curr.val] = new_node
            for nei in curr.neighbors:
                if nei.val not in idx_to_node:
                    idx_to_node[nei.val] = Node(nei.val)
                    q.append(nei)
                   # print(f'add bidirectional edge: {new_node.val} {n.val}')
                  #  new_node.neighbors.append(idx_to_node[n.val])
                  #  idx_to_node[n.val].neighbors.append(new_node)
                idx_to_node[curr.val].neighbors.append(idx_to_node[nei.val])

        return idx_to_node[1]