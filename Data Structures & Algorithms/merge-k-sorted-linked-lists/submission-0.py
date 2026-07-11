# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
          # approach: keep a pointer into each list
          # pick the index of the minimum node of the k
          # append to list, advance that node

        if lists == []:
            return None

        dummy = ListNode(-1)
        curr = dummy
        finished_lists = 0
        pointers = lists[:]
        while len(pointers) > 0:
            min_node_idx = -1
            min_val = 1001
            null_idxs = []
            for k in range(len(pointers)):
                node = pointers[k]
                if not node:
                    null_idxs.append(k)
                    continue
                if node.val <= min_val:
                    min_node_idx = k
                    min_val = node.val
            if min_node_idx >= 0:
                new_node = ListNode(min_val)
                curr.next = new_node
                curr = curr.next
                # advance the node that was added to the list
                pointers[min_node_idx] = pointers[min_node_idx].next
                for i in reversed(null_idxs):
                    del pointers[i]
            else:
                break
        return dummy.next
                