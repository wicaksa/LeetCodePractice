class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # input : list of string
        # output: string representing longest common prefix
        # prefix means letters in the beggining of a word

        # base case: if length input is 0 or 1 -> return the list
        if len(strs) == 0:
            return ""

        if len(strs) == 1:
            return strs[0]

        # create output string
        # result = ""

        # count the number of matches
        counter = 0

        # sort the list (log N)
        strs.sort()

        # iterate through the first word in the list
        for i in range(0, len(strs[0])):

            # iterate through the list
            for j in range(1, len(strs)):

                # if at any point there is no match
                if strs[j][i] != strs[0][i]:

                    # return ""
                    # return result

                    # return a substring of the first word
                    return strs[0][0:counter]

            # add the letter to the output string
            # result += strs[0][i]

            # increment the counter
            counter += 1

        # return output string
        # return result

        # return a substring of the first word
        return strs[0][0:counter]
