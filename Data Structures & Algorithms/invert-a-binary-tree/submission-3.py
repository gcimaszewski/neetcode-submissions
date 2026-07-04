# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        stack = [root]

        while len(stack) > 0:
            node = stack.pop()
            if node is None:
                continue
            tmp = node.right
            node.right = node.left
            node.left = tmp
            stack.append(node.right)
            stack.append(node.left)
        
        return root
        
        # recursive approach
        # def invertTreeRecHelper(node):
        #     if not node:
        #         return node
        #     if not node.left and not node.right:
        #         return node
        #     else:
        #         right = invertTreeRecHelper(node.right)
        #         left = invertTreeRecHelper(node.left)
        #         node.left = right
        #         node.right = left
        #         return node
        # return invertTreeRecHelper(root)