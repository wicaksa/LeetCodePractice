# Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same.
# Since it is impossible to change the length of the array in some languages, you must instead have the result be placed in the first part of the array nums.
# More formally, if there are k elements after removing the duplicates, then the first k elements of nums should hold the final result. It does not matter what you leave beyond the first k elements.
# Return k after placing the final result in the first k slots of nums.
# Do not allocate extra space for another array. You must do this by modifying the input array in-place with O(1) extra memory.

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # input : int array
        # output: int (length of int array)

        # edge case: if length == 0 or 1
        if len(nums) == 0 or len(nums) == 1:
            return len(nums)

        # create pointer
        p = len(nums) - 2

        # iterate from the second last value
        while p >= 0 and len(nums) > 1:

            # if the previous element is the same as the current
            if nums[p] == nums[p+1]:

                # pop
                nums.pop(p)

                # decrement
                p -= 1

            # decrement
            else:
                p -= 1

        # return length of nums
        return len(nums)
