class TrieNode:
    def __init__(self):
        self.children={}
        self.is_end_of_word = False
    
class Trie:

    def __init__(self, words):
        self.root = TrieNode()
        for word in words:
            self.addWord(word)

    def addWord(self, word: str) -> None:
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
        node.is_end_of_word = True

    def isPrefix(self, prfx: str) -> bool:
        node = self.root
        for c in prfx:
            if c not in node.children:
                return False
            node = node.children[c]
        return True

    def search(self, letters: List[str]) -> bool:
        # returns two booleans: one if `word` has further descendants as a prefix, one if `word` is a first-class word
        node = self.root
        for c in letters:
            if c not in node.children:
                return (False, False)
            node = node.children[c]
        return (len(node.children) > 0, node.is_end_of_word)


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:

        trie = Trie(words)
        m = len(board)
        n = len(board[0])

        # marks all cells already allocated to a word
       # used = set()
        # marks cells in the current word being tested (prevents same cell from being added multiple times)
        path = set()
        words_present = []
        idxs = []

        def backtrack(r, c, letters):
            # start a search for any of the words in the trie from this coord.
            path.add((r, c))
            letters.append(board[r][c])
            is_prefix, is_word = trie.search(letters)
            
            if is_word:
                words_present.append("".join(letters))
        
            if is_prefix:
                directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
                for (dr, dc) in directions:
                    nr, nc = (r+dr), (c+dc)
                    if (0 <= nr < m and 
                        0 <= nc < n and 
                        (nr, nc) not in path 
                        ):
                        backtrack(nr, nc, letters)
            
            path.remove((r, c))
            letters.pop()

        for r in range(m):
            for c in range(n):
                backtrack(r, c, [])
        
        return list(set(words_present))
        