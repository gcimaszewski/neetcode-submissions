"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # challenge: we need to determine what node the "random" node is
        # where does it link into the chain in the `next` position
        # create a map of index -> node? 

        dummy = Node(x=-1)
        ptr_cp = dummy
        ptr = head
        old_ptr_to_new_node = {}
        # the `next` node determines the node's identity (can't have two nodes with the same `next`)
        while ptr:
            new_node = Node(ptr.val)
            old_ptr_to_new_node[id(ptr)] = new_node
            ptr_cp.next = new_node
            ptr_cp = ptr_cp.next
            ptr = ptr.next

        ptr_random = head
        ptr2 = dummy.next
        while ptr_random:
            if ptr_random.random:
                ptr2.random = old_ptr_to_new_node.get(id(ptr_random.random))
            ptr_random= ptr_random.next
            ptr2 = ptr2.next
        return dummy.next
