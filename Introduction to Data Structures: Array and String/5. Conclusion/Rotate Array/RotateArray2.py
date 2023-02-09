# second approach using reverse list

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def reverseList(l, r, lst):
            # reverse the whole list
            l, r = 0, len(lst)-1

            while l <= r:
                lst[l], lst[r] = lst[r], lst[l]
                l += 1
                r -= 1

        # handle when k > length nums
        if k > len(nums):
            k = k % len(nums)

        # reverse the whole list
        reverseList(0, len(nums)-1, nums)

        # reverse the first k elements
        reverseList(0, k-1, nums)

        # reverse the last remaining elements
        reverseList(k, len(nums)-1, nums)
