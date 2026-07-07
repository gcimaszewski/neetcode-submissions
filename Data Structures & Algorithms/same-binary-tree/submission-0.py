# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        # intuition:
        # two trees rooted at `p` and `q` are the same if:
        # p.val == q.val AND
        # p.left is same as q.left AND p.right same as q.right

        def recHelper(n1, n2):
            if not n1 and not n2:
                return True
            
            if n1 and not n2:
                return False
            elif not n1 and n2:
                return False
            
            if n1.val != n2.val:
                return False
            
            return recHelper(n1.left, n2.left) and recHelper(n1.right, n2.right)
        
        return recHelper(p, q)