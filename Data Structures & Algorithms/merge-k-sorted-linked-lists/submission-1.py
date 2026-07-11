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

        def mergeTwoLists(l1, l2=None):
            dummy = ListNode()
            tail = dummy
            while l1 and l2:
                if l1.val <= l2.val:
                    tail.next = l1
                    l1 = l1.next
                else:
                    tail.next = l2
                    l2 = l2.next
                tail = tail.next
            tail.next = l1 if not l2 else l2
            return dummy.next
        
        def recursiveTwoSplitter(list_of_lists, i, j):
            if i == j:
                return list_of_lists[i]
            mid = i + (j - i)//2
            left_half = recursiveTwoSplitter(list_of_lists, i, mid)
            right_half = recursiveTwoSplitter(list_of_lists, mid + 1, j)
            return mergeTwoLists(left_half, right_half)
        
        return recursiveTwoSplitter(lists, 0, len(lists) - 1)

    #     dummy = ListNode(-1)
    #     curr = dummy
    #     finished_lists = 0
    #  #   pointers = lists[:]
    #     while len(lists) > 0:
    #         min_node_idx = -1
    #         min_val = 1001
    #         null_idxs = []
    #         for k in range(len(lists)):
    #             node = lists[k]
    #             if not node:
    #                 null_idxs.append(k)
    #                 continue
    #             if node.val <= min_val:
    #                 min_node_idx = k
    #                 min_val = node.val
    #         if min_node_idx >= 0:
    #             new_node = ListNode(min_val)
    #             curr.next = new_node
    #             curr = curr.next
    #             # advance the node that was added to the list
    #             lists[min_node_idx] = lists[min_node_idx].next
    #             for i in reversed(null_idxs):
    #                 del lists[i]
    #         else:
    #             break
    #     return dummy.next
                