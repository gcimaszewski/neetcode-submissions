# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # a binary tree is balanced if:
        # the left subtree is balanced AND
        # the righ tsubstree is balanced AND
        # abs(height_right - height_left) <= 1

        def checkHeightBalanced(node):
            if not node: 
                return 0
            
            if not node.left and not node.right:
                return 1
            
            # check the heights of left and right subtrees and see if they are balanced
            left_height = checkHeightBalanced(node.left)
            if left_height == -1:
                return -1
            
            right_height = checkHeightBalanced(node.right)
            if right_height == -1:
                return -1
            
            if abs(left_height - right_height) > 1:
                return -1
            
            return max(left_height, right_height) + 1
        
        balanced_height = checkHeightBalanced(root)
        if balanced_height == -1:
            return False
        else:
            return True