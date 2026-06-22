class LinkedList:
    
    class LinkedListNode:
        def __init__(self, val):
            self.value = val
            self.next_node = None

    def __init__(self):
        self.head = None
    
    def get(self, index: int) -> int:
        i = 0
        # inv: node holds the node at index i
        node = self.head
        while i < index and not node is None:
            node = node.next_node
            i += 1
        if node is None:
            return -1
        return node.value

    def insertHead(self, val: int) -> None:
        new_head = self.LinkedListNode(val)
        if not self.head:
            self.head = new_head
        else:
            new_head.next_node = self.head
            self.head = new_head
        print(self.getValues())

    def insertTail(self, val: int) -> None:
        if not self.head:
            self.head = self.LinkedListNode(val)
            return
        node = self.head
        while not node.next_node is None:
            node = node.next_node
        node.next_node = self.LinkedListNode(val)
        print(self.getValues())


    def remove(self, index: int) -> bool:
        if not self.head:
            return False
        i = 0
        prev = None
        node = self.head
        while i < index and not node is None:
            i += 1
            prev = node
            node = node.next_node
        if node is None or i < index:
            return False
        if prev is None:
            self.head = node.next_node
        else:
        # patch together:
        # for the node just prior to the node to be removed,
        # set its next to that node's `next_node`
            prev.next_node = node.next_node
        return True

    def getValues(self) -> List[int]:
        vals = []
        node = self.head
        while node:
            vals.append(node.value)
            node = node.next_node
        return vals
        
