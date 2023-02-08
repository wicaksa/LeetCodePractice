class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:

        # Input: target = 7, nums = [2,3,1,2,4,3]

        # edge case
        if len(nums) == 0:
            return 0

        if sum(nums) < target:
            return 0

        # initialize variable to keep track of min value
        minVal = 10 ** 5

        # create two pointers left and right
        l = 0
        r = 1

        # while the right pointer is less than length of nums
        while r <= len(nums):

            # if current sub array < target
            if sum(nums[l:r]) < target:

                # move right pointer
                r += 1

            # elif current sub array > target
            elif sum(nums[l:r]) > target:

                minVal = min(minVal, len(nums[l:r]))

                # move left pointer
                l += 1

            # else current sub == target
            else:

                # get length of subarray
                # store minimum value
                minVal = min(minVal, len(nums[l:r]))

                # move right pointer
                r += 1

        # now right pointer is out of range we move the left pointer
        # move back right pointer bc it's past the iteration point
        r -= 1  # should be back at length of nums

        # while left pointer is less than length of nums
        while l <= len(nums) and sum(nums[l:r]) >= target:

            # get length of subarray
            # store minimum value
            minVal = min(minVal, len(nums[l:r]))

            # move left pointer
            l += 1

            loops += 1

        # return min value
        if minVal == 10 ** 5:
            return 0
        else:
            return minVal
