class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        # counter
        maxTuples = 0

        # create hash map for sums of nums1 and nums2
        hashMap = {}

        for num1 in nums1:

            for num2 in nums2:

                hashMap[num1+num2] = hashMap.get(num1+num2, 0) + 1

        # for loop through nums3
        for num3 in nums3:

            # for loop through nums 2
            for num4 in nums4:

                # if the negative sum of the two numbers is a key in the hash map
                key = (num3 + num4) * (-1)

                if key in hashMap.keys() and hashMap.get(key) != 0:

                    # increment counter
                    maxTuples += hashMap.get(key)

        # return counter
        return maxTuples
