# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        tree = []
        level = []
        
        q = [root]
        while len(q) > 0:
            # BFS: the queue contains all the nodes at one level 
            # at the beginning of the `while` iteration
            
            count_at_level = len(q)
            for _ in range(count_at_level):
                node = q.pop(0)
                level.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            tree.append(level[:])
            level.clear()
        
        return tree
