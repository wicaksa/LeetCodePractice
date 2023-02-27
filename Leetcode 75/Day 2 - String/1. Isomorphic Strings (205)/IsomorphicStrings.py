class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        # input: 2 strings
        # output: boolean

        # you can't map two letters to the same letter (e -> g and f -> g)
        # you CAN map the a letter to the same letter (e -> e)
        """
        Input: s = "egg", t = "add"
        Output: true

        hashMap = {}

        1:
            1. is e a key in the map?
            2. it is not so we add (e, a)
                3. { e:a }

        2.
            1. is g in the map?
            2. it is not so we add (g, d)
                3. { e:a, g:d }

        3. 
            1. is g in the map?
            2. it is so we check if the value matches up to d 
            3. value of g matches to d 
                if it doesn't match, we return false

        make sure you don't have more than 1 count of the same letter
        """

        hashMap = {}

        for i in range(0, len(s)):

            if s[i] not in hashMap.keys():

                if t[i] not in hashMap.values():

                    hashMap[s[i]] = t[i]

                else:
                    return False

            else:  # if s[i] is a key

                if hashMap[s[i]] != t[i]:

                    return False

        return True
