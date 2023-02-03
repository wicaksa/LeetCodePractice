class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:

        # edge case: if matrix = 0
        if len(mat[0]) == 0:
            return mat

        # keep track of result
        result = []

        # set coordinates and variables
        x = 0
        y = 0
        p = len(mat) * len(mat[0])  # how many times we need to iterate

        while p > 0:

            # append current value at mat[x][y]
            result.append(mat[x][y])

            # if x + y coord is even
            if (x + y) % 2 == 0:

                # if you can go up and right
                if x - 1 >= 0 and y + 1 < len(mat[0]):

                    # go up
                    x -= 1

                    # go right
                    y += 1

                # else if you can't go up but can go right
                elif x - 1 < 0 and y + 1 < len(mat[0]):

                    # go right
                    y += 1

                # if you can't do both
                else:  # mat[x][y+1] != null and mat[x-1][y] != null:

                    # go down (edge)
                    x += 1

            # else if x + y is odd
            elif (x + y) % 2 != 0:

                # if you can go down and if you can go left
                if x + 1 < len(mat) and y - 1 >= 0:

                    # go down
                    x += 1

                    # go left
                    y -= 1

                # if you can go down but can't go left
                elif x + 1 < len(mat) and y - 1 < 0:

                    # go down
                    x += 1

                # if you cant do both
                else:

                    # go right
                    y += 1

            # dec p
            p -= 1

        return result
