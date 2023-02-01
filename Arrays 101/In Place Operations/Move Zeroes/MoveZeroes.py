"""
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.

In this instance, I used a two pointer approach. I created a zero and non zero pointer.
The non zero pointer will scan ahead until it reaches a non zero value.
Then, it will swap values with the zero pointer. 
This loop will go on until the non zero pointer is less than the length of the array.
"""


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        Input: nums = [0,1,0,3,12]
        Output: [1,3,12,0,0]

        """

        # two pointer approach

        # edge case: when length of nums is 0 or 1
        l = len(nums)

        # create a zero and non zero pointer
        z = 0
        nz = 0

        # while non zero pointer is less than length of array
        while nz < l:
            # print
            print("nums: ", nums)

            # if the non zero pointer == 0
            if nums[nz] == 0:

                # increment the non zero pointer
                nz += 1

            # else
            else:

                temp = nums[z]

                # element at 0 pointer = element at non zero pointer
                nums[z] = nums[nz]

                # element at non zero pointer temp
                nums[nz] = temp

                # increment non zero pointer
                nz += 1

                # increment zero pointer
                z += 1
