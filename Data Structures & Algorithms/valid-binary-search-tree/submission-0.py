# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def getMinimum(self, root):
        if not root:
            return float('inf')
        node = root
        while node.left is not None:
            node = node.left
        return node.val
    
    def getMaximum(self, root):
        if not root:
            return float('-inf')
        node = root
        while node.right is not None:
            node = node.right
        return node.val

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        # check proper ordering at this root
        if root.left and root.left.val >= root.val:
            return False
        
        if root.right and root.right.val <= root.val:
            return False
        
        max_ = self.getMaximum(root.left)
        min_ = self.getMinimum(root.right)
        print(f'max of left: {max_}. min of right: {min_}')
        if not self.getMaximum(root.left) < root.val:
            return False
        if not self.getMinimum(root.right) > root.val:
            return False
        
        return self.isValidBST(root.left) and self.isValidBST(root.right)
        