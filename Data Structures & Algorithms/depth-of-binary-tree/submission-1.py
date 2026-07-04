# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
    
        # recursive impl
        # def heightHelper(node):
        #     if not node:
        #         return 0
        #     if not node.right and not node.left:  # leaf node
        #         return 1
        #     else:
        #         left_height = heightHelper(node.left)
        #         right_height = heightHelper(node.right)
        #         return 1 + max(left_height, right_height)

        # return heightHelper(root)

        if not root:
            return 0
        queue = [root]
        height = 0
        while len(queue) > 0:
            # at each outer iteration, the queue only holds nodes at a single level
            level_len = len(queue)
            for _ in range(level_len):
                node = queue.pop(0)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            height += 1
        return height

