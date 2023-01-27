# Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. The relative order of the elements may be changed.

# Since it is impossible to change the length of the array in some languages, you must instead have the result be placed in the first part of the array nums. More formally, if there are k elements after removing the duplicates, then the first k elements of nums should hold the final result. It does not matter what you leave beyond the first k elements.

# Return k after placing the final result in the first k slots of nums.

# Do not allocate extra space for another array. You must do this by modifying the input array in-place with O(1) extra memory.


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:

        # edge case if every single value in the array == target value
        # O(n) - counting
        if len(nums) == nums.count(val):
            return 0

        # create two pointers
        l = 0
        r = len(nums) - 1

        # keep track of how many numbers are removed
        k = 0

        # while your left and right pointers have not passed each other
        while l <= r and r >= l:
            # case where target value == value at right pointer
            if val == nums[r]:
                # decrement the right pointer
                r -= 1
                # increment k
                k += 1
            # case where target value == value at left pointer
            elif val == nums[l]:
                # swap value at left pointer with right pointer
                nums[l] = nums[r]
                nums[r] = val
                # increment left pointer
                l += 1
                # decrement right pointer
                r -= 1
                # increment k
                k += 1
            # case where left value doesn't equal target value
            else:
                # increment left pointer
                l += 1

        # return the length of nums - k
        return len(nums) - k
