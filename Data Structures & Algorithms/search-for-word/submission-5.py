class Solution:
    """
    Word Search

    Given a 2-D grid of characters board and a string word, return true if the word is present in the grid, otherwise return false.

    For the word to be present it must be possible to form it with a path in the board with horizontally or vertically neighboring cells. The same cell may not be used more than once in a word.
    """
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])
        substr = []
        visited = set()
        # approach:
        # construct all possible paths over the board in DFS
        # if the substring doesn't match `word`: exit the path
        # continue across the entire tree
        def backtrack(row_idx, col_idx):
            if len(substr) == len(word) and "".join(substr) == word:
                return True

            # if row_idx < 0 or row_idx >= m or col_idx < 0 or col_idx >= n:
            #     return False

            # if (row_idx, col_idx) in visited:
            #     return False

            # move downwards
            if 0 <= row_idx < m and 0 <= col_idx < n and (row_idx, col_idx) not in visited:
                letter = board[row_idx][col_idx]
                substr.append(letter)
                visited.add((row_idx, col_idx))
                word_so_far = "".join(substr)
                found = False
                if word_so_far == word[:len(word_so_far)]:
                    found = (backtrack(row_idx + 1, col_idx) or 
                    backtrack(row_idx - 1, col_idx) or 
                    backtrack(row_idx, col_idx + 1) or 
                    backtrack(row_idx, col_idx - 1))
                substr.pop()
                visited.remove((row_idx, col_idx))
                return found
        
        for i in range(m):
            for j in range(n):
                if backtrack(i, j):
                    return True
        return False