class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        # crete hash set for row, col, and grid
        rows = collections.defaultdict(set)
        cols = collections.defaultdict(set)
        grid = collections.defaultdict(set)

        TOTAL_ROWS = 9
        TOTAL_COLS = 9

        for r in range(0, TOTAL_ROWS):

            for c in range(0, TOTAL_COLS):

                if board[r][c] == ".":

                    continue

                elif (board[r][c] in rows[r] or
                      board[r][c] in cols[c] or
                      board[r][c] in grid[(r//3, c//3)]):

                    return False

                else:

                    rows[r].add(board[r][c])
                    cols[c].add(board[r][c])
                    grid[(r//3, c//3)].add(board[r][c])

        return True
