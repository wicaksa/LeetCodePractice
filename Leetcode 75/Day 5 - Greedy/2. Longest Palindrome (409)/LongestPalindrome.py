class Solution:
    def longestPalindrome(self, s: str) -> int:

        largestPalindrome = 0
        hashMap = {}
        thereIsOdd = False

        for letter in s:
            hashMap[letter] = hashMap.get(letter, 0) + 1

        for v in hashMap.values():
            if v % 2 == 0:
                largestPalindrome += v
            else:
                largestPalindrome += (v-1)
                thereIsOdd = True

        if thereIsOdd:
            return largestPalindrome + 1

        return largestPalindrome
