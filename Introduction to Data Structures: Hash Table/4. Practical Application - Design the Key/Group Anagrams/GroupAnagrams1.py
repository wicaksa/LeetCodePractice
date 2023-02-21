class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        # create a hash map
        hashMap = {}

        # iterate through each word in the string
        for s in strs:

            # convert the string to a list so we can sort
            k = [x for x in s]

            # sort the list
            k.sort()

            # convert the list back to a string
            k = "".join(k)

            # check hash map if key exists
            if hashMap.get(k) != None:

                # append the string to the value list if key already exists
                hashMap.get(k).append(s)

            else:
                # create a new list with string and save it as the value for k
                hashMap[k] = [s]

        # return the values
        return hashMap.values()
