class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        hashSet = set()
        l = 0
        r = 0
        maxLength = 0

        while r < len(s):

            if s[r] not in hashSet:

                hashSet.add(s[r])

                r += 1

                maxLength = max(maxLength, len(hashSet))

            else:

                hashSet.remove(s[l])

                l += 1

        return maxLength
