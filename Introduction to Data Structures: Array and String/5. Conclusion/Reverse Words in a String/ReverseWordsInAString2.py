# Approach: Splitting the string into a list of strings, reversing the list, then joining the elements of the list separated by " ".

class Solution:
    def reverseWords(self, s: str) -> str:

        # Split the string into a list of strings
        # The default separator is white space so need to do extra string preprocessing
        l = s.split()

        # Reverse the list
        l.reverse()

        # Join each element in the list by a white space and return
        return " ".join(l)
