class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:

        res = []

        hashMap = {}

        for i in range(0, len(list1)):

            word = list1[i]

            if word in list2:

                hashMap[word] = i + list2.index(word)

        minVal = min(hashMap.values())

        for key in hashMap.keys():

            if hashMap[key] == minVal:

                res.append(key)

        return res
