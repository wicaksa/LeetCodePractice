class Solution:
    def reverseWords(self, s: str) -> str:

        # create a list of string
        listOfWords = s.split()

        # iterate the list and reverse each string
        for i in range(0, len(listOfWords)):

            listOfWords[i] = listOfWords[i][::-1]

        # convert list back to a string and return it
        return " ".join(listOfWords)
