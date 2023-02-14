class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:

        # create a list to hold result
        output = set()

        # sort the lists
        nums1.sort()
        nums2.sort()

        print(nums1, nums2)
        # create two pointers
        p1 = 0
        p2 = 0

        # while each pointer is less than their respective lengths
        while p1 < len(nums1) and p2 < len(nums2):

            # if elements are the same
            if nums1[p1] == nums2[p2]:

                # put it in the result list
                output.add(nums1[p1])

                # increment both pointers
                p1 += 1
                p2 += 1

            # if elements are not the same
            else:

                # move the pointer with the lowest value
                if nums1[p1] < nums2[p2]:
                    p1 += 1
                else:
                    p2 += 1

        # return result
        return output
