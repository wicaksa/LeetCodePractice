class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:

        # edge case if matrix is empty return an empty array
        if len(matrix) == 0:
            return []

        # initialize an empty array to store the results
        result = []

        # find the top most row
        minRow = 0

        # find the bottom most row
        maxRow = len(matrix) - 1

        # find the left most column
        minCol = 0

        # find the right most column
        maxCol = len(matrix[0]) - 1

        # while the number of elements needed > 0
        while minRow <= maxRow and minCol <= maxCol:

            # go right until we reach the edge
            for col in range(minCol, maxCol+1):

                # append element to the list
                result.append(matrix[minRow][col])

            # remove the top edge
            minRow += 1

            # go down until we reach the bottom edge
            for row in range(minRow, maxRow+1):

                # append element to the list
                result.append(matrix[row][maxCol])

            # remove the right edge
            maxCol -= 1

            # do a check to see if minRow <= maxRow before proceeding
            if (minRow <= maxRow):

                # go left until we reach the left edge
                for col in range(maxCol, minCol-1, -1):

                    # append element to the list
                    result.append(matrix[maxRow][col])

                # remove the bottom edge
                maxRow -= 1

            # do another check to see if minCol <= maxCol
            if (minCol <= maxCol):

                # go up until you reach min row
                for row in range(maxRow, minRow-1, -1):

                    # appened element to list
                    result.append(matrix[row][minCol])

                # remove left edge
                minCol += 1

        # return the result array
        return result
