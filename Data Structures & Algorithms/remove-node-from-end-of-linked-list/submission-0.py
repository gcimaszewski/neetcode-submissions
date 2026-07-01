# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        # fast-slow pointer method
        # advance the fast pointer n places,
        # then advance both until fast at None

        # [1, 2, 3]
        # fast= 3; slow=1
        # fast= None; slow=2

        # fast= None; slow=3


        fast, slow = head, head
        for i in range(n):
            fast = fast.next
        before_slow = None
        while fast is not None:
            before_slow = slow
            slow = slow.next
            fast = fast.next
        # now `slow` is pointing to nth from end node
        # to delete it: set its predecessor node to slow.next
        # case where the head node is the one deleted: 
        if not before_slow:
            return slow.next
        # normal case
        before_slow.next = slow.next
        return head

        
