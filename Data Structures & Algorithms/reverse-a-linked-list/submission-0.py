# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # reverse the linked list in place
        # the place 
        left = None
        middle = head
        while middle is not None:
            tmp = middle.next
            middle.next = left
            left = middle
            middle = tmp
        return left

        