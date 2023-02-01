"""
Given an integer array nums, move all the even integers at the beginning of the array followed by all the odd integers.

Return any array that satisfies this condition.

Solved using a two pointer approach similar to Move Zeroes.
"""


class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        # UMPIRE
        # input : int array
        # output: int array

        # edge case : nums length 1 or 0
        l = len(nums)  # length of nums

        if l == 1 or l == 0:
            return nums

        # create two pointers
        even = 0
        odd = 0

        # while even pointer < len nums
        while even < l:

            # if even pointer is at odd element
            if nums[even] % 2 != 0 and nums[even] != 0:

                # increment pointer
                even += 1

            # else
            else:

                # swap
                temp = nums[odd]
                nums[odd] = nums[even]
                nums[even] = temp

                # increment pointers
                even += 1
                odd += 1

        return nums
