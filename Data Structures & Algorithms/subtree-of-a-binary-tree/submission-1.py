# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        

        def checkIfTreesEqual(n1, n2) -> bool:
            # can't fit a non-empty tree into an empty tree
            if (not n1 and n2) or (n1 and not n2):
                return False
            
            # base case: no more nodes to check for subtree 
            if (not n1 and not n2):
                return True
            
            return (n1.val==n2.val) and checkIfTreesEqual(n1.left, n2.left) and checkIfTreesEqual(n1.right, n2.right)

        def checkIfSubtree(parent: Optional[TreeNode], subtree: Optional[TreeNode]) -> bool:

            if parent is None:
                return False

            # if root of the subtree is not equal to the parent node,
            # keep moving down the parent tree to search the left, right subtrees
            # if parent.val != subtree.val:
            #     return checkIfSubtree(parent.left, subtree) or checkIfSubtree(parent.right, subtree)
            
            if checkIfTreesEqual(parent, subtree):
                return True
            return (checkIfSubtree(parent.left, subtree) or 
                    checkIfSubtree(parent.right, subtree))

            # the parent node is equal
          #  return checkIfTreesEqual(parent.left, subtree.left) and checkIfTreesEqual(parent.right, subtree.right)


        return checkIfSubtree(root, subRoot)