# You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1.
# If a string is longer than the other, append the additional letters onto the end of the merged string.

# Return the merged string.


def mergeAlternately(self, word1: str, word2: str) -> str:
    # input : 2 strings
    # output: 1 string with alt letters

    # create an empty string to store result
    result = ""

    # get the max length out of the two strings
    maxLength = max(len(word1), len(word2))

    # iterate through max length
    for i in range(0, maxLength):
        # if p1 at word 1 is not null
        if i <= len(word1) - 1:
            # append letter to empty string
            result += word1[i]

            # increment p1
            p1 += 1

        # if p2 at word 2 is not null
        if i <= len(word2) - 1:
            # append letter to empty string
            result += word2[i]

            # increment p2
            p2 += 1

    # return result string
    return result
