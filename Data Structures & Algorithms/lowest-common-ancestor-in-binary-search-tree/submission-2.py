# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    """
    Lowest Common Ancestor in Binary Search Tree

    Given a binary search tree (BST) where all node values are unique, and two nodes from the tree p and q,
    return the lowest common ancestor (LCA) of the two nodes.

    The lowest common ancestor between two nodes p and q is the lowest node in a tree T such that both p and q as descendants.
    The ancestor is allowed to be a descendant of itself.

    """
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
         # path consists of upward part -> downward part
         # upward: when node.val < target and node = parent.left OR => up right
         #              node.val > target and node = parent.right  => up left
         # downward: node.val < target and node = parent.right => down right
         #           node.val > target and node = parent.left => down left


        # the LCA is the smallest node where p and q are no longer on the same side
        # two nodes are on the same side wrt. root if both are either g.t. or l.t. root.val

        if p.val == root.val or q.val == root.val:
            return root
        
        if min(p.val, q.val) < root.val and max(p.val, q.val) > root.val:
            return root

        curr = root
        while curr.val != p.val and curr.val != q.val:
            if p.val < curr.val and q.val < curr.val:
                curr = curr.left
            elif p.val > curr.val and q.val > curr.val:
                curr = curr.right
            else:
                break
        
        return curr

        # trace path from p to q
        # if we hit root: that is the LCA
        # wlg: pick the node with smaller value
        smaller = p if p.val < q.val else q
        
        # # get upward path from root -> node
        # path_from_root = [root]
        # def get_path_from_root_to_node(target):
        #     curr = root
        #     path = [root]
        #     while curr.val != target.val:
        #         if curr.val > target.val:
        #             curr = curr.left
        #         else:
        #             curr = curr.right
        #         path.append(curr)
        #     return path
         
        # path_up = get_path_from_root_to_node(smaller)
        # node = path_up.pop()
        # parent = path_up.pop()
        # while parent is not None and node.val < parent.val and parent.val < larger:
        #     node = parent
        #     parent = path_up.pop() if path_up else None
        # return node
