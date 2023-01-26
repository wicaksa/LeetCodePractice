# Given an array nums of integers, return how many of them contain an even number of digits.

class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        # input : integer array of length 1 to 500
        # output: integer representing how many elements contain an even number of digits

        # create a result variable
        result = 0

        # iterate through the elements
        for num in nums:

            # convert element to a string
            s = str(num)

            # if the length is even, add one to result
            if len(s) % 2 == 0:

                result += 1

        # return result variable
        return result
