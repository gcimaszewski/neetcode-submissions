# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # approach: reverse both of the LLs and then add
        def _reverse_in_place(head):
            dummy = ListNode(val=-1, next=head)
            while dummy and dummy.next is not None:
                middle = dummy.next
                right = middle.next
                middle.next = dummy
                dummy = right
            return dummy

        carry = 0
        new_sum = head = ListNode(val=0)
        node1 = l1
        node2 = l2
        while node1 or node2:
            v1 = node1.val if node1 else 0
            v2 = node2.val if node2 else 0
            sum_ = v1+v2+carry 
            carry = sum_//10
            new_sum.next = ListNode(val=sum_%10)
            new_sum = new_sum.next
            node1 = node1.next if node1 else None
            node2 = node2.next if node2 else None
        if carry > 0:
            new_sum.next = ListNode(val=carry)
        return head.next