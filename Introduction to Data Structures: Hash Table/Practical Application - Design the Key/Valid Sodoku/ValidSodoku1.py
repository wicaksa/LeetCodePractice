# Naive Solution

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        hashSet = set()
        # check row

        # iterate one row at a time
        for row in range(0, len(board)):

            # clear hashSet
            hashSet.clear()

            # go through each element in each row
            for col in range(0, len(board[0])):

                # if the element is in the hash set return false
                if board[row][col] in hashSet:

                    return False

                # else if it's not and it's not a ".", add it to the hash set
                elif board[row][col] != ".":

                    hashSet.add(board[row][col])

        # check col
        for col in range(0, len(board)):

            # clear hashSet
            hashSet.clear()

            for row in range(0, len(board[0])):

                if board[row][col] in hashSet:

                    return False

                else:

                    if board[row][col] != ".":
                        hashSet.add(board[row][col])

        # check 3x3
        x = 0
        y = 3

        while x < 9:

            hashSet.clear()

            for row in range(x, x+3):

                for col in range(y-3, y):

                    if board[row][col] in hashSet:

                        return False

                    else:

                        if board[row][col] != ".":
                            hashSet.add(board[row][col])

            if y == 9:

                x = x + 3
                y = 3

            else:

                y = y + 3

        # return true if cases pass
        return True
