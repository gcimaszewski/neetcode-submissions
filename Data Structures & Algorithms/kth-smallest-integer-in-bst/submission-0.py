# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    """
    Kth Smallest Integer in BST

    Given the root of a binary search tree, and an integer k, return the kth smallest value (1-indexed) in the tree.

    """
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # approach:
        # do a slightly modified DFS in-order traversal
        # keep track of a counter for every visited node
        # the first node is the 1st smallest
        # break when counter = k

        stack = []
        node = root
        ith_smallest_count = 0
        while node is not None or len(stack) > 0:
            while node is not None:
                stack.append(node)
                node = node.left
            
            # now, node is None
            node = stack.pop()
            ith_smallest_count += 1
            if ith_smallest_count == k:
                break
            node = node.right
        
        return node.val


