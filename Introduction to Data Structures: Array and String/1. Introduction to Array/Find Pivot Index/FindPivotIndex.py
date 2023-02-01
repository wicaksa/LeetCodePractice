class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        # helper method to calculate rightSum
        def calcRightSum(totalSum, leftSum, currentVal):
            return totalSum - leftSum - currentVal

        # calculate the sum of nums
        totalSum = sum(nums)

        # create a variable to keep track of left sum
        leftSum = 0

        # iterate throught the list
        for i in range(0, len(nums)):

            # if left sum = right sum
            if i != 0:
                leftSum += nums[i-1]

            if leftSum == calcRightSum(totalSum, leftSum, nums[i]):

                # return current index
                return i

        # return -1
        return -1
