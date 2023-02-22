class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        # create an array to hold result
        output = []

        # create hash map to keep track of how many times we see an element
        hashMap = {}

        # create another array to keep track of how many elements there are in increasing order
        sortedMap = [0] * (len(nums) + 1)

        # populate the hash map with key and value
        for num in nums:

            hashMap[num] = hashMap.get(num, 0) + 1

        # get each key value pair from the hash map
        for key, val in hashMap.items():

            # if the sortedMap at index val is 0 (untouched)
            if sortedMap[val] == 0:

                # store the key in an array at that index
                sortedMap[val] = [key]

            # if that index is already populated
            else:

                # append the key to the running array
                sortedMap[val].append(key)

        # iterate through the sorted map from the end
        for i in range(len(sortedMap)-1, -1, -1):

            # if the value at the index is 0, continue
            if sortedMap[i] == 0:

                continue

            # otherwise
            else:

                # get the element at that index
                listOfNumbers = sortedMap[i]

                # iterate through the array
                for num in listOfNumbers:

                    # append each element into the output
                    output.append(num)

                    # if the output length is equal to k, just return the output
                    if len(output) == k:

                        return output
