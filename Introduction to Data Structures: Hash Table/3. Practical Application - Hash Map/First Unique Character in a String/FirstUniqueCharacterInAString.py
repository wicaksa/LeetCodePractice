class Solution:
    def firstUniqChar(self, s: str) -> int:

        # create a hashMap
        hashMap = {}

        # iterate through s
        for i in range(0, len(s)):

            char = s[i]

            # add or update key value pair
            hashMap[char] = hashMap.get(char, 0) + 1

        for key in hashMap.keys():

            if hashMap.get(key) == 1:

                return s.index(key)

        return -1
