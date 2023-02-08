class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """

        # input : list of str
        # output: none (modify input in place)

        # edge case: input has length 0 or 1 don't do anything

        # if length of input > 1
        if len(s) > 1:

            # create left and right pointer
            l = 0
            r = len(s) - 1

            # while left pointer <= right pointer and right pointer is >= left pointer
            while l <= r and r >= l:

                # swap
                temp = s[l]
                s[l] = s[r]
                s[r] = temp

                # increment left pointer
                l += 1

                # decrement right pointer
                r -= 1
