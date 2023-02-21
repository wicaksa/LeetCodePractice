class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:

        hashMap = {}

        for i in range(0, len(nums)):

            if hashMap.get(nums[i]) != None:

                # print(i, hashMap.get(nums[i]), k)

                if i - hashMap.get(nums[i]) <= k:

                    return True

            hashMap[nums[i]] = i

        return False
