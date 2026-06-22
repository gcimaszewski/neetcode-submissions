class LinkedList:
    
    def __init__(self):
        self.head = None
    
    def get(self, index: int) -> int:
        count = 0
        ptr = self.head
        while ptr and (count < index):
            count += 1
            ptr = ptr.next_
        if not ptr:
            return -1
        else:
            return ptr.val

    def insertHead(self, val: int) -> None:
        if not self.head:
            self.head = Node(val)
        else:
            old_head = self.head
            self.head = Node(val)
            self.head.next_ = old_head

    def insertTail(self, val: int) -> None:
        # make new node; find last node of current list;
        # make last.next = new_node
        if not self.head:
            self.head = Node(val)
        else:
            ptr = self.head
            while ptr.next_:
                ptr = ptr.next_
            ptr.next_ = Node(val)

    def remove(self, index: int) -> bool:
        # to remove i^th node: need (i-1)th, (i+1)th nodes
        # make node_i-1.next = node_i+1
        if index == 0:
            if self.head:
                self.head = self.head.next_
                return True
            else:
                return False
        else:
            prev = self.head
            count = 0
            while (count + 1) < index and prev:
                prev = prev.next_
                count += 1
            
            if not prev or not prev.next_:
                # ith node doesn't exist, return false
                return False
            
            prev.next_ = prev.next_.next_
            return True


    def getValues(self) -> List[int]:
        vals = []
        ptr = self.head
        while ptr:
            vals.append(ptr.val)
            ptr = ptr.next_
        return vals
        
class Node:

    def __init__(self, val=0, next_=None):
        self.val = val
        self.next_ = next_