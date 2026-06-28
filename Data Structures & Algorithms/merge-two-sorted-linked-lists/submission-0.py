# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # steps:
        # decide on the head (pick the min. node)
        # then: keep pointers for each list. interleave nodes for the next lowest value
        if not list1:
            return list2
        elif not list2:
            return list1
        
        head = prev = None
        prev = ListNode() # dummy to store next
        while list1 and list2:
            if list1.val <= list2.val:
                prev.next = list1
                list1 = list1.next
            else:
                prev.next = list2
                list2 = list2.next
            prev = prev.next
            if not head:
                head = prev
            
        # at the end: if one of them is non-None but the other is,
        # just insert that pointer node and we're done
        if list1:
            prev.next = list1
        elif list2:
            prev.next = list2
        return head

            

