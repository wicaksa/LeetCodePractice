class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        # input : 2 integer arrays, nums1 and nums2
        # output: nothing, modify nums1 in place

        # approach 1: create a temp array. use two pointers
        #             to add elements from each array starting
        #             with the lowest to the greates

        # get the last index of nums1
        last = m + n - 1

        # merge in reverse order
        while m > 0 and n > 0:

            if nums1[m-1] > nums2[n-1]:

                nums1[last] = nums1[m-1]

                m -= 1

            else:

                nums1[last] = nums2[n-1]

                n -= 1

            last -= 1

        # fill in nums1 with leftoever nums2 elements
        while n > 0:
            nums1[last] = nums2[n-1]

            n -= 1
            last -= 1
