# Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        # input : integer array sorted increasing order

        # output: integer array sorted increasing order with elements of input squared

        # approach 1

        # square each element in the array

        # implement a sorting algorithm to sort the array

        # approach 2

        # [1, 2, 3, 4, 5] min value > 0

        # [0, 2, 3, 4, 5] min value == 0

        # [-1, 0, 1, 2, 3, 4] min value < 0
        #   ^              ^

        # if min value is >= 0
        if min(nums) >= 0:

            # iterate through the array
            for i in range(0, len(nums)):

                # square the element
                nums[i] = nums[i]**2

            # return nums
            return nums

        # else
        else:

            # create an empty array
            resultArray = []

            # create pointers at the left and right end points
            l = 0
            r = len(nums) - 1

            # while left pointer < right pointer and right pointer > left pointer :
            while l <= r and r >= l:

                # if abs val of right pointer element > abs val left pointer element  or if abs val right pointer element == abs val left pointer element
                if abs(nums[r]) > abs(nums[l]) or abs(nums[r]) == abs(nums[l]):

                    # square right pointer value
                    tempVal = nums[r]**2

                    # insert value into empty array
                    resultArray.insert(0, tempVal)

                    # decrement right pointer
                    r -= 1

                # if abs val of left pointer element > abs val right pointer element  or if abs val right pointer element == abs val left pointer element
                elif abs(nums[l]) > abs(nums[r]) or abs(nums[l]) == abs(nums[r]):

                    # square left value
                    tempVal = nums[l]**2

                    # insert into empty array
                    resultArray.insert(0, tempVal)

                    # increment left pointer
                    l += 1

            # return the new array
            return resultArray
