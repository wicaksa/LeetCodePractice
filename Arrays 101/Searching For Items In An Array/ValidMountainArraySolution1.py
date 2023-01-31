# Given an array of integers arr, return true if and only if it is a valid mountain array.

# Recall that arr is a mountain array if and only if:

#     arr.length >= 3
#     There exists some i with 0 < i < arr.length - 1 such that:
#         arr[0] < arr[1] < ... < arr[i - 1] < arr[i]
#         arr[i] > arr[i + 1] > ... > arr[arr.length - 1]

class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        # input : integer array
        # output: boolean value

        # find the index of the max value
        maxValIdx = arr.index(max(arr))

        # edge case : if length of array < 3, return false
        if len(arr) < 3 or maxValIdx == 0 or maxValIdx == len(arr)-1:
            return False

        # create pointers to the left and right of previous index
        l = maxValIdx - 1
        r = maxValIdx + 1

        # while the left pointer >= 0
        while l >= 0:

            # if current value is < previous value,
            if arr[l] < arr[l+1]:

                # decrement left pointer
                l -= 1

            # else
            else:

                # return false
                return False

        # while the right pointer <= len(arr)-1
        while r <= len(arr)-1:

            # if current value is < previous value
            if arr[r] < arr[r-1]:

                # increment right pointer
                r += 1

            # else
            else:

                # return false
                return False

        return True
