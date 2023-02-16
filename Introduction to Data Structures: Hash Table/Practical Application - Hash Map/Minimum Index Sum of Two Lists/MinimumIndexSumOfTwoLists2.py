class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:

        res = []

        hashMap = {}

        minVal = float('inf')

        for i in range(0, len(list1)):

            hashMap[list1[i]] = i

        for i in range(0, len(list2)):

            total = 0

            if hashMap.get(list2[i]) != None:

                total = i + (hashMap.get(list2[i]))

                if total < minVal:

                    res.clear()

                    minVal = total

                    res.append(list2[i])

                elif total == minVal:

                    res.append(list2[i])

        return res
