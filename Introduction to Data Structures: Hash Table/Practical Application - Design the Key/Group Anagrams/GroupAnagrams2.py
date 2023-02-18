class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        hashMap = {}

        MAX_LENGTH = 26

        for word in strs:

            key = [0] * MAX_LENGTH

            for letter in word:

                i = ord(letter) - ord('a')

                key[i] += 1

            key = tuple(key)

            if hashMap.get(key) != None:

                hashMap.get(key).append(word)

            else:

                hashMap[key] = [word]

        return hashMap.values()
