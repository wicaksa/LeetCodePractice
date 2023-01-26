# Given a fixed-length integer array arr, duplicate each occurrence of zero, shifting the remaining elements to the right.
# Note that elements beyond the length of the original array are not written. Do the above modifications to the input array in place and do not return anything.

class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        # input : integer array
        # output: integer array
        # arr = [1,0,2,3,0,4,5,0]
        #          1           6
        # ceate a pointer
        p = 0

        # iterate the list while pointer < length of array
        while p < len(arr)-1:

            # if you see a zero
            if arr[p] == 0:

                # shift elements to right of the current index by 1
                r = len(arr) - 1

                while r > p:

                    arr[r] = arr[r-1]

                    r -= 1

                # replace element at current index + 1 with a 0

                # increment pointer by 1
                p += 1

            # increment pointer by 1
            p += 1
