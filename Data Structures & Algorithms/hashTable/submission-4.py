class LinkedListNode:

    def __init__(self, key,  val, next_=None):
        self.next_node = next_
        self.key = key
        self.val = val


class HashTable:
    
    def __init__(self, capacity: int):
        self.bins = [None] * capacity
        self.capacity = capacity
        self.size = 0


    def _hash(self, key, m):
        return key % m

    def getLoadFactor(self):
        return self.size/self.capacity

    def _insertNoResize(self, key, value, table, m):
        hashed_key = self._hash(key, m)
        ll = table[hashed_key]
        if ll is None:
            table[hashed_key] = LinkedListNode(key=key, val=value)
            return 1
        # find the last node in the list
        while ll is not None:
            if ll.key == key:
                ll.val = value
                return 0
            if ll.next_node is None:
                break
            ll = ll.next_node
        ll.next_node = LinkedListNode(key=key, val=value)
        return 1

    def insert(self, key: int, value: int) -> None:
        added_count = self._insertNoResize(key, value, self.bins, self.capacity)
        self.size += added_count
        if self.getLoadFactor() >= 0.5:
            self.resize()

    def get(self, key: int) -> int:
        h = self._hash(key, self.capacity)
        ll = self.bins[h]
        while ll is not None:
            if ll.key == key:
                return ll.val
            ll = ll.next_node
        return -1

    def remove(self, key: int) -> bool:
        h = self._hash(key, self.capacity)
        ll = self.bins[h]
        prev = None
        while ll is not None:
            if ll.key == key:
                # found the key we want
                # take the node just before, and set its next_node to this_node.next_node
                if prev is None:
                    # case where this is the first node in the list
                    self.bins[h] = ll.next_node
                else:
                    prev.next_node = ll.next_node
                self.size -= 1
                return True
            prev = ll
            ll = ll.next_node
        return False

    def getSize(self) -> int:
        return self.size

    def getCapacity(self) -> int:
        return self.capacity

    def resize(self) -> None:
        # don't need to change total hashtable size for resizing (no elems added or removed)
        new_capacity = self.capacity * 2
        new_bins = [None] * new_capacity
        for ll in self.bins:
            while ll is not None:  # no need to remap empty bins
                next_old = ll.next_node
                # quick insert at the front 
                # we know there's no duplicates, so no need to scan whole list
                h = self._hash(ll.key, new_capacity)
                ll.next_node = new_bins[h]
                new_bins[h] = ll
                ll = next_old
        self.bins = new_bins
        self.capacity = new_capacity

