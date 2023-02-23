class RandomizedSet:

    def __init__(self):
        self.hashMap = {}
        self.nums = []

    def insert(self, val: int) -> bool:

        valNotInHashMap = val not in self.hashMap.keys()

        if valNotInHashMap:

            self.hashMap[val] = len(self.nums)

            self.nums.append(val)

        return valNotInHashMap

    def remove(self, val: int) -> bool:

        valInHashMap = val in self.hashMap.keys()

        if valInHashMap:

            # get last element in nums and store it in a variable
            lastElement = self.nums[-1]

            # get index of val
            indexOfVal = self.hashMap[val]

            # replace that element with the last element
            self.nums[indexOfVal] = lastElement

            # remove last element
            self.nums.pop()

            # change mapping of last element to the index of val
            self.hashMap[lastElement] = indexOfVal

            # remove mapping of element in hash map
            self.hashMap.pop(val)

        return valInHashMap

    def getRandom(self) -> int:

        return random.choice(self.nums)

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
