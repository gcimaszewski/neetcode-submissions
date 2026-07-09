"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from collections import deque

class Solution:
    """
    Clone Graph

    Given a node in a connected undirected graph, return a deep copy of the graph.

    Each node in the graph contains an integer value and a list of its neighbors.

    """
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return

        old_to_new = {}
        q = deque([node])
        while q:
            curr = q.popleft()
            try:
                new_node = old_to_new[curr.val]
            except KeyError:
                new_node = Node(curr.val)
                old_to_new[curr.val] = new_node
            for nei in curr.neighbors:
                if nei.val not in old_to_new:
                    old_to_new[nei.val] = Node(nei.val)
                    q.append(nei)
                old_to_new[new_node.val].neighbors.append(old_to_new[nei.val])

        return old_to_new[1]