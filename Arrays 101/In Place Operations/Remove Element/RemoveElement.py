"""

Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. The relative order of the elements may be changed.

Since it is impossible to change the length of the array in some languages, you must instead have the result be placed in the first part of the array nums. More formally, if there are k elements after removing the duplicates, then the first k elements of nums should hold the final result. It does not matter what you leave beyond the first k elements.

Return k after placing the final result in the first k slots of nums.

Do not allocate extra space for another array. You must do this by modifying the input array in-place with O(1) extra memory.

Approach: I used a two pointer approach for this problem starting from the end of the array.
The first pointer searches for the k value while the other pointer stays put.
Once a k value is found, the elements will be swapped and the pointers decremented.
This will continue until the first pointer reaches out of bounds.
The number of swaps will be kept tracked of using a variable. 
The return value is the length of the array minus the number of swaps that occurred.
The edge case is when the length of nums == 0. 
Space complexity = O(1), Time complexity = O(N).

"""


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:

        # edge case if length of nums = 0
        l = len(nums)
        if (l < 1):
            return l

        # create pointers and counter
        counter = 0
        kfinder = l - 1
        trailing = l - 1

        # while kf >= 0
        while (kfinder >= 0):

            # if value at kfinder != val
            if (nums[kfinder] != val):

                # decrement kfinder
                kfinder -= 1

            # if value at kfinder == val
            else:

                # swap
                temp = nums[trailing]
                nums[trailing] = nums[kfinder]
                nums[kfinder] = temp

                # decrement both pointers and increment counter
                counter += 1
                kfinder -= 1
                trailing -= 1

        # return counter
        return l - counter
