class Solution:
    def singleNumber(self, nums: List[int]) -> int:

        d = dict()

        for number in nums:
            if d.get(number) == None:
                d[number] = 1

            else:
                d[number] += 1

        for key in d.keys():
            if d[key] == 1:
                return key
