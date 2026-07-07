# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        rightside = []
        if not root:
            return []
        
        q = [root]
        while len(q) > 0:
            num_in_level = len(q)
            rightmost_node = q[-1]
            rightside.append(rightmost_node.val)

            for _ in range(num_in_level):
                node = q.pop(0)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        
        return rightside