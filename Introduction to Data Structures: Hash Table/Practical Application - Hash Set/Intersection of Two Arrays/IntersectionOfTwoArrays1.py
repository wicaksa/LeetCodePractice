class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:

        output = set()

        for nums in nums1:

            if nums in nums2:

                output.add(nums)

        return output
