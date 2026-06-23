class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # approach:
        # create sets of numbers for each:
        # third of row, third of column
        # reassemble each to create squares, full rows, full cols

        row_sets = {i: set() for i in range(9)}
        col_sets = {i: set() for i in range(9)}
        block_sets = {i: set() for i in range(9)}
        for row_idx in range(len(board)):
            row = board[row_idx]
            row_set = set()
            for col_idx in range(len(row)):
                entry = row[col_idx]
                block_idx = (row_idx//3)*3 + (col_idx//3)
                if entry == ".":
                    continue
                if entry in col_sets[col_idx]:
                    return False
                if entry in row_sets[row_idx]:
                    return False
                if entry in block_sets[block_idx]:
                    return False
                col_sets[col_idx].add(entry)
                row_sets[row_idx].add(entry)
                block_sets[block_idx].add(entry)
        return True
