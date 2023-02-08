class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        # edge case where nums == 0 - 2
        if len(nums) == 0:
            return 0

        if len(nums) == 1 or len(nums) == 2:
            return nums[0]

        # sort -> [1, 2, 2, 5, 6, 6]
        nums.sort()

        # iterate nums and add every other element -> 1 + 2 + 6 = 9
        result = 0

        for i in range(0, len(nums), 2):
            result += nums[i]

        return result
