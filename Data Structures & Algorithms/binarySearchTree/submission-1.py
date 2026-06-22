class TreeNode: 
    
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.left = None
        self.right = None

    def __eq__(self, other):
        if not isinstance(other, TreeNode):
            return NotImplemented
        return self.key == other.key

    def __gt__(self, other):
        if not isinstance(other, TreeNode):
            return NotImplemented
        return self.key > other.key

    def __lt__(self, other):
        if not isinstance(other, TreeNode):
            return NotImplemented
        return self.key < other.key


    def __repr__(self):
        return f"{self.__class__.__name__}(key={self.key}:val={self.val})"

    def isLeaf(self):
        return self.left is None and self.right is None


class TreeMap:
    
    def __init__(self):
        self.root = None

    def insert(self, key: int, val: int) -> None:
        if self.root is None:
            self.root = TreeNode(key, val)
            return
        
        prev = None
        node = self.root
        while node is not None:
            if node.key == key:
                node.val = val
                return
            elif key > node.key:
                prev = node
                node = node.right
            else:
                prev = node
                node = node.left
        new_node = TreeNode(key, val)
        if new_node > prev:
            prev.right = new_node
        else:
            prev.left = new_node


    def get(self, key: int) -> int:
        if self.root is None:
            return -1
        
        current = self.root
        while current is not None:
            if key > current.key:
                current = current.right
            elif key < current.key:
                current = current.left
            else:
                return current.val
        return -1

    def getMinimumNodeAt(self, node):
        if node is None:
            return None
        while node.left is not None:
            node = node.left
        return node

    def getMin(self) -> int:
        min_node = self.getMinimumNodeAt(self.root)
        if min_node is None:
            return -1
        
        return min_node.val        

    def getMaximumNodeAt(self, node):
        if node is None:
            return None
        while node.right is not None:
            node = node.right
        return node

    def getMax(self) -> int:
        max_node = self.getMaximumNodeAt(self.root)
        if max_node is None:
            return -1
        return max_node.val

    def removeFromSubtree(self, root, key):
        """Deletes node with a given key in the tree starting from `root`.
        Returns the root of the updated tree with node `key` removed.
        """
        
        if root is None:
            return
        
        # search for the node to delete 
        if key < root.key:
            root.left = self.removeFromSubtree(root.left, key)
        elif key > root.key:
            root.right = self.removeFromSubtree(root.right, key)
        
        else:
            # case where this node is the one we want to delete (root = key)
            # we delete root, then continue to swap up
            # case where only one child exists
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            else:
                pred_node = self.getPredecessorNode(root)
                root.val = pred_node.val
                root.key = pred_node.key
                # because we moved up a key that was less than the deleted key, we only work on the left subtree
                root.left = self.removeFromSubtree(root.left, pred_node.key)

        return root

    def remove(self, key: int) -> None:
        self.root = self.removeFromSubtree(self.root, key)


    def getParentStack(self, target_node):
        stack = [None]
        current = self.root
        while current is not None and current != target_node:
            stack.append(current)
            if target_node > current:
                current = current.right
            else:
                current = current.left
        return stack

    def getPredecessorNode(self, node):
        if node.left is not None:
            return self.getMaximumNodeAt(node.left)
        # case where there is no left subtree to this node
        # in that case, we need to go up the tree, and find the 
        # y = node.parent
        # while y is not None and node == y.right:
        # node = y; y = y.parent;
        # return node
        parents = self.getParentStack(node)
        parent = parents.pop()
        while parent is not None and node == parent.left:
            node = parent
            parent = parents.pop() if parents else None
        return parent

    def getInorderKeys(self) -> List[int]:
        stack = []
        current = self.root

        keys = []
        while current is not None or len(stack) > 0:
            while current is not None:
                stack.append(current)
                current = current.left
            
            current = stack.pop()
            keys.append(current.key)
            
            current = current.right
        
        return keys