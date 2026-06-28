# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # fast, slow pointer technique
        slow = fast = head
        while slow is not None and fast is not None:
            slow = slow.next
            fast = fast.next
            if fast:
                fast = fast.next
            
            if slow == fast and slow is not None:
                return True
        return False
