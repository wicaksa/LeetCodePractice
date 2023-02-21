class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        hashMap = {}  # also called dictionary in Python

        for i in range(0, len(nums)):

            diff = target - nums[i]

            if diff in hashMap.keys():

                return [i, hashMap[diff]]

            else:

                hashMap[nums[i]] = i
