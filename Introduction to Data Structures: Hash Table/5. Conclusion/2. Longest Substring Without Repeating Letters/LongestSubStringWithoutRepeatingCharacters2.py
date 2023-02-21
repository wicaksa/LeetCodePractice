class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        if len(s) < 2:

            return len(s)

        maxLength = 0

        l = 0

        r = 1

        while r < len(s):

            if s[r] not in s[l:r]:

                r += 1

                maxLength = max(maxLength, len(s[l:r]))

            else:

                l += 1

        return maxLength
