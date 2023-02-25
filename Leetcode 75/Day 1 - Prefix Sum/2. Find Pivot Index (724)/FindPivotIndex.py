class Solution:
    def pivotIndex(self, nums: List[int]) -> int:

        # edge case when length = 1
        if len(nums) == 1:
            return 0

        lSum = 0
        totalSum = sum(nums)

        for i in range(0, len(nums)):
            rSum = totalSum - lSum - nums[i]

            if lSum == rSum:
                return i

            lSum += nums[i]

        return -1
