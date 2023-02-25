class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        curSum = nums[0]

        if len(nums) == 1:
            return curSum

        for i in range(1, len(nums)):

            nums[i] += curSum

            curSum = nums[i]

        return nums
