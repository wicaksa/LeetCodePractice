# Given an array arr, replace every element in that array with the greatest element among the elements to its right, and replace the last element with -1.

# After doing so, return the array.

class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        # input : int array
        # output: int array(in-place)

        # edge case: when length of arr == 0
        if len(arr) == 0:

            return arr

        # edge case: when length of arr == 1
        if len(arr) == 1:

            return [-1]

        # create var for max value: set it to last element
        maxVal = arr[-1]

        # set last element to -1
        arr[-1] = -1

        # iterate from the second to last element
        for i in range(len(arr) - 2, -1, -1):

            # create a temp variable to store current element
            temp = arr[i]

            # replace current element with the max value
            arr[i] = maxVal

            # if the temp variable > max value
            if temp > maxVal:

                # replace the max value with temp variable
                maxVal = temp

        # return arr
        return arr
