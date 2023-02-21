class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:

        hashMap = {}

        result = []

        for num in nums1:

            hashMap[num] = hashMap.get(num, 0) + 1

        for num in nums2:

            if (hashMap.get(num, 0) != 0):

                result.append(num)

                hashMap[num] = hashMap.get(num) - 1

        return result
