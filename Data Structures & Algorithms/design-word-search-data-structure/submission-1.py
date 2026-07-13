class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
        

    def addWord(self, word: str) -> None:
        node = self.root
        for c in word:
            if c in node.children:
                node = node.children[c]
            else:
                node.children[c] = TrieNode()
                node = node.children[c]
        node.is_end_of_word = True
        

    def search(self, word: str) -> bool:
        
        def backtrack(curr, i):
            if i == len(word):
                return curr.is_end_of_word
            char_here = word[i]
            if char_here == '.':
                for l in curr.children:
                    if backtrack(curr.children[l], i+1):
                        return True
                return False
            else:
                if not char_here in curr.children:
                    return False
                return backtrack(curr.children[char_here], i+1)
        
        return backtrack(self.root, 0)
