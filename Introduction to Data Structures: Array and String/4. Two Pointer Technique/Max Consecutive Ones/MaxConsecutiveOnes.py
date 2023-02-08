class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        # input : integer array
        # output: integer representing the maximum number of consecutive 1's

        # create a variable to store the max result
        maxResult = 0

        # create a variable to store current result
        currentResult = 0

        # iterate through the array
        for i in range(0, len(nums)):

            # if the number is a 1
            if nums[i] == 1:

                # add 1 to the current result variable
                currentResult += 1

            # if the number is 0
            else:

                # check if the current result is greater than the max result

                # if the current result > max result
                # set current result to max result
                maxResult = max(currentResult, maxResult)

                # reset the current result variable to 0
                currentResult = 0

        # if we finish iterating we wont be able to compare max and current result
        # so we do it here
        return max(currentResult, maxResult)
