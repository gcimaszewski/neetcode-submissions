# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    """
    You are given the head of a singly linked-list.

    The positions of a linked list of length = 7 for example, can intially be represented as:

    [0, 1, 2, 3, 4, 5, 6]

    Reorder the nodes of the linked list to be in the following order:

    [0, 6, 1, 5, 2, 4, 3]

    Notice that in the general case for a list of length = n the nodes are reordered to be in the following order:

    [0, n-1, 1, n-2, 2, n-3, ...]

    You may not modify the values in the list's nodes, but instead you must reorder the nodes themselves.
    """

    def reorderList(self, head: Optional[ListNode]) -> None:
        # base case: if next is None 
        # something like this
        # take node `head`
        # recurse until next is None (base case)
        # then assign head.next = return val of recursive helper
        # then continue to recurse with head.old_next

        # tiny mental model:
        # front = node
        # old_next = front.next
        # tail = removed last node
        # front.next = tail
        # tail.next = old_next
        # continue from old_next

        if not head:
            return
        
        # iterative approach:
        # get the length of the LL
        # only idx >= len(LL)//2 we need to care about
        # len(5): idx 3, 4
        # len(6): idx 3, 4, 5
        # then we advance a pointer this far, and interleave
        len_ = 0
        curr = head
        while curr:
            len_ += 1
            curr = curr.next
        
        print(len_)
        if len_ <= 2:
            return

        # strategy:
        # find the second half of the list
        # reverse it in place
        # then splice it together
        prev = None
        ptr_back = head
        for i in range( (len_+1)//2):
            prev = ptr_back
            ptr_back = ptr_back.next
        prev.next = None
        # reverse the second half, in place
        left = None
        middle = ptr_back
        while middle is not None:
            tmp = middle.next
            middle.next = left
            left = middle
            middle = tmp
        # now left holds the new head to our list
        second_head = left
        ptr_forward = head
        while second_head:
            old_next = ptr_forward.next
            back_next = second_head.next
            ptr_forward.next = second_head
            second_head.next = old_next
            ptr_forward = old_next
            second_head = back_next
        return

        # # we need at least 3 nodes to have to do any rotation
        # def recHelper(node, curr):
        #     if not curr or not curr.next:
        #         # len of 1 or 2: no rotation needed
        #         return  
        #     # if a node is the tail: disconnect it and return
        #     # then it can be interleaved with the first node
        #     old_next = node.next
        #     if curr.next.next is None:
        #         tail = curr.next
        #         # untie the tail node from curr
        #         node.next = tail
        #         curr.next = None
                
        #         tail.next = old_next
        #         recHelper(old_next, old_next.next)
        #     else:
        #       #  return
        #         tmp = curr.next
        #         recHelper(node, tmp)
        #  #   recHelper(old_next, old_next.next)
        
        # return recHelper(head, head.next)