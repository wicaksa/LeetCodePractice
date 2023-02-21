class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:

        hashMap = {}

        for j in jewels:

            hashMap[j] = 0

        for s in stones:

            if hashMap.get(s) != None:

                hashMap[s] += 1

        return sum(hashMap.values())
