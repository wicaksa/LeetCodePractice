class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:

        # handle edge case
        if len(nums) == 0:
            return 0

        # create a left pointer
        l = 0

        # create a running sum
        currentSum = 0

        # create result to store smalles size subarray
        # we add a + 1 since there could be a min length of the max length
        minSubArrLen = 10**5 + 1

        # iterate through the array (this will be the right pointer)
        for i in range(0, len(nums)):

            # add current element to the running sum
            currentSum += nums[i]

            # while the running sum >= target
            while currentSum >= target:

                # calculate subarray length and compare it with the result to see which is smaller
                minSubArrLen = min(minSubArrLen, i - l + 1)

                # remove left pointer value from running sum
                currentSum -= nums[l]

                # increment left pointer
                l += 1

        # return result make sure it's not max value
        if minSubArrLen == 10**5 + 1:
            return 0

        return minSubArrLen
