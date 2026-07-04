class DoubleLinkedNode:

    def __init__(self, key: int, val: int):
        self.prev = None
        self.next = None
        self.key = key
        self.val = val

class LRUCache:

    # approach:
    # store cache entries as nodes in double linked list
    # when `get` is called on a node that exists or `put`: 
    # node gets added to the end of the list
    # to delete lru node when list beyond capacity: delete the head of the list
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.key_to_node = {}
        self.head = None
        self.tail = None

    def _disconnect_node_from_list(self, node: DoubleLinkedNode):
        if not node.prev and not node.next:
            self.head = None
            self.tail = None
        elif not node.prev:
            self.head = node.next
            node.next.prev = None
        elif not node.next:
            self.tail = node.prev
            node.prev.next = None
        else:
            node.prev.next = node.next
            node.next.prev = node.prev
        node.next = None
        node.prev = None
        del self.key_to_node[node.key]


    def _add_node_to_tail(self, node: DoubleLinkedNode):
        if not self.head:
            self.head = node
        else:
            node.prev = self.tail
            self.tail.next = node
            node.next = None
        self.tail = node
        self.key_to_node[node.key] = node
        

    def get(self, key: int) -> int:
        node = self.key_to_node.get(key)
        if not node:
            return -1

        self._disconnect_node_from_list(node)
        self._add_node_to_tail(node)
        return node.val


    def put(self, key: int, value: int) -> None:
        node = self.key_to_node.get(key)
        # two cases:
        # the node doesn't exist -> we make a new node and add it to the tail
        # the node does exist -> we disconnect it from the existing list and add it to the tail
        if not node:
            node = DoubleLinkedNode(key, value)
            self._add_node_to_tail(node)

        else:
            node.val = value
            self._disconnect_node_from_list(node)
            self._add_node_to_tail(node)
        
        if len(self.key_to_node) > self.capacity:
            # delete the head
            self._disconnect_node_from_list(self.head)
