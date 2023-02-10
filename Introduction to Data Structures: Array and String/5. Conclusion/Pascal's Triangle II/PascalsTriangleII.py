class Solution:
    def getRow(self, rowIndex: int) -> List[int]:

        result = []

        for i in range(0, rowIndex + 1):

            tempResult = []

            for j in range(0, i+1):

                if j == 0 or j == i:

                    tempResult.append(1)

                else:

                    tempResult.append(result[i-1][j] + result[i-1][j-1])

            result.append(tempResult)

        return result[-1]
