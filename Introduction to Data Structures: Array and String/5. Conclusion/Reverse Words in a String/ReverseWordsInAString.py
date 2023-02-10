class Solution:
    def reverseWords(self, s: str) -> str:

        # create an empty string to store result
        output = ""

        # preprocess input and remove leading and trailing white spaces
        s = s.strip()

        # create a temp variable
        temp = ""

        # iterate from the last element to the beginning
        for i in range(len(s)-1, -1, -1):

            # if the char is not a space
            if s[i] != " ":

                # append it to the temp
                temp = s[i] + temp

            # if the char is a space
            else:

                # check if temp is not empty
                if len(temp) != 0:
                    output += temp + " "
                    temp = ""

        # return output
        return output + temp
