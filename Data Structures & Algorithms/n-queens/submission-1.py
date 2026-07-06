class Solution:
    """
    The n-queens puzzle is the problem of placing n queens on an n x n chessboard so that no two queens can attack each other.

    A queen in a chessboard can attack horizontally, vertically, and diagonally.

    Given an integer n, return all distinct solutions to the n-queens puzzle.

    Each solution contains a unique board layout where the queen pieces are placed.
    'Q' indicates a queen and '.' indicates an empty space.

    You may return the answer in any order.
    """
    def solveNQueens(self, n: int) -> List[List[str]]:
        # approach:
        # place a queen on the board (queens can be on any space?)
        # then mark the entire bounding box around that queen space as "cannot be used"
        # when backtracking: check that the index to be added is not in the bad space set
        # track the number of queens still needing to be placed
        # base case: all queens are placed

        valid_boards = []
        state = []
        marked = set()

        def get_queen_bounding_box(x, y):
            spaces = set()
            for i in range(n):
                spaces.add((i, y))
                spaces.add((x, i))
            # TODO: add the diagonal spaces too
            # for horizontal in range(-1, 2):
            #     for vertical in range(-1, 2):
            #         move_x = x+horizontal
            #         move_y = y+vertical
            #         if 0 <= move_x < n and 0<=move_y < n:
            #             spaces.add((move_x, move_y))
            return spaces

        # because we store only the coordinates of the queens,
        # we need to translate this into the board config
        def generate_board_layout(queen_coords):
            board = [["." for i in range(n)] for j in range(n)]
            for (x, y) in queen_coords:
                board[x][y] = "Q"
            return ["".join(row) for row in board]

        marked_cols = set()

        def backtrack(x, num_queens_to_place):
            print(f'backtrack: rownum={x},numqueens={num_queens_to_place}')
            if num_queens_to_place == 0:
                valid_boards.append(generate_board_layout(state))
                return
            if x >= n:
                return
            
            # insight: only one queen can be placed per row
            for y in range(n):
                if y in marked_cols:
                    continue
                # check if diagonal to any other placed queens
                # diagonal rule: (x2-x1)= (y2-y1)
                breaks_diagonal = False
                for (x_q, y_q) in state:
                    if abs(x - x_q) == abs(y - y_q):
                        breaks_diagonal = True
                        break
                if breaks_diagonal: continue
                
                marked_cols.add(y)
                state.append((x, y))
                backtrack(x + 1, num_queens_to_place - 1)
                state.pop()
                marked_cols.remove(y)

        backtrack(0, n)
        return valid_boards
