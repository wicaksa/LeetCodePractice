class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:

        hashMap = {}

        for i in range(0, len(s)):

            if s[i] not in hashMap.keys():

                if t[i] not in hashMap.values():

                    hashMap[s[i]] = t[i]
                else:
                    return False

            else:

                val = hashMap[s[i]]

                if val != t[i]:

                    return False

        return True
