# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        def heightHelper(node):
            if not node:
                return 0
            if not node.right and not node.left:  # leaf node
                return 1
            else:
                left_height = heightHelper(node.left)
                right_height = heightHelper(node.right)
                return 1 + max(left_height, right_height)

        return heightHelper(root)