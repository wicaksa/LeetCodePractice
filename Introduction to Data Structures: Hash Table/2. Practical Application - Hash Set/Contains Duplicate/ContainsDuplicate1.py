class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:

        d = dict()

        for i in range(0, len(nums)):

            if d.get(nums[i]) == None:
                d[nums[i]] = 1

            else:
                d[nums[i]] += 1
                if d[nums[i]] > 1:
                    return True

        return False
