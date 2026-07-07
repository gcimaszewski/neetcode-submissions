# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # intuition: DFS, where search paths with `bad` node not further explored
        # initialize stack with root
        # from there: 
       # good_nodes = []
        good_nodes_count = 0
        stack = [(root, float('-inf'))]
        while len(stack) > 0:
            node, max_val_on_path = stack.pop()
            updated_max = max(max_val_on_path, node.val)
            if node.val >= max_val_on_path:
                good_nodes_count += 1
               # good_nodes.append(node)
            if node.left:
                stack.append((node.left, updated_max))
            if node.right:
                stack.append((node.right, updated_max))
        
        return good_nodes_count
     #   return len(good_nodes)
            
