class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        # find the largest value in the list
        maxVal = max(nums)

        # iterate the list
        for i in range(0, len(nums)):

            # if largest value is less than current value * 2 and current value != largest value
            if nums[i] * 2 > maxVal and nums[i] != maxVal:

                # return -1
                return -1

        return nums.index(maxVal)
