class TrieNode:

    def __init__(self, val=""):
        self.val = val
        self.out_edges = {}
        self.children = []

class PrefixTree:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for idx, char in enumerate(word):
            if char in node.out_edges:
                e_idx = node.out_edges[char]
                node = node.children[e_idx]
            else:
                nn = TrieNode(val=word[:idx+1])
                node.out_edges[char] = len(node.children)
                node.children.append(nn)
                node = nn
        node.out_edges["$"] = len(node.children)
        node.children.append(TrieNode(val=word+"$"))



    def search(self, word: str) -> bool:
        node = self.root
        while len(node.children) > 0:
            for char in word + "$":
                if char not in node.out_edges:
                    return False
                node = node.children[node.out_edges[char]]
        return node.val==word+"$"

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for c in prefix:
            if c not in node.out_edges:
                return False
            node = node.children[node.out_edges[c]]
        return True
        
        